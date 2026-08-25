"""Pytest fixtures for Second Brain.

Every test runs against a fresh, isolated temporary SQLite database so tests
never touch (or corrupt) real user data.
"""
import os
import sys
import tempfile

import pytest

# Point the app at a throwaway database BEFORE importing backend modules.
_TMPDIR = tempfile.mkdtemp(prefix="second-brain-test-")
os.environ["SECOND_BRAIN_DB"] = os.path.join(_TMPDIR, "test.db")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend import config, db, store  # noqa: E402


@pytest.fixture(autouse=True)
def fresh_db():
    """Recreate the schema and User entity before every test."""
    # Remove any existing db file(s).
    for suffix in ("", "-wal", "-shm"):
        p = config.DB_PATH + suffix
        if os.path.exists(p):
            os.remove(p)
    db.init_db()
    store.ensure_user_entity()
    yield
    # Clean up after the test.
    for suffix in ("", "-wal", "-shm"):
        p = config.DB_PATH + suffix
        if os.path.exists(p):
            os.remove(p)


@pytest.fixture
def no_ollama(monkeypatch):
    """Force the offline (rule-based) path for deterministic tests."""
    import backend.ollama as ollama
    monkeypatch.setattr(ollama, "available", lambda: False)
    return ollama


@pytest.fixture
def fake_ollama(monkeypatch):
    """Simulate an available Ollama with a deterministic JSON extraction."""
    import backend.ollama as ollama

    def fake_chat(model, messages, temperature=0.0, format_json=False, timeout=None):
        user_text = messages[-1]["content"] if messages else ""
        import json
        if "rust" in user_text.lower() and "game" in user_text.lower():
            return json.dumps({
                "entities": [
                    {"name": "User", "type": "person", "description": "", "confidence": 1.0},
                    {"name": "Rust", "type": "technology", "description": "", "confidence": 0.95},
                    {"name": "Game Engine", "type": "project", "description": "", "confidence": 0.9},
                ],
                "relationships": [
                    {"source": "User", "target": "Rust", "relation": "learning", "confidence": 0.95},
                    {"source": "User", "target": "Game Engine", "relation": "wants", "confidence": 0.9},
                ],
                "stops": [],
            })
        return json.dumps({"entities": [], "relationships": [], "stops": []})

    def fake_chat_stream(model, messages, temperature=0.0, timeout=None):
        text = fake_chat(model, messages, temperature=temperature)
        for i in range(0, len(text), 24):
            yield text[i:i + 24]

    monkeypatch.setattr(ollama, "available", lambda: True)
    monkeypatch.setattr(ollama, "chat", fake_chat)
    monkeypatch.setattr(ollama, "chat_stream", fake_chat_stream)
    return ollama
