"""Graph store: entities, relationships, conversations, memories, messages.

Implements normalization, duplicate detection, entity merging, memory
supersession (stale/outdated facts), and source tracking so the brain stays
clean and trustworthy instead of accumulating duplicate or contradictory nodes.
"""
import json
import re

import numpy as np

from . import config, db, fallback, ollama


# --------------------------------------------------------------------------
# Normalization helpers
# --------------------------------------------------------------------------

def normalize_name(name):
    """Lowercase, collapse whitespace, strip surrounding punctuation."""
    if not name:
        return ""
    n = name.strip().lower()
    n = re.sub(r"\s+", " ", n)
    n = n.strip("\"'“”‘’()[]{}.,:;!?*")
    return n


def normalize_type(t):
    return config.TYPE_SYNONYMS.get((t or "").strip().lower(), "concept")


def normalize_relation(raw):
    """Return (canonical_relation, swap) for a raw relation label."""
    label = re.sub(r"[^a-z_]", "_", (raw or "").strip().lower()).strip("_")
    label = re.sub(r"_+", "_", label)
    if label in config.RELATION_INVERSE:
        return config.RELATION_INVERSE[label], True
    return config.RELATION_SYNONYMS.get(label, "related_to"), False


def vec_to_json(vec):
    if vec is None:
        return None
    return json.dumps([float(v) for v in vec])


def vec_from_json(s):
    if not s:
        return None
    return np.array(json.loads(s), dtype=np.float32)


_EMBED_CACHE = {}
_EMBED_CACHE_MAX = 256


def embed_text(text, model=None):
    """Embed text using Ollama if available, else the fallback hasher."""
    if model is None:
        model = db.get_setting("embedding_model", config.DEFAULT_EMBEDDING_MODEL)
    cache_key = (model or "", text or "")
    cached = _EMBED_CACHE.get(cache_key)
    if cached is not None:
        return cached
    vec = None
    if ollama.available():
        try:
            vec = np.array(ollama.embed(model or config.DEFAULT_EMBEDDING_MODEL, text),
                           dtype=np.float32)
        except Exception:
            vec = None
    if vec is None or vec.size == 0:
        vec = np.array(fallback.fallback_embed(text), dtype=np.float32)
    if len(_EMBED_CACHE) >= _EMBED_CACHE_MAX:
        _EMBED_CACHE.pop(next(iter(_EMBED_CACHE)))
    _EMBED_CACHE[cache_key] = vec
    return vec


def merge_similarity_threshold():
    return db.get_setting_float("merge_similarity", config.DEFAULT_MERGE_SIMILARITY)


# --------------------------------------------------------------------------
# Entity CRUD + merging
# --------------------------------------------------------------------------

def ensure_user_entity():
    """Create the special 'User' entity if it does not exist yet."""
    existing = db.query_one(
        "SELECT id FROM entities WHERE norm_name=?",
        (normalize_name(config.USER_ENTITY_NAME),),
    )
    if existing:
        return existing["id"]
    return create_entity(
        name=config.USER_ENTITY_NAME,
        etype="person",
        description=config.USER_ENTITY_DESCRIPTION,
        confidence=1.0,
    )


def find_entity_by_name(name):
    return db.query_one("SELECT * FROM entities WHERE norm_name=?", (normalize_name(name),))


def create_entity(name, etype="concept", description="", confidence=0.8,
                  aliases=None, source_message_id=None, embedding=None, meta=None):
    norm = normalize_name(name)
    if not norm:
        return None
    now = db.utcnow()
    eid = db.execute(
        "INSERT INTO entities(name, norm_name, type, description, aliases, embedding, "
        "confidence, source_message_id, created_at, updated_at, meta) "
        "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        (name.strip(), norm, normalize_type(etype), description or "",
         json.dumps(aliases or []), vec_to_json(embedding), confidence,
         source_message_id, now, now, json.dumps(meta or {})),
    )
    return eid


def update_entity(eid, **fields):
    allowed = {"name", "type", "description", "aliases", "confidence", "meta",
               "status", "pinned", "important"}
    sets, params = [], []
    for k, v in fields.items():
        if k not in allowed:
            continue
        if k in ("aliases", "meta"):
            v = json.dumps(v)
        sets.append(f"{k}=?")
        params.append(v)
    if not sets:
        return
    sets.append("updated_at=?")
    params.append(db.utcnow())
    params.append(eid)
    db.execute(f"UPDATE entities SET {', '.join(sets)} WHERE id=?", params)
    if "name" in fields:
        db.execute("UPDATE entities SET norm_name=? WHERE id=?",
                   (normalize_name(fields["name"]), eid))


def _cosine(a, b):
    if a is None or b is None or a.size == 0 or b.size == 0:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


