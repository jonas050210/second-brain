"""Tests for the extraction pipeline (offline fallback path)."""
import json

from backend import config, db, extract, store


def _run(text):
    return extract.extract(text)


def test_trivial_filtering():
    for msg in ["hello", "hi", "thanks", "ok", "what time is it", "tell me a joke",
                "how are you", "lol", "👍"]:
        r = _run(msg)
        assert r["trivial"] is True, f"'{msg}' should be trivial"
        assert r["entities"] == [] and r["relationships"] == []


def test_extract_learning():
    r = _run("I am learning Python")
    assert not r["trivial"]
    names = [e["name"] for e in r["entities"]]
    assert "Python" in names
    # relationship User -> learning -> Python
    assert any(rel["relation"] == "learning" for rel in r["relationships"])


def test_extract_project_uses():
    r = _run("My new project Nebula uses Next.js and Ollama")
    names = [e["name"] for e in r["entities"]]
    assert "Nebula" in names and "Next.js" in names and "Ollama" in names
    rels = [(store.entity_row(x["source"])["name"], x["relation"], store.entity_row(x["target"])["name"])
            for x in r["relationships"]]
    assert ("Nebula", "uses", "Next.js") in rels
    assert ("Nebula", "uses", "Ollama") in rels


def test_no_duplicate_on_repeat():
    _run("I am learning Python")
    before = store.all_entities()
    _run("I am learning Python")
    after = store.all_entities()
    assert len(after) == len(before), "re-asserting the same fact must not create duplicates"


def test_preference_relation():
    r = _run("I prefer Python")
    rels = [(x["relation"]) for x in r["relationships"]]
    assert "prefers" in rels


def test_prefer_instead_does_not_create_junk_entity():
    _run("I prefer Python")
    r = _run("I prefer Rust instead of Python")
    names = {e["name"] for e in store.all_entities()}
    assert "Rust Instead Of Python" not in names
    assert "Rust" in names
    uid = store.ensure_user_entity()
    py = store.find_entity_by_name("Python")
    rust = store.find_entity_by_name("Rust")
    py_rel = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, py["id"]))
    rust_rel = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, rust["id"]))
    assert py_rel and py_rel[0]["status"] == "superseded"
    assert rust_rel and rust_rel[0]["status"] == "active"


def test_location_relation():
    r = _run("I live in Berlin")
    rels = [(x["relation"]) for x in r["relationships"]]
    assert "lives_in" in rels


def test_confidence_recorded():
    _run("I am learning Python")
    py = store.find_entity_by_name("Python")
    assert py is not None
    assert 0.0 < py["confidence"] <= 1.0


def test_source_message_tracking():
    mid = store.add_message("user", "I am learning Go")
    r = extract.extract("I am learning Go", source_message_id=mid)
    go = store.find_entity_by_name("Go")
    assert go is not None
    # The entity created during this extraction should reference the message.
    assert go["source_message_id"] == mid


def test_stopped_creates_supersession():
    _run("I am learning Rust")
    r = _run("I stopped learning Rust")
    assert r["superseded"] or any("no longer active" in u for u in r.get("relationship_updates", []))
    # The learning relationship should now be superseded.
    rust = store.find_entity_by_name("Rust")
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='learning'",
        (uid, rust["id"]))
    assert rels and rels[0]["status"] == "superseded"


def test_switched_detects_conflict():
    _run("I use Python")
    r = _run("I switched from Python to Rust")
    # Old learning/usage should be superseded; new preference recorded.
    assert r["superseded"] or any("no longer active" in u for u in r.get("relationship_updates", []))


def test_embedding_stored():
    _run("I am learning Python")
    py = store.find_entity_by_name("Python")
    assert py["embedding"] is not None
    vec = store.vec_from_json(py["embedding"])
    assert vec is not None and vec.size > 0


def test_memory_events_written():
    _run("I am learning Python")
    mems = store.recent_memories()
    assert any("Python" in m["text"] for m in mems)


def test_multiword_concepts_not_trimmed():
    # Regression: "game engine" must not be trimmed to just "Engine".
    r = _run("I am learning Rust and I want to build a game engine")
    names = [e["name"] for e in r["entities"]]
    assert "Game Engine" in names
    types = {e["name"]: e["type"] for e in r["entities"]}
    assert types.get("Game Engine") == "project"


def test_junk_clause_is_not_an_entity():
    r = _run("I prefer Rust instead of Python")
    names = {e["name"] for e in store.all_entities()}
    assert "Instead Of Python" not in names
    assert "Rust Instead Of Python" not in names
    assert extract.is_junk_entity_name("instead of Python")
    assert extract.is_junk_entity_name("a")
    assert not extract.is_junk_entity_name("Python")


def test_relearn_after_stop_is_remembered():
    _run("I am learning Rust")
    _run("I stopped learning Rust")
    r = _run("I am learning Rust")
    assert any(x["relation"] == "learning" for x in r["relationships"])
    rust = store.find_entity_by_name("Rust")
    uid = store.ensure_user_entity()
    assert store.relationship_active(uid, rust["id"], "learning")


def test_list_learning_extracts_each_item():
    r = _run("I am learning Python, Rust, and Go")
    names = {e["name"] for e in r["entities"]}
    assert {"Python", "Rust", "Go"} <= names
    rels = [x["relation"] for x in r["relationships"]]
    assert rels.count("learning") >= 3


def test_work_on_creates_project():
    r = _run("I am working on Second Brain")
    names = {e["name"] for e in r["entities"]}
    assert "Second Brain" in names
    assert any(x["relation"] == "works_on" for x in r["relationships"])


def test_skill_extraction():
    r = _run("I'm good at public speaking")
    names = {e["name"] for e in r["entities"]}
    assert "Public Speaking" in names
    types = {e["name"]: e["type"] for e in r["entities"]}
    assert types.get("Public Speaking") == "skill"


def test_confidence_threshold_respected(no_ollama, monkeypatch):
    monkeypatch.setattr(db, "get_setting_float",
                        lambda k, d: 0.99 if k == "confidence_threshold" else d)
    # With a very high threshold, nothing should be persisted.
    r = extract.extract("I am learning Python")
    # entities list in result is only appended for created entities; but even
    # upserts below threshold are skipped entirely.
    assert r["entities"] == [] or all(e.get("created") is False for e in r["entities"])
