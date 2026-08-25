"""Unified memory search with multi-hop retrieval and grounded answers.

Combines keyword (exact), vector (semantic) and graph (relational) signals —
plus recency, confidence and status — into a deterministic, explainable hybrid
ranking. Multi-hop traversal follows only relevant graph paths (bounded BFS) so
answers can chain facts ("what technology does the project I'm learning Rust
for use?"). Every answer is classified KNOWN / UNKNOWN / UNCERTAIN and carries
a traceable list of sources, so nothing is hallucinated.
"""
import json
import re

import numpy as np

from . import config, db, fallback, graph, ollama, store

INTENT_KEYWORDS = {
    "project": ["project", "projects", "app", "apps", "building", "startup", "working on", "working"],
    "learning": ["learn", "learning", "study", "studying"],
    "technology": ["technology", "tech", "technologies", "stack", "tools", "using"],
    "person": ["people", "person", "friends", "friend", "who", "met"],
    "goal": ["goal", "goals", "plan", "want", "objective", "aiming"],
    "interest": ["interest", "interested", "hobbies", "like", "enjoy", "prefer", "preference"],
    "location": ["live", "located", "based"],
    "organization": ["work at", "work for", "company", "employer", "organization"],
}

STOPWORDS = {
    "the", "a", "an", "and", "or", "i", "me", "my", "we", "our", "you", "your",
    "do", "does", "did", "is", "are", "am", "was", "were", "be", "have", "has",
    "had", "use", "using", "used", "with", "for", "to", "of", "in", "on", "at",
    "it", "that", "this", "what", "who", "how", "when", "where", "which", "why",
    "tell", "show", "give", "list", "about", "any", "some", "can", "could",
    "would", "should", "there", "their", "them", "from", "as", "by", "not",
    "no", "yes", "please", "remember", "know",
}


def detect_intent(query):
    q = query.lower()
    for intent, words in INTENT_KEYWORDS.items():
        if any(w in q for w in words):
            return intent
    return None


def _cosine(a, b):
    if a is None or b is None:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


def re_tokenize(s):
    return re.findall(r"[a-z0-9#+.\-']+", s.lower())


_SHORT_TERMS = {
    "go", "ai", "js", "ts", "ui", "ux", "ml", "c#", "c++", "r", "k8s",
}


def query_terms(query_text):
    """Content tokens for ranking. Keeps short tech names (Go, AI, C#)."""
    out = []
    for t in re_tokenize(query_text):
        if t in STOPWORDS:
            continue
        if len(t) > 2 or t in _SHORT_TERMS:
            out.append(t)
    return out


def json_loads(s):
    try:
        value = json.loads(s or "[]")
    except (TypeError, ValueError, json.JSONDecodeError):
        return []
    return value if isinstance(value, (list, dict)) else []


# --------------------------------------------------------------------------
# Signal 1: vector (semantic)
# --------------------------------------------------------------------------

def vector_search(query_text, k=None):
    k = k or config.VECTOR_SEARCH_K
    qv = store.embed_text(query_text)
    rows = db.query("SELECT * FROM entities WHERE embedding IS NOT NULL")
    scored = []
    for r in rows:
        ev = store.vec_from_json(r.get("embedding"))
        if ev is None:
            continue
        scored.append((_cosine(qv, ev), r))
    scored.sort(key=lambda x: -x[0])
    return [(s, r) for s, r in scored[:k] if s > 0.1]


# --------------------------------------------------------------------------
# Signal 2: keyword (exact)
# --------------------------------------------------------------------------

def keyword_search(query_text, limit=10):
    terms = query_terms(query_text)
    rows = db.query("SELECT * FROM entities")
    scored = []
    for r in rows:
        name = r["name"].lower()
        aliases = [store.normalize_name(a) for a in json_loads(r.get("aliases"))]
        score = 0.0
        for t in terms:
            if t == name:
                score += 5.0
            elif t in name:
                score += 1.0
            elif any(t == a or t in a for a in aliases):
                score += 2.0
        if score:
            scored.append((score, r))
    scored.sort(key=lambda x: -x[0])
    return [(s, r) for s, r in scored[:limit]]


# --------------------------------------------------------------------------
# Graph facts
# --------------------------------------------------------------------------

def graph_facts_for_entity(eid, active_only=True):
    """Relationships touching an entity, in canonical "s relation t" form."""
    status_filter = " AND r.status='active'" if active_only else ""
    rels = db.query(
        "SELECT r.*, s.name sname, t.name tname FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE (r.source_id=? OR r.target_id=?)" + status_filter,
        (eid, eid),
    )
    return [{"text": f'{r["sname"]} {r["relation"]} {r["tname"]}',
             "confidence": r["confidence"], "rid": r["id"],
             "source_message_id": r["source_message_id"],
             "entities": [r["source_id"], r["target_id"]]} for r in rels]