def find_duplicate(entity_name, etype, embedding=None):
    """Find an existing entity that this one should merge into.

    1. Exact normalized-name match (including aliases).
    2. Vector similarity above the configured merge threshold (re-worded concepts).
    """
    norm = normalize_name(entity_name)
    row = db.query_one("SELECT * FROM entities WHERE norm_name=?", (norm,))
    if row:
        return row

    alias_rows = db.query(
        "SELECT * FROM entities WHERE aliases LIKE ?",
        (f"%{norm}%",),
    )
    for r in alias_rows:
        try:
            aliases = json.loads(r.get("aliases") or "[]")
        except ValueError:
            aliases = []
        if norm in [normalize_name(a) for a in aliases]:
            return r

    if embedding is not None:
        threshold = merge_similarity_threshold()
        alias_rows = db.query("SELECT * FROM entities WHERE embedding IS NOT NULL")
        for r in alias_rows:
            if normalize_name(r["name"]) in ("user",) and etype == "person":
                continue
            emb = vec_from_json(r.get("embedding"))
            if emb is not None and _cosine(embedding, emb) >= threshold:
                return r
    return None


def upsert_entity(name, etype, description="", confidence=0.8, source_message_id=None,
                  embedding=None, meta=None):
    """Insert or merge an entity. Returns (entity_id, created_bool)."""
    name = name.strip()
    if not name or normalize_name(name) == "":
        return None, False

    if normalize_name(name) in ("i", "me", "my", "myself", "mine", "user"):
        return ensure_user_entity(), False

    dup = find_duplicate(name, etype, embedding)
    if dup:
        new_desc = dup.get("description") or description
        aliases = []
        try:
            aliases = json.loads(dup.get("aliases") or "[]")
        except ValueError:
            aliases = []
        if normalize_name(name) != dup["norm_name"] and name not in aliases:
            aliases.append(name)
        update_entity(dup["id"], description=new_desc, aliases=aliases,
                      confidence=max(dup["confidence"], confidence))
        if embedding is not None and not dup.get("embedding"):
            db.execute("UPDATE entities SET embedding=? WHERE id=?",
                       (vec_to_json(embedding), dup["id"]))
        return dup["id"], False

    eid = create_entity(name, etype, description, confidence, source_message_id=source_message_id,
                        embedding=embedding, meta=meta)
    return eid, True


def merge_entities(keep_id, drop_id):
    """Merge `drop_id` into `keep_id`."""
    keep = db.query_one("SELECT * FROM entities WHERE id=?", (keep_id,))
    drop = db.query_one("SELECT * FROM entities WHERE id=?", (drop_id,))
    if not keep or not drop or keep_id == drop_id:
        return {"error": "invalid merge target"}

    db.execute("UPDATE OR IGNORE relationships SET source_id=? WHERE source_id=?", (keep_id, drop_id))
    db.execute("UPDATE OR IGNORE relationships SET target_id=? WHERE target_id=?", (keep_id, drop_id))
    db.execute("DELETE FROM relationships WHERE source_id=target_id")

    aliases = json.loads(keep.get("aliases") or "[]")
    for a in json.loads(drop.get("aliases") or "[]"):
        if a not in aliases:
            aliases.append(a)
    if drop["name"] not in aliases:
        aliases.append(drop["name"])
    desc = keep.get("description") or drop.get("description") or ""
    update_entity(keep_id, description=desc, aliases=aliases,
                  confidence=max(keep["confidence"], drop["confidence"]))
    # Rewrite every memory that references the dropped entity (including
    # multi-id memories such as relationship events).
    mems = db.query("SELECT id, entity_ids FROM memories WHERE entity_ids LIKE ?",
                    (f"%{drop_id}%",))
    for m in mems:
        try:
            ids = json.loads(m["entity_ids"] or "[]")
        except ValueError:
            continue
        if drop_id not in ids:
            continue
        rewritten, seen = [], set()
        for i in ids:
            nid = keep_id if i == drop_id else i
            if nid in seen:
                continue
            seen.add(nid)
            rewritten.append(nid)
        db.execute("UPDATE memories SET entity_ids=? WHERE id=?",
                   (json.dumps(rewritten), m["id"]))
    db.execute("DELETE FROM entities WHERE id=?", (drop_id,))
    return {"ok": True, "id": keep_id}


def delete_entity(eid):
    db.execute("DELETE FROM entities WHERE id=?", (eid,))


def set_entity_status(eid, status):
    db.execute("UPDATE entities SET status=? WHERE id=?", (status, eid))


def toggle_entity_flag(eid, flag):
    if flag not in ("pinned", "important"):
        return False
    row = entity_row(eid)
    if not row:
        return False
    db.execute(f"UPDATE entities SET {flag}=? WHERE id=?", (0 if row[flag] else 1, eid))
    return True


