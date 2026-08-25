"""Ollama client wrapper.

The LLM and embedding model are both swappable via config (OLLAMA_MODEL /
EMBEDDING_MODEL). Every call gracefully reports availability so the app can
fall back to the local rule-based extractor when Ollama is absent.
"""
import json
import time

import requests

from . import config


class OllamaError(Exception):
    pass


# Availability is checked on many request paths. Cache briefly so a down
# Ollama instance does not add a 2s timeout to every chat / embed call.
_AVAIL_TTL = 5.0
_avail_cache = {"t": 0.0, "v": False, "url": None}


def get_base_url():
    """Runtime-configurable base URL (persisted via Settings)."""
    try:
        from . import db
        return db.get_setting("ollama_base_url", config.OLLAMA_BASE_URL) or config.OLLAMA_BASE_URL
    except Exception:
        return config.OLLAMA_BASE_URL


def _url(path):
    base = get_base_url()
    if not isinstance(base, str):
        raise ValueError("Ollama URL must be text")
    return base.rstrip("/") + path


def available(timeout=2, force=False):
    """True if Ollama is reachable at the configured base URL.

    Ollama is optional, so malformed configuration and unexpected local-server
    responses are treated exactly like an offline server rather than escaping
    into the health check or chat request.
    """
    now = time.monotonic()
    try:
        url = get_base_url()
        cache_key = url if isinstance(url, str) else None
        if (
            not force
            and _avail_cache["url"] == cache_key
            and (now - _avail_cache["t"]) < _AVAIL_TTL
        ):
            return _avail_cache["v"]
        r = requests.get(_url("/api/tags"), timeout=timeout)
        payload = r.json() if r.status_code == 200 else None
        value = r.status_code == 200 and isinstance(payload, dict)
    except Exception:
        url = locals().get("url")
        value = False
    _avail_cache.update({"t": now, "v": value, "url": url if isinstance(url, str) else None})
    return value


def list_models():
    """Return installed model names, or an empty list when Ollama is offline."""
    try:
        r = requests.get(_url("/api/tags"), timeout=min(max(config.OLLAMA_TIMEOUT, 0.5), 2))
        r.raise_for_status()
        payload = r.json()
        models = payload.get("models", []) if isinstance(payload, dict) else []
        if not isinstance(models, list):
            return []
        return [m.get("name") for m in models if isinstance(m, dict) and m.get("name")]
    except Exception:
        return []


def model_installed(name):
    if not name:
        return False
    installed = list_models()
    if name in installed:
        return True
    # Ollama may report a tag suffix (qwen3:0.6b-q8_0).
    return any(m == name or m.startswith(name + "-") or m.startswith(name + ":")
               for m in installed)


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


def chat_stream(model, messages, temperature=0.0, timeout=None):
    """Yield assistant text chunks from a streaming Ollama chat call."""
    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
        "options": {"temperature": temperature, "num_ctx": 4096},
    }
    with requests.post(
        _url("/api/chat"),
        json=payload,
        timeout=timeout or config.OLLAMA_TIMEOUT,
        stream=True,
    ) as r:
        r.raise_for_status()
        for raw in r.iter_lines(decode_unicode=True):
            if not raw:
                continue
            try:
                data = json.loads(raw)
            except ValueError:
                continue
            piece = (data.get("message") or {}).get("content") or ""
            if piece:
                yield piece
            if data.get("done"):
                break


def embed(model, text):
    """Return an embedding vector (list of floats) for `text`.

    Tries the current `/api/embed` contract first, then the legacy
    `/api/embeddings` endpoint so both Ollama generations work. An unavailable
    or malformed Ollama response returns an empty vector; the store then uses
    its deterministic offline embedding.
    """
    try:
        r = requests.post(
            _url("/api/embed"),
            json={"model": model, "input": text},
            timeout=config.OLLAMA_TIMEOUT,
        )
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, dict) and data.get("embeddings"):
                return data["embeddings"][0]
            if isinstance(data, dict) and data.get("embedding"):
                return data["embedding"]
    except Exception:
        pass
    try:
        r = requests.post(
            _url("/api/embeddings"),
            json={"model": model, "prompt": text},
            timeout=config.OLLAMA_TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        return data.get("embedding", []) if isinstance(data, dict) else []
    except Exception:
        return []
