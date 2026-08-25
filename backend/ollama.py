"""Ollama client wrapper.

The LLM and embedding model are both swappable via config (OLLAMA_MODEL /
EMBEDDING_MODEL). Every call gracefully reports availability so the app can
fall back to the local rule-based extractor when Ollama is absent.
"""
import requests

from . import config


class OllamaError(Exception):
    pass


def get_base_url():
    """Runtime-configurable base URL (persisted via Settings)."""
    try:
        from . import db
        return db.get_setting("ollama_base_url", config.OLLAMA_BASE_URL)
    except Exception:
        return config.OLLAMA_BASE_URL


def _url(path):
    return get_base_url().rstrip("/") + path


def available(timeout=2):
    """True if Ollama is reachable at the configured base URL."""
    try:
        r = requests.get(_url("/api/tags"), timeout=timeout)
        return r.status_code == 200
    except requests.RequestException:
        return False


def list_models():
    try:
        r = requests.get(_url("/api/tags"), timeout=config.OLLAMA_TIMEOUT)
        r.raise_for_status()
        return [m.get("name") for m in r.json().get("models", [])]
    except requests.RequestException:
        return []


def model_installed(name):
    return name in list_models()


def chat(model, messages, temperature=0.0, format_json=False, timeout=None):
    """Run a chat completion. Returns the assistant's text."""
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature, "num_ctx": 4096},
    }
    if format_json:
        payload["format"] = "json"
    r = requests.post(
        _url("/api/chat"),
        json=payload,
        timeout=timeout or config.OLLAMA_TIMEOUT,
    )
    r.raise_for_status()
    data = r.json()
    return data.get("message", {}).get("content", "")


def embed(model, text):
    """Return an embedding vector (list of floats) for `text`."""
    r = requests.post(
        _url("/api/embeddings"),
        json={"model": model, "prompt": text},
        timeout=config.OLLAMA_TIMEOUT,
    )
    r.raise_for_status()
    return r.json().get("embedding", [])