def set_confidence(eid, confidence):
    db.execute("UPDATE entities SET confidence=?, updated_at=? WHERE id=?",
               (confidence, db.utcnow(), eid))


def entity_row(eid):
    return db.query_one("SELECT * FROM entities WHERE id=?", (eid,))


def all_entities():
    return db.query("SELECT * FROM entities ORDER BY type, name COLLATE NOCASE")


# --------------------------------------------------------------------------
# Relationships (with supersession for stale facts)
# --------------------------------------------------------------------------

def add_relationship(source_id, target_id, relation, confidence=0.8, source_message_id=None):
    if source_id == target_id:
        return None
    existing = db.query_one(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation=?",
        (source_id, target_id, relation),
    )
    if existing:
        # Re-activate a previously superseded relationship when re-asserted.
        db.execute(
            "UPDATE relationships SET confidence=MAX(confidence,?), status='active' WHERE id=?",
            (confidence, existing["id"]),
        )
        return existing["id"]
    return db.execute(
        "INSERT INTO relationships(source_id, target_id, relation, confidence, "
        "source_message_id, created_at, status) VALUES(?,?,?,?,?,?,'active')",
        (source_id, target_id, relation, confidence, source_message_id, db.utcnow()),
    )


def relationship_exists(source_id, target_id, relation):
    return db.query_one(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? AND relation=?",
        (source_id, target_id, relation),
    ) is not None


def relationship_active(source_id, target_id, relation):
    return db.query_one(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? "
        "AND relation=? AND status='active'",
        (source_id, target_id, relation),
    ) is not None


def supersede_relationship(source_id, target_id, relation):
    """Mark a matching active relationship as superseded. Returns count changed."""
    rows = db.query(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? AND relation=? AND status='active'",
        (source_id, target_id, relation),
    )
    for r in rows:
        db.execute("UPDATE relationships SET status='superseded' WHERE id=?", (r["id"],))
    return len(rows)


def supersede_relations_of_type(source_id, relation, except_target_id=None, target_type=None):
    """Supersede all active `relation` links from `source_id` (optionally
    matching a target entity type), used for conflict resolution. Returns ids."""
    sql = "SELECT r.id, r.target_id, e.type ttype FROM relationships r JOIN entities e ON e.id=r.target_id WHERE r.source_id=? AND r.relation=? AND r.status='active'"
    rows = db.query(sql, (source_id, relation))
    changed = []
    for r in rows:
        if except_target_id and r["target_id"] == except_target_id:
            continue
        if target_type and r["ttype"] != target_type:
            continue
        db.execute("UPDATE relationships SET status='superseded' WHERE id=?", (r["id"],))
        changed.append(r["target_id"])
    return changed


def update_relationship(rid, **fields):
    """Update relation label, confidence, or status. Never deletes the row."""
    allowed = {"relation", "confidence", "status"}
    sets, params = [], []
    for k, v in fields.items():
        if k not in allowed:
            continue
        if k == "relation":
            rel, _swap = normalize_relation(v)
            v = rel
        if k == "confidence":
            try:
                v = max(0.0, min(1.0, float(v)))
            except (TypeError, ValueError):
                continue
        if k == "status" and v not in ("active", "superseded"):
            continue
        sets.append(f"{k}=?")
        params.append(v)
    if not sets:
        return False
    params.append(rid)
    db.execute(f"UPDATE relationships SET {', '.join(sets)} WHERE id=?", params)
    return True


def delete_relationship(rid):
    db.execute("DELETE FROM relationships WHERE id=?", (rid,))


def all_relationships(active_only=False):
    if active_only:
        return db.query("SELECT * FROM relationships WHERE status='active'")
    return db.query("SELECT * FROM relationships")


def relationship_row(rid):
    return db.query_one("SELECT * FROM relationships WHERE id=?", (rid,))


# --------------------------------------------------------------------------
# Conversations (short-term context, separate from long-term memory)
# --------------------------------------------------------------------------

def create_conversation(title=""):
    now = db.utcnow()
    return db.execute(
        "INSERT INTO conversations(title, created_at, updated_at) VALUES(?,?,?)",
        (title, now, now),
    )


def touch_conversation(cid, title=None):
    fields, params = [], []
    if title is not None:
        fields.append("title=?")
        params.append(title)
    fields.append("updated_at=?")
    params.append(db.utcnow())
    params.append(cid)
    db.execute(f"UPDATE conversations SET {', '.join(fields)} WHERE id=?", params)


def conversation_row(cid):
    return db.query_one("SELECT * FROM conversations WHERE id=?", (cid,))


def all_conversations():
    return db.query("SELECT * FROM conversations ORDER BY updated_at DESC, id DESC")


def _like_pattern(query):
    raw = (query or "").strip()
    if not raw:
        return None
    escaped = raw.replace("#", "##").replace("%", "#%").replace("_", "#_")
    return f"%{escaped}%"


