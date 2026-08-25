"""Automatic memory extraction pipeline.

user message
    -> trivial-message filter
    -> LLM structured extraction (or rule-based fallback)
    -> JSON parse + validation
    -> entity / relation normalization
    -> duplicate detection + merging
    -> confidence check + conflict/supersession handling
    -> persist to graph + timeline
"""
import json
import re

from . import config, db, fallback, ollama, store

EXTRACTION_SYSTEM_PROMPT = """You are a knowledge-extraction engine for a personal "Second Brain".

Extract durable facts from the user's message: entities and the relationships
between them. Output ONLY a single JSON object, nothing else.

Entity types (choose the MOST SPECIFIC one, only if confident; otherwise use
"concept"): person, project, technology, topic, skill, goal, interest,
preference, fact, location, organization, concept, task, event.

Relationship types (use EXACTLY these): learning, uses, knows, likes, created,
interested_in, related_to, wants, works_on, prefers, works_at, lives_in,
located_in, member_of.

Rules:
- The person speaking is ALWAYS represented by the entity name "User".
  ("I", "me", "my" all refer to "User".)
- Only extract meaningful, lasting knowledge. Ignore greetings, small talk,
  thanks, jokes and chit-chat (then return empty lists).
- Merge near-identical concepts into a single entity; do not duplicate.
- Keep entity names short and canonical (e.g. "Python", "Next.js", "AI agents").
- Give every entity and relationship a confidence between 0.0 and 1.0.
- If the user says they STOPPED doing something ("I stopped learning Rust",
  "I no longer use X", "I switched from X to Y"), put the OUTDATED fact in a
  "stops" list, NOT in "relationships".

Examples:
"I am learning Python" ->
  {"entities":[{"name":"User","type":"person","description":"","confidence":1.0},
   {"name":"Python","type":"technology","description":"","confidence":0.95}],
   "relationships":[{"source":"User","target":"Python","relation":"learning","confidence":0.95}],
   "stops":[]}

"I stopped learning Rust" ->
  {"entities":[],"relationships":[],
   "stops":[{"source":"User","target":"Rust","relation":"learning"}]}

"I prefer Python over Java" ->
  {"entities":[{"name":"Python","type":"technology","description":"","confidence":0.9}],
   "relationships":[{"source":"User","target":"Python","relation":"prefers","confidence":0.9}],
   "stops":[]}

"hello" -> {"entities":[],"relationships":[],"stops":[]}

Return JSON in exactly this shape:
{"entities":[{"name":"...","type":"...","description":"...","confidence":0.9}],
 "relationships":[{"source":"...","target":"...","relation":"...","confidence":0.9}],
 "stops":[{"source":"...","target":"...","relation":"..."}]}
"""


