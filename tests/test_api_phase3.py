"""API tests for Phase 3 endpoints: advanced graph, export/import, backup,
summarization, and filtered search."""
import json

import pytest
from fastapi.testclient import TestClient

from backend import app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


def _seed(client):
    client.post("/api/chat", json={"content": "I am learning Rust and I want to build a game engine"})
    client.post("/api/chat", json={"content": "My new project Game Engine uses Bevy"})


def test_graph_filter_endpoint(client):
    _seed(client)
    r = client.get("/api/graph/filter", params={"entity_type": "technology"})
    assert r.status_code == 200
    assert all(n["type"] == "technology" for n in r.json()["nodes"])


def test_graph_neighborhood_endpoint(client):
    _seed(client)
    rust = [e for e in client.get("/api/entities").json() if e["name"] == "Rust"][0]
    r = client.get(f"/api/graph/neighborhood/{rust['id']}", params={"depth": 2})
    assert r.status_code == 200
    names = {n["name"] for n in r.json()["nodes"]}
    assert "Game Engine" in names


def test_graph_path_endpoint(client):
    _seed(client)
    rust = [e for e in client.get("/api/entities").json() if e["name"] == "Rust"][0]
    bevy = [e for e in client.get("/api/entities").json() if e["name"] == "Bevy"][0]
    r = client.get("/api/graph/path", params={"source_id": rust["id"], "target_id": bevy["id"]})
    assert r.status_code == 200
    assert r.json()["found"] is True


def test_graph_stats_endpoint(client):
    _seed(client)
    r = client.get("/api/graph/stats")
    assert r.status_code == 200
    assert r.json()["nodes"] >= 3


def test_export_json_endpoint(client):
    _seed(client)
    r = client.get("/api/export/json")
    assert r.status_code == 200
    data = json.loads(r.text)
    assert data["format"] == "second-brain"


def test_export_markdown_endpoint(client):
    _seed(client)
    r = client.get("/api/export/markdown")
    assert r.status_code == 200
    assert "## Entities" in r.text


def test_import_merge_endpoint(client):
    _seed(client)
    data = json.loads(client.get("/api/export/json").text)
    r = client.post("/api/import", json={"data": json.dumps(data), "mode": "merge"})
    assert r.status_code == 200
    assert r.json()["ok"] is True


def test_replace_import_creates_safety_backup(client):
    _seed(client)
    data = json.loads(client.get("/api/export/json").text)
    response = client.post("/api/import", json={
        "data": json.dumps(data), "mode": "replace", "confirm": True,
    })
    assert response.status_code == 200
    safety = response.json().get("safety_backup")
    assert safety and safety != ""


def test_import_invalid_rejected(client):
    r = client.post("/api/import", json={"data": "not json", "mode": "merge"})
    assert r.json()["ok"] is False


def test_backup_endpoint(client):
    _seed(client)
    r = client.post("/api/backup")
    assert r.status_code == 200
    assert r.json()["ok"] is True
    s = client.get("/api/backup/status").json()
    assert s["count"] >= 1
    listed = client.get("/api/backups").json()
    assert isinstance(listed, list) and listed


def test_backup_restore_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Python"})
    created = client.post("/api/backup").json()
    name = created["path"].rstrip("/").split("/")[-1]
    client.post("/api/reset", json={"confirm": True})
    assert not any(e["name"] == "Python" for e in client.get("/api/entities").json())
    bad = client.post("/api/backup/restore", json={"name": name, "confirm": False})
    assert bad.status_code == 400
    traversal = client.post("/api/backup/restore", json={"name": "../etc", "confirm": True})
    assert traversal.status_code == 400
    ok = client.post("/api/backup/restore", json={"name": name, "confirm": True})
    assert ok.status_code == 200
    assert any(e["name"] == "Python" for e in client.get("/api/entities").json())


def test_summarize_candidates_endpoint(client):
    _seed(client)
    r = client.get("/api/summarize/candidates")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_search_with_filters_endpoint(client):
    _seed(client)
    r = client.post("/api/search", json={"query": "game engine", "type": "project"})
    body = r.json()
    assert r.status_code == 200
    assert "sources" in body
    assert all(e["type"] == "project" for e in body["entities"])


def test_search_returns_sources_and_reasons(client):
    _seed(client)
    r = client.post("/api/search", json={"query": "Rust"})
    body = r.json()
    assert "sources" in body
    assert "reasons" in body["entities"][0]


def test_facts_endpoint(client):
    _seed(client)
    r = client.get("/api/facts")
    assert r.status_code == 200
    assert any("Rust" in f["text"] or "Bevy" in f["text"] for f in r.json())


def test_conversation_rename_and_delete(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    cid = client.get("/api/conversations").json()[0]["id"]
    r = client.patch(f"/api/conversations/{cid}", json={"title": "Rust notes"})
    assert r.status_code == 200
    titles = [c["title"] for c in client.get("/api/conversations").json()]
    assert "Rust notes" in titles
    client.delete(f"/api/conversations/{cid}")
    ids = [c["id"] for c in client.get("/api/conversations").json()]
    assert cid not in ids


def test_privacy_in_settings(client):
    s = client.get("/api/settings").json()
    assert s["privacy"]["telemetry"] is False
    assert s["privacy"]["mode"] == "local-first"


def test_chat_stream(client):
    with client.stream("POST", "/api/chat/stream",
                       json={"content": "I am learning Python"}) as res:
        assert res.status_code == 200
        text = b"".join(res.iter_bytes()).decode()
    assert "event: done" in text


def test_entity_history_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/chat", json={"content": "I stopped learning Rust"})
    rust = [e for e in client.get("/api/entities").json() if e["name"] == "Rust"][0]
    d = client.get(f"/api/entities/{rust['id']}").json()
    assert "history" in d
    assert "current" in d["history"] and "superseded" in d["history"]
    assert any(r["status"] == "superseded" for r in d["related"])
