"""Malformed input, size caps, and database-recovery safety.

These tests never delete or replace a real user brain. They only use the
isolated fixture database.
"""
from backend import config, db, export, fallback, graph, search, store


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


def test_invalid_import_is_rejected_before_any_write():
    before = len(store.all_entities())
    bad_payloads = [
        {"format": "second-brain", "entities": [{"name": 123}], "relationships": []},
        {"format": "second-brain", "entities": [{"name": "X", "type": 123}], "relationships": []},
        {"format": "second-brain", "entities": [{"name": "X"}],
         "relationships": [{"source_id": 1, "target_id": 2, "relation": 123}]},
    ]
    for payload in bad_payloads:
        result = export.import_merge(payload)
        assert result["ok"] is False
        assert len(store.all_entities()) == before


def test_corrupt_embeddings_are_ignored_by_search():
    good = store.create_entity(
        "Good vector", "concept", embedding=fallback.fallback_embed("Good vector")
    )
    bad = store.create_entity("Bad vector", "concept")
    db.execute("UPDATE entities SET embedding=? WHERE id=?", ("not-json", bad))
    assert search.vector_search("Good vector")
    assert store.similar_entities(good) == []


def test_shortest_path_honors_depth_limit():
    nodes = [store.create_entity(f"Node {i}", "concept") for i in range(4)]
    for left, right in zip(nodes, nodes[1:]):
        store.add_relationship(left, right, "related_to")
    assert graph.shortest_path(nodes[0], nodes[-1], max_depth=2) is None
    assert graph.shortest_path(nodes[0], nodes[-1], max_depth=3)
