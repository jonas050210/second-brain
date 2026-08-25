"""Tests for JSON/Markdown export and import (validation, merge, replace)."""
import json

from backend import db, export, extract, store


def _seed():
    extract.extract("I am learning Python.")
    extract.extract("My project Nebula uses Next.js.")


def test_json_export_shape():
    _seed()
    data = json.loads(export.export_json())
    assert data["format"] == "second-brain"
    assert data["version"] >= 1
    assert isinstance(data["entities"], list) and data["entities"]
    assert isinstance(data["relationships"], list)
    assert "exported_at" in data


def test_json_export_roundtrip_merge():
    _seed()
    data = json.loads(export.export_json())
    before = len(store.all_entities())
    result = export.import_merge(data)
    assert result["ok"] is True
    # Merge into an identical graph should not create duplicates.
    after = len(store.all_entities())
    assert after == before
    assert result["entities_created"] == 0


def test_markdown_export():
    _seed()
    md = export.export_markdown()
    assert "Second Brain" in md
    assert "## Entities" in md
    assert "## Relationships" in md
    assert "Python" in md


def test_import_validation_rejects_garbage():
    r = export.import_from_json("not json at all", mode="merge")
    assert r["ok"] is False


def test_import_validation_rejects_wrong_format():
    r = export.import_from_json(json.dumps({"format": "other", "entities": []}), mode="merge")
    assert r["ok"] is False


def test_import_validation_rejects_missing_keys():
    r = export.import_from_json(json.dumps({"format": "second-brain"}), mode="merge")
    assert r["ok"] is False


def test_import_merge_adds_new_entities():
    _seed()
    payload = {
        "format": "second-brain", "version": 1,
        "entities": [{"id": 999, "name": "Kubernetes", "type": "technology",
                      "description": "", "confidence": 0.9}],
        "relationships": [],
    }
    r = export.import_from_json(json.dumps(payload), mode="merge")
    assert r["ok"] is True
    assert store.find_entity_by_name("Kubernetes") is not None


def test_import_replace_wipes_and_loads():
    _seed()
    payload = {
        "format": "second-brain", "version": 1,
        "entities": [{"id": 1, "name": "Go", "type": "technology",
                      "description": "", "confidence": 0.9}],
        "relationships": [],
    }
    r = export.import_from_json(json.dumps(payload), mode="replace")
    assert r["ok"] is True
    ents = store.all_entities()
    names = {e["name"] for e in ents}
    assert "Go" in names
    # Old entities are gone (except the User entity).
    assert "Python" not in names
    assert "User" in names


def test_import_preserves_relationships():
    _seed()
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    store.add_relationship(a, b, "uses")
    data = json.loads(export.export_json())
    # Clear and re-import.
    export.import_from_json(json.dumps(data), mode="replace")
    rels = store.all_relationships()
    assert any(r["relation"] == "uses" for r in rels)


def test_export_includes_status_and_confidence():
    _seed()
    data = json.loads(export.export_json())
    ent = next(e for e in data["entities"] if e["name"] == "Python")
    assert "confidence" in ent and isinstance(ent["confidence"], (int, float))
    assert "status" in ent


def test_export_includes_facts():
    _seed()
    data = json.loads(export.export_json())
    assert "facts" in data and data["facts"]
    assert any("Python" in f["text"] for f in data["facts"])


def test_replace_import_restores_user_relationships():
    _seed()
    data = json.loads(export.export_json())
    r = export.import_from_json(json.dumps(data), mode="replace")
    assert r["ok"] is True
    py = store.find_entity_by_name("Python")
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=?",
        (uid, py["id"]),
    )
    assert rels, "learning relationship from User must survive replace import"


def test_note_chunk_split_and_import():
    chunks = export.split_note_chunks("I am learning Python.\n\n# Project\nNebula uses Ollama.")
    assert len(chunks) >= 2
    r = export.import_notes("I am learning Python.\n\nMy project Nebula uses Ollama.")
    assert r["ok"] is True
    assert store.find_entity_by_name("Python") is not None


def test_replace_import_preserves_source_messages_and_conversation():
    cid = store.create_conversation("Python notes", pinned=1, archived=1)
    mid = store.add_message("user", "I am learning Python", conversation_id=cid)
    extract.extract("I am learning Python", source_message_id=mid)
    data = json.loads(export.export_json())

    result = export.import_from_json(json.dumps(data), mode="replace")
    assert result["ok"] is True
    imported = store.conversation_summaries(archived=None)
    assert len(imported) == 1
    assert imported[0]["title"] == "Python notes"
    assert imported[0]["pinned"] == 1 and imported[0]["archived"] == 1
    imported_messages = store.conversation_messages(imported[0]["id"])
    assert imported_messages
    imported_mid = imported_messages[0]["id"]
    py = store.find_entity_by_name("Python")
    assert py["source_message_id"] == imported_mid
    rel = db.query_one("SELECT * FROM relationships WHERE relation='learning'")
    assert rel["source_message_id"] == imported_mid
    mem = db.query_one("SELECT * FROM memories WHERE message_id IS NOT NULL")
    assert mem["message_id"] == imported_mid


def test_import_merge_reports_exclusive_conflict_and_skips():
    extract.extract("I live in Berlin")
    uid = store.ensure_user_entity()
    payload = {
        "format": "second-brain", "version": 1,
        "entities": [
            {"id": uid, "name": "User", "type": "person", "confidence": 1.0},
            {"id": 99, "name": "Paris", "type": "location", "confidence": 0.9},
        ],
        "relationships": [
            {"source_id": uid, "target_id": 99, "relation": "lives_in", "confidence": 0.9},
            {"source_id": 12345, "target_id": 99, "relation": "related_to", "confidence": 0.5},
        ],
    }
    r = export.import_merge(payload)
    assert r["ok"] is True
    assert r["conflicts"]
    assert any(c.get("superseded") == "Berlin" for c in r["conflicts"])
    assert r["relationships_skipped"] >= 1
    assert any(s.get("reason") == "missing_endpoint" for s in r["skipped"])
    paris = store.find_entity_by_name("Paris")
    berlin = store.find_entity_by_name("Berlin")
    assert paris and berlin
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND relation='lives_in'",
        (uid,),
    )
    active = [x for x in rels if x["status"] == "active"]
    assert len(active) == 1
    assert active[0]["target_id"] == paris["id"]
    assert r.get("report") and "conflicts" in r["report"]