def _llm_extract(text, model):
    resp = ollama.chat(
        model,
        messages=[
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.0,
        format_json=True,
    )
    return _parse_json(resp)


def _parse_json(resp):
    if not resp:
        return None
    try:
        return json.loads(resp)
    except ValueError:
        pass
    m = re.search(r"\{.*\}", resp, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except ValueError:
            pass
    return None


def confidence_threshold():
    return db.get_setting_float("confidence_threshold", config.DEFAULT_CONFIDENCE_THRESHOLD)


def extract(text, model=None, source_message_id=None, demo=False):
    """Run the full extraction pipeline. Returns a dict summary of updates."""
    if model is None:
        model = db.get_setting("llm_model", config.DEFAULT_LLM_MODEL)
    demo_meta = {"demo": True} if demo else None
    result = {
        "used_fallback": False, "entities": [], "relationships": [],
        "entity_updates": [], "relationship_updates": [], "trivial": False,
        "memories": [], "remembered": [], "superseded": [],
    }

    if fallback.is_trivial(text):
        result["trivial"] = True
        return result

    data = None
    if ollama.available():
        try:
            data = _llm_extract(text, model)
        except Exception:
            data = None
    if not data:
        data = fallback.extract_with_rules(text)
        result["used_fallback"] = True

    data = _augment_from_text(text, data or {})
    entities = data.get("entities", []) or []
    relationships = data.get("relationships", []) or []
    stops = data.get("stops", []) or []

    store.ensure_user_entity()
    threshold = confidence_threshold()
    exclusive_relations = {"prefers", "lives_in", "works_at"}

    # ---- Entities ------------------------------------------------------
    id_by_name = {}
    for ent in entities:
        try:
            name = (ent.get("name") or "").strip()
            etype = ent.get("type") or "concept"
            desc = ent.get("description") or ""
            conf = float(ent.get("confidence", 0.8))
        except (AttributeError, ValueError):
            continue
        if not name or conf < threshold:
            continue
        if normalize_me(name):
            eid = store.ensure_user_entity()
            id_by_name[name.lower()] = eid
            continue
        embedding = store.embed_text(name + " " + desc)
        eid, created = store.upsert_entity(
            name, etype, desc, confidence=conf, embedding=embedding,
            source_message_id=source_message_id, meta=demo_meta,
        )
        if eid is None:
            continue
        id_by_name[name.lower()] = eid
        row = store.entity_row(eid)
        result["entities"].append({"id": eid, "name": row["name"], "type": row["type"],
                                   "created": created})
        if created:
            mem = f'New {row["type"]} "{row["name"]}" detected'
            store.add_memory("entity", mem, entity_ids=[eid], message_id=source_message_id,
                             confidence=conf)
            result["memories"].append(mem)
            result["entity_updates"].append(f'+ New {row["type"]} "{row["name"]}"')
            result["remembered"].append(
                {"kind": "entity", "name": row["name"], "type": row["type"],
                 "entity_id": eid, "confidence": round(conf, 3)})

    # ---- Relationships ------------------------------------------------
    for rel in relationships:
        try:
            src = (rel.get("source") or "").strip()
            tgt = (rel.get("target") or "").strip()
            relation_raw = (rel.get("relation") or "").strip()
            conf = float(rel.get("confidence", 0.8))
        except (AttributeError, ValueError):
            continue
        if not src or not tgt or conf < threshold:
            continue

        relation, swap = store.normalize_relation(relation_raw)
        if swap:
            src, tgt = tgt, src

        sid = _resolve_entity(src, conf, id_by_name, source_message_id, demo_meta)
        tid = _resolve_entity(tgt, conf, id_by_name, source_message_id, demo_meta)
        if sid is None or tid is None or sid == tid:
            continue

        # Exclusive facts: a new prefers / lives_in / works_at replaces the old one.
        if relation in exclusive_relations:
            superseded_ids = store.supersede_relations_of_type(sid, relation,
                                                               except_target_id=tid)
            for old_id in superseded_ids:
                old = store.entity_row(old_id)
                if old:
                    store.add_memory(
                        "conflict",
                        f'{relation} changed: now {store.entity_row(tid)["name"]} (was {old["name"]})',
                        entity_ids=[tid, old_id], message_id=source_message_id,
                        confidence=conf,
                    )
                    result["superseded"].append(old["name"])

        existed = store.relationship_exists(sid, tid, relation)
        store.add_relationship(sid, tid, relation, confidence=conf, source_message_id=source_message_id)
        srow, trow = store.entity_row(sid), store.entity_row(tid)
        if not existed:
            label = f'{srow["name"]} → {relation} → {trow["name"]}'
            store.add_memory("relationship", label, entity_ids=[sid, tid],
                             message_id=source_message_id, confidence=conf)
            result["memories"].append(label)
            result["relationship_updates"].append(f"+ {label}")
            result["remembered"].append(
                {"kind": "relationship", "source": srow["name"], "relation": relation,
                 "target": trow["name"], "entity_id": tid,
                 "source_id": sid, "target_id": tid,
                 "confidence": round(conf, 3)})
        result["relationships"].append(
            {"source": sid, "target": tid, "relation": relation, "new": not existed}
        )

    # ---- Stops / supersession ------------------------------------------
    for stop in stops:
        try:
            src = (stop.get("source") or "").strip()
            tgt = (stop.get("target") or "").strip()
            relation_raw = (stop.get("relation") or "").strip()
        except AttributeError:
            continue
        if not src or not tgt:
            continue
        relation, swap = store.normalize_relation(relation_raw)
        if swap:
            src, tgt = tgt, src
        if normalize_me(src):
            sid = store.ensure_user_entity()
        else:
            sid = id_by_name.get(src.lower()) or _resolve_entity(src, 0.6, id_by_name, source_message_id, demo_meta)
        tid = _resolve_entity(tgt, 0.6, id_by_name, source_message_id, demo_meta)
        if sid is None or tid is None:
            continue
        changed = store.supersede_relationship(sid, tid, relation)
        if changed:
            srow, trow = store.entity_row(sid), store.entity_row(tid)
            label = f'{srow["name"]} {relation} {trow["name"]}'
            store.add_memory("superseded", f'Superseded: {label}',
                             entity_ids=[sid, tid], message_id=source_message_id,
                             confidence=0.9)
            result["superseded"].append(label)
            result["relationship_updates"].append(f"~ {label} (no longer active)")

    return result


def _resolve_entity(name, conf, id_by_name, source_message_id=None, demo_meta=None):
    if normalize_me(name):
        return store.ensure_user_entity()
    eid = id_by_name.get(name.lower())
    if eid is not None:
        return eid
    emb = store.embed_text(name)
    eid, _ = store.upsert_entity(name, "concept", "", confidence=conf, embedding=emb,
                                 source_message_id=source_message_id, meta=demo_meta)
    id_by_name[name.lower()] = eid
    return eid


def normalize_me(name):
    return store.normalize_name(name) in ("i", "me", "my", "myself", "mine", "user")


# Reliability net: even if the LLM misses a stop/switch, the text itself is
# enough to supersede contradictory active facts.
_SWITCH_RE = re.compile(
    r"(?:switched|switching|moved)\s+from\s+(.+?)\s+to\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_INSTEAD_RE = re.compile(
    r"(?:now|instead)\s+(?:learning|using|studying)?\s*(.+?)\s+(?:instead of|rather than)\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_STOP_RE = re.compile(
    r"(?:stopped|no longer|quit|gave up on|dropped)\s+"
    r"(?:learning|studying|using|working on|practicing|learn|use)\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_PREFER_INSTEAD_RE = re.compile(
    r"prefer(?:s)?\s+(.+?)\s+(?:instead of|rather than|over)\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)


def _augment_from_text(text, data):
    """Add stops (and missing entities) detected deterministically from the text."""
    data = dict(data)
    data.setdefault("entities", [])
    data.setdefault("relationships", [])
    data.setdefault("stops", [])
    stops = list(data["stops"])

    def _add_stop(target, relation):
        target = (target or "").strip().strip("\"'")
        if not target or len(target) < 2:
            return
        stops.append({"source": "User", "target": target, "relation": relation})

    for m in _SWITCH_RE.finditer(text):
        old, new = m.group(1).strip(), m.group(2).strip()
        _add_stop(old, "learning")
        _add_stop(old, "uses")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "prefers", "confidence": 0.9}
            )
            data["entities"].append(
                {"name": new, "type": "technology", "description": "", "confidence": 0.9}
            )
    for m in _INSTEAD_RE.finditer(text):
        new, old = m.group(1).strip(), m.group(2).strip()
        _add_stop(old, "learning")
        _add_stop(old, "uses")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "learning", "confidence": 0.9}
            )
    for m in _STOP_RE.finditer(text):
        _add_stop(m.group(1).strip(), "learning")
        _add_stop(m.group(1).strip(), "uses")
    for m in _PREFER_INSTEAD_RE.finditer(text):
        new, old = m.group(1).strip(), m.group(2).strip()
        _add_stop(old, "prefers")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "prefers", "confidence": 0.9}
            )
            data["entities"].append(
                {"name": new, "type": "preference", "description": "", "confidence": 0.9}
            )

    seen, dedup = set(), []
    for s in stops:
        key = (
            (s.get("source") or "").lower(),
            (s.get("target") or "").lower(),
            (s.get("relation") or "").lower(),
        )
        if key in seen or not key[1]:
            continue
        seen.add(key)
        dedup.append(s)
    data["stops"] = dedup
    return data
