"""Malformed input, size caps, and database-recovery safety.

These tests never delete or replace a real user brain. They only use the
isolated fixture database.
"""
from backend import config, db, export, store


def test_integrity_ok_on_healthy_file():
    assert db.integrity_ok() is True


def test_integrity_ok_false_on_garbage_does_not_rebuild():
    path = config.DB_PATH
    with open(path, "wb") as fh:
        fh.write(b"not a sqlite database at all")
    assert db.integrity_ok() is False
    # The file is still there — we do not delete or replace a bad brain.
    with open(path, "rb") as fh:
        assert fh.read().startswith(b"not a sqlite")


def test_import_rejects_non_object_and_wrong_types():
    assert export.import_from_json("[]", mode="merge")["ok"] is False
    assert export.import_from_json("null", mode="merge")["ok"] is False
    bad = '{"format":"second-brain","entities":"nope","relationships":[]}'
    assert export.import_from_json(bad, mode="merge")["ok"] is False


def test_conversation_summaries_escape_like_wildcards():
    cid = store.create_conversation("Rust notes")
    store.add_message("user", "I am learning Rust", conversation_id=cid)
    hits = store.conversation_summaries(query="Rust")
    assert any(c["id"] == cid for c in hits)
    assert store.conversation_summaries(query="%") == []
    assert store.conversation_summaries(query="_") == []
    assert store.conversation_summaries(query="no-such-thread") == []
