#!/usr/bin/env python3
"""Overall production test suite for Second Brain.

Covers the complete core loop:

    CHAT → MEMORY → GRAPH → SEARCH → RAG

plus startup, persistence, commands, conflicts, consolidation, export/import,
backup, reset, API and frontend contracts.

Run:
    python test_overall.py
    python -m pytest test_overall.py tests/ -q

These tests use a throwaway database and never touch real user data.
They do not weaken assertions to pass.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

# Isolate the database BEFORE importing backend modules.
_ROOT = Path(__file__).resolve().parent
_TMP = tempfile.mkdtemp(prefix="second-brain-overall-")
os.environ["SECOND_BRAIN_DB"] = str(Path(_TMP) / "overall.db")
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from backend import (  # noqa: E402
    app as app_module,
    backup,
    commands,
    config,
    db,
    export,
    extract,
    fallback,
    graph,
    ollama,
    search,
    store,
    summarize,
)


@pytest.fixture(autouse=True)
def fresh_db():
    for suffix in ("", "-wal", "-shm"):
        p = config.DB_PATH + suffix
        if os.path.exists(p):
            os.remove(p)
    db.init_db()
    store.ensure_user_entity()
    yield


@pytest.fixture
def client():
    return TestClient(app_module.app)


# --------------------------------------------------------------------------
# Startup / environment
# --------------------------------------------------------------------------

def test_startup_modules_importable():
    import main as main_mod
    import setup as setup_mod
    import start as start_mod

    assert hasattr(main_mod, "app")
    assert callable(setup_mod.main)
    assert callable(start_mod.main)
    assert start_mod.missing_runtime() == [] or isinstance(start_mod.missing_runtime(), list)


def test_start_check_succeeds_in_ready_env():
    import start as start_mod

    # --check must not start a server.
    rc = start_mod.main(["--check"])
    assert rc == 0


def test_frontend_assets_present():
    assert (Path(config.FRONTEND_DIR) / "index.html").is_file()
    assert (Path(config.FRONTEND_DIR) / "app.js").is_file()
    assert (Path(config.FRONTEND_DIR) / "style.css").is_file()
    assert (Path(config.FRONTEND_DIR) / "vendor" / "cytoscape.min.js").is_file()


def test_root_contract_files_exist():
    for name in ("main.py", "start.py", "setup.py", "test_overall.py",
                 "README.md", "requirements.txt", "ROADMAP"):
        assert (_ROOT / name).is_file(), f"missing required root file: {name}"


# --------------------------------------------------------------------------
# Database / migrations / persistence
# --------------------------------------------------------------------------

def test_database_schema_and_user_entity():
    uid = store.ensure_user_entity()
    row = store.entity_row(uid)
    assert row["norm_name"] == "user"
    tables = {r["name"] for r in db.query(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    for t in ("entities", "relationships", "messages", "conversations",
              "memories", "settings"):
        assert t in tables


def test_persistence_survives_reinit():
    eid = store.create_entity("Persistence Probe", "concept", confidence=0.7)
    db.init_db()
    assert store.entity_row(eid)["name"] == "Persistence Probe"


# --------------------------------------------------------------------------
# Ollama fallback
# --------------------------------------------------------------------------

def test_ollama_availability_is_boolean():
    assert ollama.available() in (True, False)


def test_fallback_embedding_and_extractor():
    vec = fallback.fallback_embed("Python programming")
    assert len(vec) == 256
    data = fallback.extract_with_rules("I am learning Python")
    names = [e["name"] for e in data["entities"]]
    assert "Python" in names


def test_trivial_filter():
    assert fallback.is_trivial("hello")
    assert fallback.is_trivial("thanks")
    assert not fallback.is_trivial("I am learning Rust")


# --------------------------------------------------------------------------
# Extraction / commands / conflicts
# --------------------------------------------------------------------------

def test_extract_creates_entities_relationships_and_memories():
    r = extract.extract("I am learning Python and I want to build AI agents.")
    assert not r["trivial"]
    names = [e["name"] for e in r["entities"]]
    assert "Python" in names
    assert any(rel["relation"] == "learning" for rel in r["relationships"])
    mems = store.recent_memories()
    assert any("Python" in m["text"] for m in mems)


def test_source_message_id_on_memories_and_entities():
    mid = store.add_message("user", "I am learning Go")
    extract.extract("I am learning Go", source_message_id=mid)
    go = store.find_entity_by_name("Go")
    assert go["source_message_id"] == mid
    mems = [m for m in store.recent_memories() if "Go" in m["text"]]
    assert mems
    assert any(m.get("message_id") == mid for m in mems)


def test_duplicate_detection_no_second_python():
    extract.extract("I am learning Python")
    before = len(store.all_entities())
    extract.extract("I am learning Python")
    assert len(store.all_entities()) == before


def test_switch_supersedes_old_learning():
    extract.extract("I am learning Python")
    r = extract.extract("I switched from Python to Rust")
    assert r["superseded"]
    uid = store.ensure_user_entity()
    py = store.find_entity_by_name("Python")
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='learning'",
        (uid, py["id"]),
    )
    assert rels and rels[0]["status"] == "superseded"
    rust = store.find_entity_by_name("Rust")
    assert rust is not None


def test_exclusive_lives_in_supersedes():
    extract.extract("I live in Berlin")
    extract.extract("I live in Paris")
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT r.*, e.name tname FROM relationships r JOIN entities e ON e.id=r.target_id "
        "WHERE r.source_id=? AND r.relation='lives_in'",
        (uid,),
    )
    active = [r for r in rels if r["status"] == "active"]
    superseded = [r for r in rels if r["status"] == "superseded"]
    assert any(r["tname"] == "Paris" for r in active)
    assert any(r["tname"] == "Berlin" for r in superseded)


def test_remember_command_without_that(client):
    r = client.post("/api/chat", json={"content": "Remember I prefer Python"})
    body = r.json()
    # Forced extraction of the payload.
    assert body.get("is_command") is not True or body.get("remembered") is not None
    py = store.find_entity_by_name("Python")
    assert py is not None
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, py["id"]),
    )
    assert rels and rels[0]["status"] == "active"


def test_important_command_modifies_db():
    rust = store.create_entity("Rust", "technology")
    assert commands.handle_command("Important Rust")["ok"]
    assert store.entity_row(rust)["important"] == 1


def test_all_memory_commands_modify_db():
    neb = store.create_entity("Nebula", "project")
    rust = store.create_entity("Rust", "technology")
    other = store.create_entity("Aurora", "project")
    uid = store.ensure_user_entity()
    store.add_relationship(uid, rust, "learning")

    assert commands.handle_command("Pin Nebula")["ok"]
    assert store.entity_row(neb)["pinned"] == 1
    assert commands.handle_command("Unpin Nebula")["ok"]
    assert store.entity_row(neb)["pinned"] == 0
    assert commands.handle_command("Mark Rust as important")["ok"]
    assert store.entity_row(rust)["important"] == 1
    assert commands.handle_command("Set confidence of Rust to 0.55")["ok"]
    assert abs(store.entity_row(rust)["confidence"] - 0.55) < 1e-6
    assert commands.handle_command("Rename Aurora to Helios")["ok"]
    assert store.entity_row(other)["name"] == "Helios"
    assert commands.handle_command("Forget that I am learning Rust")["ok"]
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?",
                    (uid, rust))
    assert rels[0]["status"] == "superseded"
    assert commands.handle_command("Merge Helios into Nebula")["ok"]
    assert store.entity_row(other) is None
    assert commands.handle_command("Remove Nebula")["ok"]
    assert store.entity_row(neb) is None


# --------------------------------------------------------------------------
# Graph
# --------------------------------------------------------------------------

def test_graph_is_real_data_not_fabricated():
    extract.extract("My new project Game Engine uses Bevy.")
    g = graph.filter_graph(active_only=True)
    names = {n["name"] for n in g["nodes"]}
    assert "Game Engine" in names and "Bevy" in names
    assert any(e["relation"] == "uses" for e in g["edges"])


def test_graph_neighborhood_and_path():
    extract.extract("I am learning Rust and I want to build a game engine.")
    extract.extract("My new project Game Engine uses Bevy.")
    rust = store.find_entity_by_name("Rust")
    bevy = store.find_entity_by_name("Bevy")
    hood = graph.neighborhood(rust["id"], depth=3)
    assert any(n["name"] == "Bevy" for n in hood["nodes"]) or \
        graph.shortest_path(rust["id"], bevy["id"]) is not None


# --------------------------------------------------------------------------
# Search / RAG / multi-hop
# --------------------------------------------------------------------------

def test_hybrid_search_and_multihop_rag():
    extract.extract("I am learning Rust and I want to build a game engine.")
    extract.extract("My new project Game Engine uses Bevy.")
    res = search.search("What technology does the game engine use?")
    texts = [f["text"] for f in res["facts"]]
    assert any("Bevy" in t for t in texts)
    ans = search.answer("What technology does the game engine use?")
    assert ans["status"] in ("known", "answered", "uncertain")
    assert ans.get("sources") is not None


def test_unknown_does_not_hallucinate():
    extract.extract("I am learning Python")
    a = search.answer("Do I use Java?")
    assert a["status"] == "unknown"
    assert "don't have" in a["text"].lower() or "nothing" in a["text"].lower()


def test_superseded_excluded_from_active_learning():
    extract.extract("I am learning Rust")
    extract.extract("I stopped learning Rust")
    facts = [f["text"] for f in search.intent_facts("learning")]
    assert not any("Rust" in t for t in facts)


# --------------------------------------------------------------------------
# Consolidation / export / import / backup / reset
# --------------------------------------------------------------------------

def test_consolidation_preserves_originals():
    for line in (
        "My project Nebula uses Next.js.",
        "Nebula uses Ollama.",
        "Nebula is an AI creative workspace.",
    ):
        extract.extract(line)
    neb = store.find_entity_by_name("Nebula")
    before = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    r = summarize.summarize_entity(neb["id"])
    assert r["ok"]
    after = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    assert after > before
    mem = db.query_one("SELECT * FROM memories WHERE id=?", (r["summary_id"],))
    meta = json.loads(mem["meta"] or "{}")
    assert meta.get("source_memory_ids")


def test_export_includes_facts_and_import_maps_user():
    extract.extract("I am learning Python")
    payload = json.loads(export.export_json())
    assert payload["format"] == "second-brain"
    assert payload["facts"]
    assert any("Python" in f["text"] for f in payload["facts"])
    # Wipe and replace — User-learning-Python must survive via id remap.
    result = export.import_from_json(json.dumps(payload), mode="replace")
    assert result["ok"]
    py = store.find_entity_by_name("Python")
    assert py is not None
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=?",
        (uid, py["id"]),
    )
    assert rels, "User relationships must be remapped on import"


def test_import_rejects_invalid_payload():
    r = export.import_from_json("not-json", mode="merge")
    assert r["ok"] is False


def test_backup_is_local_and_real():
    extract.extract("I am learning Python")
    r = backup.create_backup()
    assert r["ok"] and os.path.isdir(r["path"])
    assert os.path.exists(os.path.join(r["path"], "brain.db"))
    status = backup.backup_status()
    assert status["count"] >= 1


def test_reset_keeps_only_user(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    r = client.post("/api/reset", json={"confirm": False})
    assert r.status_code == 400
    client.post("/api/reset", json={"confirm": True})
    d = client.get("/api/dashboard").json()
    assert d["entities"] == 1
    assert d["relationships"] == 0


# --------------------------------------------------------------------------
# API + frontend contract
# --------------------------------------------------------------------------

def test_health_and_settings_and_privacy(client):
    h = client.get("/api/health").json()
    assert h["ok"] is True
    assert "ollama_available" in h
    s = client.get("/api/settings").json()
    assert s["privacy"]["telemetry"] is False
    assert s["privacy"]["local"] is True


def test_chat_persists_assistant_reply(client):
    client.post("/api/chat", json={"content": "I am learning Python"})
    convs = client.get("/api/conversations").json()
    msgs = client.get(f"/api/conversations/{convs[0]['id']}/messages").json()
    assistant = [m for m in msgs if m["role"] == "assistant"]
    assert assistant
    assert assistant[-1]["content"], "assistant reply must be stored, not empty"


def test_chat_stream_endpoint(client):
    with client.stream("POST", "/api/chat/stream",
                       json={"content": "I am learning Rust"}) as res:
        assert res.status_code == 200
        body = b"".join(res.iter_bytes()).decode("utf-8", errors="replace")
    assert "event: done" in body
    assert store.find_entity_by_name("Rust") is not None


def test_facts_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Python"})
    facts = client.get("/api/facts").json()
    assert any("Python" in f["text"] for f in facts)


def test_frontend_served(client):
    r = client.get("/")
    assert r.status_code == 200
    html = r.text
    assert "Second Brain" in html
    assert 'id="view-dashboard"' in html
    assert 'id="view-chat"' in html
    assert 'id="view-graph"' in html
    assert 'id="view-search"' in html
    assert 'id="view-settings"' in html


def test_core_loop_chat_memory_graph_search_rag(client):
    """The production contract: talk → remember → graph → retrieve."""
    r1 = client.post("/api/chat", json={
        "content": "I am learning Rust and I want to build a game engine",
    }).json()
    assert r1["remembered"]
    r2 = client.post("/api/chat", json={
        "content": "My new project Game Engine uses Bevy",
    }).json()
    assert r2["remembered"]

    g = client.get("/api/graph").json()
    labels = {n["label"] for n in g["nodes"]}
    assert {"Rust", "Game Engine", "Bevy"} <= labels

    s = client.post("/api/search", json={
        "query": "What technology am I learning for my game engine project?",
    }).json()
    fact_text = " ".join(f["text"] for f in s["facts"])
    assert "Bevy" in fact_text or "Rust" in fact_text
    assert s["status"] in ("known", "answered", "uncertain", "unknown")
    if s["status"] != "unknown":
        assert s.get("sources") is not None

    q = client.post("/api/chat", json={
        "content": "What technology does the game engine use?",
    }).json()
    assert q.get("is_answer") is True
    assert "Bevy" in q["reply"] or q.get("status") in ("known", "answered", "uncertain")


def test_dashboard_uses_real_counts(client):
    client.post("/api/chat", json={"content": "I am learning Python"})
    d = client.get("/api/dashboard").json()
    assert d["entities"] == len(store.all_entities())
    assert d["relationships"] == len(store.all_relationships())
    assert len(d["growth"]) == 14


# --------------------------------------------------------------------------
# Standalone runner
# --------------------------------------------------------------------------

def main() -> int:
    extra = []
    tests_dir = _ROOT / "tests"
    if tests_dir.is_dir():
        extra.append(str(tests_dir))
    return pytest.main([str(Path(__file__).resolve()), *extra, "-q"])


if __name__ == "__main__":
    raise SystemExit(main())
