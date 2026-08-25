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
