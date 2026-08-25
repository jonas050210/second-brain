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

    # Optionally polish wording with Ollama (only when useful).
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
            if polished:
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


def summarize_all(limit=10):
    """Summarize the top consolidation candidates. Returns a list of results."""
    candidates = find_consolidation_candidates(limit=limit)
    results = []
    for c in candidates:
        r = summarize_entity(c["entity_id"], memory_ids=c["memory_ids"])
        results.append(r)
    return results
