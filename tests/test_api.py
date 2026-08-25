"""API integration tests using FastAPI's TestClient."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient  # noqa: E402

from backend import app as app_module  # noqa: E402


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


def test_import_rejects_oversized_payload(client):
    huge = "x" * (8 * 1024 * 1024 + 50)
    r = client.post("/api/import", json={"data": huge, "mode": "merge"})
    assert r.status_code == 400
