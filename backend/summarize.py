"""Memory consolidation / summarization.

Detects clusters of related memories (by shared entities) and produces a
deterministic summary. The original memories are never deleted — a summary is a
new `summary` memory whose `meta` references the source memory ids it was
generated from.

Uses Ollama only to *polish* wording when available and genuinely useful;
otherwise falls back to a deterministic template, so consolidation always works
locally.
"""
import json

from . import config, db, ollama, store

MIN_MEMORIES_TO_SUMMARIZE = 3


def find_consolidation_candidates(min_shared=MIN_MEMORIES_TO_SUMMARIZE, limit=20):
    """Find clusters of memories that share an entity and are ripe for
    summarization. Returns a list of {entity, memory_ids, count}."""
    memories = db.query(
        "SELECT * FROM memories WHERE kind IN ('entity','relationship','update') "
        "ORDER BY created_at DESC LIMIT 500")
    # Map entity_id -> memory ids.
    clusters = {}
    for m in memories:
        try:
            ids = json.loads(m["entity_ids"] or "[]")
        except ValueError:
            ids = []
        for eid in ids:
            clusters.setdefault(eid, []).append(m["id"])

    out = []
    for eid, mids in clusters.items():
        if len(mids) < min_shared:
            continue
        ent = store.entity_row(eid)
        if not ent:
            continue
        # Skip entities already summarized recently.
        if _already_summarized(mids):
            continue
        out.append({"entity_id": eid, "entity_name": ent["name"],
                    "entity_type": ent["type"], "memory_ids": sorted(set(mids))[:30],
                    "count": len(set(mids))})
    out.sort(key=lambda x: -x["count"])
    return out[:limit]


def _already_summarized(memory_ids):
    """Avoid re-summarizing a cluster that a summary already references."""
    ids = set(memory_ids)
    rows = db.query("SELECT meta FROM memories WHERE kind='summary'")
    for r in rows:
        try:
            meta = json.loads(r["meta"] or "{}")
        except ValueError:
            continue
        refs = set(meta.get("source_memory_ids", []))
        if refs and ids and len(ids & refs) >= min(3, len(ids)):
            return True
    return False


def summarize_entity(entity_id, memory_ids=None):
    """Generate a summary for an entity. Returns the created summary memory."""
    ent = store.entity_row(entity_id)
    if not ent:
        return {"ok": False, "error": "entity not found"}

    if memory_ids is None:
        cands = find_consolidation_candidates(min_shared=1)
        target = next((c for c in cands if c["entity_id"] == entity_id), None)
        memory_ids = target["memory_ids"] if target else []

    mems = [db.query_one("SELECT * FROM memories WHERE id=?", (mid,)) for mid in memory_ids]
    mems = [m for m in mems if m]

    facts = store_relationships_readable(entity_id)

    # Build a deterministic summary body.
    parts = [f'{ent["name"]} is a {ent["type"]}.']
    if ent.get("description"):
        parts.append(ent["description"])
    if facts:
        parts.append("Key facts: " + "; ".join(facts[:8]) + ".")
    if mems:
        parts.append(f"Recorded across {len(mems)} memory events.")

    text = " ".join(parts)

    # Optionally polish wording with Ollama (only when useful and grounded).
    if ollama.available():
        try:
            prompt = (
                "Summarize the following memory of a personal knowledge graph "
                "into 2-3 concise, factual sentences. Do not invent anything.\n\n"
                f"{text}")
            polished = ollama.chat(
                db.get_setting("llm_model", config.DEFAULT_LLM_MODEL),
                [{"role": "system", "content": "You summarize personal memories factually."},
                 {"role": "user", "content": prompt}],
                temperature=0.3).strip()
            if polished and _summary_is_grounded(polished, ent, facts, mems):
                text = polished
        except Exception:
            pass

    summary_id = store.add_memory(
        "summary", text, entity_ids=[entity_id],
        confidence=max([ent["confidence"], 0.7]),
    )
    db.execute("UPDATE memories SET meta=? WHERE id=?",
               (json.dumps({"source_memory_ids": memory_ids}), summary_id))
    return {"ok": True, "summary_id": summary_id, "text": text,
            "entity": ent["name"], "source_memory_ids": memory_ids}


def store_relationships_readable(entity_id):
    """Readable active relationships for an entity (canonical direction)."""
    rels = db.query(
        "SELECT s.name sname, t.name tname, r.relation rel, r.source_id sid "
        "FROM relationships r JOIN entities s ON s.id=r.source_id "
        "JOIN entities t ON t.id=r.target_id "
        "WHERE (r.source_id=? OR r.target_id=?) AND r.status='active'",
        (entity_id, entity_id))
    out = []
    for r in rels:
        if r["sid"] == entity_id:
            out.append(f'{r["sname"]} {r["rel"]} {r["tname"]}')
        else:
            out.append(f'{r["tname"]} {r["rel"]} {r["sname"]}')
    return out


def _summary_is_grounded(text, ent, facts, mems=None):
    """False if the polish invents a stored entity name not in this summary."""
    from . import search
    allowed_facts = list(facts or [])
    for m in mems or []:
        if m.get("text"):
            allowed_facts.append(m["text"])
    res = {
        "entities": [{"name": (ent or {}).get("name") or ""}],
        "facts": [{"text": t} for t in allowed_facts],
    }
    return search.reply_is_grounded(text, res, (ent or {}).get("name") or "")


def summarize_conversation(cid):
    """Write a recap memory for one chat. Never deletes messages."""
    conv = store.conversation_row(cid)
    if not conv:
        return {"ok": False, "error": "conversation not found"}
    msgs = store.conversation_messages(cid)
    user_msgs = [m for m in msgs if m.get("role") == "user" and (m.get("content") or "").strip()]
    if not user_msgs:
        return {"ok": False, "error": "empty conversation"}
    mids = [m["id"] for m in msgs if m.get("id") is not None]
    facts, eids = [], []
    if mids:
        placeholders = ",".join("?" for _ in mids)
        rels = db.query(
            "SELECT s.name sname, t.name tname, r.relation rel, r.source_id sid, r.target_id tid "
            "FROM relationships r JOIN entities s ON s.id=r.source_id "
            "JOIN entities t ON t.id=r.target_id "
            f"WHERE r.source_message_id IN ({placeholders}) AND r.status='active'",
            tuple(mids),
        )
        for r in rels:
            facts.append(f'{r["sname"]} {r["rel"]} {r["tname"]}')
            eids.extend([r["sid"], r["tid"]])
    title = conv.get("title") or "untitled"
    turns = len(user_msgs)
    parts = [f'Conversation “{title}” ({turns} user turn{"s" if turns != 1 else ""}).']
    if facts:
        parts.append("Stored facts: " + "; ".join(facts[:12]) + ".")
    else:
        parts.append("No durable facts were stored from this conversation.")
    text = " ".join(parts)
    unique_eids = list(dict.fromkeys(eids))[:20]
    summary_id = store.add_memory(
        "summary", text, entity_ids=unique_eids, confidence=0.85,
        meta={"conversation_id": cid, "source_message_ids": mids[:80]},
    )
    return {
        "ok": True,
        "summary_id": summary_id,
        "text": text,
        "conversation_id": cid,
        "facts": facts[:12],
        "messages_kept": len(msgs),
    }


def summarize_all(limit=10):
    """Summarize the top consolidation candidates. Returns a list of results."""
    candidates = find_consolidation_candidates(limit=limit)
    results = []
    for c in candidates:
        r = summarize_entity(c["entity_id"], memory_ids=c["memory_ids"])
        results.append(r)
    return results
