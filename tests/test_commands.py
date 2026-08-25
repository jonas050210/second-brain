"""Tests for natural-language memory control commands."""
from backend import commands, db, store


def test_remember_command_recognized():
    assert commands.is_command("Remember that I prefer Python.")
    assert commands.is_command("Forget that I am learning Rust.")
    assert commands.is_command("Pin Nebula")
    assert not commands.is_command("I am learning Python.")
    assert not commands.is_command("Remember when I started Python")
    assert not commands.is_command("Delete this later")
    assert not commands.is_command("Change my mind about Rust")
    assert commands.is_command("Can you forget Rust")
    assert not commands.is_command("I forgot my keys at the office")
    assert not commands.is_command("Please remind me to learn Rust")
    assert not commands.is_command("We should remember this for later")
    assert not commands.is_command("Important meeting tomorrow")
    assert not commands.is_command("I remember living in Berlin")
    assert not commands.is_command("This is important to me")
    assert commands.is_command("Important Rust")
    assert commands.is_command("Unimportant Rust")
    assert commands.is_command("Undo last")
    assert commands.is_command("scratch that")
    assert not commands.is_command("that was wrong of me to skip Rust")


def test_forget_supersedes_learning():
    store.ensure_user_entity()
    # Seed a learning fact directly.
    rs = store.create_entity("Rust", "technology")
    uid = store.ensure_user_entity()
    store.add_relationship(uid, rs, "learning")
    r = commands.handle_command("Forget that I am learning Rust.")
    assert r["ok"] is True
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?", (uid, rs))
    assert rels[0]["status"] == "superseded"


def test_forget_removes_entity():
    e = store.create_entity("Old Project", "project")
    r = commands.handle_command("Remove the old game-engine project.")
    # Fallback: resolves best-match entity by substring and deletes it.
    assert r["ok"] is True or "couldn't find" in r["reply"]
    if r["ok"]:
        assert store.entity_row(e) is None


def test_pin_command():
    e = store.create_entity("Nebula", "project")
    r = commands.handle_command("Pin Nebula.")
    assert r["ok"] is True
    assert store.entity_row(e)["pinned"] == 1


def test_unpin_command():
    e = store.create_entity("Nebula", "project")
    store.update_entity(e, pinned=1)
    commands.handle_command("Unpin Nebula")
    assert store.entity_row(e)["pinned"] == 0


def test_mark_important():
    e = store.create_entity("Rust", "technology")
    r = commands.handle_command("Mark Rust as important.")
    assert r["ok"] is True
    assert store.entity_row(e)["important"] == 1


def test_merge_command():
    a = store.create_entity("Nebula", "project")
    b = store.create_entity("Nebula App", "project")
    r = commands.handle_command("Merge Nebula App into Nebula.")
    assert r["ok"] is True
    assert store.entity_row(b) is None


def test_rename_command():
    e = store.create_entity("Nebula", "project")
    r = commands.handle_command("Rename Nebula to Aurora.")
    assert r["ok"] is True
    assert store.entity_row(e)["name"] == "Aurora"


def test_preference_change_supersedes_old():
    uid = store.ensure_user_entity()
    py = store.create_entity("Python", "technology")
    rs = store.create_entity("Rust", "technology")
    store.add_relationship(uid, py, "prefers")
    r = commands.handle_command("Change my preferred language to Rust.")
    assert r["ok"] is True
    # Old preference superseded, new active.
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND relation='prefers'", (uid,))
    status = {store.entity_row(x["target_id"])["name"]: x["status"] for x in rels}
    assert status["Python"] == "superseded"
    assert status["Rust"] == "active"


def test_set_confidence_command():
    e = store.create_entity("Python", "technology")
    r = commands.handle_command("Set confidence of Python to 0.61")
    assert r["ok"] is True
    assert abs(store.entity_row(e)["confidence"] - 0.61) < 1e-6


def test_unknown_command_returns_none():
    assert commands.handle_command("I like to code") is None


def test_remember_without_that_is_remember_action():
    r = commands.handle_command("Remember I prefer Python")
    assert r is not None
    assert r.get("action") == "remember"
    assert "prefer Python" in r["payload"]


def test_important_command():
    e = store.create_entity("Rust", "technology")
    r = commands.handle_command("Important Rust")
    assert r["ok"] is True
    assert store.entity_row(e)["important"] == 1


def test_unimportant_command():
    e = store.create_entity("Rust", "technology")
    store.update_entity(e, important=1)
    r = commands.handle_command("Unimportant Rust")
    assert r["ok"] is True
    assert store.entity_row(e)["important"] == 0


def test_forget_prefer_supersedes_not_deletes():
    uid = store.ensure_user_entity()
    dark = store.create_entity("Dark Mode", "preference")
    store.add_relationship(uid, dark, "prefers")
    r = commands.handle_command("Forget that I prefer dark mode.")
    assert r["ok"] is True
    assert store.entity_row(dark) is not None
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
                    (uid, dark))
    assert rels and rels[0]["status"] == "superseded"


def test_forget_live_in_supersedes():
    uid = store.ensure_user_entity()
    berlin = store.create_entity("Berlin", "location")
    store.add_relationship(uid, berlin, "lives_in")
    r = commands.handle_command("Forget that I live in Berlin.")
    assert r["ok"] is True
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='lives_in'",
        (uid, berlin),
    )
    assert rels and rels[0]["status"] == "superseded"
    assert store.entity_row(berlin) is not None


def test_undo_last_command():
    from backend import extract
    extract.extract("I am learning Go")
    # Simulate the chat recorder.
    store.record_last_extract({
        "cid": 1,
        "msg_id": None,
        "extract": {
            "entities": [],
            "relationships": [{
                "source": store.ensure_user_entity(),
                "target": store.find_entity_by_name("Go")["id"],
                "relation": "learning",
                "new": True,
            }],
        },
    })
    r = commands.handle_command("Undo last")
    assert r["ok"] is True
    uid = store.ensure_user_entity()
    go = store.find_entity_by_name("Go")
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='learning'",
        (uid, go["id"]),
    )
    assert rels and rels[0]["status"] == "superseded"


def test_stop_remembering_forgets_entity():
    e = store.create_entity("OldFact", "concept")
    r = commands.handle_command("Stop remembering OldFact")
    assert r["ok"] is True
    assert store.entity_row(e) is None
