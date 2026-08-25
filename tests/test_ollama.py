"""Tests for the Ollama-backed extraction path and model switching.

Uses a deterministic fake Ollama so the LLM path is exercised without a real
local model, alongside the offline fallback path.
"""
import json

from backend import db, extract, ollama, store


def test_llm_extraction_entities_and_relationships(fake_ollama):
    r = extract.extract("I am learning Rust and want to build a game engine")
    assert not r["used_fallback"], "should use the (fake) LLM, not fallback"
    names = [e["name"] for e in r["entities"]]
    assert "Rust" in names and "Game Engine" in names
    rels = [(x["relation"]) for x in r["relationships"]]
    assert "learning" in rels and "wants" in rels


def test_llm_extraction_stops(fake_ollama, monkeypatch):
    # Override the fake to return a "stops" list.
    def fake_chat(model, messages, temperature=0.0, format_json=False, timeout=None):
        return json.dumps({
            "entities": [{"name": "User", "type": "person", "confidence": 1.0}],
            "relationships": [],
            "stops": [{"source": "User", "target": "Rust", "relation": "learning"}],
        })
    monkeypatch.setattr(ollama, "chat", fake_chat)
    # Seed an active learning relationship first.
    uid = store.ensure_user_entity()
    rust = store.create_entity("Rust", "technology")
    store.add_relationship(uid, rust, "learning")
    r = extract.extract("I stopped learning Rust")
    assert r["superseded"], "stop list should supersede the learning relationship"
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?", (uid, rust))
    assert rels[0]["status"] == "superseded"


def test_model_switching_via_settings(fake_ollama, monkeypatch):
    seen_models = []
    def fake_chat(model, messages, **kw):
        seen_models.append(model)
        return json.dumps({"entities": [], "relationships": [], "stops": []})
    monkeypatch.setattr(ollama, "chat", fake_chat)
    db.set_setting("llm_model", "qwen3:1.7b")
    extract.extract("I am learning Rust")
    assert seen_models and seen_models[-1] == "qwen3:1.7b", "should use the configured model"


def test_embedding_model_switching(fake_ollama, monkeypatch):
    seen = []
    def fake_embed(model, text):
        seen.append(model)
        return [0.0] * 16
    monkeypatch.setattr(ollama, "embed", fake_embed)
    db.set_setting("embedding_model", "custom-embed")
    store.embed_text("hello")
    assert seen and seen[-1] == "custom-embed"


def test_offline_fallback_used(no_ollama):
    r = extract.extract("I am learning Python")
    assert r["used_fallback"] is True


def test_llm_failure_falls_back_to_rules(fake_ollama, monkeypatch):
    def boom(*a, **kw):
        raise RuntimeError("model unavailable")
    monkeypatch.setattr(ollama, "chat", boom)
    r = extract.extract("I am learning Python")
    assert r["used_fallback"] is True
    names = [e["name"] for e in r["entities"]]
    assert "Python" in names
