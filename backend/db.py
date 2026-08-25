"""SQLite persistence layer for Second Brain.

Everything is stored locally in a single SQLite file: entities, relationships,
messages (original sources), conversations (short-term grouping), memories
(timeline events), embeddings and settings. Nothing ever leaves the machine.

The schema is versioned via `PRAGMA user_version` and migrated in place so
existing databases are upgraded (never discarded) on startup.
"""
import json
import os
import sqlite3
import threading
from datetime import datetime, timezone

from . import config

_write_lock = threading.Lock()

SCHEMA_VERSION = 3

SCHEMA = """
CREATE TABLE IF NOT EXISTS entities (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    name              TEXT NOT NULL,
    norm_name         TEXT NOT NULL UNIQUE,
    type              TEXT NOT NULL DEFAULT 'concept',
    description       TEXT NOT NULL DEFAULT '',
    aliases           TEXT NOT NULL DEFAULT '[]',
    embedding         TEXT,                -- JSON array of floats (or NULL)
    confidence        REAL NOT NULL DEFAULT 0.8,
    source_message_id INTEGER,
    created_at        TEXT NOT NULL,
    updated_at        TEXT NOT NULL,
    meta              TEXT NOT NULL DEFAULT '{}',
    status            TEXT NOT NULL DEFAULT 'active',   -- 'active' | 'superseded'
    pinned            INTEGER NOT NULL DEFAULT 0,
    important         INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS relationships (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id         INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    target_id         INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    relation          TEXT NOT NULL,
    confidence        REAL NOT NULL DEFAULT 0.8,
    source_message_id INTEGER,
    created_at        TEXT NOT NULL,
    status            TEXT NOT NULL DEFAULT 'active',   -- 'active' | 'superseded'
    UNIQUE(source_id, target_id, relation)
);
CREATE INDEX IF NOT EXISTS idx_rel_source ON relationships(source_id);
CREATE INDEX IF NOT EXISTS idx_rel_target ON relationships(target_id);
CREATE INDEX IF NOT EXISTS idx_rel_source_status ON relationships(source_id, status);
CREATE INDEX IF NOT EXISTS idx_rel_target_status ON relationships(target_id, status);
CREATE INDEX IF NOT EXISTS idx_ent_type_status ON entities(type, status);

CREATE TABLE IF NOT EXISTS conversations (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL DEFAULT '',
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER,
    role            TEXT NOT NULL,        -- 'user' | 'assistant' | 'system'
    content         TEXT NOT NULL,
    created_at      TEXT NOT NULL,
    embedding       TEXT,                 -- JSON array of floats (or NULL)
    extracted       INTEGER NOT NULL DEFAULT 0,
    meta            TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_msg_conv ON messages(conversation_id);

CREATE TABLE IF NOT EXISTS memories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kind        TEXT NOT NULL,            -- 'entity' | 'relationship' | 'update' | 'superseded' | 'conflict' | 'command' | 'summary'
    text        TEXT NOT NULL,
    entity_ids  TEXT NOT NULL DEFAULT '[]',
    message_id  INTEGER,
    confidence  REAL NOT NULL DEFAULT 0.8,
    created_at  TEXT NOT NULL,
    meta        TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_mem_created ON memories(created_at);
CREATE INDEX IF NOT EXISTS idx_mem_kind ON memories(kind);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT
);
"""

# Incremental migrations: columns added to pre-existing databases.
MIGRATIONS = {
    1: [
        ("entities", "status", "TEXT NOT NULL DEFAULT 'active'"),
        ("entities", "pinned", "INTEGER NOT NULL DEFAULT 0"),
        ("entities", "important", "INTEGER NOT NULL DEFAULT 0"),
        ("relationships", "status", "TEXT NOT NULL DEFAULT 'active'"),
        ("messages", "conversation_id", "INTEGER"),
        ("memories", "confidence", "REAL NOT NULL DEFAULT 0.8"),
    ],
    2: [],
    3: [
        ("memories", "meta", "TEXT NOT NULL DEFAULT '{}'"),
    ],
}


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def _connect():
    parent = os.path.dirname(os.path.abspath(config.DB_PATH))
    if parent:
        os.makedirs(parent, exist_ok=True)
    conn = sqlite3.connect(config.DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def _columns(conn, table):
    return {r["name"] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()}


def init_db():
    with _write_lock:
        conn = _connect()
        try:
            conn.executescript(SCHEMA)

            # Apply column migrations for existing databases.
            current = conn.execute("PRAGMA user_version").fetchone()[0]
            for version in sorted(MIGRATIONS):
                if version > current:
                    for table, column, ddl in MIGRATIONS[version]:
                        if column not in _columns(conn, table):
                            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")
                    conn.execute(f"PRAGMA user_version={version}")

            conn.commit()
        finally:
            conn.close()


def query(sql, params=()):
    conn = _connect()
    try:
        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def query_one(sql, params=()):
    rows = query(sql, params)
    return rows[0] if rows else None


def execute(sql, params=()):
    with _write_lock:
        conn = _connect()
        try:
            cur = conn.execute(sql, params)
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()


# --------------------------------------------------------------------------
# Settings (typed helpers)
# --------------------------------------------------------------------------

def get_setting(key, default=None):
    row = query_one("SELECT value FROM settings WHERE key=?", (key,))
    if row is None:
        return default
    return row["value"]


def set_setting(key, value):
    execute(
        "INSERT INTO settings(key, value) VALUES(?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (key, json.dumps(value) if not isinstance(value, str) else value),
    )


def get_setting_float(key, default):
    try:
        return float(get_setting(key, default))
    except (TypeError, ValueError):
        return default


def get_setting_bool(key, default):
    v = get_setting(key, default)
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("1", "true", "yes", "on")
    return bool(v)


def all_settings():
    rows = query("SELECT key, value FROM settings ORDER BY key")
    out = {}
    for r in rows:
        try:
            out[r["key"]] = json.loads(r["value"])
        except (ValueError, TypeError):
            out[r["key"]] = r["value"]
    return out


def integrity_ok():
    """True when SQLite reports a healthy file. Never deletes or rebuilds the DB."""
    try:
        row = query_one("PRAGMA integrity_check")
        if not row:
            return False
        return str(next(iter(row.values()))).lower() == "ok"
    except Exception:
        return False
