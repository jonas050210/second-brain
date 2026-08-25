"""Tests for the database migration path (schema v2 -> v3 and idempotency)."""
import os
import sqlite3

from backend import config, db


def _build_v2_db(path):
    """Create a schema-v2 database (pre-`memories.meta`) with one memory row."""
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA user_version=2")
    conn.executescript("""
    CREATE TABLE entities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, norm_name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL DEFAULT 'concept', description TEXT NOT NULL DEFAULT '',
        aliases TEXT NOT NULL DEFAULT '[]', embedding TEXT,
        confidence REAL NOT NULL DEFAULT 0.8, source_message_id INTEGER,
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}',
        status TEXT NOT NULL DEFAULT 'active', pinned INTEGER NOT NULL DEFAULT 0,
        important INTEGER NOT NULL DEFAULT 0);
    CREATE TABLE relationships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_id INTEGER NOT NULL, target_id INTEGER NOT NULL, relation TEXT NOT NULL,
        confidence REAL NOT NULL DEFAULT 0.8, source_message_id INTEGER,
        created_at TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'active',
        UNIQUE(source_id, target_id, relation));
    CREATE TABLE conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
    CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT, conversation_id INTEGER,
        role TEXT NOT NULL, content TEXT NOT NULL, created_at TEXT NOT NULL,
        embedding TEXT, extracted INTEGER NOT NULL DEFAULT 0, meta TEXT NOT NULL DEFAULT '{}');
    CREATE TABLE memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT, kind TEXT NOT NULL, text TEXT NOT NULL,
        entity_ids TEXT NOT NULL DEFAULT '[]', message_id INTEGER,
        confidence REAL NOT NULL DEFAULT 0.8, created_at TEXT NOT NULL);
    CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT);
    """)
    conn.execute("INSERT INTO memories(kind, text, entity_ids, confidence, created_at) "
                 "VALUES('entity', 'legacy memory', '[]', 0.8, '2026-01-01T00:00:00+00:00')")
    conn.commit()
    conn.close()


def test_migration_v2_to_v3(monkeypatch, tmp_path):
    db_path = str(tmp_path / "legacy.db")
    _build_v2_db(db_path)
    monkeypatch.setattr(config, "DB_PATH", db_path)

    # Run the migration.
    db.init_db()

    conn = sqlite3.connect(db_path)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(memories)")}
    # New column added.
    assert "meta" in cols
    # Legacy data preserved.
    n = conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
    assert n == 1
    # user_version bumped.
    ver = conn.execute("PRAGMA user_version").fetchone()[0]
    assert ver == db.SCHEMA_VERSION
    conn.close()


def test_migration_idempotent(monkeypatch, tmp_path):
    """Running init_db() twice must not error or duplicate columns."""
    db_path = str(tmp_path / "idem.db")
    _build_v2_db(db_path)
    monkeypatch.setattr(config, "DB_PATH", db_path)
    db.init_db()
    db.init_db()  # second run must be a no-op
    conn = sqlite3.connect(db_path)
    cols = [r[1] for r in conn.execute("PRAGMA table_info(memories)")]
    assert cols.count("meta") == 1
    conn.close()