def intent_facts(intent):
    """Graph facts directly matching a question intent (e.g. 'learning')."""
    out = []
    if intent == "learning":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='learning' AND r.status='active'")
        out = [{"text": f'{r["sname"]} learning {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent in ("interest", "preference"):
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.relation rel, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation IN ('prefers','interested_in','likes') AND r.status='active'")
        out = [{"text": f'{r["sname"]} {r["rel"]} {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "project":
        rows = db.query("SELECT * FROM entities WHERE type='project' AND status='active'")
        out = [{"text": f'project {r["name"]}', "confidence": r["confidence"],
                "entities": [r["id"]], "source_message_id": r.get("source_message_id")} for r in rows]
    elif intent == "technology":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='uses' AND r.status='active'")
        out = [{"text": f'{r["sname"]} uses {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "goal":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='wants' AND r.status='active'")
        out = [{"text": f'{r["sname"]} wants {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "person":
        rows = db.query("SELECT * FROM entities WHERE type='person' AND status='active' AND norm_name != 'user'")
        out = [{"text": f'person {r["name"]}', "confidence": r["confidence"],
                "entities": [r["id"]], "source_message_id": r.get("source_message_id")} for r in rows]
    elif intent == "location":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='lives_in' AND r.status='active'")
        out = [{"text": f'{r["sname"]} lives_in {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "organization":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='works_at' AND r.status='active'")
        out = [{"text": f'{r["sname"]} works_at {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    return out


# --------------------------------------------------------------------------
# Source attribution
# --------------------------------------------------------------------------

def _source_for_message(message_id):
    if not message_id:
        return None
    m = store.message_by_id(message_id)
    if not m:
        return None
    conv = store.conversation_row(m.get("conversation_id")) if m.get("conversation_id") else None
    return {"message_id": m["id"], "content": m["content"], "created_at": m["created_at"],
            "conversation_id": m.get("conversation_id"),
            "conversation_title": conv["title"] if conv else None}


def sources_for_facts(facts, limit=8):
    """Build a compact, deduplicated source list for a set of facts/entities."""
    seen = set()
    sources = []
    for f in facts:
        fact_src = _source_for_message(f.get("source_message_id"))
        for eid in f.get("entities", []):
            ent = store.entity_row(eid)
            if not ent:
                continue
            src = fact_src or _source_for_message(ent.get("source_message_id"))
            key = (ent["name"], ent["id"], src["message_id"] if src else None)
            if key in seen:
                continue
            seen.add(key)
            snippet = (src["content"][:160] if src and src.get("content") else None)
            sources.append({
                "entity_id": ent["id"], "name": ent["name"], "type": ent["type"],
                "message_id": src["message_id"] if src else None,
                "conversation_title": src["conversation_title"] if src else None,
                "created_at": (src["created_at"] if src else None) or ent["created_at"],
                "snippet": snippet,
                "fact": f.get("text"),
            })
            if len(sources) >= limit:
                return sources
    return sources


# --------------------------------------------------------------------------
# Hybrid search (with multi-hop)
# --------------------------------------------------------------------------

def search(query_text, filters=None, multi_hop_depth=3):
    """Combined ranking + multi-hop fact retrieval.

    filters (optional): {type, min_confidence, status, pinned, important}
    """
    filters = filters or {}
    intent = detect_intent(query_text)
    vhits = vector_search(query_text)
    khits = keyword_search(query_text)

    merged = {}
    for s, r in vhits:
        merged[r["id"]] = {"entity": r, "score": s * 0.6, "vector": round(s, 3), "reasons": ["semantic"]}
    for s, r in khits:
        cur = merged.get(r["id"])
        if cur:
            cur["score"] += s
            cur["keyword"] = round(s, 1)
            if "keyword" not in cur["reasons"]:
                cur["reasons"].append("keyword")
        else:
            merged[r["id"]] = {"entity": r, "score": float(s), "keyword": round(s, 1), "reasons": ["keyword"]}

    # Graph-connectivity signal.
    adj, _ = graph._load_edges(active_only=True)
    for eid, rec in merged.items():
        deg = len(adj.get(eid, []))
        if deg >= 2:
            rec["score"] += min(deg, 10) * 0.05
            rec["reasons"].append("graph")
        # recency / flags
        rec["score"] += _recency_boost(rec["entity"])
        if _is_recent(rec["entity"]):
            rec["reasons"].append("recent")
        if rec["entity"].get("pinned"):
            rec["score"] += 0.8
            rec["reasons"].append("pinned")
        if rec["entity"].get("important"):
            rec["score"] += 0.5
            rec["reasons"].append("important")
        # status penalty
        if rec["entity"].get("status") == "superseded":
            rec["score"] -= 5.0

    # Apply filters.
    if filters:
        merged = {eid: rec for eid, rec in merged.items()
                  if _passes_filters(rec["entity"], filters)}

    results = sorted(merged.values(), key=lambda x: -x["score"])
    entities = [{
        "id": e["entity"]["id"], "name": e["entity"]["name"],
        "type": e["entity"]["type"], "description": e["entity"]["description"],
        "confidence": e["entity"]["confidence"],
        "score": round(e["score"], 3),
        "vector": e.get("vector"), "keyword": e.get("keyword"),
        "reasons": e.get("reasons", []),
        "status": e["entity"].get("status", "active"),
        "pinned": e["entity"].get("pinned", 0),
        "important": e["entity"].get("important", 0),
    } for e in results if e["score"] > 0]

    # Facts: direct + intent + multi-hop.
    facts = []
    seed_ids = [e["entity"]["id"] for e in results[:5]]
    for e in results[:5]:
        facts.extend(graph_facts_for_entity(e["entity"]["id"]))
    facts.extend(intent_facts(intent))
    if seed_ids:
        facts.extend(graph.multi_hop(seed_ids, max_depth=multi_hop_depth))

    seen, dedup = set(), []
    for f in facts:
        if f["text"] not in seen:
            seen.add(f["text"])
            dedup.append(f)

    # Entity filters must constrain facts as well as the entity result list;
    # otherwise the UI can show a filtered list beside an unfiltered answer.
    dedup = _filter_direct_facts(dedup, filters)
    dedup = _rank_facts(dedup, query_text)

    return {"intent": intent, "entities": entities, "facts": dedup,
            "sources": sources_for_facts(dedup)}


def _rank_facts(facts, query_text):
    q_terms = set(query_terms(query_text))
    def _score(f):
        blob = (f.get("text") or "").lower()
        tok = sum(1 for t in q_terms if t in blob)
        depth = f.get("depth") or 1
        conf = f.get("confidence") or 0.5
        return (tok * 3.0) + float(conf) - (max(int(depth), 1) - 1) * 0.45
    return sorted(facts, key=_score, reverse=True)


def _is_recent(row):
    import datetime as _dt
    try:
        d = _dt.datetime.fromisoformat(row.get("updated_at") or row.get("created_at") or "")
        return (_dt.datetime.now(_dt.timezone.utc) - d).total_seconds() < 86400 * 7
    except (ValueError, TypeError):
        return False


def _recency_boost(row):
    return 0.3 if _is_recent(row) else 0.0


def _passes_filters(row, filters):
    if filters.get("type") and row["type"] != filters["type"]:
        return False
    if filters.get("min_confidence") is not None and row["confidence"] < filters["min_confidence"]:
        return False
    if filters.get("status") and row.get("status", "active") != filters["status"]:
        return False
    if filters.get("pinned") is not None and bool(row.get("pinned", 0)) != bool(filters["pinned"]):
        return False
    if filters.get("important") is not None and bool(row.get("important", 0)) != bool(filters["important"]):
        return False
    created = (row.get("created_at") or "")[:10]
    updated = (row.get("updated_at") or created)[:10]
    if filters.get("date_from") and updated < str(filters["date_from"])[:10]:
        return False
    if filters.get("date_to") and created > str(filters["date_to"])[:10]:
        return False
    if filters.get("source"):
        src_filter = str(filters["source"])
        if src_filter.lower() == "demo":
            try:
                meta = json.loads(row.get("meta") or "{}")
            except ValueError:
                meta = {}
            if not meta.get("demo"):
                return False
        else:
            mid = row.get("source_message_id")
            msg = store.message_by_id(mid) if mid else None
            if not msg or str(msg.get("conversation_id")) != src_filter:
                return False
    return True


# --------------------------------------------------------------------------
# Grounded answer (KNOWN / UNKNOWN / UNCERTAIN)
# --------------------------------------------------------------------------

_YN_FACT = re.compile(
    r"^(?:do i|did i|am i|have i)\s+"
    r"(using|use|learning|learn|preferring|prefer|living in|live in|"
    r"working at|work at|working on|work on|know)\s+(.+?)\??$",
    re.I,
)

_YN_REL = {
    "use": "uses", "using": "uses",
    "learn": "learning", "learning": "learning",
    "prefer": "prefers", "preferring": "prefers",
    "live in": "lives_in", "living in": "lives_in",
    "work at": "works_at", "working at": "works_at",
    "work on": "works_on", "working on": "works_on",
    "know": "knows",
}


def _entity_matches_filters(entity, filters):
    """Apply search filters to an entity used by a direct answer."""
    if not filters:
        return True
    if filters.get("type") and entity.get("type") != filters["type"]:
        return False
    if filters.get("min_confidence") is not None \
            and entity.get("confidence", 0) < filters["min_confidence"]:
        return False
    if filters.get("status") and entity.get("status", "active") != filters["status"]:
        return False
    for flag in ("pinned", "important"):
        if filters.get(flag) is not None and bool(entity.get(flag, 0)) != bool(filters[flag]):
            return False
    created = (entity.get("created_at") or "")[:10]
    updated = (entity.get("updated_at") or created)[:10]
    if filters.get("date_from") and updated < str(filters["date_from"])[:10]:
        return False
    if filters.get("date_to") and created > str(filters["date_to"])[:10]:
        return False
    if filters.get("source"):
        source = str(filters["source"])
        if source.lower() == "demo":
            try:
                meta = json_loads(entity.get("meta"))
            except Exception:
                meta = {}
            if not meta.get("demo"):
                return False
        else:
            mid = entity.get("source_message_id")
            msg = store.message_by_id(mid) if mid else None
            if not msg or str(msg.get("conversation_id")) != source:
                return False
    return True


def _filter_direct_facts(facts, filters):
    """Keep facts that have at least one endpoint matching active filters."""
    if not filters:
        return list(facts)
    result = []
    for fact in facts:
        if filters.get("status") and fact.get("status", "active") != filters["status"]:
            continue
        if filters.get("min_confidence") is not None \
                and (fact.get("confidence") or 0) < filters["min_confidence"]:
            continue
        if filters.get("source"):
            source = str(filters["source"])
            source_message = store.message_by_id(fact.get("source_message_id")) if fact.get("source_message_id") else None
            if source.lower() == "demo":
                message_meta = json_loads(source_message.get("meta")) if source_message else {}
                message_demo = isinstance(message_meta, dict) and message_meta.get("demo")
                entity_demo = False
                for eid in fact.get("entities", []):
                    entity = store.entity_row(eid)
                    if entity:
                        entity_meta = json_loads(entity.get("meta"))
                        if isinstance(entity_meta, dict) and entity_meta.get("demo"):
                            entity_demo = True
                            break
                if not (message_demo or entity_demo):
                    continue
            elif not source_message or str(source_message.get("conversation_id")) != source:
                continue
        entities = [store.entity_row(eid) for eid in fact.get("entities", [])]
        entities = [entity for entity in entities if entity]
        if entities and any(_entity_matches_filters(entity, filters) for entity in entities):
            result.append(fact)
    return result


def _direct_fact_answer(query_text, filters=None):
    """Yes/no questions about a specific stored fact. Never invents."""
    m = _YN_FACT.match((query_text or "").strip())
    if not m:
        return None
    rel = _YN_REL.get(m.group(1).lower())
    name = (m.group(2) or "").strip().strip("?. ")
    if not rel or not name:
        return None
    target = store.find_entity_by_name(name)
    if not target:
        hits = keyword_search(name, limit=3)
        if hits and hits[0][0] >= 5:
            target = hits[0][1]
    uid = store.ensure_user_entity()
    unknown = {
        "text": (
            f"I don't have a memory indicating that. Nothing in your brain "
            f"matches “{query_text}” yet."
        ),
        "status": "unknown",
        "sources": [],
    }
    if not target or not _entity_matches_filters(target, filters):
        return unknown
    if filters and filters.get("status") == "superseded":
        return unknown
    row = db.query_one(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? "
        "AND relation=? AND status='active'",
        (uid, target["id"], rel),
    )
    if not row:
        return unknown
    fact = {"text": f'User {rel} {target["name"]}', "confidence": row["confidence"],
            "entities": [uid, target["id"]], "source_message_id": row.get("source_message_id")}
    return {
        "text": f'Yes — User {rel} {target["name"]}. (from stored memory)',
        "status": "known",
        "sources": sources_for_facts([fact]),
    }


_ABOUT = re.compile(
    r"^(?:tell me about|what do (?:i|you) know about|who is|what about)\s+(.+?)\??$",
    re.I,
)
_PATH_Q = re.compile(
    r"^(?:how (?:is|are)\s+(.+?)\s+related\s+to\s+(.+?)"
    r"|what(?:'s| is) the (?:connection|relationship|link) between\s+(.+?)\s+and\s+(.+?))"
    r"\??$",
    re.I,
)
_ARTICLES = re.compile(r"^(?:the|a|an|my|our|this|that)\s+", re.I)
_USES_OF = re.compile(
    r"^(?:what(?: technology| technologies| tools?)? does)\s+(.+?)\s+use\??$",
    re.I,
)
_LIST_QUESTIONS = (
    (re.compile(r"^(?:where do i live|where am i based|where do i live now)\??$", re.I),
     "location", " lives_in "),
    (re.compile(r"^(?:where do i work|who do i work for|where am i employed)\??$", re.I),
     "organization", " works_at "),
    (re.compile(r"^(?:who do i know|who have i met)\??$", re.I),
     "person", " knows "),
    (re.compile(r"^(?:what do i prefer|what(?:'s| is) my (?:preference|favorite|favourite)(?: language)?)\??$", re.I),
     "interest", " prefers "),
    (re.compile(r"^(?:what do i use|what(?: tools| tech| technologies) do i use)\??$", re.I),
     "technology", " uses "),
)


def _resolve_named_entity(name):
    name = (name or "").strip().strip("?. ")
    name = _ARTICLES.sub("", name).strip()
    if not name:
        return None
    hit = store.find_entity_by_name(name)
    if hit:
        return hit
    hits = keyword_search(name, limit=3)
    if hits and hits[0][0] >= 5:
        return hits[0][1]
    tokens = [t for t in query_terms(name) if t not in STOPWORDS]
    if not tokens:
        return None
    best = None
    for row in db.query("SELECT * FROM entities"):
        blob = (row["name"] or "").lower()
        if all(t in blob for t in tokens):
            if best is None or len(blob) < len(best["name"]):
                best = row
    return best


def _about_answer(query_text):
    m = _ABOUT.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return {
            "text": (
                f"I don't have a memory indicating that. Nothing in your brain "
                f"matches “{query_text}” yet."
            ),
            "status": "unknown",
            "sources": [],
        }
    facts = graph_facts_for_entity(ent["id"])
    sources = sources_for_facts(
        facts or [{"text": ent["name"], "entities": [ent["id"]],
                   "source_message_id": ent.get("source_message_id")}]
    )
    lines = [f'{ent["name"]} is stored as a {ent["type"]}.']
    if ent.get("description"):
        lines.append(ent["description"])
    if facts:
        lines.append("Known facts: " + "; ".join(f["text"] for f in facts[:8]) + ".")
    else:
        lines.append("No active relationships yet.")
    if sources and sources[0].get("snippet"):
        lines.append(f'Source: “{sources[0]["snippet"]}”')
    return {"text": " ".join(lines) + " (from stored memory)",
            "status": "known", "sources": sources}


def _path_answer(query_text):
    m = _PATH_Q.match((query_text or "").strip())
    if not m:
        return None
    left = m.group(1) or m.group(3)
    right = m.group(2) or m.group(4)
    a = _resolve_named_entity(left)
    b = _resolve_named_entity(right)
    if not a or not b:
        return {
            "text": (
                f"I don't have a memory indicating that. Nothing in your brain "
                f"matches “{query_text}” yet."
            ),
            "status": "unknown",
            "sources": [],
        }
    hops = graph.shortest_path(a["id"], b["id"])
    if not hops:
        return {
            "text": f"I don't have a stored path between {a['name']} and {b['name']}.",
            "status": "unknown",
            "sources": [],
        }
    names = {a["id"]: a["name"], b["id"]: b["name"]}
    bits = []
    for hop in hops:
        if "relation" not in hop:
            continue
        src = store.entity_row(hop["from"])
        tgt = store.entity_row(hop["to"])
        if src and tgt:
            names[src["id"]] = src["name"]
            names[tgt["id"]] = tgt["name"]
            bits.append(f'{src["name"]} {hop["relation"]} {tgt["name"]}')
    if not bits:
        return {
            "text": f"{a['name']} and {b['name']} are the same stored entity.",
            "status": "known",
            "sources": [],
        }
    facts = [{"text": t, "entities": [a["id"], b["id"]]} for t in bits]
    return {
        "text": " → ".join(bits) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
    }


def _unknown(query_text):
    return {
        "text": (
            f"I don't have a memory indicating that. Nothing in your brain "
            f"matches “{query_text}” yet."
        ),
        "status": "unknown",
        "sources": [],
        "final": True,
    }


def _list_intent_answer(query_text, filters=None):
    """Direct answers for where I live / who I know / what I prefer."""
    q = (query_text or "").strip()
    for rx, intent, _needle in _LIST_QUESTIONS:
        if not rx.match(q):
            continue
        facts = _filter_direct_facts(intent_facts(intent), filters)
        if not facts:
            return _unknown(query_text)
        return {
            "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
            "status": "known",
            "sources": sources_for_facts(facts),
            "final": True,
        }
    return None


def _uses_of_answer(query_text, filters=None):
    m = _USES_OF.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return _unknown(query_text)
    facts = [f for f in graph_facts_for_entity(ent["id"]) if " uses " in f["text"]]
    facts = _filter_direct_facts(facts, filters)
    if not facts:
        return {
            "text": f"I don't have a stored uses-relationship for {ent['name']}.",
            "status": "unknown",
            "sources": [],
            "final": True,
        }
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


_STOPPED_Q = re.compile(
    r"^(?:what did i stop|what have i stopped|what did i quit)(?:\s+\w+)?\??$",
    re.I,
)
_CHANGED_Q = re.compile(
    r"^(?:what changed(?: this week| recently)?|what did i change(?: this week| recently)?)\??$",
    re.I,
)
_USED_BY = re.compile(
    r"^(?:who uses|what uses|which (?:projects?|apps?|tools?) (?:use|uses))\s+(.+?)\??$",
    re.I,
)
_WHEN_Q = re.compile(
    r"^when did i (?:start |begin )?(?:learning |using |working (?:on |at )?"
    r"|living (?:in )?|meet(?:ing)? )?(.+?)\??$",
    re.I,
)
_OVERVIEW_Q = re.compile(
    r"^(?:what do i know|what do you know(?: about me)?|"
    r"summarize (?:my )?(?:brain|memory|memories)|"
    r"give me an overview|what(?:'s| is) in my (?:brain|memory))\??$",
    re.I,
)
_COUNT_Q = re.compile(
    r"^(?:how many|what(?:'s| is) the number of)\s+"
    r"(projects?|people|persons?|friends|technologies|entities|"
    r"memories|conversations|facts)"
    r"(?:\s+do i have|\s+have i|\s+are there|\s+do i store)?\??$",
    re.I,
)


def _used_by_answer(query_text, filters=None):
    """Inverse of uses-of: which stored things use this entity."""
    m = _USED_BY.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return _unknown(query_text)
    needle = f' uses {ent["name"]}'
    facts = [f for f in graph_facts_for_entity(ent["id"]) if needle in f.get("text", "")]
    facts = _filter_direct_facts(facts, filters)
    if not facts:
        return {
            "text": f'I don\'t have a stored uses-relationship pointing at {ent["name"]}.',
            "status": "unknown",
            "sources": [],
            "final": True,
        }
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


def _when_answer(query_text):
    """Date of the earliest stored fact about a named entity. Never invents."""
    m = _WHEN_Q.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return _unknown(query_text)
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT r.*, s.name sname, t.name tname FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE (r.source_id=? AND r.target_id=?) OR (r.source_id=? AND r.target_id=?) "
        "ORDER BY r.created_at ASC, r.id ASC",
        (uid, ent["id"], ent["id"], uid),
    )
    if rels:
        first = rels[0]
        when = (first.get("created_at") or "")[:10] or "an unknown date"
        extra = " (no longer active)" if first.get("status") != "active" else ""
        fact = {
            "text": f'{first["sname"]} {first["relation"]} {first["tname"]}',
            "entities": [first["source_id"], first["target_id"]],
            "source_message_id": first.get("source_message_id"),
            "confidence": first.get("confidence") or 0.8,
        }
        return {
            "text": (
                f'You first stored “{fact["text"]}” on {when}{extra}. '
                f"(from stored memory)"
            ),
            "status": "known",
            "sources": sources_for_facts([fact]),
            "final": True,
        }
    when = (ent.get("created_at") or "")[:10]
    if not when:
        return _unknown(query_text)
    return {
        "text": f'{ent["name"]} was first stored on {when}. (from stored memory)',
        "status": "known",
        "sources": sources_for_facts([{
            "text": ent["name"], "entities": [ent["id"]],
            "source_message_id": ent.get("source_message_id"),
        }]),
        "final": True,
    }


def _stopped_answer(query_text, filters=None):
    """Active history: superseded facts. Never invents."""
    if not _STOPPED_Q.match((query_text or "").strip()):
        return None
    rels = db.query(
        "SELECT r.source_message_id smid, s.name sname, t.name tname, r.relation rel, "
        "r.confidence c, r.source_id sid, r.target_id tid "
        "FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE r.status='superseded' ORDER BY r.created_at DESC LIMIT 12"
    )
    if not rels:
        return _unknown(query_text)
    facts = [{"text": f'{r["sname"]} {r["rel"]} {r["tname"]} (no longer active)',
              "confidence": r["c"], "entities": [r["sid"], r["tid"]],
              "source_message_id": r["smid"], "status": "superseded"} for r in rels]
    facts = _filter_direct_facts(facts, filters)
    if not facts:
        return _unknown(query_text)
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


def _changed_answer(query_text, filters=None):
    """Recent superseded / conflict / command memories from the last 7 days."""
    if not _CHANGED_Q.match((query_text or "").strip()):
        return None
    import datetime as _dt
    cutoff = (_dt.datetime.now(_dt.timezone.utc) - _dt.timedelta(days=7)).isoformat()
    mems = db.query(
        "SELECT * FROM memories WHERE kind IN ('superseded','conflict','command') "
        "AND created_at >= ? ORDER BY created_at DESC LIMIT 12",
        (cutoff,),
    )
    if not mems:
        return _unknown(query_text)
    facts = [{"text": m["text"], "confidence": m.get("confidence") or 0.8,
              "entities": json_loads(m.get("entity_ids")),
              "source_message_id": m.get("message_id")} for m in mems]
    facts = _filter_direct_facts(facts, filters)
    if not facts:
        return _unknown(query_text)
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }



def _overview_answer(query_text):
    """Compact grounded recap of active facts. Never invents."""
    if not _OVERVIEW_Q.match((query_text or "").strip()):
        return None
    facts, seen = [], set()
    for intent in ("learning", "project", "technology", "interest", "goal",
                   "person", "location", "organization"):
        for f in intent_facts(intent):
            key = f.get("text")
            if not key or key in seen:
                continue
            seen.add(key)
            facts.append(f)
    if not facts:
        return _unknown(query_text)
    return {
        "text": "; ".join(f["text"] for f in facts[:12]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


def _count_answer(query_text):
    """Count stored things. Reads SQLite only."""
    m = _COUNT_Q.match((query_text or "").strip())
    if not m:
        return None
    kind = (m.group(1) or "").lower()
    ents = store.all_entities()
    if kind.startswith("project"):
        n = sum(1 for e in ents if e["type"] == "project" and e.get("status", "active") == "active")
        label = "project" if n == 1 else "projects"
    elif kind.startswith("technolog"):
        n = sum(1 for e in ents if e["type"] == "technology" and e.get("status", "active") == "active")
        label = "technology" if n == 1 else "technologies"
    elif kind in ("people", "persons", "person", "friends"):
        n = sum(1 for e in ents if e["type"] == "person" and e.get("norm_name") != "user"
                and e.get("status", "active") == "active")
        label = "person" if n == 1 else "people"
    elif kind.startswith("entit"):
        n = len(ents)
        label = "entity" if n == 1 else "entities"
    elif kind.startswith("memor"):
        n = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
        label = "memory" if n == 1 else "memories"
    elif kind.startswith("conversation"):
        n = len(store.all_conversations())
        label = "conversation" if n == 1 else "conversations"
    else:
        n = len(store.all_relationships(active_only=True))
        label = "fact" if n == 1 else "facts"
    return {
        "text": f"You have {n} stored {label}. (from stored memory)",
        "status": "known",
        "sources": [],
        "final": True,
    }


def retrieve_answer(query_text, filters=None):
    """Deterministic retrieval. `final` answers skip the LLM composer."""
    direct = _direct_fact_answer(query_text, filters=filters)
    if direct is not None:
        out = dict(direct)
        out["final"] = True
        return out
    stopped = _stopped_answer(query_text, filters=filters)
    if stopped is not None:
        return stopped
    changed = _changed_answer(query_text, filters=filters)
    if changed is not None:
        return changed
    listed = _list_intent_answer(query_text, filters=filters)
    if listed is not None:
        return listed
    uses = _uses_of_answer(query_text, filters=filters)
    if uses is not None:
        return uses
    used_by = _used_by_answer(query_text, filters=filters)
    if used_by is not None:
        return used_by
    when = _when_answer(query_text)
    if when is not None:
        return when
    overview = _overview_answer(query_text)
    if overview is not None:
        return overview
    counted = _count_answer(query_text)
    if counted is not None:
        return counted
    about = _about_answer(query_text)
    if about is not None:
        out = dict(about)
        out["final"] = True
        return out
    path = _path_answer(query_text)
    if path is not None:
        out = dict(path)
        out["final"] = True
        return out
    return {"final": False, "retrieval": search(query_text, filters=filters)}


def answer(query_text, model=None, context=None, filters=None):
    model = model or config.DEFAULT_LLM_MODEL
    retrieved = retrieve_answer(query_text, filters=filters)
    if retrieved.get("final"):
        return {k: retrieved[k] for k in ("text", "status", "sources") if k in retrieved}
    return compose_answer(query_text, retrieved["retrieval"], model, context)


def _intent_relevant_facts(facts, intent):
    keys = {
        "learning": (" learning ",),
        "project": ("project ",),
        "technology": (" uses ",),
        "interest": (" prefers ", " interested_in ", " likes "),
        "goal": (" wants ",),
        "person": ("person ", " knows "),
        "location": (" lives_in ",),
        "organization": (" works_at ",),
    }.get(intent)
    if not keys:
        return list(facts)
    return [f for f in facts if any(k in f" {f.get('text', '')} " or k.strip() in (f.get("text") or "") for k in keys)]


def _status_of(res, query_text=""):
    ents = res["entities"]
    facts = res["facts"]
    intent = res["intent"]
    if not ents and not facts:
        return "unknown"
    if intent and facts:
        relevant = _intent_relevant_facts(facts, intent)
        if relevant:
            top_conf = relevant[0].get("confidence") or 0.0
            return "known" if top_conf >= 0.6 else "uncertain"
        return "uncertain" if ents else "unknown"
    has_name = any((e.get("keyword") or 0) >= 1 for e in ents)
    if not has_name:
        return "unknown"
    top = ents[0]["score"] if ents else 0.0
    if top >= 2.0:
        return "known"
    return "uncertain"


def _knowledge_names(res, query_text=""):
    """Surface forms the composer is allowed to mention."""
    names = {"user", "i", "me"}
    for e in res.get("entities") or []:
        n = store.normalize_name(e.get("name"))
        if n:
            names.add(n)
    for f in res.get("facts") or []:
        for part in re.findall(r"[A-Za-z0-9][A-Za-z0-9+.#\-]{1,40}", f.get("text") or ""):
            n = store.normalize_name(part)
            if n:
                names.add(n)
    for t in query_terms(query_text):
        names.add(t)
    return names


def reply_is_grounded(text, res, query_text=""):
    """False if the reply names a stored entity or known tech absent from knowledge."""
    blob = (text or "").lower()
    if not blob.strip():
        return False
    allowed = _knowledge_names(res, query_text)
    for e in store.all_entities():
        n = e.get("norm_name") or ""
        if not n or n in allowed or len(n) < 3:
            continue
        if re.search(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])", blob):
            return False
    for key, display in fallback.TECH.items():
        dn = display.lower()
        if dn in allowed or key in allowed:
            continue
        if re.search(r"(?<![a-z0-9])" + re.escape(key) + r"(?![a-z0-9])", blob):
            return False
    return True


def _composer_messages(query_text, res, context=None):
    entities = res["entities"]
    facts = res["facts"]
    context_lines = []
    for e in entities[:8]:
        context_lines.append(
            f'- entity "{e["name"]}" (type: {e["type"]}, confidence {round(e["confidence"], 2)}): '
            f'{e["description"] or ""}')
    for f in facts[:12]:
        context_lines.append(f'- fact: {f["text"]} (confidence {round(f["confidence"], 2)})')
    if context:
        context_lines.append("- recent conversation:\n" + context)
    grounding = "\n".join(context_lines)
    prompt = (
        "You are the memory of a personal Second Brain. Answer the user's "
        "question using ONLY the knowledge below. Be concise and factual. "
        "If the knowledge does not contain the answer, say so explicitly — "
        "never invent personal memories. Only mention entities that appear "
        "in KNOWLEDGE. If the answer is based on low-confidence memories, "
        "say 'I believe' or 'possibly'.\n\n"
        f"KNOWLEDGE:\n{grounding}\n\nQUESTION: {query_text}\nANSWER:")
    return [
        {"role": "system",
         "content": "You are a helpful personal knowledge assistant. Answer only from the provided knowledge."},
        {"role": "user", "content": prompt},
    ]


def compose_answer(query_text, res, model, context=None):
    sources = res.get("sources", [])
    status = _status_of(res, query_text)

    if status == "unknown":
        return {"text": f"I don't have a memory indicating that. Nothing in your brain matches \u201c{query_text}\u201d yet.",
                "status": "unknown", "sources": []}

    if ollama.available():
        try:
            text = ollama.chat(model, _composer_messages(query_text, res, context),
                               temperature=0.2).strip()
            if text and reply_is_grounded(text, res, query_text):
                return {"text": text, "status": status, "sources": sources}
        except Exception:
            pass

    text = _fallback_answer(query_text, res, status)
    return {"text": text, "status": status, "sources": sources}


def compose_answer_stream(query_text, res, model, context=None):
    """Yield reply chunks after retrieval. Falls back to one complete chunk."""
    status = _status_of(res, query_text)
    if status == "unknown":
        yield f"I don't have a memory indicating that. Nothing in your brain matches \u201c{query_text}\u201d yet."
        return
    if ollama.available():
        try:
            acc = []
            for piece in ollama.chat_stream(
                model, _composer_messages(query_text, res, context), temperature=0.2,
            ):
                if piece:
                    acc.append(piece)
            text = "".join(acc).strip()
            if text and reply_is_grounded(text, res, query_text):
                yield text
                return
        except Exception:
            pass
    yield _fallback_answer(query_text, res, status)


def _fallback_answer(query_text, res, status):
    intent = res["intent"]
    entities = res["entities"]
    facts = res["facts"]

    names = [e["name"] for e in entities if (e.get("keyword") or 0) >= 1] or \
            [e["name"] for e in entities]
    if status == "uncertain":
        if names:
            return f"I have a lower-confidence memory suggesting {', '.join(names)}. Treat this as tentative."
        return "I'm not certain about that — my memory is incomplete here."

    if intent == "project":
        projs = [f["text"] for f in facts if f["text"].startswith("project ")]
        text = ("You're working on: " + ", ".join(p[8:] for p in projs) + "."
                if projs else f"Here's what I have: {', '.join(names)}.")
    elif intent == "learning":
        learns = [f["text"] for f in facts if " learning " in f["text"]]
        text = ("You're learning: " + "; ".join(learns) + "."
                if learns else f"Here's what I have: {', '.join(names)}.")
    elif intent in ("interest", "preference"):
        pref = [f["text"] for f in facts if " prefers " in f["text"] or " interested_in " in f["text"]]
        text = ("; ".join(pref) + "." if pref else f"Here's what I have: {', '.join(names)}.")
    elif intent == "goal":
        goals = [f["text"] for f in facts if " wants " in f["text"]]
        text = ("; ".join(goals) + "." if goals else f"Here's what I have: {', '.join(names)}.")
    elif intent == "organization":
        jobs = [f["text"] for f in facts if " works_at " in f["text"]]
        text = ("; ".join(jobs) + "." if jobs else f"Here's what I have: {', '.join(names)}.")
    elif intent == "location":
        locs = [f["text"] for f in facts if " lives_in " in f["text"]]
        text = ("; ".join(locs) + "." if locs else f"Here's what I have: {', '.join(names)}.")
    else:
        detail = ". ".join(f["text"] for f in facts[:5])
        text = f"I found: {', '.join(names)}. " + (detail + "." if detail else "")

    text += " (from stored memory)"
    return text


def is_question(text):
    t = text.strip()
    if not t:
        return False
    if t.endswith("?"):
        return True
    lower = t.lower()
    interrogatives = ("what", "who", "which", "when", "where", "how", "do i", "am i",
                      "have i", "did i", "list", "tell me", "show me",
                      "whats", "what's", "give me", "summarize", "what do you",
                      "what are", "what is", "do you", "can you tell",
                      "what do i know")
    return lower.startswith(interrogatives)