def conversation_summaries(query=None, limit=200):
    """List conversations with counts/previews. Optional title+message search.

    Does not load every message row. LIKE wildcards in ``query`` are escaped
    so ``%`` cannot dump the whole rail.
    """
    try:
        limit = max(1, min(int(limit or 200), 500))
    except (TypeError, ValueError):
        limit = 200
    like = _like_pattern(query)
    params = []
    where = ""
    if like:
        where = (
            "WHERE c.id IN ("
            "  SELECT id FROM conversations WHERE title LIKE ? ESCAPE '#' "
            "  UNION "
            "  SELECT conversation_id FROM messages "
            "  WHERE conversation_id IS NOT NULL AND content LIKE ? ESCAPE '#'"
            ")"
        )
        params.extend([like, like])
    sql = (
        "SELECT c.id, c.title, c.created_at, c.updated_at, "
        "  (SELECT COUNT(*) FROM messages m WHERE m.conversation_id=c.id) AS message_count, "
        "  (SELECT m.content FROM messages m WHERE m.conversation_id=c.id AND m.role='user' "
        "   ORDER BY m.id DESC LIMIT 1) AS preview "
        "FROM conversations c "
        f"{where} "
        "ORDER BY c.updated_at DESC, c.id DESC LIMIT ?"
    )
    params.append(limit)
    rows = db.query(sql, tuple(params))
    out = []
    for c in rows:
        out.append({
            "id": c["id"],
            "title": c["title"] or "(untitled)",
            "created_at": c["created_at"],
            "updated_at": c["updated_at"],
            "message_count": int(c.get("message_count") or 0),
            "preview": (c.get("preview") or "")[:80],
        })
    return out


def current_conversation_id():
    cid = db.get_setting("current_conversation_id")
    if cid is None:
        cid = create_conversation()
        db.set_setting("current_conversation_id", cid)
        return cid
    if not conversation_row(cid):
        cid = create_conversation()
        db.set_setting("current_conversation_id", cid)
    return cid


def new_conversation():
    cid = create_conversation()
    db.set_setting("current_conversation_id", cid)
    return cid


def conversation_messages(cid, limit=None):
    """Return messages in chronological order. `limit` means the last N turns."""
    if limit:
        return db.query(
            "SELECT * FROM ("
            "  SELECT * FROM messages WHERE conversation_id=? ORDER BY id DESC LIMIT ?"
            ") ORDER BY id ASC",
            (cid, int(limit)),
        )
    return db.query(
        "SELECT * FROM messages WHERE conversation_id=? ORDER BY id ASC",
        (cid,),
    )


def delete_conversation(cid):
    """Delete a conversation and its messages. Long-term memories stay."""
    db.execute("DELETE FROM messages WHERE conversation_id=?", (cid,))
    db.execute("DELETE FROM conversations WHERE id=?", (cid,))
    current = db.get_setting("current_conversation_id")
    if current is not None and str(current) == str(cid):
        db.set_setting("current_conversation_id", None)
    return True


# --------------------------------------------------------------------------
# Memories (timeline events)
# --------------------------------------------------------------------------

def add_memory(kind, text, entity_ids=None, message_id=None, confidence=0.8, meta=None):
    return db.execute(
        "INSERT INTO memories(kind, text, entity_ids, message_id, confidence, created_at, meta) "
        "VALUES(?,?,?,?,?,?,?)",
        (kind, text, json.dumps(entity_ids or []), message_id, confidence, db.utcnow(),
         json.dumps(meta or {})),
    )


def recent_memories(limit=30):
    return db.query("SELECT * FROM memories ORDER BY created_at DESC, id DESC LIMIT ?", (limit,))


def memories_for_entity(eid, limit=50):
    rows = db.query("SELECT * FROM memories ORDER BY created_at DESC, id DESC LIMIT 200")
    out = []
    for m in rows:
        try:
            ids = json.loads(m["entity_ids"] or "[]")
        except ValueError:
            ids = []
        if eid in ids:
            out.append(m)
            if len(out) >= limit:
                break
    return out


# --------------------------------------------------------------------------
# Messages
# --------------------------------------------------------------------------

def add_message(role, content, conversation_id=None, embedding=None, extracted=0, meta=None):
    return db.execute(
        "INSERT INTO messages(conversation_id, role, content, created_at, embedding, extracted, meta) "
        "VALUES(?,?,?,?,?,?,?)",
        (conversation_id, role, content, db.utcnow(), vec_to_json(embedding), extracted,
         json.dumps(meta or {})),
    )


def messages(limit=200):
    return db.query("SELECT * FROM messages ORDER BY id ASC LIMIT ?", (limit,))


def message_by_id(mid):
    return db.query_one("SELECT * FROM messages WHERE id=?", (mid,))
