"""API integration tests using FastAPI's TestClient."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient  # noqa: E402

from backend import app as app_module  # noqa: E402
from backend import store  # noqa: E402


@pytest.fixture
def client():
    return TestClient(app_module.app)


def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["ok"] is True


def test_chat_creates_memory(client):
    r = client.post("/api/chat", json={"content": "I am learning Python"})
    assert r.status_code == 200
    body = r.json()
    assert body["remembered"] != []
    assert any(x.get("name") == "Python" for x in body["remembered"])


def test_chat_trivial_no_memory(client):
    r = client.post("/api/chat", json={"content": "hello"})
    assert r.json()["trivial"] is True
    assert r.json()["remembered"] == []


def test_chat_command(client):
    r = client.post("/api/chat", json={"content": "Pin Nebula"})
    assert r.json()["is_command"] is True


def test_question_answer(client):
    client.post("/api/chat", json={"content": "I am learning Go"})
    r = client.post("/api/chat", json={"content": "What am I learning?"})
    assert r.json()["is_answer"] is True


def test_graph_endpoint(client):
    client.post("/api/chat", json={"content": "My project Nebula uses Next.js"})
    r = client.get("/api/graph")
    nodes = r.json()["nodes"]
    assert any(n["label"] == "Nebula" for n in nodes)
    assert any(n["label"] == "Next.js" for n in nodes)


def test_entities_list_and_detail(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    r = client.get("/api/entities")
    eid = [e["id"] for e in r.json() if e["name"] == "Rust"][0]
    d = client.get(f"/api/entities/{eid}").json()
    assert d["entity"]["name"] == "Rust"
    assert d["entity"]["confidence"] > 0
    assert d["entity"]["embedding"] is True


def test_entity_patch_and_delete(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    eid = [e["id"] for e in client.get("/api/entities").json() if e["name"] == "Rust"][0]
    client.patch(f"/api/entities/{eid}", json={"description": "a systems language",
                                               "important": True, "pinned": True})
    d = client.get(f"/api/entities/{eid}").json()["entity"]
    assert d["description"] == "a systems language"
    assert d["important"] == 1 and d["pinned"] == 1
    client.delete(f"/api/entities/{eid}")
    assert client.get(f"/api/entities/{eid}").status_code == 404


def test_merge_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/chat", json={"content": "I am learning Rust programming"})
    ids = {e["name"]: e["id"] for e in client.get("/api/entities").json()}
    r = client.post("/api/entities/merge", json={"keep_id": ids["Rust"], "drop_id": ids["Rust Programming"]})
    assert r.json().get("ok") or r.json().get("error") == "invalid merge target"


def test_memories_timeline(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    mems = client.get("/api/memories").json()
    assert any("Rust" in m["text"] for m in mems)


def test_search_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    r = client.post("/api/search", json={"query": "What am I learning?"})
    body = r.json()
    assert body["status"] in ("known", "answered", "unknown", "uncertain")


def test_dashboard(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    d = client.get("/api/dashboard").json()
    assert d["entities"] >= 2  # User + Rust
    assert d["relationships"] >= 1
    assert "growth" in d and len(d["growth"]) == 14


def test_settings_rejects_non_http_ollama_url(client):
    r = client.post("/api/settings", json={"ollama_base_url": "file:///etc/passwd"})
    assert r.status_code == 400


def test_settings_roundtrip(client):
    r = client.post("/api/settings", json={"llm_model": "qwen3:1.7b",
                                           "confidence_threshold": 0.5,
                                           "auto_memory": False})
    s = r.json()
    assert s["llm_model"] == "qwen3:1.7b"
    assert abs(s["confidence_threshold"] - 0.5) < 1e-6
    assert s["auto_memory"] is False


def test_reset_requires_confirmation(client):
    r = client.post("/api/reset", json={"confirm": False})
    assert r.status_code == 400


def test_reset(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/reset", json={"confirm": True})
    d = client.get("/api/dashboard").json()
    assert d["entities"] == 1  # only User remains
    assert d["relationships"] == 0


def test_conversations(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    convos = client.get("/api/conversations").json()
    assert len(convos) >= 1


def test_ollama_offline_fallback(client, monkeypatch):
    import backend.ollama as ollama
    monkeypatch.setattr(ollama, "available", lambda: False)
    r = client.post("/api/chat", json={"content": "I am learning Rust"})
    assert r.json()["used_fallback"] is True


def test_demo_endpoint(client):
    r = client.post("/api/demo")
    assert r.json()["ok"] is True
    d = client.get("/api/dashboard").json()
    assert d["entities"] > 1


def test_relationship_patch(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    rust = [e for e in client.get("/api/entities").json() if e["name"] == "Rust"][0]
    rels = client.get("/api/facts").json()
    rid = next(f["id"] for f in rels if f["target_id"] == rust["id"])
    r = client.patch(f"/api/relationships/{rid}", json={"confidence": 0.42})
    assert r.status_code == 200
    facts = client.get("/api/facts").json()
    hit = next(f for f in facts if f["id"] == rid)
    assert abs(hit["confidence"] - 0.42) < 1e-6


def test_security_headers_present(client):
    r = client.get("/api/health")
    assert r.headers.get("x-content-type-options") == "nosniff"
    assert r.headers.get("x-frame-options") == "SAMEORIGIN"
    assert "default-src 'self'" in (r.headers.get("content-security-policy") or "")


def test_create_relationship_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/chat", json={"content": "My new project Game Engine uses Bevy"})
    ents = {e["name"]: e["id"] for e in client.get("/api/entities").json()}
    r = client.post("/api/relationships", json={
        "source_id": ents["Game Engine"], "target_id": ents["Rust"], "relation": "uses",
    })
    assert r.status_code == 200
    assert r.json()["ok"] is True
    facts = client.get("/api/facts").json()
    assert any(f["source"] == "Game Engine" and f["target"] == "Rust" for f in facts)


def test_import_notes_extracts_paragraphs(client):
    r = client.post("/api/import/notes", json={
        "text": "I am learning Python.\n\nMy project Nebula uses Ollama.",
    })
    assert r.status_code == 200
    assert r.json()["ok"] is True
    assert r.json()["chunks"] >= 1
    names = {e["name"] for e in client.get("/api/entities").json()}
    assert "Python" in names or "Nebula" in names


def test_health_reports_version(client):
    h = client.get("/api/health").json()
    assert h.get("version") == "2.6.0"
    assert h.get("db_ok") is True
    assert "auto_backup" in h


def test_graph_groups_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    r = client.get("/api/graph/groups")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, dict)
    flat = {n["name"] for rows in body.values() for n in rows}
    assert "Rust" in flat


def test_auto_backup_setting_roundtrip(client):
    r = client.post("/api/settings", json={"auto_backup_hours": 12})
    assert r.status_code == 200
    assert abs(r.json()["auto_backup_hours"] - 12) < 1e-6


def test_chat_stream_emits_token_after_extract(client):
    with client.stream("POST", "/api/chat/stream",
                       json={"content": "I am learning Python"}) as res:
        assert res.status_code == 200
        text = b"".join(res.iter_bytes()).decode("utf-8", errors="replace")
    assert "event: token" in text
    assert "event: done" in text
    assert store.find_entity_by_name("Python") is not None


def test_import_rejects_oversized_payload(client):
    huge = "x" * (8 * 1024 * 1024 + 50)
    r = client.post("/api/import", json={"data": huge, "mode": "merge"})
    assert r.status_code == 400


def test_conversation_search_by_message_body(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/conversations/new")
    client.post("/api/chat", json={"content": "I live in Berlin"})
    hits = client.get("/api/conversations", params={"q": "Berlin"}).json()
    assert len(hits) >= 1
    none = client.get("/api/conversations", params={"q": "zzzz-no-such-chat"}).json()
    assert none == []
    wild = client.get("/api/conversations", params={"q": "%"}).json()
    assert wild == []


def test_graph_focus_user_hides_islands(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    from backend import store
    for i in range(45):
        store.create_entity(f"Island {i}", "concept")
    auto = client.get("/api/graph", params={"focus": "auto"}).json()
    assert auto["focus"] == "user"
    labels = {n["label"] for n in auto["nodes"]}
    assert "Rust" in labels
    assert "Island 0" not in labels
    full = client.get("/api/graph", params={"focus": "all"}).json()
    assert any(n["label"] == "Island 0" for n in full["nodes"])


def test_settings_reports_db_ok_and_no_activity_watch(client):
    s = client.get("/api/settings").json()
    assert s.get("db_ok") is True
    assert s["privacy"].get("activity_watch") is False


def test_entities_sort_degree(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/chat", json={"content": "My new project Game Engine uses Bevy"})
    rows = client.get("/api/entities", params={"sort": "degree"}).json()
    assert rows
    degrees = [r["degree"] for r in rows]
    assert degrees == sorted(degrees, reverse=True)
    names = client.get("/api/entities", params={"sort": "name"}).json()
    assert [e["name"].lower() for e in names] == sorted(e["name"].lower() for e in names)


def test_entity_detail_includes_similar(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    rust = next(e for e in client.get("/api/entities").json() if e["name"] == "Rust")
    d = client.get(f"/api/entities/{rust['id']}").json()
    assert "similar" in d
    assert isinstance(d["similar"], list)


def test_undo_last_extract_supersedes(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    rust = store.find_entity_by_name("Rust")
    assert rust is not None
    r = client.post("/api/undo").json()
    assert r["ok"] is True
    assert r["undone"] >= 1
    uid = store.ensure_user_entity()
    rels = [x for x in store.all_relationships()
            if x["source_id"] == uid and x["target_id"] == rust["id"]
            and x["relation"] == "learning"]
    assert rels and rels[0]["status"] == "superseded"
    again = client.post("/api/undo").json()
    assert again["ok"] is False


def test_conversation_pin_and_archive(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    convs = client.get("/api/conversations").json()
    cid = convs[0]["id"]
    r = client.patch(f"/api/conversations/{cid}", json={"pinned": True})
    assert r.status_code == 200
    pinned = client.get("/api/conversations").json()
    assert pinned[0]["id"] == cid
    assert pinned[0]["pinned"] == 1
    client.patch(f"/api/conversations/{cid}", json={"archived": True})
    hidden = client.get("/api/conversations").json()
    assert all(c["id"] != cid for c in hidden)
    shown = client.get("/api/conversations", params={"archived": "1"}).json()
    assert any(c["id"] == cid for c in shown)


def test_import_file_notes(client):
    r = client.post("/api/import/file", json={
        "filename": "notes.md",
        "text": "I am learning Python.\n\nI live in Berlin.",
    })
    assert r.status_code == 200
    assert r.json()["ok"] is True
    names = {e["name"] for e in client.get("/api/entities").json()}
    assert "Python" in names or "Berlin" in names


def test_entity_aliases_roundtrip(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    rust = next(e for e in client.get("/api/entities").json() if e["name"] == "Rust")
    r = client.patch(f"/api/entities/{rust['id']}", json={"aliases": ["Rustlang", "Rust Lang"]})
    assert r.status_code == 200
    d = client.get(f"/api/entities/{rust['id']}").json()
    assert "Rustlang" in d["entity"]["aliases"]


def test_memories_text_search(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    hits = client.get("/api/memories", params={"q": "Rust"}).json()
    assert any("Rust" in m["text"] for m in hits)
    none = client.get("/api/memories", params={"q": "zzzz-no-memory"}).json()
    assert none == []


def test_entities_orphans_filter(client):
    from backend import store
    store.create_entity("Lonely Island", "concept")
    rows = client.get("/api/entities", params={"orphans": True}).json()
    names = {e["name"] for e in rows}
    assert "Lonely Island" in names
    assert "User" not in names


def test_conversation_export_markdown(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    cid = client.get("/api/conversations").json()[0]["id"]
    r = client.get(f"/api/conversations/{cid}/export")
    assert r.status_code == 200
    assert "learning Rust" in r.text
    assert "text/markdown" in r.headers.get("content-type", "")


def test_favicon_served(client):
    r = client.get("/favicon.png")
    assert r.status_code == 200
    assert r.content[:8] == b"\x89PNG\r\n\x1a\n"


def test_chat_empty_and_huge_payload(client):
    empty = client.post("/api/chat", json={"content": "   "})
    assert empty.status_code == 200
    assert empty.json()["trivial"] is True
    huge = client.post("/api/chat", json={"content": "I am learning Python. " + ("x" * 20000)})
    assert huge.status_code == 200
    assert store.find_entity_by_name("Python") is not None
