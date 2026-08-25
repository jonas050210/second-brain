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

from . import config, db, graph, ollama, store

INTENT_KEYWORDS = {
    "project": ["project", "projects", "app", "apps", "building", "startup", "working on", "working"],
    "learning": ["learn", "learning", "study", "studying"],
    "technology": ["technology", "tech", "technologies", "stack", "tools", "using"],
    "person": ["people", "person", "friends", "friend", "who", "met"],
    "goal": ["goal", "goals", "plan", "want", "objective", "aiming"],
    "interest": ["interest", "interested", "hobbies", "like", "enjoy", "prefer", "preference"],
    "location": ["live", "located", "based"],
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


def json_loads(s):
    try:
        return json.loads(s or "[]")
    except ValueError:
        return []


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
    terms = [t for t in re_tokenize(query_text) if len(t) > 2 and t not in STOPWORDS]
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
        for eid in f.get("entities", []):
            ent = store.entity_row(eid)
            if not ent:
                continue
            src = _source_for_message(ent.get("source_message_id"))
            key = (ent["name"], ent["id"])
            if key in seen:
                continue
            seen.add(key)
            sources.append({
                "entity_id": ent["id"], "name": ent["name"], "type": ent["type"],
                "message_id": src["message_id"] if src else None,
                "conversation_title": src["conversation_title"] if src else None,
                "created_at": (src["created_at"] if src else None) or ent["created_at"],
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
        # recency
        rec["score"] += _recency_boost(rec["entity"])
        if _is_recent(rec["entity"]):
            rec["reasons"].append("recent")
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

    return {"intent": intent, "entities": entities, "facts": dedup,
            "sources": sources_for_facts(dedup)}


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
    return True


# --------------------------------------------------------------------------
# Grounded answer (KNOWN / UNKNOWN / UNCERTAIN)
# --------------------------------------------------------------------------

def answer(query_text, model=None, context=None, filters=None):
    model = model or config.DEFAULT_LLM_MODEL
    res = search(query_text, filters=filters)
    return compose_answer(query_text, res, model, context)


def _status_of(res):
    ents = res["entities"]
    facts = res["facts"]
    intent = res["intent"]
    if not ents and not facts:
        return "unknown"
    if intent and facts:
        # Check if the top fact is actually intent-relevant and confident.
        top_conf = facts[0]["confidence"] if facts else 0.0
        if top_conf >= 0.6:
            return "answered"
        return "uncertain"
    has_name = any((e.get("keyword") or 0) >= 1 for e in ents)
    if not has_name:
        return "unknown"
    top = ents[0]["score"] if ents else 0.0
    if top >= 2.0:
        return "answered"
    return "uncertain"


def compose_answer(query_text, res, model, context=None):
    intent = res["intent"]
    entities = res["entities"]
    facts = res["facts"]
    sources = res.get("sources", [])
    status = _status_of(res)

    if status == "unknown":
        return {"text": f"I don't have a memory indicating that. Nothing in your brain matches \u201c{query_text}\u201d yet.",
                "status": "unknown", "sources": []}

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

    if ollama.available():
        prompt = (
            "You are the memory of a personal Second Brain. Answer the user's "
            "question using ONLY the knowledge below. Be concise and factual. "
            "If the knowledge does not contain the answer, say so explicitly — "
            "never invent personal memories. If the answer is based on "
            "low-confidence memories, say 'I believe' or 'possibly'.\n\n"
            f"KNOWLEDGE:\n{grounding}\n\nQUESTION: {query_text}\nANSWER:")
        try:
            text = ollama.chat(model, [
                {"role": "system",
                 "content": "You are a helpful personal knowledge assistant. Answer only from the provided knowledge."},
                {"role": "user", "content": prompt},
            ], temperature=0.2).strip()
            return {"text": text, "status": status, "sources": sources}
        except Exception:
            pass

    text = _fallback_answer(query_text, res, status)
    return {"text": text, "status": status, "sources": sources}


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
                      "have i", "did i", "list", "tell me", "show me", "remember",
                      "whats", "what's", "give me", "summarize", "what do you",
                      "what are", "what is", "do you", "can you tell")
    return lower.startswith(interrogatives)
