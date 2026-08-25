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


def test_entity_history_endpoint(client):
    client.post("/api/chat", json={"content": "I am learning Rust"})
    client.post("/api/chat", json={"content": "I stopped learning Rust"})
    rust = [e for e in client.get("/api/entities").json() if e["name"] == "Rust"][0]
    d = client.get(f"/api/entities/{rust['id']}").json()
    assert "history" in d
    assert "current" in d["history"] and "superseded" in d["history"]
    assert any(r["status"] == "superseded" for r in d["related"])
