"""Tests for the graph store: entities, merging, confidence, supersession,
memory history, and persistence."""
import json

import numpy as np

from backend import config, db, store


def test_entity_creation_and_normalization():
    eid = store.create_entity("  Python  ", "technology", "a language", 0.9)
    row = store.entity_row(eid)
    assert row["name"] == "Python"
    assert row["norm_name"] == "python"
    assert row["type"] == "technology"


def test_upsert_merges_duplicate_names():
    eid1, created1 = store.upsert_entity("Python", "technology", confidence=0.8)
    eid2, created2 = store.upsert_entity("python", "technology", confidence=0.9)
    assert created1 is True
    assert created2 is False
    assert eid1 == eid2
    row = store.entity_row(eid1)
    assert row["confidence"] == 0.9  # boosted


def test_alias_detection():
    eid = store.create_entity("Next.js", "technology")
    store.update_entity(eid, aliases=["NextJS"])
    dup = store.find_duplicate("NextJS", "technology")
    assert dup is not None and dup["id"] == eid


def test_semantic_duplicate_detection():
    # Two near-identical embeddings should collide above the threshold.
    e1 = store.create_entity("Machine Learning", "topic",
                             embedding=np.array([1.0, 0.0, 0.0], dtype=np.float32))
    dup = store.find_duplicate("Machine-Learning", "topic",
                               embedding=np.array([0.999, 0.01, 0.0], dtype=np.float32))
    assert dup is not None and dup["id"] == e1


def test_semantic_duplicate_below_threshold():
    e1 = store.create_entity("Machine Learning", "topic",
                             embedding=np.array([1.0, 0.0, 0.0], dtype=np.float32))
    dup = store.find_duplicate("Knitting", "topic",
                               embedding=np.array([0.0, 1.0, 0.0], dtype=np.float32))
    assert dup is None


def test_manual_merge_rewires_relationships():
    a = store.create_entity("Nebula", "project")
    b = store.create_entity("Nebula2", "project")
    tech = store.create_entity("Next.js", "technology")
    store.add_relationship(b, tech, "uses")
    res = store.merge_entities(a, b)
    assert res.get("ok")
    # b is gone, a now has the relationship.
    assert store.entity_row(b) is None
    rels = store.all_relationships()
    assert any(r["source_id"] == a and r["target_id"] == tech for r in rels)


def test_add_relationship_dedup():
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    store.add_relationship(a, b, "related_to", confidence=0.5)
    store.add_relationship(a, b, "related_to", confidence=0.9)
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?",
                    (a, b))
    assert len(rels) == 1
    assert rels[0]["confidence"] == 0.9


def test_supersede_relationship():
    a = store.create_entity("User2", "person")
    b = store.create_entity("Rust", "technology")
    store.add_relationship(a, b, "learning")
    n = store.supersede_relationship(a, b, "learning")
    assert n == 1
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?", (a, b))
    assert rels[0]["status"] == "superseded"


def test_supersede_relations_of_type():
    uid = store.ensure_user_entity()
    py = store.create_entity("Python", "technology")
    rs = store.create_entity("Rust", "technology")
    store.add_relationship(uid, py, "prefers")
    store.add_relationship(uid, rs, "prefers")
    changed = store.supersede_relations_of_type(uid, "prefers", except_target_id=rs)
    assert py in changed and rs not in changed


def test_delete_entity_cascades():
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    store.add_relationship(a, b, "related_to")
    store.delete_entity(a)
    assert store.entity_row(a) is None
    rels = db.query("SELECT * FROM relationships WHERE source_id=? OR target_id=?", (a, a))
    assert rels == []


def test_pin_and_important():
    eid = store.create_entity("Nebula", "project")
    store.update_entity(eid, pinned=1, important=1)
    row = store.entity_row(eid)
    assert row["pinned"] == 1 and row["important"] == 1


def test_set_confidence():
    eid = store.create_entity("Python", "technology")
    store.set_confidence(eid, 0.42)
    assert store.entity_row(eid)["confidence"] == 0.42


def test_memory_history_preserved_on_supersede():
    uid = store.ensure_user_entity()
    rs = store.create_entity("Rust", "technology")
    store.add_relationship(uid, rs, "learning")
    store.add_memory("relationship", "User learning Rust", entity_ids=[uid, rs])
    store.supersede_relationship(uid, rs, "learning")
    # The memory event remains (history is not deleted).
    mems = store.recent_memories()
    assert any("learning Rust" in m["text"] for m in mems)


def test_conversation_lifecycle():
    cid = store.create_conversation("test")
    store.add_message("user", "hello", conversation_id=cid)
    msgs = store.conversation_messages(cid)
    assert len(msgs) == 1
    assert store.conversation_row(cid)["title"] == "test"


def test_persistence_across_reopen():
    eid = store.create_entity("Python", "technology", confidence=0.7)
    # Simulate a restart by re-initializing from the same file.
    db.init_db()
    row = store.entity_row(eid)
    assert row is not None and row["name"] == "Python"


def test_user_entity_protected():
    uid = store.ensure_user_entity()
    assert store.entity_row(uid)["norm_name"] == "user"


def test_merge_preserves_description():
    a = store.create_entity("Nebula", "project", description="AI workspace")
    b = store.create_entity("Nebula2", "project", description="")
    store.merge_entities(a, b)
    assert store.entity_row(a)["description"] == "AI workspace"
