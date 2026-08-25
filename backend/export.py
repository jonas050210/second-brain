"""Graph export / import (JSON + Markdown).

Export includes entities, relationships, memories, messages, conversations and
settings (no secrets — this app has none). Import validates the payload before
touching the database, and supports two modes:
  - merge   : upsert entities / add relationships without deleting anything
  - replace : wipe the database first (with explicit confirmation)
"""
import json
import math
import re
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
    # Never export secrets or ephemeral session keys.
    secret_tokens = ("secret", "password", "token", "api_key", "apikey")
    safe_settings = {}
    for k, v in settings.items():
        lk = (k or "").lower()
        if k == "current_conversation_id":
            continue
        if any(tok in lk for tok in secret_tokens):
            continue
        safe_settings[k] = v
    name_by_id = {e["id"]: e["name"] for e in entities}
    facts = []
    for r in relationships:
        facts.append({
            "id": r["id"],
            "text": f'{name_by_id.get(r["source_id"], "#" + str(r["source_id"]))} '
                    f'{r["relation"]} {name_by_id.get(r["target_id"], "#" + str(r["target_id"]))}',
            "source_id": r["source_id"],
            "target_id": r["target_id"],
            "relation": r["relation"],
            "confidence": r["confidence"],
            "status": r.get("status", "active"),
            "source_message_id": r.get("source_message_id"),
            "created_at": r.get("created_at"),
        })
    return {
        "format": EXPORT_FORMAT,
        "version": EXPORT_VERSION,
        "exported_at": db.utcnow(),
        "counts": {
            "entities": len(entities), "relationships": len(relationships),
            "facts": len(facts), "memories": len(memories),
            "messages": len(messages), "conversations": len(conversations),
        },
        "settings": safe_settings,
        "entities": entities,
        "relationships": relationships,
        "facts": facts,
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

def _valid_confidence(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and 0.0 <= float(value) <= 1.0
    )


def _valid_id(value, allow_none=False):
    return (allow_none and value is None) or (
        isinstance(value, int) and not isinstance(value, bool)
    )


def _valid_embedding(value):
    if value is None:
        return True
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except (TypeError, ValueError, json.JSONDecodeError):
            return False
    return store.vec_from_json(value) is not None


def _valid_json_list(value, item_type=int):
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except (TypeError, ValueError, json.JSONDecodeError):
            return False
    return isinstance(value, list) and all(
        isinstance(item, item_type) and not (item_type is int and isinstance(item, bool))
        for item in value
    )


def validate_payload(data):
    """Validate an export completely before it touches the database."""
    if not isinstance(data, dict):
        return False, "export must be a JSON object"
    if data.get("format") != EXPORT_FORMAT:
        return False, f"unrecognized format (expected '{EXPORT_FORMAT}')"
    for key in ("entities", "relationships"):
        if key not in data or not isinstance(data[key], list):
            return False, f"missing or invalid '{key}' list"
    for key in ("conversations", "messages", "memories", "facts"):
        if key in data and not isinstance(data[key], list):
            return False, f"'{key}' must be a list when present"

    for e in data["entities"]:
        if not isinstance(e, dict) or not isinstance(e.get("name"), str) \
                or not e["name"].strip():
            return False, "entities must be objects with a non-empty text 'name'"
        if e.get("type") is not None and not isinstance(e.get("type"), str):
            return False, "entity 'type' must be text"
        if e.get("description") is not None and not isinstance(e.get("description"), str):
            return False, "entity 'description' must be text"
        if not _valid_confidence(e.get("confidence", 0.8)):
            return False, "entity 'confidence' must be a number between 0 and 1"
        if e.get("aliases") is not None and not _valid_json_list(e["aliases"], str):
            return False, "entity 'aliases' must be a list of text"
        if not _valid_embedding(e.get("embedding")):
            return False, "entity 'embedding' must be a numeric vector"
        if e.get("id") is not None and not _valid_id(e["id"]):
            return False, "entity 'id' must be an integer"
        if e.get("source_message_id") is not None and not _valid_id(e["source_message_id"]):
            return False, "entity 'source_message_id' must be an integer"
        if e.get("status") is not None and e["status"] not in ("active", "superseded"):
            return False, "entity 'status' must be 'active' or 'superseded'"

    for r in data["relationships"]:
        if not isinstance(r, dict) or not _valid_id(r.get("source_id")) \
                or not _valid_id(r.get("target_id")):
            return False, "relationships must have integer source_id and target_id"
        if not isinstance(r.get("relation"), str) or not r["relation"].strip():
            return False, "relationship 'relation' must be non-empty text"
        if not _valid_confidence(r.get("confidence", 0.8)):
            return False, "relationship 'confidence' must be a number between 0 and 1"
        if r.get("source_message_id") is not None and not _valid_id(r["source_message_id"]):
            return False, "relationship 'source_message_id' must be an integer"
        if r.get("status") is not None and r["status"] not in ("active", "superseded"):
            return False, "relationship 'status' must be 'active' or 'superseded'"

    for c in data.get("conversations") or []:
        if not isinstance(c, dict):
            return False, "conversations must contain objects"
        if c.get("title") is not None and not isinstance(c["title"], str):
            return False, "conversation 'title' must be text"
        if c.get("id") is not None and not _valid_id(c["id"]):
            return False, "conversation 'id' must be an integer"
        for key in ("pinned", "archived"):
            if c.get(key) is not None and not isinstance(c[key], (bool, int)):
                return False, f"conversation '{key}' must be a boolean"

    for m in data.get("messages") or []:
        if not isinstance(m, dict) or not isinstance(m.get("content"), str):
            return False, "messages must contain objects with text content"
        if m.get("role") is not None and not isinstance(m["role"], str):
            return False, "message 'role' must be text"
        if m.get("id") is not None and not _valid_id(m["id"]):
            return False, "message 'id' must be an integer"
        if m.get("conversation_id") is not None and not _valid_id(m["conversation_id"]):
            return False, "message 'conversation_id' must be an integer"
        if m.get("extracted") is not None and not _valid_id(m["extracted"]):
            return False, "message 'extracted' must be an integer"
        if not _valid_embedding(m.get("embedding")):
            return False, "message 'embedding' must be a numeric vector"

    for m in data.get("memories") or []:
        if not isinstance(m, dict) or not isinstance(m.get("text"), str) \
                or not m["text"].strip():
            return False, "memories must contain objects with text"
        if m.get("kind") is not None and not isinstance(m["kind"], str):
            return False, "memory 'kind' must be text"
        if m.get("entity_ids") is not None and not _valid_json_list(m["entity_ids"], int):
            return False, "memory 'entity_ids' must be a list of integers"
        if m.get("message_id") is not None and not _valid_id(m["message_id"]):
            return False, "memory 'message_id' must be an integer"
        if not _valid_confidence(m.get("confidence", 0.8)):
            return False, "memory 'confidence' must be a number between 0 and 1"

    if "facts" in data and not isinstance(data["facts"], list):
        return False, "'facts' must be a list when present"
    if data.get("settings") is not None and not isinstance(data["settings"], dict):
        return False, "'settings' must be an object when present"
    return True, None


def _apply_entity_flags(eid, e, apply_meta=False):
    fields = {}
    if e.get("status"):
        fields["status"] = e["status"]
    if e.get("pinned") is not None:
        fields["pinned"] = 1 if e.get("pinned") else 0
    if e.get("important") is not None:
        fields["important"] = 1 if e.get("important") else 0
    if e.get("aliases") is not None:
        try:
            aliases = e["aliases"] if isinstance(e["aliases"], list) else json.loads(e["aliases"])
            fields["aliases"] = aliases
        except (ValueError, TypeError, json.JSONDecodeError):
            pass
    if apply_meta and e.get("meta") is not None:
        try:
            meta = e["meta"] if isinstance(e["meta"], dict) else json.loads(e["meta"])
            if isinstance(meta, dict):
                fields["meta"] = meta
        except (ValueError, TypeError, json.JSONDecodeError):
            pass
    if fields:
        store.update_entity(eid, **fields)
    emb = e.get("embedding")
    if emb is not None:
        payload = emb if isinstance(emb, str) else json.dumps(emb)
        db.execute("UPDATE entities SET embedding=? WHERE id=?", (payload, eid))


REPORT_LIMIT = 40


def _clip(items, limit=REPORT_LIMIT):
    items = list(items)
    return items[:limit], len(items)


def _entity_name(eid):
    row = store.entity_row(eid) if eid is not None else None
    return row["name"] if row else f"#{eid}"


def _import_entities(data, message_map=None, preserve_times=False):
    user_id = store.ensure_user_entity()
    id_map = {}
    created, merged, skipped = 0, 0, []
    message_map = message_map or {}
    for e in data["entities"]:
        name = (e.get("name") or "").strip()
        if not name:
            skipped.append({"reason": "empty_name"})
            continue
        if store.normalize_name(name) in ("user", "i", "me"):
            if e.get("id") is not None:
                id_map[e["id"]] = user_id
            continue
        try:
            conf = float(e.get("confidence", 0.8))
        except (TypeError, ValueError):
            skipped.append({"reason": "bad_confidence", "name": name})
            continue
        eid, is_new = store.upsert_entity(
            name, e.get("type", "concept"), e.get("description", ""),
            confidence=conf,
            source_message_id=message_map.get(e.get("source_message_id")),
        )
        if eid is None:
            skipped.append({"reason": "rejected", "name": name})
            continue
        if is_new:
            created += 1
        else:
            merged += 1
        if e.get("id") is not None:
            id_map[e["id"]] = eid
        _apply_entity_flags(eid, e, apply_meta=preserve_times or is_new)
        if preserve_times and is_new:
            created_at = e.get("created_at")
            updated_at = e.get("updated_at") or created_at
            if isinstance(created_at, str) and isinstance(updated_at, str):
                db.execute(
                    "UPDATE entities SET created_at=?, updated_at=? WHERE id=?",
                    (created_at, updated_at, eid),
                )
    return id_map, created, merged, skipped


def _import_relationships(data, id_map, message_map=None, apply_exclusive=True):
    added = 0
    message_map = message_map or {}
    duplicates = 0
    skipped = []
    conflicts = []
    exclusive = set(config.EXCLUSIVE_RELATIONS)
    for r in data["relationships"]:
        sid = id_map.get(r["source_id"])
        tid = id_map.get(r["target_id"])
        raw_rel = r.get("relation") or ""
        if sid is None or tid is None:
            skipped.append({
                "reason": "missing_endpoint",
                "relation": raw_rel,
                "source_id": r.get("source_id"),
                "target_id": r.get("target_id"),
            })
            continue
        if sid == tid:
            skipped.append({
                "reason": "self_loop",
                "relation": raw_rel,
                "name": _entity_name(sid),
            })
            continue
        rel, swap = store.normalize_relation(raw_rel)
        if swap:
            sid, tid = tid, sid
        if apply_exclusive and rel in exclusive:
            old_ids = store.supersede_relations_of_type(sid, rel, except_target_id=tid)
            for oid in old_ids:
                old = store.entity_row(oid)
                if old:
                    conflicts.append({
                        "kind": "exclusive",
                        "relation": rel,
                        "kept": _entity_name(tid),
                        "superseded": old["name"],
                    })
                    store.add_memory(
                        "conflict",
                        f'{rel} changed on import: now {_entity_name(tid)} (was {old["name"]})',
                        entity_ids=[tid, oid],
                    )
        existed = store.relationship_exists(sid, tid, rel)
        try:
            conf = float(r.get("confidence", 0.8))
        except (TypeError, ValueError):
            conf = 0.8
        rid = store.add_relationship(
            sid, tid, rel, confidence=conf,
            source_message_id=message_map.get(r.get("source_message_id")),
            created_at=r.get("created_at") if isinstance(r.get("created_at"), str) else None,
        )
        if r.get("status") and r["status"] != "active" and rid:
            store.update_relationship(rid, status=r["status"])
        if not existed:
            added += 1
        else:
            duplicates += 1
    return added, skipped, conflicts, duplicates


def _import_conversations(data):
    """Import conversations and return old-id -> local-id mapping.

    Matching the stable exported timestamps makes repeating the same merge
    idempotent while still allowing genuinely new conversations through.
    """
    conv_map = {}
    for c in data.get("conversations") or []:
        title = c.get("title") or ""
        created_at = c.get("created_at")
        existing = None
        if isinstance(created_at, str):
            existing = db.query_one(
                "SELECT id FROM conversations WHERE title=? AND created_at=?",
                (title, created_at),
            )
        if existing:
            new_id = existing["id"]
        else:
            new_id = store.create_conversation(
                title=title,
                created_at=created_at if isinstance(created_at, str) else None,
                updated_at=c.get("updated_at") if isinstance(c.get("updated_at"), str) else None,
                pinned=c.get("pinned", 0), archived=c.get("archived", 0),
            )
        if c.get("id") is not None:
            conv_map[c["id"]] = new_id
    return conv_map


def _import_messages(data, conv_map):
    """Import source messages and return old-id -> local-id mapping."""
    message_map = {}
    for m in data.get("messages") or []:
        content = m.get("content")
        if not isinstance(content, str):
            continue
        cid = conv_map.get(m.get("conversation_id"))
        created_at = m.get("created_at") if isinstance(m.get("created_at"), str) else None
        existing = None
        if created_at is not None:
            existing = db.query_one(
                "SELECT id FROM messages WHERE conversation_id IS ? AND role=? "
                "AND content=? AND created_at=?",
                (cid, m.get("role") or "user", content, created_at),
            )
        if existing:
            new_mid = existing["id"]
        else:
            meta = m.get("meta") or {}
            if isinstance(meta, str):
                try:
                    meta = json.loads(meta)
                except (TypeError, ValueError, json.JSONDecodeError):
                    meta = {}
            embedding = store.vec_from_json(m.get("embedding"))
            new_mid = store.add_message(
                m.get("role") or "user", content, conversation_id=cid,
                embedding=embedding, extracted=int(m.get("extracted") or 0),
                meta=meta, created_at=created_at,
            )
        if m.get("id") is not None:
            message_map[m["id"]] = new_mid
    return message_map


def _import_memories(data, id_map, message_map=None, dedup=True):
    added = 0
    skipped = 0
    existing = set()
    if dedup:
        existing = {(m["kind"], m["text"]) for m in db.query("SELECT kind, text FROM memories")}
    for m in data.get("memories") or []:
        if not isinstance(m, dict) or not m.get("text"):
            skipped += 1
            continue
        key = (m.get("kind") or "entity", m["text"])
        if dedup and key in existing:
            skipped += 1
            continue
        try:
            raw_ids = m.get("entity_ids") or []
            if isinstance(raw_ids, str):
                raw_ids = json.loads(raw_ids)
        except ValueError:
            raw_ids = []
        eids = [id_map[old] for old in raw_ids if old in id_map]
        mid = None
        if message_map is not None and m.get("message_id") in message_map:
            mid = message_map[m["message_id"]]
        meta = m.get("meta") or {}
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except ValueError:
                meta = {}
        try:
            conf = float(m.get("confidence", 0.8))
        except (TypeError, ValueError):
            conf = 0.8
        created_at = m.get("created_at") if isinstance(m.get("created_at"), str) else None
        store.add_memory(m.get("kind") or "entity", m["text"], entity_ids=eids,
                         message_id=mid, confidence=conf, meta=meta,
                         created_at=created_at)
        existing.add(key)
        added += 1
    return added, skipped


def _import_summary(mode, created, merged, added_rels, added_mems,
                    skipped_ents, skipped_rels, conflicts, duplicates, skipped_mems):
    skipped_ents, n_ent = _clip(skipped_ents)
    skipped_rels, n_rel = _clip(skipped_rels)
    conflicts, n_conf = _clip(conflicts)
    return {
        "ok": True, "mode": mode,
        "entities_created": created,
        "entities_merged": merged,
        "relationships_added": added_rels,
        "memories_added": added_mems,
        "entities_skipped": n_ent,
        "relationships_skipped": n_rel,
        "memories_skipped": skipped_mems,
        "duplicates": duplicates,
        "conflicts": conflicts,
        "skipped": skipped_rels,
        "report": {
            "conflicts": conflicts,
            "skipped_relationships": skipped_rels,
            "skipped_entities": skipped_ents,
            "conflict_count": n_conf,
            "skipped_relationship_count": n_rel,
            "skipped_entity_count": n_ent,
            "duplicate_relationships": duplicates,
            "memories_skipped": skipped_mems,
        },
    }


_IMPORTABLE_SETTINGS = {
    "llm_model", "embedding_model", "ollama_base_url", "confidence_threshold",
    "merge_similarity", "auto_memory", "auto_backup_hours", "theme",
}


def _apply_import_settings(data):
    """Restore user-facing settings without restoring session/backup metadata."""
    settings = data.get("settings") or {}
    for key in _IMPORTABLE_SETTINGS:
        if key not in settings:
            continue
        value = settings[key]
        if key in ("llm_model", "embedding_model", "theme"):
            if isinstance(value, str) and value.strip():
                db.set_setting(key, value.strip())
        elif key == "ollama_base_url":
            if isinstance(value, str):
                from urllib.parse import urlparse
                parsed = urlparse(value.strip())
                if parsed.scheme in ("http", "https") and parsed.netloc:
                    db.set_setting(key, value.strip().rstrip("/"))
        elif key in ("confidence_threshold", "merge_similarity", "auto_backup_hours"):
            if isinstance(value, (int, float)) and not isinstance(value, bool) \
                    and math.isfinite(float(value)):
                db.set_setting(key, value)
        elif key == "auto_memory" and isinstance(value, bool):
            db.set_setting(key, value)


def import_merge(data):
    """Merge-import without deleting local data, including source messages."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    conv_map = _import_conversations(data)
    message_map = _import_messages(data, conv_map)
    id_map, created, merged, skipped_ents = _import_entities(data, message_map=message_map)
    added_rels, skipped_rels, conflicts, duplicates = _import_relationships(
        data, id_map, message_map=message_map,
    )
    added_mems, skipped_mems = _import_memories(
        data, id_map, message_map=message_map, dedup=True,
    )
    return _import_summary("merge", created, merged, added_rels, added_mems,
                           skipped_ents, skipped_rels, conflicts, duplicates, skipped_mems)


def import_replace(data):
    """Replace-import: wipe and load while preserving traceable source data."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    for t in ("relationships", "entities", "memories", "messages", "conversations"):
        db.execute(f"DELETE FROM {t}")
    store.clear_undo_stack()
    store.ensure_user_entity()

    conv_map = _import_conversations(data)
    message_map = _import_messages(data, conv_map)
    id_map, created, merged, skipped_ents = _import_entities(
        data, message_map=message_map, preserve_times=True,
    )
    added_rels, skipped_rels, conflicts, duplicates = _import_relationships(
        data, id_map, message_map=message_map,
    )
    added_mems, skipped_mems = _import_memories(
        data, id_map, message_map=message_map, dedup=False,
    )
    _apply_import_settings(data)
    # current_conversation_id is deliberately not exported. Point the new
    # session at the newest imported conversation rather than a stale id.
    imported_ids = [
        cid for cid in conv_map.values()
        if not (store.conversation_row(cid) or {}).get("archived", 0)
    ]
    db.set_setting("current_conversation_id", imported_ids[-1] if imported_ids else None)
    return _import_summary("replace", created, merged, added_rels, added_mems,
                           skipped_ents, skipped_rels, conflicts, duplicates, skipped_mems)


def import_from_json(text, mode="merge"):
    try:
        data = json.loads(text)
    except (TypeError, ValueError, json.JSONDecodeError) as e:
        return {"ok": False, "error": f"invalid JSON: {e}"}
    if mode == "replace":
        return import_replace(data)
    return import_merge(data)


def split_note_chunks(text, limit=50):
    """Split pasted notes into extractable paragraphs. Never invents content."""
    raw = (text or "").replace("\r\n", "\n").strip()
    if not raw:
        return []
    parts = re.split(r"\n\s*\n+|^(?=#{1,3}\s)", raw, flags=re.M)
    chunks = []
    for part in parts:
        piece = " ".join(line.strip() for line in part.splitlines() if line.strip())
        piece = piece.lstrip("# ").strip()
        if len(piece) >= 8:
            chunks.append(piece[:2000])
        if len(chunks) >= limit:
            break
    if not chunks and len(raw) >= 8:
        chunks = [raw[:2000]]
    return chunks


def import_notes(text):
    """Run the existing extractor on each note paragraph. Does not wipe data."""
    from . import extract, fallback
    chunks = split_note_chunks(text)
    if not chunks:
        return {"ok": False, "error": "no usable note text"}
    cid = store.new_conversation()
    store.touch_conversation(cid, title="Imported notes")
    remembered, chunks_used = [], 0
    for chunk in chunks:
        if fallback.is_trivial(chunk):
            continue
        mid = store.add_message("user", chunk, conversation_id=cid)
        result = extract.extract(chunk, source_message_id=mid)
        remembered.extend(result.get("remembered") or [])
        chunks_used += 1
    return {
        "ok": True,
        "mode": "notes",
        "chunks": chunks_used,
        "conversation_id": cid,
        "remembered": len(remembered),
    }
