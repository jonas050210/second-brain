"""Graph export / import (JSON + Markdown).

Export includes entities, relationships, memories, messages, conversations and
settings (no secrets — this app has none). Import validates the payload before
touching the database, and supports two modes:
  - merge   : upsert entities / add relationships without deleting anything
  - replace : wipe the database first (with explicit confirmation)
"""
import json
from datetime import datetime

from . import config, db, store

EXPORT_FORMAT = "second-brain"
EXPORT_VERSION = 1


def _json_default(o):
    if isinstance(o, (datetime,)):
        return o.isoformat()
    return str(o)


def full_export():
    """Serialize the entire knowledge base to a JSON-serializable dict."""
    entities = store.all_entities()
    relationships = store.all_relationships()
    memories = db.query("SELECT * FROM memories ORDER BY id")
    messages = db.query("SELECT * FROM messages ORDER BY id")
    conversations = db.query("SELECT * FROM conversations ORDER BY id")
    settings = db.all_settings()
    # Strip nothing sensitive — there are no secrets, but keep only real keys.
    safe_settings = {k: v for k, v in settings.items()
                     if k not in ("current_conversation_id",)}
    return {
        "format": EXPORT_FORMAT,
        "version": EXPORT_VERSION,
        "exported_at": db.utcnow(),
        "counts": {
            "entities": len(entities), "relationships": len(relationships),
            "memories": len(memories), "messages": len(messages),
            "conversations": len(conversations),
        },
        "settings": safe_settings,
        "entities": entities,
        "relationships": relationships,
        "memories": memories,
        "messages": messages,
        "conversations": conversations,
    }


def export_json():
    return json.dumps(full_export(), default=_json_default, indent=2)


def export_markdown():
    """Human-readable Markdown export of the knowledge graph."""
    data = full_export()
    lines = ["# Second Brain — Knowledge Export", ""]
    lines.append(f"Exported: {data['exported_at']}")
    lines.append("")
    lines.append("## Entities")
    lines.append("")
    for e in data["entities"]:
        flags = []
        if e.get("pinned"):
            flags.append("pinned")
        if e.get("important"):
            flags.append("important")
        if e.get("status") != "active":
            flags.append(e.get("status", "active"))
        suffix = f"  _({', '.join(flags)})_" if flags else ""
        lines.append(f"- **{e['name']}** ({e['type']}, confidence {e['confidence']:.2f}){suffix}")
        if e.get("description"):
            lines.append(f"  - {e['description']}")
        aliases = json.loads(e.get("aliases") or "[]")
        if aliases:
            lines.append(f"  - aliases: {', '.join(aliases)}")
    lines.append("")
    lines.append("## Relationships")
    lines.append("")
    name = {e["id"]: e["name"] for e in data["entities"]}
    for r in data["relationships"]:
        s = name.get(r["source_id"], f"#{r['source_id']}")
        t = name.get(r["target_id"], f"#{r['target_id']}")
        status = "" if r.get("status") == "active" else f" _({r['status']})_"
        lines.append(f"- {s} \u2192 **{r['relation']}** \u2192 {t} (confidence {r['confidence']:.2f}){status}")
    lines.append("")
    lines.append("## Memory timeline")
    lines.append("")
    for m in data["memories"]:
        lines.append(f"- `{m['created_at'][:16]}` [{m['kind']}] {m['text']}")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Import
# --------------------------------------------------------------------------

def validate_payload(data):
    """Validate a JSON export before it touches the database. Returns
    (ok, error_message)."""
    if not isinstance(data, dict):
        return False, "export must be a JSON object"
    if data.get("format") != EXPORT_FORMAT:
        return False, f"unrecognized format (expected '{EXPORT_FORMAT}')"
    for key in ("entities", "relationships"):
        if key not in data or not isinstance(data[key], list):
            return False, f"missing or invalid '{key}' list"
    for e in data["entities"]:
        if not isinstance(e, dict) or not e.get("name"):
            return False, "entities must be objects with a 'name'"
        if not isinstance(e.get("confidence", 0.8), (int, float)):
            return False, "entity 'confidence' must be a number"
    for r in data["relationships"]:
        if not isinstance(r, dict) or "source_id" not in r or "target_id" not in r \
                or "relation" not in r:
            return False, "relationships must have source_id, target_id and relation"
    return True, None


def import_merge(data):
    """Merge-import: upsert entities (by name) and add relationships.
    Preserves existing data. Returns a summary."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    id_map = {}  # imported source_id -> new local entity id
    created, merged = 0, 0
    for e in data["entities"]:
        name = e["name"].strip()
        if not name or store.normalize_name(name) in ("user", "i", "me"):
            continue
        eid, is_new = store.upsert_entity(
            name, e.get("type", "concept"), e.get("description", ""),
            confidence=float(e.get("confidence", 0.8)),
            source_message_id=e.get("source_message_id"),
        )
        if is_new:
            created += 1
        else:
            merged += 1
        id_map[e["id"]] = eid

    added_rels = 0
    for r in data["relationships"]:
        sid = id_map.get(r["source_id"])
        tid = id_map.get(r["target_id"])
        if sid is None or tid is None or sid == tid:
            continue
        rel, swap = store.normalize_relation(r["relation"])
        if swap:
            sid, tid = tid, sid
        if not store.relationship_exists(sid, tid, rel):
            store.add_relationship(sid, tid, rel,
                                   confidence=float(r.get("confidence", 0.8)))
            added_rels += 1

    return {"ok": True, "mode": "merge", "entities_created": created,
            "entities_merged": merged, "relationships_added": added_rels}


def import_replace(data):
    """Replace-import: wipe and load. Returns a summary."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    for t in ("relationships", "entities", "memories", "messages", "conversations"):
        db.execute(f"DELETE FROM {t}")
    store.ensure_user_entity()

    return import_merge(data)


def import_from_json(text, mode="merge"):
    try:
        data = json.loads(text)
    except ValueError as e:
        return {"ok": False, "error": f"invalid JSON: {e}"}
    if mode == "replace":
        return import_replace(data)
    return import_merge(data)
