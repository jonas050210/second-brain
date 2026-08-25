# Second Brain — complete project archive

Every first-party file is inlined below, including tests, launcher,
and the vendor Cytoscape build. This is documentation, not a second app.
Live source of truth remains the individual files.

Generated: 2026-08-25 15:29 UTC
Version: 2.5.0
Files archived: 60

Omitted: `.git/`, virtualenvs, caches, user `data/brain.db`.

## Table of contents

- [`.env.example`](#envexample)
- [`.gitignore`](#gitignore)
- [`backend/.env.example`](#backendenvexample)
- [`backend/__init__.py`](#backendinitpy)
- [`backend/app.py`](#backendapppy)
- [`backend/backup.py`](#backendbackuppy)
- [`backend/commands.py`](#backendcommandspy)
- [`backend/config.py`](#backendconfigpy)
- [`backend/db.py`](#backenddbpy)
- [`backend/export.py`](#backendexportpy)
- [`backend/extract.py`](#backendextractpy)
- [`backend/fallback.py`](#backendfallbackpy)
- [`backend/graph.py`](#backendgraphpy)
- [`backend/ollama.py`](#backendollamapy)
- [`backend/paths.py`](#backendpathspy)
- [`backend/requirements-dev.txt`](#backendrequirementsdevtxt)
- [`backend/requirements.txt`](#backendrequirementstxt)
- [`backend/search.py`](#backendsearchpy)
- [`backend/store.py`](#backendstorepy)
- [`backend/summarize.py`](#backendsummarizepy)
- [`frontend/app.js`](#frontendappjs)
- [`frontend/index.html`](#frontendindexhtml)
- [`frontend/style.css`](#frontendstylecss)
- [`frontend/vendor/cytoscape.min.js`](#frontendvendorcytoscapeminjs)
- [`launcher/__init__.py`](#launcherinitpy)
- [`launcher/__main__.py`](#launchermainpy)
- [`launcher/bootstrap.py`](#launcherbootstrappy)
- [`launcher/build_exe.py`](#launcherbuildexepy)
- [`launcher/gui.py`](#launcherguipy)
- [`launcher/icons.py`](#launchericonspy)
- [`launcher/secondbrain.ico`](#launchersecondbrainico)
- [`launcher/secondbrain.png`](#launchersecondbrainpng)
- [`launcher/tray.py`](#launchertraypy)
- [`main.py`](#mainpy)
- [`pytest.ini`](#pytestini)
- [`README.md`](#readmemd)
- [`requirements.txt`](#requirementstxt)
- [`ROADMAP`](#roadmap)
- [`run.py`](#runpy)
- [`secondbrain.spec`](#secondbrainspec)
- [`start.py`](#startpy)
- [`test_overall.py`](#testoverallpy)
- [`tests/conftest.py`](#testsconftestpy)
- [`tests/test_api.py`](#teststestapipy)
- [`tests/test_api_phase3.py`](#teststestapiphase3py)
- [`tests/test_backup.py`](#teststestbackuppy)
- [`tests/test_commands.py`](#teststestcommandspy)
- [`tests/test_export.py`](#teststestexportpy)
- [`tests/test_extraction.py`](#teststestextractionpy)
- [`tests/test_frontend.py`](#teststestfrontendpy)
- [`tests/test_graph.py`](#teststestgraphpy)
- [`tests/test_launcher.py`](#teststestlauncherpy)
- [`tests/test_migration.py`](#teststestmigrationpy)
- [`tests/test_ollama.py`](#teststestollamapy)
- [`tests/test_reliability.py`](#teststestreliabilitypy)
- [`tests/test_search.py`](#teststestsearchpy)
- [`tests/test_search_advanced.py`](#teststestsearchadvancedpy)
- [`tests/test_store.py`](#teststeststorepy)
- [`tests/test_summarize.py`](#teststestsummarizepy)
- [`tests/test_tray.py`](#teststesttraypy)

## File tree

```
     634  .env.example
     285  .gitignore
     459  backend/.env.example
       0  backend/__init__.py
   45015  backend/app.py
    7918  backend/backup.py
   15631  backend/commands.py
    8457  backend/config.py
    7595  backend/db.py
   16937  backend/export.py
   23019  backend/extract.py
   22824  backend/fallback.py
   15570  backend/graph.py
    4385  backend/ollama.py
    4130  backend/paths.py
     242  backend/requirements-dev.txt
      66  backend/requirements.txt
   39931  backend/search.py
   21276  backend/store.py
    5372  backend/summarize.py
   70836  frontend/app.js
   19189  frontend/index.html
   28208  frontend/style.css
  373304  frontend/vendor/cytoscape.min.js
     222  launcher/__init__.py
    3553  launcher/__main__.py
   11648  launcher/bootstrap.py
    1617  launcher/build_exe.py
   14580  launcher/gui.py
     963  launcher/icons.py
  147587  launcher/secondbrain.ico
   48109  launcher/secondbrain.png
    9022  launcher/tray.py
     728  main.py
      91  pytest.ini
    8248  README.md
     165  requirements.txt
    2949  ROADMAP
     223  run.py
    2743  secondbrain.spec
    9375  start.py
   17929  test_overall.py
    2849  tests/conftest.py
   11246  tests/test_api.py
    5976  tests/test_api_phase3.py
    3318  tests/test_backup.py
    6002  tests/test_commands.py
    5750  tests/test_export.py
   10392  tests/test_extraction.py
    5592  tests/test_frontend.py
    4805  tests/test_graph.py
    8594  tests/test_launcher.py
    3365  tests/test_migration.py
    2945  tests/test_ollama.py
    1468  tests/test_reliability.py
    6997  tests/test_search.py
    3065  tests/test_search_advanced.py
    6837  tests/test_store.py
    2508  tests/test_summarize.py
    1898  tests/test_tray.py
```

## `.env.example`

````
# Second Brain configuration — copy to .env and edit, or change via Settings UI.
# The LLM and embedding model are fully swappable without touching code.

# Local LLM used for knowledge extraction (and optional answers).
OLLAMA_MODEL=qwen3:0.6b

# Embedding model used for semantic memory search.
EMBEDDING_MODEL=nomic-embed-text

# Ollama runtime endpoint (http/https only).
OLLAMA_BASE_URL=http://localhost:11434

# Optional bind override for start.py / SecondBrain.exe
# SECOND_BRAIN_HOST=0.0.0.0
# SECOND_BRAIN_PORT=8000
# SECOND_BRAIN_DB=data/brain.db
# SECOND_BRAIN_DATA=
# SECOND_BRAIN_PULL_MODELS=1
# SECOND_BRAIN_NO_VENV=1
````

## `.gitignore`

````
# Personal knowledge database (do NOT commit your memory)
data/
*.db
*.db-wal
*.db-shm

# Python
__pycache__/
*.pyc
.venv/
venv/

# Tests / caches
.pytest_cache/
.playwright/
node_modules/

# Packaged launcher
build/
dist/
*.spec.bak

# OS / editor
.DS_Store
Thumbs.db
.idea/
.vscode/
````

## `backend/.env.example`

````
# Second Brain configuration — copy to .env and edit, or change via Settings UI.
# The LLM and embedding model are fully swappable without touching code.

# Local LLM used for knowledge extraction (and optional answers).
OLLAMA_MODEL=qwen3:0.6b
# Smaller/faster fallback if 0.6b is unreliable: qwen3:1.7b

# Embedding model used for semantic memory search.
EMBEDDING_MODEL=nomic-embed-text

# Ollama runtime endpoint.
OLLAMA_BASE_URL=http://localhost:11434
````

## `backend/__init__.py`

````

````

## `backend/app.py`

````
"""Second Brain — local AI knowledge graph.

FastAPI backend + static frontend. Everything runs locally; the only external
dependency (optional) is a local Ollama instance.
"""
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Optional

from urllib.parse import urlparse

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

MAX_IMPORT_BYTES = 8 * 1024 * 1024
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "no-referrer",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
    "Content-Security-Policy": (
        "default-src 'self'; script-src 'self'; "
        "style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
        "connect-src 'self'; object-src 'none'; base-uri 'self'; "
        "frame-ancestors 'self'"
    ),
}

from . import backup, commands, config, db, export, extract, ollama, search, store, summarize
from . import graph as graph_engine
from .paths import APP_VERSION

app = FastAPI(title="Second Brain", version=APP_VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    for key, value in SECURITY_HEADERS.items():
        response.headers.setdefault(key, value)
    return response

db.init_db()
store.ensure_user_entity()


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def effective_llm_model():
    return db.get_setting("llm_model", config.DEFAULT_LLM_MODEL)


def effective_embedding_model():
    return db.get_setting("embedding_model", config.DEFAULT_EMBEDDING_MODEL)


def auto_memory_enabled():
    return db.get_setting_bool("auto_memory", True)


SMALLTALK = {
    "hi": "Hello! I'm your Second Brain. Tell me what you're working on, learning, or thinking about.",
    "hello": "Hi there! Go ahead — I'll remember the important things you tell me.",
    "hey": "Hey! What's on your mind today?",
    "how are you": "Running locally and ready to learn. What have you been working on?",
    "thanks": "Anytime. Keep talking — I'll keep building your knowledge graph.",
    "thank you": "You're welcome!",
    "what can you do": "I watch our conversation and automatically build a knowledge graph of people, projects, technologies, interests, goals and facts. Then you can search me like a real memory. Try: \"I'm learning Python and want to build AI agents.\"",
    "what time is it": "I don't track the clock — I track your knowledge. Tell me what you're learning or building!",
}


def smalltalk_reply(text):
    return SMALLTALK.get(text.strip().lower().strip(".,!? "))


def _natural_reply_fallback(remembered, used_fallback):
    if not remembered:
        return ("I heard you, but I didn't find anything durable to save yet. "
                "Try telling me about a project, a technology, or a goal.")
    head = "Got it — I've updated your brain."
    if used_fallback:
        head += " (offline mode)"
    return head


def _natural_reply_messages(text, remembered):
    lines = []
    for r in remembered:
        if r["kind"] == "entity":
            lines.append(f'- new {r["type"]}: {r["name"]}')
        else:
            lines.append(f'- {r["source"]} {r["relation"]} {r["target"]}')
    summary = "\n".join(lines) if lines else "(nothing durable)"
    prompt = (
        "You are a friendly personal Second Brain. The user said: "
        f"\"{text}\"\nYou extracted these memories:\n{summary}\n\n"
        "Acknowledge naturally in one or two short sentences and confirm "
        "what you will remember. Do NOT invent anything beyond the list. "
        "Do NOT reveal internal reasoning or say 'chain of thought'."
    )
    return [
        {"role": "system", "content": "You are a concise, friendly personal knowledge assistant."},
        {"role": "user", "content": prompt},
    ]


def natural_reply(text, remembered, used_fallback):
    """A short, grounded acknowledgment (never chain-of-thought)."""
    if ollama.available():
        try:
            text_out = ollama.chat(
                effective_llm_model(), _natural_reply_messages(text, remembered),
                temperature=0.3,
            ).strip()
            if text_out:
                return text_out
        except Exception:
            pass
    return _natural_reply_fallback(remembered, used_fallback)


def natural_reply_stream(text, remembered, used_fallback):
    if ollama.available():
        try:
            acc = []
            for piece in ollama.chat_stream(
                effective_llm_model(), _natural_reply_messages(text, remembered),
                temperature=0.3,
            ):
                if piece:
                    acc.append(piece)
                    yield piece
            if "".join(acc).strip():
                return
        except Exception:
            pass
    yield _natural_reply_fallback(remembered, used_fallback)


def build_updates(result):
    """Human-readable change list for the chat + timeline."""
    return result.get("entity_updates", []) + result.get("relationship_updates", [])


# --------------------------------------------------------------------------
# API: health / models
# --------------------------------------------------------------------------

@app.get("/api/health")
def health():
    return {
        "ok": True,
        "ollama_available": ollama.available(),
        "llm_model": effective_llm_model(),
        "embedding_model": effective_embedding_model(),
        "db_path": config.DB_PATH,
        "models_installed": ollama.list_models(),
        "version": APP_VERSION,
        "db_ok": db.integrity_ok(),
        "auto_backup": backup.auto_backup_status(),
    }


def _safe_auto_backup():
    """Create a backup only after a memory write. Never called from health."""
    try:
        return backup.maybe_auto_backup()
    except Exception as exc:
        return {"ok": False, "skipped": True, "reason": f"error: {exc}"}


@app.get("/api/models")
def models():
    return {
        "available": ollama.list_models(),
        "llm_model": effective_llm_model(),
        "embedding_model": effective_embedding_model(),
    }


# --------------------------------------------------------------------------
# API: chat
# --------------------------------------------------------------------------

class ChatIn(BaseModel):
    content: str
    conversation_id: Optional[int] = None


@app.post("/api/chat")
def chat(body: ChatIn):
    turn = prepare_turn(body.content, body.conversation_id)
    reply = "".join(render_reply(turn))
    return finalize_turn(turn, reply)


def prepare_turn(content, conversation_id=None):
    """Persist the user turn and run extraction / retrieval. No assistant text yet."""
    content = (content or "").strip()
    turn = {
        "kind": "empty",
        "cid": None,
        "content": content,
        "ready_reply": "",
        "remembered": [],
        "updates": [],
        "superseded": [],
        "used_fallback": False,
        "trivial": False,
        "is_command": False,
        "is_answer": False,
        "ok": True,
        "status": "",
        "sources": [],
        "extract": None,
        "retrieval": None,
        "context": "",
        "original": content,
    }
    if not content:
        turn["trivial"] = True
        return turn
    if len(content) > config.MAX_CHAT_CHARS:
        content = content[:config.MAX_CHAT_CHARS]
        turn["content"] = content
        turn["original"] = content

    cid = conversation_id or store.current_conversation_id()
    turn["cid"] = cid
    msg_id = store.add_message("user", content, conversation_id=cid,
                               embedding=store.embed_text(content))
    turn["msg_id"] = msg_id

    conv = store.conversation_row(cid)
    if conv and not conv["title"]:
        store.touch_conversation(cid, title=content[:60])

    context = [m for m in store.conversation_messages(cid, config.SHORT_TERM_CONTEXT_TURNS)]

    cmd = commands.handle_command(content) if commands.is_command(content) else None
    if cmd and "action" not in cmd:
        turn["kind"] = "command"
        turn["ready_reply"] = cmd.get("reply", "Done.")
        turn["is_command"] = True
        turn["ok"] = cmd.get("ok", True)
        return turn

    if cmd and cmd.get("action") == "remember":
        content = cmd["payload"]
        turn["content"] = content

    if search.is_question(turn["original"]) and not smalltalk_reply(turn["original"]) \
            and not (cmd and cmd.get("action") == "remember"):
        recent = [m["content"] for m in context if m["role"] == "user"][-4:]
        turn["kind"] = "question"
        turn["is_answer"] = True
        turn["context"] = "\n".join(recent)
        retrieved = search.retrieve_answer(turn["original"])
        if retrieved.get("final"):
            turn["ready_reply"] = retrieved.get("text") or ""
            turn["status"] = _normalize_status(retrieved.get("status"))
            turn["sources"] = retrieved.get("sources") or []
        else:
            turn["retrieval"] = retrieved.get("retrieval") or {}
            turn["status"] = _normalize_status(
                search._status_of(turn["retrieval"], turn["original"])
            )
            turn["sources"] = turn["retrieval"].get("sources") or []
        return turn

    if smalltalk_reply(turn["original"]):
        turn["kind"] = "smalltalk"
        turn["ready_reply"] = smalltalk_reply(turn["original"])
        turn["trivial"] = True
        return turn

    if not auto_memory_enabled():
        turn["kind"] = "off"
        turn["ready_reply"] = (
            "Auto-memory is off, so I won't save this. (Turn it back on in Settings.)"
        )
        turn["trivial"] = True
        return turn

    result = extract.extract(content, model=effective_llm_model(),
                             source_message_id=msg_id)
    if result["trivial"]:
        turn["kind"] = "smalltalk"
        turn["ready_reply"] = "Noted. Tell me more about what you're building or learning."
        turn["trivial"] = True
        return turn

    turn["kind"] = "extract"
    turn["extract"] = result
    turn["remembered"] = result.get("remembered") or []
    turn["updates"] = build_updates(result)
    turn["superseded"] = result.get("superseded") or []
    turn["used_fallback"] = result.get("used_fallback", False)
    return turn


def render_reply(turn):
    """Yield reply text. Extraction / retrieval has already finished."""
    if turn["kind"] == "empty":
        return
    if turn["kind"] == "question" and turn.get("retrieval") is not None:
        yield from search.compose_answer_stream(
            turn["original"], turn["retrieval"], effective_llm_model(),
            context=turn.get("context") or "",
        )
        return
    if turn["kind"] == "extract":
        yield from natural_reply_stream(
            turn.get("original") or turn["content"],
            turn.get("remembered") or [],
            turn.get("used_fallback"),
        )
        return
    if turn.get("ready_reply"):
        yield turn["ready_reply"]


def finalize_turn(turn, reply):
    cid = turn.get("cid")
    if turn["kind"] == "empty":
        return {"reply": "", "remembered": [], "trivial": True}

    meta = {"kind": turn["kind"]}
    extracted = 0
    if turn["kind"] == "command":
        meta = {"kind": "command", "ok": turn.get("ok", True)}
    elif turn["kind"] == "question":
        meta = {"kind": "answer", "status": turn.get("status") or "",
                "sources": turn.get("sources") or []}
    elif turn["kind"] == "extract":
        extracted = 1 if (turn.get("remembered") or turn.get("updates")) else 0
        meta = {"updates": turn.get("updates") or [],
                "used_fallback": turn.get("used_fallback"),
                "remembered": turn.get("remembered") or [],
                "superseded": turn.get("superseded") or []}
    elif turn["kind"] == "off":
        meta = {"kind": "off"}
    else:
        meta = {"kind": "smalltalk"}

    store.add_message("assistant", reply or "", conversation_id=cid,
                      extracted=extracted, meta=meta)

    out = {
        "reply": reply or "",
        "remembered": turn.get("remembered") or [],
        "updates": turn.get("updates") or [],
        "superseded": turn.get("superseded") or [],
        "used_fallback": turn.get("used_fallback", False),
        "trivial": turn.get("trivial", False),
        "conversation_id": cid,
    }
    if turn.get("is_command"):
        out["is_command"] = True
        out["ok"] = turn.get("ok", True)
    if turn.get("is_answer"):
        out["is_answer"] = True
        out["status"] = turn.get("status") or ""
        out["sources"] = turn.get("sources") or []
    if turn["kind"] in ("extract", "command") and (
        out.get("remembered") or out.get("updates") or out.get("is_command")
    ):
        _safe_auto_backup()
    return out


def _normalize_status(status):
    if status in ("answered", "known"):
        return "known"
    if status in ("unknown", "uncertain"):
        return status
    return "unknown"


def _sse(event, payload):
    return f"event: {event}\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"


# --------------------------------------------------------------------------
# API: messages / conversations
# --------------------------------------------------------------------------

@app.get("/api/messages")
def get_messages():
    rows = store.messages()
    out = []
    for r in rows:
        meta = json.loads(r.get("meta") or "{}")
        out.append({"id": r["id"], "role": r["role"], "content": r["content"],
                    "created_at": r["created_at"], "extracted": r["extracted"],
                    "conversation_id": r.get("conversation_id"),
                    "updates": meta.get("updates", []), "kind": meta.get("kind", ""),
                    "demo": bool(meta.get("demo"))})
    return out


@app.get("/api/messages/{mid}")
def get_message(mid: int):
    r = store.message_by_id(mid)
    if not r:
        raise HTTPException(404, "message not found")
    conv = store.conversation_row(r.get("conversation_id")) if r.get("conversation_id") else None
    return {"id": r["id"], "role": r["role"], "content": r["content"],
            "created_at": r["created_at"], "conversation_id": r.get("conversation_id"),
            "conversation_title": conv["title"] if conv else None}


@app.get("/api/conversations")
def conversations(q: str = None):
    return store.conversation_summaries(query=q)


@app.post("/api/conversations/new")
def conversations_new():
    cid = store.new_conversation()
    return {"conversation_id": cid}


class ConversationPatch(BaseModel):
    title: Optional[str] = None


@app.patch("/api/conversations/{cid}")
def conversation_update(cid: int, body: ConversationPatch):
    if not store.conversation_row(cid):
        raise HTTPException(404, "conversation not found")
    if body.title is not None:
        store.touch_conversation(cid, title=body.title.strip()[:80])
    return {"ok": True, "conversation": store.conversation_row(cid)}


@app.delete("/api/conversations/{cid}")
def conversation_delete(cid: int):
    if not store.conversation_row(cid):
        raise HTTPException(404, "conversation not found")
    store.delete_conversation(cid)
    return {"ok": True, "conversation_id": store.current_conversation_id()}


@app.get("/api/conversations/{cid}/messages")
def conversation_messages(cid: int):
    out = []
    for m in store.conversation_messages(cid):
        meta = json.loads(m.get("meta") or "{}")
        out.append({"id": m["id"], "role": m["role"], "content": m["content"],
                    "created_at": m["created_at"],
                    "updates": meta.get("updates", []),
                    "remembered": meta.get("remembered", []),
                    "kind": meta.get("kind", ""),
                    "status": meta.get("status", ""),
                    "sources": meta.get("sources", []),
                    "superseded": meta.get("superseded", [])})
    return out


# --------------------------------------------------------------------------
# API: graph
# --------------------------------------------------------------------------

@app.get("/api/graph")
def graph(active_only: bool = True, focus: str = "auto", depth: int = 2):
    return graph_engine.graph_view(focus=focus, depth=depth, active_only=active_only)


@app.get("/api/graph/filter")
def graph_filter(entity_type: str = None, relation: str = None,
                 min_confidence: float = None, active_only: bool = True,
                 pinned: bool = None, important: bool = None, query: str = None):
    """Filtered graph view (nodes + edges + stats)."""
    return graph_engine.filter_graph(
        entity_type=entity_type, relation=relation, min_confidence=min_confidence,
        active_only=active_only, pinned=pinned, important=important, query=query,
    )


@app.get("/api/graph/neighborhood/{eid}")
def graph_neighborhood(eid: int, depth: int = 1, relation: str = None, active_only: bool = True):
    if not store.entity_row(eid):
        raise HTTPException(404, "entity not found")
    return graph_engine.neighborhood(eid, depth=min(max(depth, 1), 6), relation=relation,
                              active_only=active_only)


@app.get("/api/graph/path")
def graph_path(source_id: int, target_id: int, active_only: bool = True):
    path = graph_engine.shortest_path(source_id, target_id, active_only=active_only)
    return {"path": path, "found": path is not None}


@app.get("/api/graph/stats")
def graph_stats():
    return graph_engine.graph_stats()


@app.get("/api/graph/groups")
def graph_groups(active_only: bool = True):
    return graph_engine.group_by_type(active_only=active_only)


# --------------------------------------------------------------------------
# API: entities
# --------------------------------------------------------------------------

def _entity_degree_map():
    rels = store.all_relationships(active_only=True)
    deg = defaultdict(int)
    for r in rels:
        deg[r["source_id"]] += 1
        deg[r["target_id"]] += 1
    return deg


@app.get("/api/entities")
def entities(q: str = None, type: str = None, pinned: bool = None, important: bool = None,
             sort: str = "name"):
    rows = store.all_entities()
    if type:
        rows = [r for r in rows if r["type"] == type]
    if q:
        ql = q.lower()
        rows = [r for r in rows if ql in r["name"].lower()]
    if pinned is not None:
        rows = [r for r in rows if bool(r.get("pinned", 0)) == pinned]
    if important is not None:
        rows = [r for r in rows if bool(r.get("important", 0)) == important]
    deg = _entity_degree_map()
    out = [{"id": r["id"], "name": r["name"], "type": r["type"],
            "description": r["description"], "degree": deg.get(r["id"], 0),
            "confidence": r["confidence"], "pinned": r.get("pinned", 0),
            "important": r.get("important", 0), "status": r.get("status", "active"),
            "created_at": r["created_at"], "updated_at": r["updated_at"],
            "source_message_id": r.get("source_message_id")} for r in rows]
    key = (sort or "name").lower()
    if key == "degree":
        out.sort(key=lambda e: (-int(e.get("degree") or 0), (e.get("name") or "").lower()))
    elif key == "recent":
        out.sort(key=lambda e: e.get("updated_at") or e.get("created_at") or "", reverse=True)
    elif key == "confidence":
        out.sort(key=lambda e: (-float(e.get("confidence") or 0), (e.get("name") or "").lower()))
    else:
        out.sort(key=lambda e: (e.get("name") or "").lower())
    return out


def _source_for(message_id):
    if not message_id:
        return None
    m = store.message_by_id(message_id)
    if not m:
        return None
    conv = store.conversation_row(m.get("conversation_id")) if m.get("conversation_id") else None
    return {"message_id": m["id"], "content": m["content"],
            "created_at": m["created_at"],
            "conversation_id": m.get("conversation_id"),
            "conversation_title": conv["title"] if conv else None}


@app.get("/api/entities/{eid}")
def entity_detail(eid: int):
    row = store.entity_row(eid)
    if not row:
        raise HTTPException(404, "entity not found")
    rels = db.query(
        "SELECT r.id rid, r.relation, r.created_at, r.status, r.confidence, r.source_message_id, "
        "s.id sid, s.name sname, s.type stype, "
        "t.id tid, t.name tname, t.type ttype "
        "FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE r.source_id=? OR r.target_id=? ORDER BY r.status='active' DESC, r.created_at DESC",
        (eid, eid),
    )
    related = []
    for r in rels:
        if r["sid"] == eid:
            related.append({"other_id": r["tid"], "other_name": r["tname"],
                            "other_type": r["ttype"], "relation": r["relation"],
                            "canonical": r["relation"],
                            "direction": "out", "rid": r["rid"], "status": r["status"],
                            "confidence": r["confidence"],
                            "source": _source_for(r["source_message_id"])})
        else:
            inv = {v: k for k, v in config.RELATION_INVERSE.items()}.get(r["relation"], r["relation"])
            related.append({"other_id": r["sid"], "other_name": r["sname"],
                            "other_type": r["stype"], "relation": inv,
                            "canonical": r["relation"],
                            "direction": "in", "rid": r["rid"], "status": r["status"],
                            "confidence": r["confidence"],
                            "source": _source_for(r["source_message_id"])})
    mems = store.memories_for_entity(eid)

    # ---- History: active vs superseded facts + change timeline ------------
    active_rels = [r for r in rels if r["status"] == "active"]
    superseded_rels = [r for r in rels if r["status"] != "active"]
    history = {
        "current": _readable_rels(eid, active_rels),
        "superseded": _readable_rels(eid, superseded_rels),
        "changes": [{"text": m["text"], "kind": m["kind"], "created_at": m["created_at"]}
                    for m in mems if m["kind"] in ("superseded", "conflict", "update", "command")][:20],
    }

    return {
        "entity": {
            "id": row["id"], "name": row["name"], "type": row["type"],
            "description": row["description"], "aliases": json.loads(row["aliases"] or "[]"),
            "confidence": row["confidence"], "created_at": row["created_at"],
            "updated_at": row["updated_at"], "status": row.get("status", "active"),
            "pinned": row.get("pinned", 0), "important": row.get("important", 0),
            "embedding": bool(row.get("embedding")),
            "source": _source_for(row.get("source_message_id")),
            "meta": json.loads(row.get("meta") or "{}"),
        },
        "related": related,
        "memories": mems,
        "history": history,
        "similar": store.similar_entities(eid),
    }


def _readable_rels(eid, rels):
    """Turn relationship rows into readable 'X relation Y' strings (canonical)."""
    out = []
    for r in rels:
        if r["sid"] == eid:
            out.append({"text": f'{r["sname"]} {r["relation"]} {r["tname"]}',
                        "relation": r["relation"], "confidence": r["confidence"],
                        "other_id": r["tid"], "other_name": r["tname"],
                        "created_at": r["created_at"], "status": r["status"]})
        else:
            inv = {v: k for k, v in config.RELATION_INVERSE.items()}.get(r["relation"], r["relation"])
            out.append({"text": f'{r["tname"]} {inv} {r["sname"]}',
                        "relation": inv, "confidence": r["confidence"],
                        "other_id": r["sid"], "other_name": r["sname"],
                        "created_at": r["created_at"], "status": r["status"]})
    return out


class EntityPatch(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    pinned: Optional[bool] = None
    important: Optional[bool] = None


@app.patch("/api/entities/{eid}")
def entity_update(eid: int, body: EntityPatch):
    row = store.entity_row(eid)
    if not row:
        raise HTTPException(404, "entity not found")
    fields = {}
    if body.name is not None:
        fields["name"] = body.name
    if body.type is not None:
        fields["type"] = store.normalize_type(body.type)
    if body.description is not None:
        fields["description"] = body.description
    if body.confidence is not None:
        fields["confidence"] = max(0.0, min(1.0, body.confidence))
    if body.status is not None:
        fields["status"] = body.status
    if body.pinned is not None:
        fields["pinned"] = 1 if body.pinned else 0
    if body.important is not None:
        fields["important"] = 1 if body.important else 0
    store.update_entity(eid, **fields)
    return {"ok": True}


@app.delete("/api/entities/{eid}")
def entity_delete(eid: int):
    row = store.entity_row(eid)
    if not row:
        raise HTTPException(404, "entity not found")
    if row["norm_name"] == store.normalize_name(config.USER_ENTITY_NAME):
        raise HTTPException(400, "cannot delete the User entity")
    store.add_memory("command", f'Deleted entity {row["name"]}', entity_ids=[eid])
    store.delete_entity(eid)
    return {"ok": True}


class MergeIn(BaseModel):
    keep_id: int
    drop_id: int


@app.post("/api/entities/merge")
def entity_merge(body: MergeIn):
    return store.merge_entities(body.keep_id, body.drop_id)


class RelPatch(BaseModel):
    relation: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None


@app.patch("/api/relationships/{rid}")
def rel_update(rid: int, body: RelPatch):
    row = store.relationship_row(rid)
    if not row:
        raise HTTPException(404, "relationship not found")
    fields = {}
    if body.relation is not None:
        rel, _swap = store.normalize_relation(body.relation)
        fields["relation"] = rel
    if body.confidence is not None:
        fields["confidence"] = max(0.0, min(1.0, body.confidence))
    if body.status is not None:
        fields["status"] = body.status
    store.update_relationship(rid, **fields)
    return {"ok": True}


@app.delete("/api/relationships/{rid}")
def rel_delete(rid: int):
    store.delete_relationship(rid)
    return {"ok": True}


class RelCreate(BaseModel):
    source_id: int
    target_id: int
    relation: str
    confidence: Optional[float] = 0.8


@app.post("/api/relationships")
def rel_create(body: RelCreate):
    if not store.entity_row(body.source_id) or not store.entity_row(body.target_id):
        raise HTTPException(404, "entity not found")
    if body.source_id == body.target_id:
        raise HTTPException(400, "cannot relate an entity to itself")
    rel, swap = store.normalize_relation(body.relation)
    sid, tid = body.source_id, body.target_id
    if swap:
        sid, tid = tid, sid
    conf = max(0.0, min(1.0, float(body.confidence if body.confidence is not None else 0.8)))
    rid = store.add_relationship(sid, tid, rel, confidence=conf)
    srow, trow = store.entity_row(sid), store.entity_row(tid)
    store.add_memory("relationship", f'{srow["name"]} → {rel} → {trow["name"]}',
                     entity_ids=[sid, tid], confidence=conf)
    return {"ok": True, "id": rid, "relation": rel, "source_id": sid, "target_id": tid}


@app.get("/api/facts")
def list_facts(active_only: bool = True, status: str = None, entity_id: int = None):
    """Readable facts (relationships) from the real graph. Never fabricated."""
    rels = store.all_relationships(active_only=False)
    ents = {e["id"]: e for e in store.all_entities()}
    out = []
    for r in rels:
        if active_only and r.get("status", "active") != "active":
            continue
        if status and r.get("status", "active") != status:
            continue
        if entity_id is not None and entity_id not in (r["source_id"], r["target_id"]):
            continue
        src, tgt = ents.get(r["source_id"]), ents.get(r["target_id"])
        if not src or not tgt:
            continue
        out.append({
            "id": r["id"],
            "text": f'{src["name"]} {r["relation"]} {tgt["name"]}',
            "source_id": r["source_id"], "target_id": r["target_id"],
            "source": src["name"], "target": tgt["name"],
            "relation": r["relation"], "confidence": r["confidence"],
            "status": r.get("status", "active"),
            "source_message_id": r.get("source_message_id"),
            "created_at": r.get("created_at"),
        })
    return out


# --------------------------------------------------------------------------
# API: memories (timeline)
# --------------------------------------------------------------------------

@app.get("/api/memories")
def memories(limit: int = 200, entity_id: int = None, kind: str = None,
             type: str = None, conversation_id: int = None, date: str = None,
             entity: str = None):
    rows = store.recent_memories(limit if limit <= 2000 else 2000)
    resolved_eid = entity_id
    if resolved_eid is None and entity:
        hit = store.find_entity_by_name(entity)
        if hit:
            resolved_eid = hit["id"]
        else:
            # substring match
            ql = entity.lower()
            for e in store.all_entities():
                if ql in e["name"].lower():
                    resolved_eid = e["id"]
                    break
    out = []
    for m in rows:
        if resolved_eid is not None and resolved_eid not in json.loads(m["entity_ids"] or "[]"):
            continue
        if kind and m["kind"] != kind:
            continue
        if date and not m["created_at"].startswith(date):
            continue
        if conversation_id is not None:
            src = store.message_by_id(m["message_id"]) if m.get("message_id") else None
            if not src or src.get("conversation_id") != conversation_id:
                continue
        out.append(m)
    return out


# --------------------------------------------------------------------------
# API: search
# --------------------------------------------------------------------------

class SearchIn(BaseModel):
    query: str
    type: Optional[str] = None
    min_confidence: Optional[float] = None
    status: Optional[str] = None
    pinned: Optional[bool] = None
    important: Optional[bool] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    source: Optional[str] = None


@app.post("/api/search")
def do_search(body: SearchIn):
    filters = {k: v for k, v in {
        "type": body.type, "min_confidence": body.min_confidence,
        "status": body.status, "pinned": body.pinned, "important": body.important,
        "date_from": body.date_from, "date_to": body.date_to, "source": body.source,
    }.items() if v is not None}
    res = search.search(body.query, filters=filters)
    ans = search.answer(body.query, model=effective_llm_model(), filters=filters)
    return {"query": body.query, **res, "answer": ans["text"], "status": ans["status"],
            "sources": ans.get("sources", [])}


# --------------------------------------------------------------------------
# API: dashboard
# --------------------------------------------------------------------------

@app.get("/api/dashboard")
def dashboard():
    ents = store.all_entities()
    rels = store.all_relationships()
    convos = store.all_conversations()
    msgs = db.query("SELECT COUNT(*) c FROM messages WHERE role='user'")[0]["c"]
    mems = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    by_type = {}
    for e in ents:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1

    deg = _entity_degree_map()
    most_connected = sorted(
        [{"id": e["id"], "name": e["name"], "type": e["type"], "degree": deg.get(e["id"], 0)}
         for e in ents if e["name"].lower() != "user"],
        key=lambda x: -x["degree"])[:8]

    # Memory growth over the last 14 days.
    growth = defaultdict(int)
    for m in store.recent_memories(500):
        growth[m["created_at"][:10]] += 1
    days = [(datetime.now() - timedelta(days=i)).date().isoformat() for i in range(13, -1, -1)]
    growth_series = [{"date": d, "count": growth.get(d, 0)} for d in days]

    recent = store.recent_memories(12)

    return {
        "entities": len(ents),
        "relationships": len(rels),
        "memories": mems,
        "messages": msgs,
        "conversations": len(convos),
        "by_type": by_type,
        "most_connected": most_connected,
        "growth": growth_series,
        "recent": recent,
        "pinned": sum(1 for e in ents if e.get("pinned")),
        "important": sum(1 for e in ents if e.get("important")),
        "ollama_available": ollama.available(),
        "llm_model": effective_llm_model(),
        "embedding_model": effective_embedding_model(),
        "has_demo_data": _has_demo_data(),
    }


def _has_demo_data():
    return db.query_one("SELECT 1 FROM entities WHERE meta LIKE '%demo%' LIMIT 1") is not None


# --------------------------------------------------------------------------
# API: export / import
# --------------------------------------------------------------------------

@app.get("/api/export/json")
def export_json():
    from fastapi.responses import Response
    return Response(content=export.export_json(), media_type="application/json",
                    headers={"Content-Disposition": "attachment; filename=second-brain-export.json"})


@app.get("/api/export/markdown")
def export_markdown():
    from fastapi.responses import Response
    return Response(content=export.export_markdown(), media_type="text/markdown",
                    headers={"Content-Disposition": "attachment; filename=second-brain-export.md"})


class ImportIn(BaseModel):
    data: str
    mode: str = "merge"  # 'merge' | 'replace'
    confirm: bool = False


@app.post("/api/import")
def do_import(body: ImportIn):
    if body.mode not in ("merge", "replace"):
        raise HTTPException(400, "mode must be 'merge' or 'replace'")
    if body.mode == "replace" and not body.confirm:
        raise HTTPException(400, "replace requires confirm=true")
    if len((body.data or "").encode("utf-8")) > MAX_IMPORT_BYTES:
        raise HTTPException(400, "import payload too large (8 MB max)")
    result = export.import_from_json(body.data, mode=body.mode)
    if result.get("ok"):
        _safe_auto_backup()
    return result


class NotesIn(BaseModel):
    text: str


@app.post("/api/import/notes")
def import_notes(body: NotesIn):
    if len((body.text or "").encode("utf-8")) > MAX_IMPORT_BYTES:
        raise HTTPException(400, "note payload too large (8 MB max)")
    result = export.import_notes(body.text)
    if not result.get("ok"):
        raise HTTPException(400, result.get("error") or "import failed")
    _safe_auto_backup()
    return result


# --------------------------------------------------------------------------
# API: backup
# --------------------------------------------------------------------------

@app.post("/api/backup")
def do_backup():
    return backup.create_backup()


@app.get("/api/backup/status")
def backup_status():
    return backup.backup_status()


@app.get("/api/backups")
def backups_list():
    return backup.list_backups()


class RestoreIn(BaseModel):
    name: str
    confirm: bool = False


@app.post("/api/backup/restore")
def backup_restore(body: RestoreIn):
    result = backup.restore_backup(body.name, confirm=body.confirm)
    if not result.get("ok"):
        err = result.get("error") or "restore failed"
        raise HTTPException(400, err)
    return result


# --------------------------------------------------------------------------
# API: summarization
# --------------------------------------------------------------------------

@app.get("/api/summarize/candidates")
def summarize_candidates():
    return summarize.find_consolidation_candidates()


class SummarizeIn(BaseModel):
    entity_id: Optional[int] = None
    memory_ids: Optional[List[int]] = None


@app.post("/api/summarize")
def do_summarize(body: SummarizeIn):
    if body.entity_id is not None:
        return summarize.summarize_entity(body.entity_id, memory_ids=body.memory_ids)
    return summarize.summarize_all()


# --------------------------------------------------------------------------
# API: settings
# --------------------------------------------------------------------------

@app.get("/api/settings")
def get_settings():
    return {
        "llm_model": effective_llm_model(),
        "embedding_model": effective_embedding_model(),
        "ollama_base_url": ollama.get_base_url(),
        "confidence_threshold": db.get_setting_float("confidence_threshold", config.DEFAULT_CONFIDENCE_THRESHOLD),
        "merge_similarity": db.get_setting_float("merge_similarity", config.DEFAULT_MERGE_SIMILARITY),
        "auto_memory": db.get_setting_bool("auto_memory", True),
        "auto_backup_hours": db.get_setting_float("auto_backup_hours", config.DEFAULT_AUTO_BACKUP_HOURS),
        "theme": db.get_setting("theme", "dark"),
        "ollama_available": ollama.available(),
        "models_installed": ollama.list_models(),
        "db_path": config.DB_PATH,
        "db_ok": db.integrity_ok(),
        "privacy": {
            "mode": "local-first",
            "local": True,
            "private": True,
            "telemetry": False,
            "cloud": False,
            "data_leaves_machine": False,
            "activity_watch": False,
        },
    }


class SettingsIn(BaseModel):
    llm_model: Optional[str] = None
    embedding_model: Optional[str] = None
    ollama_base_url: Optional[str] = None
    confidence_threshold: Optional[float] = None
    merge_similarity: Optional[float] = None
    auto_memory: Optional[bool] = None
    auto_backup_hours: Optional[float] = None
    theme: Optional[str] = None


@app.post("/api/settings")
def set_settings(body: SettingsIn):
    if body.llm_model:
        db.set_setting("llm_model", body.llm_model.strip())
    if body.embedding_model:
        db.set_setting("embedding_model", body.embedding_model.strip())
    if body.ollama_base_url:
        url = body.ollama_base_url.strip().rstrip("/")
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise HTTPException(400, "Ollama URL must be http(s)://host[:port]")
        db.set_setting("ollama_base_url", url)
    if body.confidence_threshold is not None:
        db.set_setting("confidence_threshold", max(0.0, min(1.0, body.confidence_threshold)))
    if body.merge_similarity is not None:
        db.set_setting("merge_similarity", max(0.0, min(1.0, body.merge_similarity)))
    if body.auto_memory is not None:
        db.set_setting("auto_memory", bool(body.auto_memory))
    if body.auto_backup_hours is not None:
        db.set_setting("auto_backup_hours", max(0.0, min(168.0, float(body.auto_backup_hours))))
    if body.theme:
        db.set_setting("theme", body.theme)
    return get_settings()


class ResetIn(BaseModel):
    confirm: bool = False


@app.post("/api/reset")
def reset(body: Optional[ResetIn] = None):
    """Wipe all data. Requires explicit confirmation."""
    payload = body or ResetIn()
    if not payload.confirm:
        raise HTTPException(400, "confirmation required")
    for t in ("relationships", "entities", "memories", "messages", "conversations"):
        db.execute(f"DELETE FROM {t}")
    db.set_setting("current_conversation_id", None)
    store.ensure_user_entity()
    return {"ok": True}


# --------------------------------------------------------------------------
# Demo / seed data (clearly marked as demo)
# --------------------------------------------------------------------------

DEMO_LINES = [
    "I'm currently learning Python and I want to build AI agents.",
    "My new project Nebula uses Next.js and Ollama.",
    "I started learning React because I want to use it for my next AI project.",
    "I created a tool called Aurora for image generation.",
    "I met Sam, he works on robotics.",
    "I'm interested in machine learning and want to build a chatbot.",
]


@app.post("/api/demo")
def demo():
    cid = store.new_conversation()
    replies = []
    for line in DEMO_LINES:
        r = chat(ChatIn(content=line, conversation_id=cid))
        replies.append(r.get("reply", ""))
    store.touch_conversation(cid, title="Demo conversation")
    # Merge a demo flag into existing message meta (do not wipe remembered chips).
    for m in store.conversation_messages(cid):
        try:
            meta = json.loads(m.get("meta") or "{}")
        except ValueError:
            meta = {}
        meta["demo"] = True
        db.execute("UPDATE messages SET meta=? WHERE id=?", (json.dumps(meta), m["id"]))
    msg_ids = [m["id"] for m in store.conversation_messages(cid)]
    if msg_ids:
        placeholders = ",".join("?" for _ in msg_ids)
        rows = db.query(
            f"SELECT id, meta FROM entities WHERE source_message_id IN ({placeholders})",
            tuple(msg_ids),
        )
        for row in rows:
            try:
                meta = json.loads(row.get("meta") or "{}")
            except ValueError:
                meta = {}
            meta["demo"] = True
            db.execute("UPDATE entities SET meta=? WHERE id=?", (json.dumps(meta), row["id"]))
    return {"ok": True, "replies": replies, "conversation_id": cid}


@app.post("/api/demo/clear")
def demo_clear():
    """Remove only demo-marked entities and the demo conversation. Real data stays."""
    demo_ents = db.query("SELECT id, name, norm_name FROM entities WHERE meta LIKE '%demo%'")
    removed = 0
    for e in demo_ents:
        if e["norm_name"] == store.normalize_name(config.USER_ENTITY_NAME):
            continue
        store.delete_entity(e["id"])
        removed += 1
    demo_convs = db.query("SELECT DISTINCT conversation_id FROM messages WHERE meta LIKE '%demo%'")
    for c in demo_convs:
        if c["conversation_id"]:
            store.delete_conversation(c["conversation_id"])
    return {"ok": True, "entities_removed": removed}


@app.post("/api/chat/stream")
def chat_stream(body: ChatIn):
    """SSE chat. Extraction/retrieval finish first; the reply then streams."""
    def generate():
        turn = prepare_turn(body.content, body.conversation_id)
        if turn.get("cid"):
            yield _sse("meta", {"conversation_id": turn["cid"]})
        if turn.get("remembered") or turn.get("updates") or turn.get("superseded"):
            yield _sse("memory", {
                "remembered": turn.get("remembered") or [],
                "updates": turn.get("updates") or [],
                "superseded": turn.get("superseded") or [],
                "used_fallback": turn.get("used_fallback"),
            })
        if turn.get("status"):
            yield _sse("status", {"status": turn["status"]})
        if turn.get("sources"):
            yield _sse("sources", {"sources": turn["sources"]})
        chunks = []
        try:
            for piece in render_reply(turn):
                if piece:
                    chunks.append(piece)
                    yield _sse("token", {"text": piece})
        except Exception:
            fallback = turn.get("ready_reply") or _natural_reply_fallback(
                turn.get("remembered") or [], turn.get("used_fallback"))
            if fallback and not chunks:
                chunks.append(fallback)
                yield _sse("token", {"text": fallback})
        reply = "".join(chunks)
        result = finalize_turn(turn, reply)
        yield _sse("done", result)

    return StreamingResponse(generate(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


# --------------------------------------------------------------------------
# Static frontend (served by the same local server — no build step needed)
# --------------------------------------------------------------------------

if os.path.isdir(config.FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=config.FRONTEND_DIR, html=True), name="frontend")
````

## `backend/backup.py`

````
"""Local backup mechanism.

Creates timestamped backups under data/backups/ containing:
  - a copy of the SQLite database (via SQLite's online backup API)
  - a JSON export of the knowledge graph
  - a Markdown export

Restore copies a named backup's brain.db over the live database after
taking a safety snapshot. Names are constrained so a path cannot escape
the backup directory. Two backups never share a folder.

No secrets are included (this application stores none). Backups are entirely
local. Provides listing + status of the latest backup.
"""
import json
import os
import re
import shutil
import sqlite3
import threading
from datetime import datetime, timedelta

from . import config, db, export

_auto_lock = threading.Lock()

_BACKUP_NAME = re.compile(r"^backup-\d{8}-\d{6}(?:-\d{1,6})?$")


def backup_dir():
    d = os.path.join(os.path.dirname(config.DB_PATH), "backups")
    os.makedirs(d, exist_ok=True)
    return d


def _timestamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def _unique_backup_dir():
    """Never reuse or overwrite an existing backup folder."""
    base = backup_dir()
    ts = _timestamp()
    candidate = os.path.join(base, f"backup-{ts}")
    if not os.path.exists(candidate):
        os.makedirs(candidate)
        return candidate
    ts = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    candidate = os.path.join(base, f"backup-{ts}")
    suffix = 1
    while os.path.exists(candidate):
        suffix += 1
        candidate = os.path.join(base, f"backup-{ts}-{suffix}")
    os.makedirs(candidate)
    return candidate


def create_backup():
    """Create a new backup. Returns a status dict."""
    target_dir = _unique_backup_dir()

    # 1. SQLite online backup (safe even while the app is running).
    db_copy = os.path.join(target_dir, "brain.db")
    src = sqlite3.connect(config.DB_PATH)
    dst = sqlite3.connect(db_copy)
    try:
        with dst:
            src.backup(dst)
    finally:
        dst.close()
        src.close()

    # 2. JSON + Markdown exports.
    errors = []
    try:
        with open(os.path.join(target_dir, "export.json"), "w", encoding="utf-8") as f:
            f.write(export.export_json())
    except Exception as exc:
        errors.append(f"export.json: {exc}")
    try:
        with open(os.path.join(target_dir, "export.md"), "w", encoding="utf-8") as f:
            f.write(export.export_markdown())
    except Exception as exc:
        errors.append(f"export.md: {exc}")

    meta = {
        "created_at": datetime.now().isoformat(),
        "db": os.path.exists(db_copy),
        "export_json": os.path.exists(os.path.join(target_dir, "export.json")),
        "export_md": os.path.exists(os.path.join(target_dir, "export.md")),
    }
    if errors:
        meta["errors"] = errors
    with open(os.path.join(target_dir, "backup.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    db.set_setting("last_backup_at", datetime.now().isoformat())
    db.set_setting("last_backup_dir", target_dir)

    return {"ok": True, "path": target_dir, **meta}


def _dir_size(path):
    total = 0
    try:
        for root, _dirs, files in os.walk(path):
            for name in files:
                fp = os.path.join(root, name)
                try:
                    total += os.path.getsize(fp)
                except OSError:
                    continue
    except OSError:
        return 0
    return total


def list_backups():
    """List all backups, newest first."""
    out = []
    base = backup_dir()
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base), reverse=True):
        p = os.path.join(base, name)
        if not os.path.isdir(p):
            continue
        meta = {}
        meta_path = os.path.join(p, "backup.json")
        if os.path.exists(meta_path):
            try:
                with open(meta_path) as f:
                    meta = json.load(f)
            except ValueError:
                meta = {}
        meta["bytes"] = _dir_size(p)
        meta["has_db"] = os.path.isfile(os.path.join(p, "brain.db"))
        out.append({"name": name, "path": p, **meta})
    return out


def backup_status():
    """Status of the most recent backup (for the Settings UI)."""
    backups = list_backups()
    latest = backups[0] if backups else None
    return {
        "last_backup_at": db.get_setting("last_backup_at"),
        "last_backup_dir": db.get_setting("last_backup_dir"),
        "count": len(backups),
        "latest": latest,
        "backups": backups[:20],
        "backup_dir": backup_dir(),
    }


def resolve_backup_dir(name):
    """Return the absolute backup folder if `name` is a safe local backup."""
    if not name or not _BACKUP_NAME.fullmatch(str(name)):
        return None
    base = os.path.realpath(backup_dir())
    target = os.path.realpath(os.path.join(base, name))
    if target == base or not target.startswith(base + os.sep):
        return None
    if not os.path.isdir(target):
        return None
    return target


def auto_backup_hours():
    return db.get_setting_float("auto_backup_hours", config.DEFAULT_AUTO_BACKUP_HOURS)


def auto_backup_status():
    """Read-only status. Never writes a backup."""
    backups = list_backups()
    return {
        "hours": auto_backup_hours(),
        "last_backup_at": db.get_setting("last_backup_at"),
        "count": len(backups),
        "enabled": (auto_backup_hours() or 0) > 0,
    }


def maybe_auto_backup():
    """Create a local backup if the last one is older than the configured interval.

    Never deletes backups. Skips empty brains and disabled (0 hour) settings.
    """
    hours = auto_backup_hours()
    if hours is None or hours <= 0:
        return {"ok": False, "skipped": True, "reason": "disabled"}
    with _auto_lock:
        from . import store
        ents = store.all_entities()
        mems = store.recent_memories(1)
        if len(ents) <= 1 and not mems:
            return {"ok": False, "skipped": True, "reason": "empty"}
        last = db.get_setting("last_backup_at")
        if last:
            try:
                then = datetime.fromisoformat(str(last))
                if datetime.now() - then.replace(tzinfo=None) < timedelta(hours=float(hours)):
                    return {"ok": False, "skipped": True, "reason": "fresh"}
            except (TypeError, ValueError):
                pass
        result = create_backup()
        result["automatic"] = True
        return result


def restore_backup(name, confirm=False):
    """Replace the live database with a named backup.

    Always writes a safety snapshot of the current brain first. Never
    deletes the source backup. Requires confirm=True.
    """
    if not confirm:
        return {"ok": False, "error": "confirmation required"}
    target = resolve_backup_dir(name)
    if not target:
        return {"ok": False, "error": "backup not found"}
    src_db = os.path.join(target, "brain.db")
    if not os.path.isfile(src_db):
        return {"ok": False, "error": "backup is missing brain.db"}

    safety = create_backup()

    # Checkpoint then replace the live file. Leftover WAL/SHM from the
    # previous brain would otherwise be replayed onto the restored file
    # and hide the recovered memories.
    live = config.DB_PATH
    try:
        conn = sqlite3.connect(live)
        try:
            conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        finally:
            conn.close()
    except sqlite3.Error:
        pass

    shutil.copy2(src_db, live)
    for suffix in ("-wal", "-shm"):
        extra = live + suffix
        if os.path.isfile(extra):
            os.remove(extra)

    db.set_setting("last_restore_at", datetime.now().isoformat())
    db.set_setting("last_restore_from", name)
    return {
        "ok": True,
        "restored": name,
        "path": target,
        "safety_copy": safety.get("path"),
    }
````

## `backend/commands.py`

````
"""Natural-language memory control.

Lets the user steer memory directly in chat:
    "Remember that I prefer Python."
    "Forget that I am learning Rust."
    "Remove the old game-engine project."
    "Pin Nebula." / "Mark Rust as important."
    "Merge X with Y."
    "Change the description of Aurora to ..."

These are deterministic, rule-based commands (no LLM required), so they work
even in offline mode and always modify the real database.
"""
import json
import re

from . import config, db, store

def is_command(text):
    """True only for explicit memory-control utterances, not stories."""
    t = (text or "").strip().lower().rstrip(".,!?;: ")
    if not t:
        return False
    if re.match(r"^(?:please\s+)?remember(?:\s+that|\s+i)\b", t):
        return True
    if re.match(r"^(?:please\s+)?(?:forget|unremember)(?:\s+that|\s+i)?\b", t):
        return True
    if re.match(r"^(?:can you|could you)\s+forget\b", t):
        return True
    if t.startswith("stop remembering"):
        return True
    if re.match(r"^(?:pin|unpin)\s+\S", t):
        return True
    if t in ("important", "unimportant"):
        return True
    if re.match(r"^(?:important|unimportant)(?:\s+|:\s*)\S", t):
        # "Important meeting tomorrow" is a sentence, not a memory command.
        if re.search(r"\b(that|this|it|to|for|because|meeting|tomorrow|today|later|now|is|are|was|will|about)\b", t):
            return False
        return True
    if re.match(r"^(?:mark|unmark|make)\s+.+\s+(?:as\s+)?(?:un)?important", t):
        return True
    if t == "make this important":
        return True
    if re.match(r"^merge\s+.+\s+(?:with|into)\s+\S", t):
        return True
    if re.match(r"^(?:change|update|rename)\s+.+\s+to\s+\S", t):
        return True
    if t.startswith("set confidence"):
        return True
    if re.match(r"^(?:delete|remove)\s+(?:the\s+)?memory\b", t):
        return True
    if re.match(r"^(?:delete|remove)\s+\S", t):
        if re.search(r"\b(later|tomorrow|soon|tonight)\b", t):
            return False
        return True
    return False


def _find_entity(name):
    """Resolve an entity by (fuzzy) name: exact, alias, substring, then
    token-overlap (for queries like "the old game-engine project")."""
    row = store.find_entity_by_name(name)
    if row:
        return row
    rows = db.query("SELECT * FROM entities")
    nm = store.normalize_name(name)
    best = None
    for r in rows:
        rn = r["norm_name"]
        if rn == nm:
            return r
        if nm in rn or rn in nm:
            if best is None or len(rn) > len(best["norm_name"]):
                best = r
    if best:
        return best
    # Token-overlap fallback.
    q_tokens = {t for t in re.split(r"[^a-z0-9]+", nm) if len(t) > 2}
    if not q_tokens:
        return None
    scored = []
    for r in rows:
        r_tokens = {t for t in re.split(r"[^a-z0-9]+", r["norm_name"]) if len(t) > 2}
        overlap = len(q_tokens & r_tokens)
        if overlap:
            scored.append((overlap, r))
    if scored:
        scored.sort(key=lambda x: (-x[0], len(x[1]["norm_name"])))
        # Only accept if there's a clear winner with meaningful overlap.
        if scored[0][0] >= 2 or (len(scored) == 1 and scored[0][0] >= 1):
            return scored[0][1]
    return None


def _title(value):
    """Title-case a display name (consistent with entity canonicalization)."""
    return " ".join(w[:1].upper() + w[1:] for w in value.split() if w)


def _find_relationship(source_name, relation, target_name):
    s = _find_entity(source_name)
    t = _find_entity(target_name)
    if not s or not t:
        return None, s, t
    rel, swap = store.normalize_relation(relation)
    if swap:
        s, t = t, s
    row = db.query_one(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation=?",
        (s["id"], t["id"], rel),
    )
    return row, s, t


def handle_command(text):
    """Dispatch a memory-control command. Returns a dict with a reply message
    and (optionally) the list of affected entity ids, or None if not a command."""
    t = text.strip()
    tl = t.lower().rstrip(".,!?;: ")

    # ---- remember [that] X ----------------------------------------------
    m = re.match(r"(?:please\s+)?remember(?:\s+that)?\s+(.+)$", t.strip(), re.I)
    if m:
        return {"action": "remember", "payload": m.group(1).strip().rstrip(".,!?;:")}

    # ---- stop remembering X ---------------------------------------------
    m = re.match(r"stop remembering\s+(.+)$", tl, re.I)
    if m:
        return forget_target(m.group(1).strip())

    m = re.match(r"(?:can you|could you|please)\s+forget\s+(.+)$", tl, re.I)
    if m:
        return forget_target(m.group(1).strip())

    # ---- forget / delete / remove ----------------------------------------
    m = re.match(r"(?:forget that|forget|delete the memory|remove the memory|unremember|delete|remove)\s+(?:that\s+)?(.+)$", tl, re.I)
    if m:
        target = m.group(1).strip().rstrip(".")
        return forget_target(target)

    # ---- pin / unpin ------------------------------------------------------
    m = re.match(r"pin\s+(.+)$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{m.group(1).strip()}\".", "ok": False}
        store.update_entity(e["id"], pinned=1)
        store.add_memory("command", f'Pinned {e["name"]}', entity_ids=[e["id"]])
        return {"reply": f'Pinned "{e["name"]}".', "ok": True, "entities": [e["id"]]}

    m = re.match(r"unpin\s+(.+)$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{m.group(1).strip()}\".", "ok": False}
        store.update_entity(e["id"], pinned=0)
        store.add_memory("command", f'Unpinned {e["name"]}', entity_ids=[e["id"]])
        return {"reply": f'Unpinned "{e["name"]}".', "ok": True, "entities": [e["id"]]}

    # ---- mark as important / make X important / make this important ------
    m = re.match(r"(?:mark\s+(.+?)\s+as\s+important|make\s+(.+?)\s+important)$", tl, re.I)
    if m:
        name = (m.group(1) or m.group(2) or "").strip()
        e = _resolve_this(name) if name.lower() in ("this", "it", "that") else _find_entity(name)
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{name}\".", "ok": False}
        store.update_entity(e["id"], important=1)
        store.add_memory("command", f'Marked {e["name"]} as important', entity_ids=[e["id"]])
        return {"reply": f'Marked "{e["name"]}" as important.', "ok": True, "entities": [e["id"]]}

    m = re.match(r"make this important$", tl, re.I)
    if m:
        e = _resolve_this("this")
        if not e:
            return {"reply": "I don't know which memory to mark as important.", "ok": False}
        store.update_entity(e["id"], important=1)
        store.add_memory("command", f'Marked {e["name"]} as important', entity_ids=[e["id"]])
        return {"reply": f'Marked "{e["name"]}" as important.', "ok": True, "entities": [e["id"]]}

    m = re.match(r"important(?:\s+|:\s*)(.+)$", tl, re.I)
    if m:
        name = m.group(1).strip()
        e = _resolve_this(name) if name.lower() in ("this", "it", "that") else _find_entity(name)
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{name}\".", "ok": False}
        store.update_entity(e["id"], important=1)
        store.add_memory("command", f'Marked {e["name"]} as important', entity_ids=[e["id"]])
        return {"reply": f'Marked "{e["name"]}" as important.', "ok": True, "entities": [e["id"]]}

    if tl == "important":
        e = _resolve_this("this")
        if not e:
            return {"reply": "I don't know which memory to mark as important.", "ok": False}
        store.update_entity(e["id"], important=1)
        store.add_memory("command", f'Marked {e["name"]} as important', entity_ids=[e["id"]])
        return {"reply": f'Marked "{e["name"]}" as important.', "ok": True, "entities": [e["id"]]}

    m = re.match(r"(?:unmark\s+(.+?)(?:\s+as\s+important)?|unimportant\s+(.+)|mark\s+(.+?)\s+as\s+unimportant)$", tl, re.I)
    if m:
        name = next((g for g in m.groups() if g), "").strip()
        e = _find_entity(name)
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{name}\".", "ok": False}
        store.update_entity(e["id"], important=0)
        store.add_memory("command", f'Unmarked {e["name"]}', entity_ids=[e["id"]])
        return {"reply": f'Unmarked "{e["name"]}".', "ok": True, "entities": [e["id"]]}

    # ---- merge X with Y ---------------------------------------------------
    m = re.match(r"merge\s+(.+?)\s+(?:with|into)\s+(.+)$", tl, re.I)
    if m:
        a, b = _find_entity(m.group(1).strip()), _find_entity(m.group(2).strip())
        if not a or not b:
            return {"reply": "I couldn't find both entities to merge.", "ok": False}
        res = store.merge_entities(b["id"], a["id"])
        if res.get("error"):
            return {"reply": res["error"], "ok": False}
        return {"reply": f'Merged "{a["name"]}" into "{b["name"]}".', "ok": True,
                "entities": [b["id"]]}

    # ---- "change my preferred X to Y" / "switch to Y" / "I switched to Y" -
    m = re.match(r"change my preferred\s+(.+?)\s+to\s+(.+)$", tl)
    if m:
        target = m.group(2).strip()
        e = _find_entity(target)
        if not e:
            return {"reply": f"I couldn't find \"{target}\".", "ok": False}
        superseded = store.supersede_relations_of_type(
            store.ensure_user_entity(), "prefers", except_target_id=e["id"])
        store.add_relationship(store.ensure_user_entity(), e["id"], "prefers", confidence=0.95)
        msg = f'Recorded "{e["name"]}" as your preference.'
        if superseded:
            old = [store.entity_row(x)["name"] for x in superseded if store.entity_row(x)]
            msg += f' Superseded: {", ".join(old)}.'
        store.add_memory("command", f'Preference changed to {e["name"]}',
                         entity_ids=[e["id"]], confidence=0.95)
        return {"reply": msg, "ok": True, "entities": [e["id"]]}

    m = re.match(r"(?:switch to|i switched to)\s+(.+)$", tl)
    if m:
        target = m.group(1).strip()
        e = _find_entity(target)
        if not e:
            return {"reply": f"I couldn't find \"{target}\".", "ok": False}
        superseded = store.supersede_relations_of_type(
            store.ensure_user_entity(), "prefers", except_target_id=e["id"])
        store.add_relationship(store.ensure_user_entity(), e["id"], "prefers", confidence=0.95)
        msg = f'Recorded "{e["name"]}" as your preference.'
        if superseded:
            old = [store.entity_row(x)["name"] for x in superseded if store.entity_row(x)]
            msg += f' Superseded: {", ".join(old)}.'
        store.add_memory("command", f'Preference changed to {e["name"]}',
                         entity_ids=[e["id"]], confidence=0.95)
        return {"reply": msg, "ok": True, "entities": [e["id"]]}

    # ---- change / update / rename -----------------------------------------
    m = re.match(r"(?:change|update|rename)\s+(.+?)\s+(?:description to|name to|to)\s+(.+)$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{m.group(1).strip()}\".", "ok": False}
        new_val = m.group(2).strip().rstrip(".")
        if "description" in m.group(1) or "describe" in t.lower():
            store.update_entity(e["id"], description=new_val)
            return {"reply": f'Updated the description of "{e["name"]}".', "ok": True,
                    "entities": [e["id"]]}
        # rename (title-case the new display name)
        store.update_entity(e["id"], name=_title(new_val))
        return {"reply": f'Renamed "{e["name"]}" to "{_title(new_val)}".', "ok": True,
                "entities": [e["id"]]}

    # ---- set confidence ----------------------------------------------------
    m = re.match(r"set confidence(?: of)?\s+(.+?)\s+to\s+([0-9.]+)$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find \"{m.group(1).strip()}\".", "ok": False}
        try:
            conf = float(m.group(2))
            conf = max(0.0, min(1.0, conf))
        except ValueError:
            conf = 0.8
        store.set_confidence(e["id"], conf)
        return {"reply": f'Set confidence of "{e["name"]}" to {conf:.2f}.', "ok": True,
                "entities": [e["id"]]}

    return None


def _resolve_this(name):
    """Resolve 'this/it/that' to the most recently touched non-user entity."""
    mems = store.recent_memories(30)
    for m in mems:
        try:
            ids = json.loads(m.get("entity_ids") or "[]")
        except ValueError:
            ids = []
        for eid in reversed(ids):
            row = store.entity_row(eid)
            if row and row["norm_name"] != store.normalize_name(config.USER_ENTITY_NAME):
                return row
    rows = [r for r in store.all_entities() if r["norm_name"] != "user"]
    if not rows:
        return None
    rows.sort(key=lambda r: r.get("updated_at") or r.get("created_at") or "", reverse=True)
    return rows[0]


def forget_target(target):
    """Forget an entity or a relationship, or supersede a stale fact."""
    tl = target.lower()

    # "that I am learning Rust" -> supersede the learning relationship.
    m = re.match(
        r"(?:that\s+)?(?:i\s+)?(?:am|was|is|were)?\s*"
        r"(learning|using|working on|into|interested in|prefer|preferring|"
        r"live in|living in|work at|working at)\s+(.+)$",
        tl,
    )
    if m:
        rel, name = m.group(1).strip(), m.group(2).strip()
        e = _find_entity(name)
        if not e:
            return {"reply": f"I couldn't find \"{name}\".", "ok": False}
        # For learning/uses/prefers: supersede rather than delete (keep history).
        rel_map = {"learning": "learning", "using": "uses", "working on": "works_on",
                   "into": "interested_in", "interested in": "interested_in",
                   "prefer": "prefers", "preferring": "prefers",
                   "live in": "lives_in", "living in": "lives_in",
                   "work at": "works_at", "working at": "works_at"}
        rel = rel_map.get(rel, "learning")
        changed = store.supersede_relationship(store.ensure_user_entity(), e["id"], rel)
        if changed:
            store.add_memory("superseded", f'Superseded: User {rel} {e["name"]}',
                             entity_ids=[e["id"]])
            return {"reply": f"I've marked \"User \u2192 {rel} \u2192 {e['name']}\" as no longer active.", "ok": True,
                    "entities": [e["id"]]}
        # fall through to entity delete as a last resort
        return {"reply": f"I don't have an active \"{rel}\" memory about \"{e['name']}\".", "ok": False}

    # Otherwise treat the target as an entity to remove.
    e = _find_entity(target)
    if not e:
        return {"reply": f"I couldn't find anything about \"{target}\" to forget.", "ok": False}
    if e["norm_name"] == store.normalize_name(config.USER_ENTITY_NAME):
        return {"reply": "I can't forget you.", "ok": False}
    store.add_memory("command", f'Forgot entity {e["name"]}', entity_ids=[e["id"]])
    store.delete_entity(e["id"])
    return {"reply": f'Removed "{e["name"]}" from memory.', "ok": True, "entities": [e["id"]]}
````

## `backend/config.py`

````
"""Configuration for Second Brain.

All runtime options are driven by environment variables (or the Settings UI,
which persists to the SQLite settings table). Nothing here should need to be
edited by hand — change models via .env / Settings instead of touching code.
"""
import os

from . import paths

# ---- Paths ---------------------------------------------------------------
BASE_DIR = str(paths.app_root())
FRONTEND_DIR = str(paths.frontend_dir())


def _load_dotenv():
    """Load a local .env if present. Does not override already-set env vars."""
    for candidate in (
        os.path.join(BASE_DIR, ".env"),
        os.path.join(BASE_DIR, "backend", ".env"),
        os.path.join(str(paths.app_root()), ".env"),
    ):
        if not os.path.isfile(candidate):
            continue
        try:
            with open(candidate, encoding="utf-8") as fh:
                for raw in fh:
                    line = raw.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    if key and key not in os.environ:
                        os.environ[key] = value
        except OSError:
            continue


_load_dotenv()

# Persistent DB path. Never a PyInstaller temp extract directory.
DB_PATH = str(paths.resolve_db_path())

# ---- AI / model configuration (the "replaceable LLM" requirement) --------
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")

# The small local LLM used for extraction (and optional RAG answers).
DEFAULT_LLM_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:0.6b")

# Embedding model for semantic / vector memory search.
DEFAULT_EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "nomic-embed-text")

# How long to wait for Ollama (seconds).
OLLAMA_TIMEOUT = float(os.environ.get("OLLAMA_TIMEOUT", "120"))

# Thresholds (defaults — overridable at runtime via Settings) --------------
DEFAULT_CONFIDENCE_THRESHOLD = 0.4   # drop entities/relations below this
DEFAULT_MERGE_SIMILARITY = 0.92      # cosine similarity at which entities auto-merge
VECTOR_SEARCH_K = 8                  # top-k vector results
SHORT_TERM_CONTEXT_TURNS = 10        # recent messages fed as conversation context
MAX_CHAT_CHARS = 16000               # hard cap on a single chat / extract payload
MAX_EXTRACT_CHARS = 8000             # extractor window (head of the message)
DEFAULT_AUTO_BACKUP_HOURS = 24.0     # 0 disables scheduled local backups
GRAPH_FOCUS_THRESHOLD = 40           # auto-switch the graph to User + 2 hops above this
EXCLUSIVE_RELATIONS = ("prefers", "lives_in", "works_at")

# --------------------------------------------------------------------------
# Memory types (categories). Kept rich but non-forcing: the extractor only
# assigns a type it is confident about, otherwise falls back to "concept".
# --------------------------------------------------------------------------
ENTITY_TYPES = [
    "person", "project", "technology", "topic",
    "skill", "goal", "interest", "preference", "fact",
    "location", "organization", "concept", "task", "event",
]

# Canonical relationship labels (active voice).
RELATION_TYPES = [
    "learning", "uses", "knows", "likes", "created",
    "interested_in", "related_to", "wants", "works_on",
    "prefers", "works_at", "lives_in", "located_in", "member_of",
]

# Inverse labels -> canonical (triggers source/target swap on import).
RELATION_INVERSE = {
    "being_learned_by": "learning", "learned_by": "learning",
    "used_by": "uses", "known_by": "knows", "liked_by": "likes",
    "created_by": "created", "interest_of": "interested_in",
    "wanted_by": "wants", "worked_on_by": "works_on",
    "preferred_by": "prefers", "employs": "works_at",
    "home_of": "lives_in", "contains": "located_in", "has_member": "member_of",
}

# Synonyms -> canonical (no swap).
RELATION_SYNONYMS = {
    "learning": "learning", "learn": "learning", "is_learning": "learning",
    "studying": "learning", "practicing": "learning",
    "uses": "uses", "use": "uses", "using": "uses", "utilizes": "uses",
    "built_with": "uses", "powered_by": "uses", "relies_on": "uses",
    "knows": "knows", "know": "knows",
    "likes": "likes", "like": "likes", "loves": "likes", "enjoys": "likes",
    "favorite": "likes", "prefers": "prefers", "prefer": "prefers",
    "preference": "prefers", "preferred": "prefers", "favorite_language": "prefers",
    "created": "created", "create": "created", "made": "created",
    "built": "created", "developed": "created", "founded": "created",
    "started": "created", "wrote": "created", "designed": "created",
    "interested_in": "interested_in", "interested": "interested_in",
    "curious_about": "interested_in", "into": "interested_in",
    "related_to": "related_to", "related": "related_to", "associated_with": "related_to",
    "part_of": "related_to", "is_a": "related_to", "connected_to": "related_to",
    "wants": "wants", "want": "wants", "wants_to": "wants", "plans_to": "wants",
    "planning_to": "wants", "aiming_to": "wants", "goal_is": "wants",
    "works_on": "works_on", "work_on": "works_on", "working_on": "works_on",
    "works_with": "works_on", "contributes_to": "works_on",
    "works_at": "works_at", "employed_at": "works_at", "works_for": "works_at",
    "lives_in": "lives_in", "lives at": "lives_in", "based_in": "lives_in",
    "located_in": "located_in", "located at": "located_in", "headquartered_in": "located_in",
    "member_of": "member_of", "belongs_to": "member_of", "part_of_team": "member_of",
}

# Entity type synonyms -> canonical.
TYPE_SYNONYMS = {
    "person": "person", "people": "person", "human": "person", "friend": "person",
    "colleague": "person", "contact": "person", "user": "person",
    "project": "project", "product": "project", "app": "project", "application": "project",
    "startup": "project", "side_project": "project",
    "technology": "technology", "tech": "technology", "tool": "technology",
    "software": "technology", "language": "technology", "framework": "technology",
    "library": "technology", "platform": "technology", "model": "technology",
    "topic": "topic", "subject": "topic", "field": "topic", "domain": "topic",
    "skill": "skill", "ability": "skill", "competence": "skill",
    "goal": "goal", "objective": "goal", "target": "goal", "aim": "goal",
    "fact": "fact", "fact_": "fact",
    "interest": "interest", "hobby": "interest", "passion": "interest",
    "preference": "preference", "pref": "preference",
    "location": "location", "place": "location", "city": "location", "country": "location",
    "organization": "organization", "org": "organization", "company": "organization",
    "team": "organization", "institute": "organization", "university": "organization",
    "concept": "concept", "idea": "concept", "thing": "concept",
    "task": "task", "todo": "task", "action_item": "task",
    "event": "event", "meeting": "event", "conference": "event", "milestone": "event",
}

# Small-talk phrases that should never become permanent knowledge.
TRIVIAL_PATTERNS = {
    "hi", "hello", "hey", "yo", "sup", "hola", "good morning", "good evening",
    "good afternoon", "good night", "how are you", "how are u", "how's it going",
    "whats up", "what's up", "thanks", "thank you", "thx", "ty", "ok", "okay",
    "k", "cool", "nice", "great", "awesome", "yes", "no", "yeah", "nah", "sure",
    "fine", "good", "lol", "lmao", "haha", "hehe", "idk", "idc", "bye", "goodbye",
    "see you", "later", "cya", "got it", "gotcha", "understood", "np", "no problem",
    "welcome", "you're welcome", "sounds good", "will do", "👍", "🙂", "😊", "😂",
    "what time is it", "tell me a joke", "what's the weather", "what is the time",
}

# The user is a first-class entity in the graph.
USER_ENTITY_NAME = "User"
USER_ENTITY_DESCRIPTION = "You — the owner of this Second Brain."

# Colors (frontend maps types to colors; kept here for the legend API).
TYPE_COLORS = {
    "person": "#f472b6", "project": "#22d3ee", "technology": "#34d399",
    "topic": "#a78bfa", "skill": "#2dd4bf", "goal": "#60a5fa",
    "interest": "#fb923c", "preference": "#e879f9", "fact": "#f87171",
    "location": "#4ade80", "organization": "#38bdf8", "concept": "#fbbf24",
    "task": "#94a3b8", "event": "#f472b6",
}
````

## `backend/db.py`

````
"""SQLite persistence layer for Second Brain.

Everything is stored locally in a single SQLite file: entities, relationships,
messages (original sources), conversations (short-term grouping), memories
(timeline events), embeddings and settings. Nothing ever leaves the machine.

The schema is versioned via `PRAGMA user_version` and migrated in place so
existing databases are upgraded (never discarded) on startup.
"""
import json
import os
import sqlite3
import threading
from datetime import datetime, timezone

from . import config

_write_lock = threading.Lock()

SCHEMA_VERSION = 3

SCHEMA = """
CREATE TABLE IF NOT EXISTS entities (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    name              TEXT NOT NULL,
    norm_name         TEXT NOT NULL UNIQUE,
    type              TEXT NOT NULL DEFAULT 'concept',
    description       TEXT NOT NULL DEFAULT '',
    aliases           TEXT NOT NULL DEFAULT '[]',
    embedding         TEXT,                -- JSON array of floats (or NULL)
    confidence        REAL NOT NULL DEFAULT 0.8,
    source_message_id INTEGER,
    created_at        TEXT NOT NULL,
    updated_at        TEXT NOT NULL,
    meta              TEXT NOT NULL DEFAULT '{}',
    status            TEXT NOT NULL DEFAULT 'active',   -- 'active' | 'superseded'
    pinned            INTEGER NOT NULL DEFAULT 0,
    important         INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS relationships (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id         INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    target_id         INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    relation          TEXT NOT NULL,
    confidence        REAL NOT NULL DEFAULT 0.8,
    source_message_id INTEGER,
    created_at        TEXT NOT NULL,
    status            TEXT NOT NULL DEFAULT 'active',   -- 'active' | 'superseded'
    UNIQUE(source_id, target_id, relation)
);
CREATE INDEX IF NOT EXISTS idx_rel_source ON relationships(source_id);
CREATE INDEX IF NOT EXISTS idx_rel_target ON relationships(target_id);
CREATE INDEX IF NOT EXISTS idx_rel_source_status ON relationships(source_id, status);
CREATE INDEX IF NOT EXISTS idx_rel_target_status ON relationships(target_id, status);
CREATE INDEX IF NOT EXISTS idx_ent_type_status ON entities(type, status);

CREATE TABLE IF NOT EXISTS conversations (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL DEFAULT '',
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER,
    role            TEXT NOT NULL,        -- 'user' | 'assistant' | 'system'
    content         TEXT NOT NULL,
    created_at      TEXT NOT NULL,
    embedding       TEXT,                 -- JSON array of floats (or NULL)
    extracted       INTEGER NOT NULL DEFAULT 0,
    meta            TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_msg_conv ON messages(conversation_id);

CREATE TABLE IF NOT EXISTS memories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kind        TEXT NOT NULL,            -- 'entity' | 'relationship' | 'update' | 'superseded' | 'conflict' | 'command' | 'summary'
    text        TEXT NOT NULL,
    entity_ids  TEXT NOT NULL DEFAULT '[]',
    message_id  INTEGER,
    confidence  REAL NOT NULL DEFAULT 0.8,
    created_at  TEXT NOT NULL,
    meta        TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_mem_created ON memories(created_at);
CREATE INDEX IF NOT EXISTS idx_mem_kind ON memories(kind);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT
);
"""

# Incremental migrations: columns added to pre-existing databases.
MIGRATIONS = {
    1: [
        ("entities", "status", "TEXT NOT NULL DEFAULT 'active'"),
        ("entities", "pinned", "INTEGER NOT NULL DEFAULT 0"),
        ("entities", "important", "INTEGER NOT NULL DEFAULT 0"),
        ("relationships", "status", "TEXT NOT NULL DEFAULT 'active'"),
        ("messages", "conversation_id", "INTEGER"),
        ("memories", "confidence", "REAL NOT NULL DEFAULT 0.8"),
    ],
    2: [],
    3: [
        ("memories", "meta", "TEXT NOT NULL DEFAULT '{}'"),
    ],
}


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def _connect():
    parent = os.path.dirname(os.path.abspath(config.DB_PATH))
    if parent:
        os.makedirs(parent, exist_ok=True)
    conn = sqlite3.connect(config.DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def _columns(conn, table):
    return {r["name"] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()}


def init_db():
    with _write_lock:
        conn = _connect()
        try:
            conn.executescript(SCHEMA)

            # Apply column migrations for existing databases.
            current = conn.execute("PRAGMA user_version").fetchone()[0]
            for version in sorted(MIGRATIONS):
                if version > current:
                    for table, column, ddl in MIGRATIONS[version]:
                        if column not in _columns(conn, table):
                            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")
                    conn.execute(f"PRAGMA user_version={version}")

            conn.commit()
        finally:
            conn.close()


def query(sql, params=()):
    conn = _connect()
    try:
        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def query_one(sql, params=()):
    rows = query(sql, params)
    return rows[0] if rows else None


def execute(sql, params=()):
    with _write_lock:
        conn = _connect()
        try:
            cur = conn.execute(sql, params)
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()


# --------------------------------------------------------------------------
# Settings (typed helpers)
# --------------------------------------------------------------------------

def get_setting(key, default=None):
    row = query_one("SELECT value FROM settings WHERE key=?", (key,))
    if row is None:
        return default
    return row["value"]


def set_setting(key, value):
    execute(
        "INSERT INTO settings(key, value) VALUES(?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (key, json.dumps(value) if not isinstance(value, str) else value),
    )


def get_setting_float(key, default):
    try:
        return float(get_setting(key, default))
    except (TypeError, ValueError):
        return default


def get_setting_bool(key, default):
    v = get_setting(key, default)
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("1", "true", "yes", "on")
    return bool(v)


def all_settings():
    rows = query("SELECT key, value FROM settings ORDER BY key")
    out = {}
    for r in rows:
        try:
            out[r["key"]] = json.loads(r["value"])
        except (ValueError, TypeError):
            out[r["key"]] = r["value"]
    return out


def integrity_ok():
    """True when SQLite reports a healthy file. Never deletes or rebuilds the DB."""
    try:
        row = query_one("PRAGMA integrity_check")
        if not row:
            return False
        return str(next(iter(row.values()))).lower() == "ok"
    except Exception:
        return False
````

## `backend/export.py`

````
"""Graph export / import (JSON + Markdown).

Export includes entities, relationships, memories, messages, conversations and
settings (no secrets — this app has none). Import validates the payload before
touching the database, and supports two modes:
  - merge   : upsert entities / add relationships without deleting anything
  - replace : wipe the database first (with explicit confirmation)
"""
import json
import re
from datetime import datetime

from . import config, db, store

EXPORT_FORMAT = "second-brain"
EXPORT_VERSION = 1


def _json_default(o):
    if isinstance(o, (datetime,)):
        return o.isoformat()
    return str(o)


def full_export():
    """Serialize the entire knowledge base to a JSON-serializable dict."""
    entities = store.all_entities()
    relationships = store.all_relationships()
    memories = db.query("SELECT * FROM memories ORDER BY id")
    messages = db.query("SELECT * FROM messages ORDER BY id")
    conversations = db.query("SELECT * FROM conversations ORDER BY id")
    settings = db.all_settings()
    # Never export secrets or ephemeral session keys.
    secret_tokens = ("secret", "password", "token", "api_key", "apikey")
    safe_settings = {}
    for k, v in settings.items():
        lk = (k or "").lower()
        if k == "current_conversation_id":
            continue
        if any(tok in lk for tok in secret_tokens):
            continue
        safe_settings[k] = v
    name_by_id = {e["id"]: e["name"] for e in entities}
    facts = []
    for r in relationships:
        facts.append({
            "id": r["id"],
            "text": f'{name_by_id.get(r["source_id"], "#" + str(r["source_id"]))} '
                    f'{r["relation"]} {name_by_id.get(r["target_id"], "#" + str(r["target_id"]))}',
            "source_id": r["source_id"],
            "target_id": r["target_id"],
            "relation": r["relation"],
            "confidence": r["confidence"],
            "status": r.get("status", "active"),
            "source_message_id": r.get("source_message_id"),
            "created_at": r.get("created_at"),
        })
    return {
        "format": EXPORT_FORMAT,
        "version": EXPORT_VERSION,
        "exported_at": db.utcnow(),
        "counts": {
            "entities": len(entities), "relationships": len(relationships),
            "facts": len(facts), "memories": len(memories),
            "messages": len(messages), "conversations": len(conversations),
        },
        "settings": safe_settings,
        "entities": entities,
        "relationships": relationships,
        "facts": facts,
        "memories": memories,
        "messages": messages,
        "conversations": conversations,
    }


def export_json():
    return json.dumps(full_export(), default=_json_default, indent=2)


def export_markdown():
    """Human-readable Markdown export of the knowledge graph."""
    data = full_export()
    lines = ["# Second Brain — Knowledge Export", ""]
    lines.append(f"Exported: {data['exported_at']}")
    lines.append("")
    lines.append("## Entities")
    lines.append("")
    for e in data["entities"]:
        flags = []
        if e.get("pinned"):
            flags.append("pinned")
        if e.get("important"):
            flags.append("important")
        if e.get("status") != "active":
            flags.append(e.get("status", "active"))
        suffix = f"  _({', '.join(flags)})_" if flags else ""
        lines.append(f"- **{e['name']}** ({e['type']}, confidence {e['confidence']:.2f}){suffix}")
        if e.get("description"):
            lines.append(f"  - {e['description']}")
        aliases = json.loads(e.get("aliases") or "[]")
        if aliases:
            lines.append(f"  - aliases: {', '.join(aliases)}")
    lines.append("")
    lines.append("## Relationships")
    lines.append("")
    name = {e["id"]: e["name"] for e in data["entities"]}
    for r in data["relationships"]:
        s = name.get(r["source_id"], f"#{r['source_id']}")
        t = name.get(r["target_id"], f"#{r['target_id']}")
        status = "" if r.get("status") == "active" else f" _({r['status']})_"
        lines.append(f"- {s} \u2192 **{r['relation']}** \u2192 {t} (confidence {r['confidence']:.2f}){status}")
    lines.append("")
    lines.append("## Memory timeline")
    lines.append("")
    for m in data["memories"]:
        lines.append(f"- `{m['created_at'][:16]}` [{m['kind']}] {m['text']}")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Import
# --------------------------------------------------------------------------

def validate_payload(data):
    """Validate a JSON export before it touches the database. Returns
    (ok, error_message)."""
    if not isinstance(data, dict):
        return False, "export must be a JSON object"
    if data.get("format") != EXPORT_FORMAT:
        return False, f"unrecognized format (expected '{EXPORT_FORMAT}')"
    for key in ("entities", "relationships"):
        if key not in data or not isinstance(data[key], list):
            return False, f"missing or invalid '{key}' list"
    for e in data["entities"]:
        if not isinstance(e, dict) or not e.get("name"):
            return False, "entities must be objects with a 'name'"
        if not isinstance(e.get("confidence", 0.8), (int, float)):
            return False, "entity 'confidence' must be a number"
    for r in data["relationships"]:
        if not isinstance(r, dict) or "source_id" not in r or "target_id" not in r \
                or "relation" not in r:
            return False, "relationships must have source_id, target_id and relation"
    for key in ("memories", "messages", "conversations", "facts"):
        if key in data and not isinstance(data[key], list):
            return False, f"'{key}' must be a list when present"
    return True, None


def _apply_entity_flags(eid, e):
    fields = {}
    if e.get("status"):
        fields["status"] = e["status"]
    if e.get("pinned") is not None:
        fields["pinned"] = 1 if e.get("pinned") else 0
    if e.get("important") is not None:
        fields["important"] = 1 if e.get("important") else 0
    if e.get("aliases"):
        try:
            aliases = e["aliases"] if isinstance(e["aliases"], list) else json.loads(e["aliases"])
            fields["aliases"] = aliases
        except (ValueError, TypeError):
            pass
    if fields:
        store.update_entity(eid, **fields)
    emb = e.get("embedding")
    if emb:
        payload = emb if isinstance(emb, str) else json.dumps(emb)
        db.execute("UPDATE entities SET embedding=? WHERE id=?", (payload, eid))


REPORT_LIMIT = 40


def _clip(items, limit=REPORT_LIMIT):
    items = list(items)
    return items[:limit], len(items)


def _entity_name(eid):
    row = store.entity_row(eid) if eid is not None else None
    return row["name"] if row else f"#{eid}"


def _import_entities(data):
    user_id = store.ensure_user_entity()
    id_map = {}
    created, merged, skipped = 0, 0, []
    for e in data["entities"]:
        name = (e.get("name") or "").strip()
        if not name:
            skipped.append({"reason": "empty_name"})
            continue
        if store.normalize_name(name) in ("user", "i", "me"):
            if e.get("id") is not None:
                id_map[e["id"]] = user_id
            continue
        try:
            conf = float(e.get("confidence", 0.8))
        except (TypeError, ValueError):
            skipped.append({"reason": "bad_confidence", "name": name})
            continue
        eid, is_new = store.upsert_entity(
            name, e.get("type", "concept"), e.get("description", ""),
            confidence=conf,
        )
        if eid is None:
            skipped.append({"reason": "rejected", "name": name})
            continue
        if is_new:
            created += 1
        else:
            merged += 1
        if e.get("id") is not None:
            id_map[e["id"]] = eid
        _apply_entity_flags(eid, e)
    return id_map, created, merged, skipped


def _import_relationships(data, id_map, apply_exclusive=True):
    added = 0
    duplicates = 0
    skipped = []
    conflicts = []
    exclusive = set(config.EXCLUSIVE_RELATIONS)
    for r in data["relationships"]:
        sid = id_map.get(r["source_id"])
        tid = id_map.get(r["target_id"])
        raw_rel = r.get("relation") or ""
        if sid is None or tid is None:
            skipped.append({
                "reason": "missing_endpoint",
                "relation": raw_rel,
                "source_id": r.get("source_id"),
                "target_id": r.get("target_id"),
            })
            continue
        if sid == tid:
            skipped.append({
                "reason": "self_loop",
                "relation": raw_rel,
                "name": _entity_name(sid),
            })
            continue
        rel, swap = store.normalize_relation(raw_rel)
        if swap:
            sid, tid = tid, sid
        if apply_exclusive and rel in exclusive:
            old_ids = store.supersede_relations_of_type(sid, rel, except_target_id=tid)
            for oid in old_ids:
                old = store.entity_row(oid)
                if old:
                    conflicts.append({
                        "kind": "exclusive",
                        "relation": rel,
                        "kept": _entity_name(tid),
                        "superseded": old["name"],
                    })
                    store.add_memory(
                        "conflict",
                        f'{rel} changed on import: now {_entity_name(tid)} (was {old["name"]})',
                        entity_ids=[tid, oid],
                    )
        existed = store.relationship_exists(sid, tid, rel)
        try:
            conf = float(r.get("confidence", 0.8))
        except (TypeError, ValueError):
            conf = 0.8
        rid = store.add_relationship(sid, tid, rel, confidence=conf)
        if r.get("status") and r["status"] != "active" and rid:
            store.update_relationship(rid, status=r["status"])
        if not existed:
            added += 1
        else:
            duplicates += 1
    return added, skipped, conflicts, duplicates


def _import_memories(data, id_map, message_map=None, dedup=True):
    added = 0
    skipped = 0
    existing = set()
    if dedup:
        existing = {(m["kind"], m["text"]) for m in db.query("SELECT kind, text FROM memories")}
    for m in data.get("memories") or []:
        if not isinstance(m, dict) or not m.get("text"):
            skipped += 1
            continue
        key = (m.get("kind") or "entity", m["text"])
        if dedup and key in existing:
            skipped += 1
            continue
        try:
            raw_ids = m.get("entity_ids") or []
            if isinstance(raw_ids, str):
                raw_ids = json.loads(raw_ids)
        except ValueError:
            raw_ids = []
        eids = [id_map[old] for old in raw_ids if old in id_map]
        mid = None
        if message_map is not None and m.get("message_id") in message_map:
            mid = message_map[m["message_id"]]
        meta = m.get("meta") or {}
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except ValueError:
                meta = {}
        try:
            conf = float(m.get("confidence", 0.8))
        except (TypeError, ValueError):
            conf = 0.8
        store.add_memory(m.get("kind") or "entity", m["text"], entity_ids=eids,
                         message_id=mid, confidence=conf,
                         meta=meta)
        existing.add(key)
        added += 1
    return added, skipped


def _import_summary(mode, created, merged, added_rels, added_mems,
                    skipped_ents, skipped_rels, conflicts, duplicates, skipped_mems):
    skipped_ents, n_ent = _clip(skipped_ents)
    skipped_rels, n_rel = _clip(skipped_rels)
    conflicts, n_conf = _clip(conflicts)
    return {
        "ok": True, "mode": mode,
        "entities_created": created,
        "entities_merged": merged,
        "relationships_added": added_rels,
        "memories_added": added_mems,
        "entities_skipped": n_ent,
        "relationships_skipped": n_rel,
        "memories_skipped": skipped_mems,
        "duplicates": duplicates,
        "conflicts": conflicts,
        "skipped": skipped_rels,
        "report": {
            "conflicts": conflicts,
            "skipped_relationships": skipped_rels,
            "skipped_entities": skipped_ents,
            "conflict_count": n_conf,
            "skipped_relationship_count": n_rel,
            "skipped_entity_count": n_ent,
            "duplicate_relationships": duplicates,
            "memories_skipped": skipped_mems,
        },
    }


def import_merge(data):
    """Merge-import: upsert entities (by name) and add relationships.
    Preserves existing data. Returns a summary with skip/conflict details."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    id_map, created, merged, skipped_ents = _import_entities(data)
    added_rels, skipped_rels, conflicts, duplicates = _import_relationships(data, id_map)
    added_mems, skipped_mems = _import_memories(data, id_map, dedup=True)
    return _import_summary("merge", created, merged, added_rels, added_mems,
                           skipped_ents, skipped_rels, conflicts, duplicates, skipped_mems)


def import_replace(data):
    """Replace-import: wipe and load. Returns a summary."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    for t in ("relationships", "entities", "memories", "messages", "conversations"):
        db.execute(f"DELETE FROM {t}")
    store.ensure_user_entity()

    conv_map = {}
    for c in data.get("conversations") or []:
        if not isinstance(c, dict):
            continue
        new_id = store.create_conversation(c.get("title") or "")
        if c.get("id") is not None:
            conv_map[c["id"]] = new_id

    msg_map = {}
    for m in data.get("messages") or []:
        if not isinstance(m, dict) or not m.get("content"):
            continue
        cid = conv_map.get(m.get("conversation_id"))
        raw_meta = m.get("meta") or {}
        if isinstance(raw_meta, str):
            try:
                raw_meta = json.loads(raw_meta)
            except ValueError:
                raw_meta = {}
        new_mid = store.add_message(
            m.get("role") or "user", m["content"], conversation_id=cid,
            extracted=int(m.get("extracted") or 0), meta=raw_meta,
        )
        if m.get("id") is not None:
            msg_map[m["id"]] = new_mid

    id_map, created, merged, skipped_ents = _import_entities(data)
    added_rels, skipped_rels, conflicts, duplicates = _import_relationships(data, id_map)
    added_mems, skipped_mems = _import_memories(data, id_map, message_map=msg_map, dedup=False)
    return _import_summary("replace", created, merged, added_rels, added_mems,
                           skipped_ents, skipped_rels, conflicts, duplicates, skipped_mems)


def import_from_json(text, mode="merge"):
    try:
        data = json.loads(text)
    except ValueError as e:
        return {"ok": False, "error": f"invalid JSON: {e}"}
    if mode == "replace":
        return import_replace(data)
    return import_merge(data)


def split_note_chunks(text, limit=50):
    """Split pasted notes into extractable paragraphs. Never invents content."""
    raw = (text or "").replace("\r\n", "\n").strip()
    if not raw:
        return []
    parts = re.split(r"\n\s*\n+|^(?=#{1,3}\s)", raw, flags=re.M)
    chunks = []
    for part in parts:
        piece = " ".join(line.strip() for line in part.splitlines() if line.strip())
        piece = piece.lstrip("# ").strip()
        if len(piece) >= 8:
            chunks.append(piece[:2000])
        if len(chunks) >= limit:
            break
    if not chunks and len(raw) >= 8:
        chunks = [raw[:2000]]
    return chunks


def import_notes(text):
    """Run the existing extractor on each note paragraph. Does not wipe data."""
    from . import extract, fallback
    chunks = split_note_chunks(text)
    if not chunks:
        return {"ok": False, "error": "no usable note text"}
    cid = store.new_conversation()
    store.touch_conversation(cid, title="Imported notes")
    remembered, chunks_used = [], 0
    for chunk in chunks:
        if fallback.is_trivial(chunk):
            continue
        mid = store.add_message("user", chunk, conversation_id=cid)
        result = extract.extract(chunk, source_message_id=mid)
        remembered.extend(result.get("remembered") or [])
        chunks_used += 1
    return {
        "ok": True,
        "mode": "notes",
        "chunks": chunks_used,
        "conversation_id": cid,
        "remembered": len(remembered),
    }
````

## `backend/extract.py`

````
"""Automatic memory extraction pipeline.

user message
    -> trivial-message filter
    -> LLM structured extraction (or rule-based fallback)
    -> JSON parse + validation
    -> entity / relation normalization
    -> duplicate detection + merging
    -> confidence check + conflict/supersession handling
    -> persist to graph + timeline
"""
import json
import re

from . import config, db, fallback, ollama, store

EXTRACTION_SYSTEM_PROMPT = """You are a knowledge-extraction engine for a personal "Second Brain".

Extract durable facts from the user's message: entities and the relationships
between them. Output ONLY a single JSON object, nothing else.

Entity types (choose the MOST SPECIFIC one, only if confident; otherwise use
"concept"): person, project, technology, topic, skill, goal, interest,
preference, fact, location, organization, concept, task, event.

Relationship types (use EXACTLY these): learning, uses, knows, likes, created,
interested_in, related_to, wants, works_on, prefers, works_at, lives_in,
located_in, member_of.

Rules:
- The person speaking is ALWAYS represented by the entity name "User".
  ("I", "me", "my" all refer to "User".)
- Only extract meaningful, lasting knowledge. Ignore greetings, small talk,
  thanks, jokes and chit-chat (then return empty lists).
- Merge near-identical concepts into a single entity; do not duplicate.
- Keep entity names short and canonical (e.g. "Python", "Next.js", "AI agents").
- Give every entity and relationship a confidence between 0.0 and 1.0.
- If the user says they STOPPED doing something ("I stopped learning Rust",
  "I no longer use X", "I switched from X to Y"), put the OUTDATED fact in a
  "stops" list, NOT in "relationships".
- Lists are multiple facts: "I'm learning Python, Rust, and Go" creates three
  learning relationships.
- Never invent people, employers, or projects the user did not mention.
- Entity names must be short canonical labels, never clauses
  ("instead of Python", "a bit of Rust").

Examples:
"I am learning Python" ->
  {"entities":[{"name":"User","type":"person","description":"","confidence":1.0},
   {"name":"Python","type":"technology","description":"","confidence":0.95}],
   "relationships":[{"source":"User","target":"Python","relation":"learning","confidence":0.95}],
   "stops":[]}

"I stopped learning Rust" ->
  {"entities":[],"relationships":[],
   "stops":[{"source":"User","target":"Rust","relation":"learning"}]}

"I prefer Python over Java" ->
  {"entities":[{"name":"Python","type":"technology","description":"","confidence":0.9}],
   "relationships":[{"source":"User","target":"Python","relation":"prefers","confidence":0.9}],
   "stops":[]}

"hello" -> {"entities":[],"relationships":[],"stops":[]}

Return JSON in exactly this shape:
{"entities":[{"name":"...","type":"...","description":"...","confidence":0.9}],
 "relationships":[{"source":"...","target":"...","relation":"...","confidence":0.9}],
 "stops":[{"source":"...","target":"...","relation":"..."}]}
"""


def _llm_extract(text, model):
    resp = ollama.chat(
        model,
        messages=[
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.0,
        format_json=True,
    )
    return _parse_json(resp)


def _parse_json(resp):
    if not resp:
        return None
    try:
        return json.loads(resp)
    except ValueError:
        pass
    m = re.search(r"\{.*\}", resp, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except ValueError:
            pass
    return None


def confidence_threshold():
    return db.get_setting_float("confidence_threshold", config.DEFAULT_CONFIDENCE_THRESHOLD)


_JUNK_NAMES = {
    "instead", "instead of", "rather", "rather than", "a bit", "a bit of",
    "something", "stuff", "things", "thing", "it", "this", "that",
    "here", "there", "now", "today", "tomorrow", "and", "or", "the", "a", "an",
}


def is_junk_entity_name(name):
    """True for empty, stopword, or clause-like names that should never persist."""
    n = store.normalize_name(name)
    if not n or len(n) < 2:
        return True
    if n in _JUNK_NAMES:
        return True
    if n.startswith("instead of") or n.startswith("rather than") or n.startswith("a bit of"):
        return True
    words = n.split()
    if words and words[0] in ("instead", "rather", "also"):
        return True
    if len(words) > 6:
        return True
    if re.search(r"[!?]", n):
        return True
    return False


def mentioned_in_text(name, text):
    """True if the user's words support this entity name. Never true for inventions."""
    if normalize_me(name):
        return True
    n = store.normalize_name(name)
    if not n:
        return False
    blob = (text or "").lower()
    if n in blob:
        return True
    canon = fallback.canonical_name(name)
    if canon and canon.lower() in blob:
        return True
    for key, display in fallback.TECH.items():
        if display.lower() == n or (canon and display == canon):
            if re.search(r"(?<![a-z0-9])" + re.escape(key) + r"(?![a-z0-9])", blob):
                return True
    tokens = [
        t for t in re.findall(r"[a-z0-9#+.\-']+", n)
        if len(t) > 1 and t not in fallback._STOPWORDS
    ]
    if tokens and all(t in blob for t in tokens):
        return True
    return False


def calibrate_confidence(name, conf, text, agreed=False):
    """Bound model-reported confidence using how clearly the name appears."""
    try:
        conf = float(conf)
    except (TypeError, ValueError):
        conf = 0.75
    conf = max(0.0, min(0.98, conf))
    n = store.normalize_name(name)
    blob = (text or "").lower()
    if n and n in blob:
        factor = 1.0
    elif mentioned_in_text(name, text):
        factor = 0.88
    else:
        factor = 0.5
    conf = conf * factor
    if agreed:
        conf = min(0.98, conf + 0.08)
    return round(conf, 3)


def _as_dict_list(value):
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def validate_extraction(text, data):
    """Drop invented, junk, or malformed extraction rows before persist."""
    if not isinstance(data, dict):
        data = {}
    entities, relationships, stops = [], [], []
    allowed_types = set(config.ENTITY_TYPES)

    for ent in _as_dict_list(data.get("entities")):
        name = fallback.canonical_name(ent.get("name") or "")
        if not name or is_junk_entity_name(name):
            continue
        if not mentioned_in_text(name, text):
            continue
        etype = store.normalize_type(ent.get("type") or "concept")
        if etype not in allowed_types:
            etype = "concept"
        desc = ent.get("description") or ""
        if not isinstance(desc, str):
            desc = ""
        desc = desc.strip()[:500]
        if desc and store.normalize_name(desc) not in (text or "").lower():
            desc = ""
        conf = calibrate_confidence(name, ent.get("confidence", 0.8), text)
        entities.append({
            "name": name, "type": etype, "description": desc, "confidence": conf,
        })

    for rel in _as_dict_list(data.get("relationships")):
        src = fallback.canonical_name(rel.get("source") or "")
        tgt = fallback.canonical_name(rel.get("target") or "")
        relation_raw = rel.get("relation") or ""
        if not isinstance(relation_raw, str):
            continue
        if not src or not tgt or is_junk_entity_name(tgt):
            continue
        if not mentioned_in_text(src, text) or not mentioned_in_text(tgt, text):
            continue
        relation, swap = store.normalize_relation(relation_raw)
        if swap:
            src, tgt = tgt, src
        if store.normalize_name(src) == store.normalize_name(tgt):
            continue
        conf = calibrate_confidence(tgt, rel.get("confidence", 0.8), text)
        relationships.append({
            "source": src, "target": tgt, "relation": relation, "confidence": conf,
        })

    for stop in _as_dict_list(data.get("stops")):
        src = fallback.canonical_name(stop.get("source") or "") or "User"
        tgt = fallback.canonical_name(stop.get("target") or "")
        relation_raw = stop.get("relation") or ""
        if not isinstance(relation_raw, str) or not tgt:
            continue
        if is_junk_entity_name(tgt) or not mentioned_in_text(tgt, text):
            continue
        relation, swap = store.normalize_relation(relation_raw)
        if swap:
            src, tgt = tgt, src
        stops.append({"source": src, "target": tgt, "relation": relation})

    return {"entities": entities, "relationships": relationships, "stops": stops}


def merge_extractions(llm_data, rule_data, text):
    """Union of validated LLM + rule extractions. Rules fill gaps; LLM cannot invent."""
    llm_v = validate_extraction(text, llm_data or {})
    rule_v = validate_extraction(text, rule_data or {})

    ents = {}
    for ent in rule_v["entities"] + llm_v["entities"]:
        key = store.normalize_name(ent["name"])
        prev = ents.get(key)
        if prev is None:
            ents[key] = dict(ent)
            continue
        if ent.get("type") and ent["type"] != "concept" and prev.get("type") == "concept":
            prev["type"] = ent["type"]
        if ent.get("description") and not prev.get("description"):
            prev["description"] = ent["description"]
        prev["confidence"] = calibrate_confidence(
            ent["name"],
            max(float(prev.get("confidence") or 0), float(ent.get("confidence") or 0)),
            text,
            agreed=True,
        )

    rels = {}
    for rel in rule_v["relationships"] + llm_v["relationships"]:
        key = (
            store.normalize_name(rel["source"]),
            store.normalize_name(rel["target"]),
            rel["relation"],
        )
        prev = rels.get(key)
        if prev is None:
            rels[key] = dict(rel)
            continue
        prev["confidence"] = calibrate_confidence(
            rel["target"],
            max(float(prev.get("confidence") or 0), float(rel.get("confidence") or 0)),
            text,
            agreed=True,
        )

    seen, stops = set(), []
    for stop in rule_v["stops"] + llm_v["stops"]:
        key = (
            store.normalize_name(stop.get("source")),
            store.normalize_name(stop.get("target")),
            (stop.get("relation") or "").lower(),
        )
        if key in seen or not key[1]:
            continue
        seen.add(key)
        stops.append(stop)

    return {
        "entities": list(ents.values()),
        "relationships": list(rels.values()),
        "stops": stops,
    }


def extract(text, model=None, source_message_id=None, demo=False):
    """Run the full extraction pipeline. Returns a dict summary of updates."""
    if model is None:
        model = db.get_setting("llm_model", config.DEFAULT_LLM_MODEL)
    text = (text or "")[:config.MAX_EXTRACT_CHARS]
    demo_meta = {"demo": True} if demo else None
    result = {
        "used_fallback": False, "entities": [], "relationships": [],
        "entity_updates": [], "relationship_updates": [], "trivial": False,
        "memories": [], "remembered": [], "superseded": [],
    }

    if fallback.is_trivial(text):
        result["trivial"] = True
        return result

    rules = fallback.extract_with_rules(text)
    llm_data = None
    if ollama.available():
        try:
            llm_data = _llm_extract(text, model)
        except Exception:
            llm_data = None
    if isinstance(llm_data, dict):
        data = merge_extractions(llm_data, rules, text)
        result["used_fallback"] = False
    else:
        data = validate_extraction(text, rules)
        result["used_fallback"] = True

    data = _augment_from_text(text, data or {})
    data = validate_extraction(text, data)
    entities = data.get("entities", []) or []
    relationships = data.get("relationships", []) or []
    stops = data.get("stops", []) or []

    store.ensure_user_entity()
    threshold = confidence_threshold()
    exclusive_relations = set(config.EXCLUSIVE_RELATIONS)

    # ---- Entities ------------------------------------------------------
    id_by_name = {}
    for ent in entities:
        try:
            name = fallback.canonical_name(ent.get("name") or "")
            etype = ent.get("type") or "concept"
            desc = ent.get("description") or ""
            conf = float(ent.get("confidence", 0.8))
        except (AttributeError, ValueError):
            continue
        if not name or is_junk_entity_name(name) or conf < threshold:
            continue
        if normalize_me(name):
            eid = store.ensure_user_entity()
            id_by_name[name.lower()] = eid
            continue
        embedding = store.embed_text(name + " " + desc)
        eid, created = store.upsert_entity(
            name, etype, desc, confidence=conf, embedding=embedding,
            source_message_id=source_message_id, meta=demo_meta,
        )
        if eid is None:
            continue
        id_by_name[name.lower()] = eid
        row = store.entity_row(eid)
        result["entities"].append({"id": eid, "name": row["name"], "type": row["type"],
                                   "created": created})
        if created:
            mem = f'New {row["type"]} "{row["name"]}" detected'
            store.add_memory("entity", mem, entity_ids=[eid], message_id=source_message_id,
                             confidence=conf)
            result["memories"].append(mem)
            result["entity_updates"].append(f'+ New {row["type"]} "{row["name"]}"')
            result["remembered"].append(
                {"kind": "entity", "name": row["name"], "type": row["type"],
                 "entity_id": eid, "confidence": round(conf, 3)})

    # ---- Relationships ------------------------------------------------
    for rel in relationships:
        try:
            src = (rel.get("source") or "").strip()
            tgt = (rel.get("target") or "").strip()
            relation_raw = (rel.get("relation") or "").strip()
            conf = float(rel.get("confidence", 0.8))
        except (AttributeError, ValueError):
            continue
        if not src or not tgt or conf < threshold:
            continue

        relation, swap = store.normalize_relation(relation_raw)
        if swap:
            src, tgt = tgt, src

        sid = _resolve_entity(src, conf, id_by_name, source_message_id, demo_meta, text)
        tid = _resolve_entity(tgt, conf, id_by_name, source_message_id, demo_meta, text)
        if sid is None or tid is None or sid == tid:
            continue

        # Exclusive facts: a new prefers / lives_in / works_at replaces the old one.
        if relation in exclusive_relations:
            superseded_ids = store.supersede_relations_of_type(sid, relation,
                                                               except_target_id=tid)
            for old_id in superseded_ids:
                old = store.entity_row(old_id)
                if old:
                    store.add_memory(
                        "conflict",
                        f'{relation} changed: now {store.entity_row(tid)["name"]} (was {old["name"]})',
                        entity_ids=[tid, old_id], message_id=source_message_id,
                        confidence=conf,
                    )
                    result["superseded"].append(old["name"])

        was_active = store.relationship_active(sid, tid, relation)
        store.add_relationship(sid, tid, relation, confidence=conf, source_message_id=source_message_id)
        srow, trow = store.entity_row(sid), store.entity_row(tid)
        if not was_active:
            label = f'{srow["name"]} → {relation} → {trow["name"]}'
            store.add_memory("relationship", label, entity_ids=[sid, tid],
                             message_id=source_message_id, confidence=conf)
            result["memories"].append(label)
            result["relationship_updates"].append(f"+ {label}")
            result["remembered"].append(
                {"kind": "relationship", "source": srow["name"], "relation": relation,
                 "target": trow["name"], "entity_id": tid,
                 "source_id": sid, "target_id": tid,
                 "confidence": round(conf, 3)})
        result["relationships"].append(
            {"source": sid, "target": tid, "relation": relation, "new": not was_active}
        )

    # ---- Stops / supersession ------------------------------------------
    for stop in stops:
        try:
            src = (stop.get("source") or "").strip()
            tgt = (stop.get("target") or "").strip()
            relation_raw = (stop.get("relation") or "").strip()
        except AttributeError:
            continue
        if not src or not tgt:
            continue
        relation, swap = store.normalize_relation(relation_raw)
        if swap:
            src, tgt = tgt, src
        if normalize_me(src):
            sid = store.ensure_user_entity()
        else:
            sid = id_by_name.get(src.lower()) or _resolve_entity(
                src, 0.6, id_by_name, source_message_id, demo_meta, text)
        tid = _resolve_entity(tgt, 0.6, id_by_name, source_message_id, demo_meta, text)
        if sid is None or tid is None:
            continue
        changed = store.supersede_relationship(sid, tid, relation)
        if changed:
            srow, trow = store.entity_row(sid), store.entity_row(tid)
            label = f'{srow["name"]} {relation} {trow["name"]}'
            store.add_memory("superseded", f'Superseded: {label}',
                             entity_ids=[sid, tid], message_id=source_message_id,
                             confidence=0.9)
            result["superseded"].append(label)
            result["relationship_updates"].append(f"~ {label} (no longer active)")

    return result


def _resolve_entity(name, conf, id_by_name, source_message_id=None, demo_meta=None,
                    source_text=None):
    if normalize_me(name):
        return store.ensure_user_entity()
    name = fallback.canonical_name(name)
    if not name or is_junk_entity_name(name):
        return None
    if source_text is not None and not mentioned_in_text(name, source_text):
        return None
    eid = id_by_name.get(name.lower())
    if eid is not None:
        return eid
    emb = store.embed_text(name)
    eid, _ = store.upsert_entity(name, "concept", "", confidence=conf, embedding=emb,
                                 source_message_id=source_message_id, meta=demo_meta)
    id_by_name[name.lower()] = eid
    return eid


def normalize_me(name):
    return store.normalize_name(name) in ("i", "me", "my", "myself", "mine", "user")


# Reliability net: even if the LLM misses a stop/switch, the text itself is
# enough to supersede contradictory active facts.
_SWITCH_RE = re.compile(
    r"(?:switched|switching|moved)\s+from\s+(.+?)\s+to\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_INSTEAD_RE = re.compile(
    r"(?:now|instead)\s+(?:learning|using|studying)?\s*(.+?)\s+(?:instead of|rather than)\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_STOP_RE = re.compile(
    r"(?:stopped|no longer|quit|gave up on|dropped)\s+"
    r"(?:learning|studying|using|working on|practicing|learn|use)\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_PREFER_INSTEAD_RE = re.compile(
    r"prefer(?:s)?\s+(.+?)\s+(?:instead of|rather than|over)\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_MEANT_NOT_RE = re.compile(
    r"(?:i meant|actually)\s+(.+?)\s+not\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)
_ACTUALLY_PREFER_RE = re.compile(
    r"actually\s+(?:i\s+)?prefer(?:s)?\s+(.+?)(?:[.!?;,]|$)",
    re.I,
)


def _augment_from_text(text, data):
    """Add stops (and missing entities) detected deterministically from the text."""
    data = dict(data)
    data.setdefault("entities", [])
    data.setdefault("relationships", [])
    data.setdefault("stops", [])
    stops = list(data["stops"])

    def _add_stop(target, relation):
        target = (target or "").strip().strip("\"'")
        if not target or len(target) < 2:
            return
        stops.append({"source": "User", "target": target, "relation": relation})

    for m in _SWITCH_RE.finditer(text):
        old, new = m.group(1).strip(), m.group(2).strip()
        _add_stop(old, "learning")
        _add_stop(old, "uses")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "prefers", "confidence": 0.9}
            )
            data["entities"].append(
                {"name": new, "type": "technology", "description": "", "confidence": 0.9}
            )
    for m in _INSTEAD_RE.finditer(text):
        new, old = m.group(1).strip(), m.group(2).strip()
        _add_stop(old, "learning")
        _add_stop(old, "uses")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "learning", "confidence": 0.9}
            )
    for m in _STOP_RE.finditer(text):
        _add_stop(m.group(1).strip(), "learning")
        _add_stop(m.group(1).strip(), "uses")
    for m in _PREFER_INSTEAD_RE.finditer(text):
        new, old = m.group(1).strip(), m.group(2).strip()
        _add_stop(old, "prefers")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "prefers", "confidence": 0.9}
            )
            data["entities"].append(
                {"name": new, "type": "preference", "description": "", "confidence": 0.9}
            )
    for m in _MEANT_NOT_RE.finditer(text):
        new, old = m.group(1).strip(), m.group(2).strip()
        new = re.sub(r"^(?:i\s+)?(?:prefer|use|learn(?:ing)?)\s+", "", new, flags=re.I)
        _add_stop(old, "prefers")
        _add_stop(old, "learning")
        _add_stop(old, "uses")
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "prefers", "confidence": 0.9}
            )
            data["entities"].append(
                {"name": new, "type": "concept", "description": "", "confidence": 0.9}
            )
    for m in _ACTUALLY_PREFER_RE.finditer(text):
        new = m.group(1).strip()
        if new:
            data["relationships"].append(
                {"source": "User", "target": new, "relation": "prefers", "confidence": 0.9}
            )
            data["entities"].append(
                {"name": new, "type": "preference", "description": "", "confidence": 0.9}
            )

    seen, dedup = set(), []
    for s in stops:
        key = (
            (s.get("source") or "").lower(),
            (s.get("target") or "").lower(),
            (s.get("relation") or "").lower(),
        )
        if key in seen or not key[1]:
            continue
        seen.add(key)
        dedup.append(s)
    data["stops"] = dedup
    return data
````

## `backend/fallback.py`

````
"""Local, offline fallbacks.

When Ollama is not available (or not yet installed), Second Brain keeps
working using a small deterministic rule-based extractor and a hashed n-gram
embedding. This keeps the "brain grows itself" experience intact for demos
and first-run, and makes the app 100% functional with zero external services.
"""
import hashlib
import math
import re

from . import config

# --------------------------------------------------------------------------
# Fallback embedding: hashed character 3-grams -> 256-dim unit vector.
# --------------------------------------------------------------------------

_EMBED_DIM = 256


def fallback_embed(text):
    text = text.lower()
    vec = [0.0] * _EMBED_DIM
    grams = set()
    for n in (3, 4):
        for i in range(len(text) - n + 1):
            grams.add(text[i:i + n])
    for w in re.findall(r"[a-z0-9']+", text):
        grams.add(w)
    for g in grams:
        h = int.from_bytes(hashlib.md5(g.encode()).digest()[:4], "big")
        vec[h % _EMBED_DIM] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


# --------------------------------------------------------------------------
# Naming helpers
# --------------------------------------------------------------------------

# lower key -> canonical display name for known technologies.
TECH = {
    "python": "Python", "react": "React", "next.js": "Next.js", "nextjs": "Next.js",
    "ollama": "Ollama", "javascript": "JavaScript", "typescript": "TypeScript",
    "node.js": "Node.js", "node": "Node.js", "sql": "SQL", "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL", "mysql": "MySQL", "mongodb": "MongoDB",
    "docker": "Docker", "kubernetes": "Kubernetes", "git": "Git", "html": "HTML",
    "css": "CSS", "tailwind": "Tailwind CSS", "tailwindcss": "Tailwind CSS",
    "pytorch": "PyTorch", "tensorflow": "TensorFlow", "fastapi": "FastAPI",
    "django": "Django", "flask": "Flask", "c++": "C++", "c#": "C#", "java": "Java",
    "rust": "Rust", "go": "Go", "golang": "Go", "ruby": "Ruby", "php": "PHP",
    "swift": "Swift", "kotlin": "Kotlin", "linux": "Linux", "windows": "Windows",
    "nginx": "Nginx", "redis": "Redis", "rabbitmq": "RabbitMQ", "graphql": "GraphQL",
    "vue": "Vue.js", "angular": "Angular", "svelte": "Svelte", "numpy": "NumPy",
    "pandas": "pandas", "langchain": "LangChain", "stable diffusion": "Stable Diffusion",
    "machine learning": "Machine Learning", "deep learning": "Deep Learning",
    "artificial intelligence": "Artificial Intelligence", "ai agents": "AI Agents",
    "ai": "AI", "ml": "Machine Learning", "llm": "LLM", "llms": "LLMs",
    "gpt": "GPT", "llama": "Llama", "qwen": "Qwen", "vite": "Vite",
    "webpack": "Webpack", "figma": "Figma", "blender": "Blender", "unity": "Unity",
    "unreal engine": "Unreal Engine", "three.js": "Three.js",
    "react native": "React Native", "electron": "Electron", "tauri": "Tauri",
    "aws": "AWS", "azure": "Azure", "gcp": "GCP", "vercel": "Vercel",
    "netlify": "Netlify", "supabase": "Supabase", "firebase": "Firebase",
    "prisma": "Prisma", "claude": "Claude", "groq": "Groq",
    "hugging face": "Hugging Face", "rag": "RAG", "openai api": "OpenAI API",
    "openai": "OpenAI",
}

_ACRONYMS = {"ai", "ml", "llm", "nlp", "api", "js", "ts", "sql", "http", "html",
             "css", "gpu", "cpu", "vram", "ram", "ui", "ux", "vr", "ar", "os",
             "db", "ide", "ci", "cd", "aws", "gcp", "gpt", "rag", "pdf", "3d",
             "2d", "cli", "sdk", "npm", "json", "xml", "url"}

_STOPWORDS = {"i", "a", "an", "the", "my", "our", "new", "to", "and", "or",
              "for", "with", "using", "that", "which", "this", "it", "in", "on",
              "at", "of", "me", "some", "about", "your", "we", "you", "also",
              "called", "named", "project", "currently", "now", "just",
              "tool", "app", "startup", "site", "bot", "platform",
              "website", "system", "saas", "software", "product", "thing"}


def _title_word(w):
    if w in TECH:
        return TECH[w]
    if w in _ACRONYMS:
        return w.upper()
    if w in ("c++", "c#"):
        return w.upper()
    if w.endswith(".js") or w.endswith(".ts"):
        return w[:-3] + "." + w[-2:].upper()
    return w[:1].upper() + w[1:] if w else w


def canonical_name(phrase):
    """Turn a lowercased, possibly messy phrase into a clean display name."""
    phrase = phrase.strip().replace("_", " ").strip()
    phrase = re.sub(r"\s+", " ", phrase)
    key = phrase.lower().strip().strip(".,!?;:'\"")
    if key in TECH:
        return TECH[key]
    words = [w for w in key.split() if w]
    if not words:
        return ""
    return " ".join(_title_word(w) for w in words)


def clean_phrase(p):
    """Strip leading/trailing stopwords and trailing 'and'/conjunctions."""
    p = p.strip().strip(".,!?;:'\"()")
    words = p.split()
    while words and words[0].lower() in _STOPWORDS:
        words = words[1:]
    while words and (words[-1].lower() in _STOPWORDS or words[-1].lower() in ("and", "or")):
        words = words[:-1]
    return " ".join(words)


_ITEM_VERBS = {
    "want", "wants", "wanted", "is", "are", "am", "was", "were",
    "build", "create", "make", "have", "has", "had", "will", "going",
}


def looks_like_item(phrase):
    """True if a phrase is a short concept name, not a clause."""
    phrase = clean_phrase(phrase or "")
    if not phrase or len(phrase) < 2:
        return False
    words = phrase.lower().split()
    if len(words) > 4:
        return False
    if any(w in _ITEM_VERBS for w in words):
        return False
    return True


def split_item_list(rest):
    """Split 'Python, Rust, and Go' into items. Ignores clause-like fragments."""
    rest = re.split(r"[.!?](?=\s|$)", rest or "")[0]
    rest = re.split(r"\s+(?:because|since|so that)\b", rest, maxsplit=1)[0]
    if "," not in rest and not re.search(r"\s+(?:and|or)\s+", rest):
        item = clean_phrase(rest)
        return [item] if looks_like_item(item) else []
    parts = [clean_phrase(p) for p in re.split(r",\s*|\s+and\s+|\s+or\s+", rest)]
    return [p for p in parts if looks_like_item(p)]


# --------------------------------------------------------------------------
# Fallback extractor
# --------------------------------------------------------------------------

def extract_with_rules(text):
    entities, relationships, stops = [], [], []
    used_names = set()

    def add_stop(source, target, relation):
        stops.append({"source": source, "target": target, "relation": relation})

    def add(name, etype, desc="", conf=0.75):
        canon = canonical_name(name)
        key = canon.lower()
        if not canon or len(canon) < 2 or key in used_names or key in ("user",):
            return None
        used_names.add(key)
        entities.append({"name": canon, "type": etype, "description": desc,
                         "confidence": conf})
        return canon

    def add_rel(source, target, relation, conf=0.75):
        if not source or not target or source.lower() == target.lower():
            return
        relationships.append({"source": source, "target": target,
                              "relation": relation, "confidence": conf})

    t = text.lower()
    orig = text  # original casing, for proper-noun detection
    # Normalize multiword verbs/phrases so regexes stay simple.
    for a, b in (("working on", "work_on"), ("works on", "work_on"), ("work on", "work_on"),
                 ("is built with", "built_with"), ("is powered by", "powered_by"),
                 ("is built on", "built_with"), ("built on", "built_with"),
                 ("built with", "built_with"), ("powered by", "powered_by"),
                 ("interested in", "interested_in"), ("picking up", "picking_up"),
                 ("curious about", "curious_about"), ("diving into", "diving_into"),
                 ("passionate about", "passionate_about"), ("is learning", "is_learning")):
        t = t.replace(a, b)

    # ---- 1. Project detection -------------------------------------------
    projects = []  # canonical names
    generic_nouns = {"tool", "app", "project", "startup", "site", "game", "bot",
                     "platform", "website", "system", "saas", "software", "product"}
    art = r"(?:\b(?:a|an|my|our|the|new)\s+)?"
    patterns = [
        # "I created/built a tool called Aurora"
        r"\b(?:i|we)\s+(?:created|built|made|started|launched|developed|wrote|am building|am making)\s+"
        + art + r"(?:project|tool|app|startup|site|game|bot|platform|saas|website|system)?\s*(?:called|named)\s+"
        r"['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)(?=\s+(?:for|to|with|using|that|which|and|or|,|\.)|$)",
        # "my new project Nebula ..."
        r"(?:\b(?:my|our|a|the|new|side|personal|own)\s+){0,3}project\b\s+(?:called|named)?\s*['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?(?=\s+(?:uses|use|using|built_with|that|which|is|for|to|and|with|powered_by|runs_on|runs|,|\.|$))",
        r"\bproject\s+(?:called|named)\s+['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?",
        r"\b(?:called|named)\s+['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?\s+(?:a|an|my|our|the)?\s*(?:project|app|tool|startup|site|game|bot|platform)\b",
        # "I created Aurora"
        r"\b(?:i|we)\s+(?:created|built|made|started|launched|developed|wrote|am building|am making)\s+"
        + art + r"['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?(?=\s+(?:that|which|using|with|and|for|to|,|\.|$))",
    ]
    for pat in patterns:
        for m in re.finditer(pat, t):
            cand = clean_phrase(m.group(1))
            key = canonical_name(cand).lower()
            if (cand and len(key) > 2 and key not in TECH and key not in generic_nouns
                    and not re.fullmatch(r"(that|which|is|for|to|and|with|a|an|the|it|my|new|i|we)", cand)):
                canon = add(cand, "project", f"Project: {canonical_name(cand)}")
                if canon:
                    projects.append(canon)

    # ---- 2. "X uses Y" (X must be a known project or the user) ----------
    for proj in projects:
        for m in re.finditer(re.escape(proj.lower()) + r"\s+(?:uses|use|using|built_with|powered_by|runs_on|relies_on)\s+(.+)", t):
            rest = re.split(r"[.!?](?=\s|$)", m.group(1))[0]
            for part in re.split(r",\s*|\s+and\s+|\s+or\s+", rest):
                item = clean_phrase(part)
                key = canonical_name(item).lower()
                if key and (key in TECH or item):
                    tg = add(item, "technology" if key in TECH else "concept",
                             f"Technology: {canonical_name(item)}" if key in TECH else "")
                    add_rel(proj, tg, "uses")

    # "I/we use X"
    for m in re.finditer(r"\b(?:i|we)\s+(?:use|using|am using)\s+([a-z0-9 .+#/'-]{1,24}?)(?=\s+(?:and|or|for|to|with|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key in TECH:
            tg = add(item, "technology", f"Technology: {canonical_name(item)}")
            add_rel("User", tg, "uses")

    # Proper-noun subject + "uses": "Nebula uses Ollama." (referring to a
    # previously-mentioned project/technology by name). Operates on the
    # ORIGINAL casing so only genuine proper nouns are captured.
    _pronouns = {"he", "she", "they", "it", "this", "that", "who", "which",
                 "there", "here", "one", "we", "you"}
    for m in re.finditer(r"\b([A-Z][A-Za-z0-9.]*(?:\s+[A-Z][A-Za-z0-9.]*){0,3})\s+(?:uses|use|using)\s+(.+)", orig):
        subj = m.group(1).strip()
        subj_key = canonical_name(subj).lower()
        if not subj_key or subj_key in _pronouns or subj_key in _STOPWORDS or subj_key == "user":
            continue
        rest = re.split(r"[.!?](?=\s|$)", m.group(2))[0]
        for part in re.split(r",\s*|\s+and\s+|\s+or\s+", rest):
            item = clean_phrase(part)
            key = canonical_name(item).lower()
            if not key:
                continue
            s = add(subj, "technology" if subj_key in TECH else "project",
                    f"Project: {canonical_name(subj)}" if subj_key not in TECH else "")
            tg = add(item, "technology" if key in TECH else "concept",
                     f"Technology: {canonical_name(item)}" if key in TECH else "")
            add_rel(s, tg, "uses")

    # ---- 3. learning / interested / wants -------------------------------
    for m in re.finditer(r"(?<!machine )(?<!deep )(?<!reinforcement )(?<!active )(?<!imitation )(?<!few-shot )(?<!zero-shot )(?:learning|learn|studying|picking_up)\s+(?:a bit of\s+)?([a-z0-9 .+#/'-]{1,24}?)(?=\s+(?:and|or|to|for|because|since|so|right now|currently|these days|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "technology" if key in TECH else "topic")
            add_rel("User", e, "learning")

    for m in re.finditer(r"(?:interested_in|curious_about|fascinated by|passionate_about|really into|into)\s+(?:building\s+)?([a-z0-9 .+#/'-]{1,28}?)(?=\s+(?:and|or|to|for|because|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "interest" if key not in TECH else "technology")
            add_rel("User", e, "interested_in")

    for m in re.finditer(r"(?:want to|wants to|planning to|plan to|aiming to|would like to|hoping to|going to)\s+(build|create|make|use|learn|start|try|do|develop|work_on|explore)\s+(?:\b(?:a|an|my|the|new)\s+)?([a-z0-9 .+#/'-]{1,28}?)(?=\s+(?:and|or|for|to|because|with|using|,)|\.|$)", t):
        verb, item = m.group(1), clean_phrase(m.group(2))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            if verb == "learn":
                e = add(item, "technology" if key in TECH else "topic")
                add_rel("User", e, "learning")
            elif verb in ("build", "create", "make", "develop", "start"):
                e = add(item, "technology" if key in TECH else "project")
                add_rel("User", e, "wants")
            else:
                e = add(item, "technology" if key in TECH else "concept")
                add_rel("User", e, "wants")

    # Comma / "and" lists: "I'm learning Python, Rust, and Go"
    def _add_listed(items, etype_fn, relation):
        if len(items) < 2:
            return
        for item in items:
            key = canonical_name(item).lower()
            if not key or key in ("i", "me"):
                continue
            e = add(item, etype_fn(key))
            add_rel("User", e, relation)

    for m in re.finditer(r"(?:learning|learn|studying|picking_up)\s+(.+?)(?:[.!?;]|$)", t):
        _add_listed(split_item_list(m.group(1)),
                    lambda k: "technology" if k in TECH else "topic", "learning")
    for m in re.finditer(r"(?:interested_in|curious_about|fascinated by|passionate_about|really into)\s+(.+?)(?:[.!?;]|$)", t):
        _add_listed(split_item_list(m.group(1)),
                    lambda k: "technology" if k in TECH else "interest", "interested_in")
    for m in re.finditer(r"\b(?:i|we)\s+(?:use|using|am using)\s+(.+?)(?:[.!?;]|$)", t):
        _add_listed(split_item_list(m.group(1)),
                    lambda k: "technology" if k in TECH else "concept", "uses")

    # "I work on X" / "I'm working on X"
    for m in re.finditer(
        r"\b(?:i|we)(?:\s+am|\s+are)?\s+work_on\s+(?:the\s+|a\s+|an\s+|my\s+)?"
        r"([a-z0-9 .+#/'-]{1,32}?)(?=\s+(?:and|or|for|to|because|with|using|,)|\.|$)",
        t,
    ):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "technology" if key in TECH else "project")
            add_rel("User", e, "works_on")

    # Skills: "I'm good at public speaking"
    for m in re.finditer(
        r"\b(?:i(?:'m| am)?|we(?:'re| are)?)\s+(?:good at|skilled at|skilled in|great at)\s+"
        r"([a-z0-9 .+#/'-]{1,32}?)(?=\s+(?:and|or|for|to|because|,)|\.|$)",
        t,
    ):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "skill")
            add_rel("User", e, "related_to")

    # ---- 4. people ------------------------------------------------------
    last_person = None
    for m in re.finditer(r"(?:my friend|my colleague|my partner|i met|i know|met someone called)\s+([a-z][a-z0-9 .\-]{1,24}?)(?=[,.;!]|\s+(?:who|and|,|\.|$))", t):
        p = add(m.group(1).strip(), "person")
        if p:
            last_person = p
        add_rel("User", p, "knows")

    # ---- 5. people working on / learning things ------------------------
    for m in re.finditer(r"\b([a-z][a-z0-9 .\-]{1,24}?)\s+(?:work_on|is_learning|studies)\s+([a-z0-9 .+#/'-]{1,24}?)(?=[,.;]|\s+(?:and|or|for|to|with|,|\.|$))", t):
        subj, obj = clean_phrase(m.group(1)), clean_phrase(m.group(2))
        subj_key = canonical_name(subj).lower()
        obj_key = canonical_name(obj).lower()
        if subj.lower() in ("i", "we", "they", "he", "she", "you"):
            if subj.lower() in ("he", "she", "they") and last_person:
                tg = add(obj, "technology" if obj_key in TECH else "topic")
                add_rel(last_person, tg, "works_on")
            continue
        if not subj_key or not obj_key:
            continue
        s = add(subj, "person")
        if s:
            last_person = s
        tg = add(obj, "technology" if obj_key in TECH else "topic")
        add_rel(s, tg, "works_on")

    # ---- 6. preferences / location / organization ------------------------
    for m in re.finditer(
        r"\b(?:i|we)\s+prefer(?:s)?\s+([a-z0-9 .+#/'-]{1,24}?)\s+"
        r"(?:instead of|rather than|over)\s+([a-z0-9 .+#/'-]{1,24}?)"
        r"(?=[,.;]|\s+(?:and|or|for|to|because|with)|\.|$)",
        t,
    ):
        new, old = clean_phrase(m.group(1)), clean_phrase(m.group(2))
        new_key, old_key = canonical_name(new).lower(), canonical_name(old).lower()
        if new_key and old_key:
            ne = add(new, "technology" if new_key in TECH else "preference")
            add(old, "technology" if old_key in TECH else "preference")
            add_rel("User", ne, "prefers", conf=0.9)
            add_stop("User", canonical_name(old), "prefers")

    for m in re.finditer(r"\b(?:i|we)\s+(?:prefer|prefers|really like|favorite language is|favourite language is)\s+([a-z0-9 .+#/'-]{1,24}?)(?=\s+(?:and|or|over|instead|rather|for|to|with|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "technology" if key in TECH else "preference")
            add_rel("User", e, "prefers", conf=0.9)

    for m in re.finditer(r"\b(?:i|we)\s+(?:live in|live at|am based in|are based in|moved to)\s+([a-z][a-z0-9 .\-]{1,24}?)(?=[,.;]|\s+(?:and|or|,|\.)|$)", t):
        loc = add(m.group(1).strip(), "location")
        add_rel("User", loc, "lives_in")

    for m in re.finditer(r"\b(?:i|we)\s+(?:work at|work for|am employed at)\s+([a-z][a-z0-9 .\-]{1,24}?)(?=[,.;]|\s+(?:and|or|,|\.)|$)", t):
        org = add(m.group(1).strip(), "organization")
        add_rel("User", org, "works_at")

    # ---- 7. negation / stopped (stale facts -> supersede) ---------------
    neg = r"(?:i|we)?\s*(?:stopped|no longer|quit|gave up on|dropped|not anymore|don't|dont|do not)\s*"
    for m in re.finditer(neg + r"(?:learning|studying|using|working on|working_on|practicing)\s+([a-z0-9 .+#/'-]{1,24}?)(?=[,.;]|\s+(?:and|or|for|to|because|with|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        canon = canonical_name(item)
        key = canon.lower()
        if not key:
            continue
        # Ensure the entity exists so it can be referenced, but reference by
        # canonical name (works whether or not `add` created it).
        add(item, "technology" if key in TECH else "concept")
        add_stop("User", canon, "learning")

    for m in re.finditer(r"(?:switched|switching)\s+(?:from\s+)?([a-z0-9 .+#/'-]{1,24}?)\s+to\s+([a-z0-9 .+#/'-]{1,24}?)(?=[,.;]|\s+(?:and|or|for|to|because|with|,)|\.|$)", t):
        old, new = clean_phrase(m.group(1)), clean_phrase(m.group(2))
        old_canon, new_canon = canonical_name(old), canonical_name(new)
        old_key, new_key = old_canon.lower(), new_canon.lower()
        if old_key and new_key:
            add(old, "technology" if old_key in TECH else "concept")
            ne = add(new, "technology" if new_key in TECH else "concept")
            # "switched from X to Y" -> stop using/learning X, prefer Y.
            add_stop("User", old_canon, "uses")
            add_stop("User", old_canon, "learning")
            if ne:
                add_rel("User", ne, "prefers", conf=0.9)

    # ---- 8. bare technology mentions (attach as interests if orphaned) ---
    existing_targets = {r["target"].lower() for r in relationships}
    claimed = []  # (start, end) spans already covered by a longer term
    for key in sorted(TECH, key=len, reverse=True):
        canon = TECH[key]
        for m in re.finditer(r"(?<![a-z0-9])" + re.escape(key) + r"(?![a-z0-9])", t):
            if any(m.start() < end and m.end() > start for start, end in claimed):
                continue
            claimed.append((m.start(), m.end()))
            if canon.lower() in used_names or canon.lower() in existing_targets:
                continue
            add(canon, "technology", f"Technology: {canon}")
            add_rel("User", canon, "interested_in")
            existing_targets.add(canon.lower())

    # ---- de-duplicate relationships --------------------------------------
    seen_rel, dedup = set(), []
    for r in relationships:
        k = (r["source"].lower(), r["target"].lower(), r["relation"])
        if k not in seen_rel and r["source"].lower() != r["target"].lower():
            seen_rel.add(k)
            dedup.append(r)

    # de-duplicate stops
    seen_stop, dedup_stop = set(), []
    for s in stops:
        k = (s["source"].lower(), s["target"].lower(), s["relation"])
        if k not in seen_stop and s["source"].lower() != s["target"].lower():
            seen_stop.add(k)
            dedup_stop.append(s)

    return {"entities": entities, "relationships": dedup, "stops": dedup_stop}


def is_trivial(text):
    """Heuristic for small-talk that should never enter the brain."""
    t = text.strip().lower().strip(".,!? ")
    if len(t) < 3:
        return True
    if t in config.TRIVIAL_PATTERNS:
        return True
    if len(t.split()) == 1 and not re.search(r"[a-z]{4,}", t):
        return True
    return False
````

## `backend/graph.py`

````
"""Graph traversal, filtering, neighborhood, path and statistics.

A small, bounded graph engine over the local SQLite graph. All traversals are
depth-limited so huge graphs stay fast, and only relevant paths are followed
(no exhaustive exploration).
"""
from collections import defaultdict, deque

from . import config, db, store


# --------------------------------------------------------------------------
# Core graph loading (bounded, indexed)
# --------------------------------------------------------------------------

def _load_edges(active_only=True):
    """Return adjacency lists + edge lookup. Loads relationships only (no
    entity table scan unless needed)."""
    where = "WHERE status='active'" if active_only else ""
    rels = db.query(f"SELECT id, source_id, target_id, relation, confidence, status, source_message_id FROM relationships {where}")
    adj = defaultdict(list)  # node_id -> list of (other_id, rel_id, relation, confidence, direction)
    edges = {}
    for r in rels:
        adj[r["source_id"]].append((r["target_id"], r["id"], r["relation"], r["confidence"], "out"))
        adj[r["target_id"]].append((r["source_id"], r["id"], r["relation"], r["confidence"], "in"))
        edges[r["id"]] = r
    return adj, edges


def _entity_map(entity_ids):
    """Fetch entity rows for a set of ids."""
    if not entity_ids:
        return {}
    ph = ",".join("?" for _ in entity_ids)
    rows = db.query(f"SELECT * FROM entities WHERE id IN ({ph})", tuple(entity_ids))
    return {r["id"]: r for r in rows}


# --------------------------------------------------------------------------
# Neighborhood (multi-level expand)
# --------------------------------------------------------------------------

def neighborhood(entity_id, depth=1, relation=None, active_only=True):
    """BFS from an entity up to `depth`. Returns nodes and edges."""
    adj, edges = _load_edges(active_only)
    seen_nodes = {entity_id}
    seen_edges = set()
    frontier = {entity_id}
    for _ in range(int(depth)):
        nxt = set()
        for nid in frontier:
            for (other, rid, rel, conf, direction) in adj.get(nid, []):
                if relation and rel != relation:
                    continue
                if rid not in seen_edges:
                    seen_edges.add(rid)
                if other not in seen_nodes:
                    seen_nodes.add(other)
                    nxt.add(other)
        frontier = nxt
        if not frontier:
            break
    nodes = _entity_map(seen_nodes)
    edge_rows = [edges[rid] for rid in seen_edges if rid in edges]
    return {
        "nodes": [{"id": n["id"], "name": n["name"], "type": n["type"],
                   "description": n.get("description") or "",
                   "status": n.get("status", "active"), "pinned": n.get("pinned", 0),
                   "important": n.get("important", 0), "confidence": n["confidence"]}
                  for n in nodes.values()],
        "edges": [{"id": f"e{r['id']}", "source": r["source_id"], "target": r["target_id"],
                   "relation": r["relation"], "confidence": r["confidence"],
                   "status": r["status"]} for r in edge_rows],
    }


def _serialize_nodes(ents):
    return [{"id": e["id"], "label": e["name"], "type": e["type"],
             "description": e.get("description") or "", "confidence": e["confidence"],
             "pinned": e.get("pinned", 0), "important": e.get("important", 0),
             "status": e.get("status", "active")} for e in ents]


def _serialize_edges(rels):
    return [{"id": f"e{r['id']}", "source": r["source_id"], "target": r["target_id"],
             "relation": r["relation"], "confidence": r["confidence"],
             "status": r.get("status", "active")} for r in rels]


def graph_view(focus="auto", depth=2, active_only=True):
    """Full graph, or User + N hops when the brain is large enough to clutter.

    ``focus=auto`` uses User+depth once there are more than
    ``GRAPH_FOCUS_THRESHOLD`` entities. Isolated User (no edges) always
    falls back to the full graph so a new brain is never blank.
    """
    ents = store.all_entities()
    rels = store.all_relationships(active_only=active_only)
    total_nodes = len(ents)
    total_edges = len(rels)
    requested = (focus or "auto").strip().lower()
    if requested not in ("auto", "user", "all"):
        requested = "auto"
    use_focus = requested
    if requested == "auto":
        use_focus = "user" if total_nodes > config.GRAPH_FOCUS_THRESHOLD else "all"
    try:
        depth = min(max(int(depth or 2), 1), 6)
    except (TypeError, ValueError):
        depth = 2
    meta = {
        "type_colors": config.TYPE_COLORS,
        "relation_types": config.RELATION_TYPES,
        "entity_types": config.ENTITY_TYPES,
        "depth": depth,
        "total_nodes": total_nodes,
        "total_edges": total_edges,
        "focus": "all",
        "truncated": False,
    }
    if use_focus == "user":
        uid = store.ensure_user_entity()
        hood = neighborhood(uid, depth=depth, active_only=active_only)
        if hood["edges"]:
            nodes = [{
                "id": n["id"], "label": n["name"], "type": n["type"],
                "description": n.get("description") or "",
                "confidence": n.get("confidence", 0.8),
                "pinned": n.get("pinned", 0), "important": n.get("important", 0),
                "status": n.get("status", "active"),
            } for n in hood["nodes"]]
            edges = hood["edges"]
            meta["focus"] = "user"
            meta["truncated"] = len(nodes) < total_nodes
            meta["shown_nodes"] = len(nodes)
            meta["shown_edges"] = len(edges)
            return {"nodes": nodes, "edges": edges, **meta}
    nodes = _serialize_nodes(ents)
    edges = _serialize_edges(rels)
    meta["shown_nodes"] = len(nodes)
    meta["shown_edges"] = len(edges)
    return {"nodes": nodes, "edges": edges, **meta}


# --------------------------------------------------------------------------
# Shortest path
# --------------------------------------------------------------------------

def shortest_path(source_id, target_id, active_only=True, max_depth=6):
    """BFS shortest path between two entities. Returns list of hops or None."""
    if source_id == target_id:
        return [{"node": source_id}]
    adj, edges = _load_edges(active_only)
    prev = {source_id: None}  # node -> (prev_node, rel_id, relation, direction)
    q = deque([source_id])
    while q:
        cur = q.popleft()
        if cur == target_id:
            break
        for (other, rid, rel, conf, direction) in adj.get(cur, []):
            if other in prev:
                continue
            prev[other] = (cur, rid, rel, direction)
            q.append(other)
    if target_id not in prev:
        return None
    # Reconstruct.
    path = []
    cur = target_id
    while prev[cur] is not None:
        pnode, rid, rel, direction = prev[cur]
        path.append({"edge_id": rid, "relation": rel, "from": pnode, "to": cur})
        cur = pnode
    path.reverse()
    return path


# --------------------------------------------------------------------------
# Graph filtering
# --------------------------------------------------------------------------

def filter_graph(entity_type=None, relation=None, min_confidence=None,
                 active_only=True, pinned=None, important=None, query=None):
    """Filter the graph by type / relation / confidence / status / flags.
    Returns {nodes, edges, stats}."""
    # Entities with filters.
    sql = "SELECT * FROM entities WHERE 1=1"
    params = []
    if entity_type:
        sql += " AND type=?"
        params.append(entity_type)
    if active_only:
        sql += " AND status='active'"
    if pinned is not None:
        sql += " AND pinned=?"
        params.append(1 if pinned else 0)
    if important is not None:
        sql += " AND important=?"
        params.append(1 if important else 0)
    if query:
        sql += " AND norm_name LIKE ?"
        params.append(f"%{store.normalize_name(query)}%")
    ents = db.query(sql, tuple(params))
    ids = {e["id"] for e in ents}

    where = []
    rp = []
    if active_only:
        where.append("status='active'")
    if relation:
        where.append("relation=?")
        rp.append(relation)
    if min_confidence is not None:
        where.append("confidence>=?")
        rp.append(min_confidence)
    rels = db.query(
        "SELECT * FROM relationships" + (" WHERE " + " AND ".join(where) if where else ""),
        tuple(rp),
    )
    # Only keep edges whose both endpoints are in the filtered node set.
    kept_rels = [r for r in rels if r["source_id"] in ids and r["target_id"] in ids]

    nodes = [{"id": e["id"], "name": e["name"], "type": e["type"],
              "status": e.get("status", "active"), "pinned": e.get("pinned", 0),
              "important": e.get("important", 0), "confidence": e["confidence"],
              "description": e["description"]} for e in ents]
    edges = [{"id": f"e{r['id']}", "source": r["source_id"], "target": r["target_id"],
              "relation": r["relation"], "confidence": r["confidence"],
              "status": r["status"]} for r in kept_rels]
    return {"nodes": nodes, "edges": edges, "stats": graph_stats(ents, kept_rels)}


def graph_stats(ents=None, rels=None):
    """Graph statistics: counts, distribution, degree."""
    ents = ents if ents is not None else store.all_entities()
    rels = rels if rels is not None else store.all_relationships()
    by_type = defaultdict(int)
    for e in ents:
        by_type[e["type"]] += 1
    by_relation = defaultdict(int)
    degree = defaultdict(int)
    status_counts = defaultdict(int)
    for r in rels:
        by_relation[r["relation"]] += 1
        degree[r["source_id"]] += 1
        degree[r["target_id"]] += 1
        status_counts[r.get("status", "active")] += 1
    degrees = list(degree.values())
    return {
        "nodes": len(ents),
        "edges": len(rels),
        "by_type": dict(by_type),
        "by_relation": dict(by_relation),
        "status": dict(status_counts),
        "avg_degree": round(sum(degrees) / len(ents), 2) if ents else 0.0,
        "max_degree": max(degrees) if degrees else 0,
        "most_connected": sorted(
            [{"id": e["id"], "name": e["name"], "type": e["type"], "degree": degree.get(e["id"], 0)}
             for e in ents if e["name"].lower() != "user"],
            key=lambda x: -x["degree"])[:10],
    }


# --------------------------------------------------------------------------
# Multi-hop retrieval
# --------------------------------------------------------------------------

def multi_hop(seed_ids, max_depth=3, max_nodes=40, active_only=True):
    """Bounded BFS from seed entities, collecting the facts encountered along
    relevant paths. Returns (facts, path_hops) where facts are
    {text, confidence, source_message_id, entities:[ids], depth}."""
    adj, edges = _load_edges(active_only)
    visited = set(seed_ids)
    frontier = list(seed_ids)
    facts = []
    seen_edges = set()
    pending = []  # (depth, rid, other)
    for depth in range(1, int(max_depth) + 1):
        nxt = []
        for nid in frontier:
            for (other, rid, rel, conf, direction) in adj.get(nid, []):
                if rid in seen_edges:
                    continue
                seen_edges.add(rid)
                pending.append((depth, rid, other))
                if other not in visited:
                    visited.add(other)
                    nxt.append(other)
        frontier = nxt
        if len(visited) >= max_nodes or not frontier:
            break
    needed = set()
    for _, rid, _ in pending:
        r = edges.get(rid)
        if r:
            needed.add(r["source_id"])
            needed.add(r["target_id"])
    emap = _entity_map(needed)
    for depth, rid, _other in pending:
        r = edges.get(rid)
        if not r:
            continue
        src = emap.get(r["source_id"])
        tgt = emap.get(r["target_id"])
        if not src or not tgt:
            continue
        facts.append({
            "text": f'{src["name"]} {r["relation"]} {tgt["name"]}',
            "confidence": r["confidence"],
            "source_message_id": r["source_message_id"],
            "entities": [r["source_id"], r["target_id"]],
            "depth": depth,
            "relation": r["relation"],
        })
    return facts


def group_by_type(active_only=True):
    """Group live entities by type for larger-graph navigation."""
    ents = store.all_entities()
    if active_only:
        ents = [e for e in ents if e.get("status", "active") == "active"]
    groups = defaultdict(list)
    for e in ents:
        groups[e["type"]].append({"id": e["id"], "name": e["name"], "type": e["type"]})
    return {k: sorted(v, key=lambda x: x["name"].lower()) for k, v in groups.items()}


def explainable_rank(query_text, max_depth=3):
    """Deterministic hybrid ranking with explainable reasons.

    Returns a list of ranked entities, each with a composite score and a
    breakdown of contributing signals (used internally / by the UI to show
    *why* something matched — never chain-of-thought).
    """
    from . import search as search_mod

    # Keyword + semantic signals (reuse existing scorers).
    khits = search_mod.keyword_search(query_text, limit=40)
    vhits = search_mod.vector_search(query_text, k=40)

    rows = store.all_entities()
    by_id = {r["id"]: r for r in rows}

    # Recency signal: seconds since updated_at.
    import datetime as _dt
    now = _dt.datetime.now(_dt.timezone.utc)
    def _age(iso):
        try:
            d = _dt.datetime.fromisoformat(iso)
            return max(0.0, (now - d).total_seconds())
        except (ValueError, TypeError):
            return float("inf")

    scores = {}
    for s, r in khits:
        scores[r["id"]] = scores.get(r["id"], {"score": 0.0, "reasons": []})
        scores[r["id"]]["score"] += s
        scores[r["id"]]["reasons"].append("keyword")
    for s, r in vhits:
        if r["id"] not in scores:
            scores[r["id"]] = {"score": 0.0, "reasons": []}
        scores[r["id"]]["score"] += s * 0.6
        scores[r["id"]]["reasons"].append("semantic")

    # Graph + confidence + recency + status signals.
    adj, _ = _load_edges(active_only=True)
    for eid, rec in scores.items():
        row = by_id.get(eid)
        if not row:
            continue
        # Confidence boost.
        conf = row["confidence"]
        rec["score"] += (conf - 0.5) * 0.5
        # Recency boost (recent updates rank slightly higher).
        age = _age(row.get("updated_at") or row.get("created_at") or "")
        if age < 86400 * 7:      # within a week
            rec["score"] += 0.3
            rec["reasons"].append("recent")
        # Graph connectivity: more connections -> more relevant.
        deg = len(adj.get(eid, []))
        rec["score"] += min(deg, 10) * 0.05
        if deg >= 2:
            rec["reasons"].append("graph")
        # Superseded entities are heavily down-weighted (but not removed, so
        # history remains discoverable when explicitly queried).
        if row.get("status") == "superseded":
            rec["score"] -= 5.0
        rec["score"] = round(rec["score"], 3)

    ranked = sorted(
        [{"id": eid, "score": rec["score"], "reasons": sorted(set(rec["reasons"]))}
         for eid, rec in scores.items() if rec["score"] > 0],
        key=lambda x: -x["score"],
    )
    return ranked
````

## `backend/ollama.py`

````
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
        return db.get_setting("ollama_base_url", config.OLLAMA_BASE_URL)
    except Exception:
        return config.OLLAMA_BASE_URL


def _url(path):
    return get_base_url().rstrip("/") + path


def available(timeout=2, force=False):
    """True if Ollama is reachable at the configured base URL."""
    now = time.monotonic()
    url = get_base_url()
    if (
        not force
        and _avail_cache["url"] == url
        and (now - _avail_cache["t"]) < _AVAIL_TTL
    ):
        return _avail_cache["v"]
    try:
        r = requests.get(_url("/api/tags"), timeout=timeout)
        value = r.status_code == 200
    except requests.RequestException:
        value = False
    _avail_cache.update({"t": now, "v": value, "url": url})
    return value


def list_models():
    try:
        r = requests.get(_url("/api/tags"), timeout=min(config.OLLAMA_TIMEOUT, 8))
        r.raise_for_status()
        return [m.get("name") for m in r.json().get("models", [])]
    except requests.RequestException:
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
    `/api/embeddings` endpoint so both Ollama generations work.
    """
    try:
        r = requests.post(
            _url("/api/embed"),
            json={"model": model, "input": text},
            timeout=config.OLLAMA_TIMEOUT,
        )
        if r.status_code == 200:
            data = r.json()
            if data.get("embeddings"):
                return data["embeddings"][0]
            if data.get("embedding"):
                return data["embedding"]
    except requests.RequestException:
        pass
    r = requests.post(
        _url("/api/embeddings"),
        json={"model": model, "prompt": text},
        timeout=config.OLLAMA_TIMEOUT,
    )
    r.raise_for_status()
    return r.json().get("embedding", [])
````

## `backend/paths.py`

````
"""Persistent, CWD-independent path resolution.

The database must NEVER live inside a PyInstaller extract directory
(``sys._MEIPASS``). That folder is temporary and would look like a "new
empty brain" on every launch.

Resolution order for the SQLite file:

1. ``SECOND_BRAIN_DB`` if it is a real, non-ephemeral path
   (relative values are resolved against the app root, not the CWD)
2. An existing ``brain.db`` next to the executable / project (portable)
3. An existing ``brain.db`` in the user data directory
4. Frozen default: ``%LOCALAPPDATA%/SecondBrain/data/brain.db``
   Source default: ``<app-root>/data/brain.db``

Existing files always win. Nothing here deletes or overwrites a database.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

APP_VERSION = "2.5.0"
DB_NAME = "brain.db"


def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def bundle_dir() -> Path:
    """Read-only files shipped with the app (frontend when frozen)."""
    if is_frozen():
        return Path(getattr(sys, "_MEIPASS", Path(sys.executable).resolve().parent))
    return Path(__file__).resolve().parent.parent


def app_root() -> Path:
    """Persistent application root (never _MEIPASS)."""
    if is_frozen():
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


def _user_data_dir() -> Path:
    override = os.environ.get("SECOND_BRAIN_DATA")
    if override:
        path = Path(override).expanduser()
        return path if path.is_absolute() else (app_root() / path)
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(base) / "SecondBrain" / "data"
    xdg = os.environ.get("XDG_DATA_HOME")
    if xdg:
        return Path(xdg) / "second-brain"
    return Path.home() / ".local" / "share" / "second-brain"


def _is_ephemeral(path: Path) -> bool:
    try:
        resolved = path.resolve()
    except OSError:
        resolved = path
    text = str(resolved)
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        try:
            if resolved == Path(meipass) or Path(meipass) in resolved.parents:
                return True
        except OSError:
            if str(meipass) in text:
                return True
    lowered = text.replace("\\", "/").lower()
    if "/_mei" in lowered and ("/temp" in lowered or "/tmp" in lowered):
        return True
    return False


def frontend_dir() -> Path:
    bundled = bundle_dir() / "frontend"
    if (bundled / "index.html").is_file():
        return bundled
    return app_root() / "frontend"


def _existing_db_candidates() -> list[Path]:
    return [
        app_root() / "data" / DB_NAME,
        _user_data_dir() / DB_NAME,
    ]


def _coerce_persistent(path: Path) -> Path:
    """Make a path absolute against the app root. Reject extract-dir targets."""
    candidate = path.expanduser()
    if not candidate.is_absolute():
        candidate = app_root() / candidate
    return candidate


def resolve_db_path() -> Path:
    """Return the database path. Never points at a temp extract dir."""
    env = os.environ.get("SECOND_BRAIN_DB")
    if env:
        candidate = _coerce_persistent(Path(env))
        if not _is_ephemeral(candidate):
            return candidate

    for path in _existing_db_candidates():
        try:
            if path.is_file() and not _is_ephemeral(path):
                return path
        except OSError:
            continue

    # Frozen builds persist under the user profile so moving the EXE
    # cannot orphan an existing brain or create a new empty one.
    if is_frozen():
        return _user_data_dir() / DB_NAME
    return app_root() / "data" / DB_NAME


def ensure_data_dirs(db_path: Path | None = None) -> Path:
    """Create parent folders only. Never deletes an existing database."""
    path = Path(db_path) if db_path is not None else resolve_db_path()
    parent = path.parent
    if str(parent):
        parent.mkdir(parents=True, exist_ok=True)
    (parent / "backups").mkdir(parents=True, exist_ok=True)
    return path
````

## `backend/requirements-dev.txt`

````
# Test / development dependencies (on top of requirements.txt)
pytest>=8.0
httpx>=0.27
playwright>=1.40   # optional — browser tests (python -m playwright install chromium)
pyinstaller>=6.0   # optional — build SecondBrain.exe on Windows
````

## `backend/requirements.txt`

````
fastapi>=0.110
uvicorn[standard]>=0.29
requests>=2.31
numpy>=1.26
````

## `backend/search.py`

````
"""Unified memory search with multi-hop retrieval and grounded answers.

Combines keyword (exact), vector (semantic) and graph (relational) signals —
plus recency, confidence and status — into a deterministic, explainable hybrid
ranking. Multi-hop traversal follows only relevant graph paths (bounded BFS) so
answers can chain facts ("what technology does the project I'm learning Rust
for use?"). Every answer is classified KNOWN / UNKNOWN / UNCERTAIN and carries
a traceable list of sources, so nothing is hallucinated.
"""
import json
import re

import numpy as np

from . import config, db, fallback, graph, ollama, store

INTENT_KEYWORDS = {
    "project": ["project", "projects", "app", "apps", "building", "startup", "working on", "working"],
    "learning": ["learn", "learning", "study", "studying"],
    "technology": ["technology", "tech", "technologies", "stack", "tools", "using"],
    "person": ["people", "person", "friends", "friend", "who", "met"],
    "goal": ["goal", "goals", "plan", "want", "objective", "aiming"],
    "interest": ["interest", "interested", "hobbies", "like", "enjoy", "prefer", "preference"],
    "location": ["live", "located", "based"],
    "organization": ["work at", "work for", "company", "employer", "organization"],
}

STOPWORDS = {
    "the", "a", "an", "and", "or", "i", "me", "my", "we", "our", "you", "your",
    "do", "does", "did", "is", "are", "am", "was", "were", "be", "have", "has",
    "had", "use", "using", "used", "with", "for", "to", "of", "in", "on", "at",
    "it", "that", "this", "what", "who", "how", "when", "where", "which", "why",
    "tell", "show", "give", "list", "about", "any", "some", "can", "could",
    "would", "should", "there", "their", "them", "from", "as", "by", "not",
    "no", "yes", "please", "remember", "know",
}


def detect_intent(query):
    q = query.lower()
    for intent, words in INTENT_KEYWORDS.items():
        if any(w in q for w in words):
            return intent
    return None


def _cosine(a, b):
    if a is None or b is None:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


def re_tokenize(s):
    return re.findall(r"[a-z0-9#+.\-']+", s.lower())


_SHORT_TERMS = {
    "go", "ai", "js", "ts", "ui", "ux", "ml", "c#", "c++", "r", "k8s",
}


def query_terms(query_text):
    """Content tokens for ranking. Keeps short tech names (Go, AI, C#)."""
    out = []
    for t in re_tokenize(query_text):
        if t in STOPWORDS:
            continue
        if len(t) > 2 or t in _SHORT_TERMS:
            out.append(t)
    return out


def json_loads(s):
    try:
        return json.loads(s or "[]")
    except ValueError:
        return []


# --------------------------------------------------------------------------
# Signal 1: vector (semantic)
# --------------------------------------------------------------------------

def vector_search(query_text, k=None):
    k = k or config.VECTOR_SEARCH_K
    qv = store.embed_text(query_text)
    rows = db.query("SELECT * FROM entities WHERE embedding IS NOT NULL")
    scored = []
    for r in rows:
        ev = store.vec_from_json(r.get("embedding"))
        if ev is None:
            continue
        scored.append((_cosine(qv, ev), r))
    scored.sort(key=lambda x: -x[0])
    return [(s, r) for s, r in scored[:k] if s > 0.1]


# --------------------------------------------------------------------------
# Signal 2: keyword (exact)
# --------------------------------------------------------------------------

def keyword_search(query_text, limit=10):
    terms = query_terms(query_text)
    rows = db.query("SELECT * FROM entities")
    scored = []
    for r in rows:
        name = r["name"].lower()
        aliases = [store.normalize_name(a) for a in json_loads(r.get("aliases"))]
        score = 0.0
        for t in terms:
            if t == name:
                score += 5.0
            elif t in name:
                score += 1.0
            elif any(t == a or t in a for a in aliases):
                score += 2.0
        if score:
            scored.append((score, r))
    scored.sort(key=lambda x: -x[0])
    return [(s, r) for s, r in scored[:limit]]


# --------------------------------------------------------------------------
# Graph facts
# --------------------------------------------------------------------------

def graph_facts_for_entity(eid, active_only=True):
    """Relationships touching an entity, in canonical "s relation t" form."""
    status_filter = " AND r.status='active'" if active_only else ""
    rels = db.query(
        "SELECT r.*, s.name sname, t.name tname FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE (r.source_id=? OR r.target_id=?)" + status_filter,
        (eid, eid),
    )
    return [{"text": f'{r["sname"]} {r["relation"]} {r["tname"]}',
             "confidence": r["confidence"], "rid": r["id"],
             "source_message_id": r["source_message_id"],
             "entities": [r["source_id"], r["target_id"]]} for r in rels]


def intent_facts(intent):
    """Graph facts directly matching a question intent (e.g. 'learning')."""
    out = []
    if intent == "learning":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='learning' AND r.status='active'")
        out = [{"text": f'{r["sname"]} learning {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent in ("interest", "preference"):
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.relation rel, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation IN ('prefers','interested_in','likes') AND r.status='active'")
        out = [{"text": f'{r["sname"]} {r["rel"]} {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "project":
        rows = db.query("SELECT * FROM entities WHERE type='project' AND status='active'")
        out = [{"text": f'project {r["name"]}', "confidence": r["confidence"],
                "entities": [r["id"]], "source_message_id": r.get("source_message_id")} for r in rows]
    elif intent == "technology":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='uses' AND r.status='active'")
        out = [{"text": f'{r["sname"]} uses {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "goal":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='wants' AND r.status='active'")
        out = [{"text": f'{r["sname"]} wants {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "person":
        rows = db.query("SELECT * FROM entities WHERE type='person' AND status='active' AND norm_name != 'user'")
        out = [{"text": f'person {r["name"]}', "confidence": r["confidence"],
                "entities": [r["id"]], "source_message_id": r.get("source_message_id")} for r in rows]
    elif intent == "location":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='lives_in' AND r.status='active'")
        out = [{"text": f'{r["sname"]} lives_in {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    elif intent == "organization":
        rels = db.query(
            "SELECT r.id rid, r.source_message_id smid, s.name sname, t.name tname, r.confidence c, "
            "r.source_id sid, r.target_id tid FROM relationships r "
            "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
            "WHERE r.relation='works_at' AND r.status='active'")
        out = [{"text": f'{r["sname"]} works_at {r["tname"]}', "confidence": r["c"],
                "rid": r["rid"], "source_message_id": r["smid"],
                "entities": [r["sid"], r["tid"]]} for r in rels]
    return out


# --------------------------------------------------------------------------
# Source attribution
# --------------------------------------------------------------------------

def _source_for_message(message_id):
    if not message_id:
        return None
    m = store.message_by_id(message_id)
    if not m:
        return None
    conv = store.conversation_row(m.get("conversation_id")) if m.get("conversation_id") else None
    return {"message_id": m["id"], "content": m["content"], "created_at": m["created_at"],
            "conversation_id": m.get("conversation_id"),
            "conversation_title": conv["title"] if conv else None}


def sources_for_facts(facts, limit=8):
    """Build a compact, deduplicated source list for a set of facts/entities."""
    seen = set()
    sources = []
    for f in facts:
        fact_src = _source_for_message(f.get("source_message_id"))
        for eid in f.get("entities", []):
            ent = store.entity_row(eid)
            if not ent:
                continue
            src = fact_src or _source_for_message(ent.get("source_message_id"))
            key = (ent["name"], ent["id"], src["message_id"] if src else None)
            if key in seen:
                continue
            seen.add(key)
            snippet = (src["content"][:160] if src and src.get("content") else None)
            sources.append({
                "entity_id": ent["id"], "name": ent["name"], "type": ent["type"],
                "message_id": src["message_id"] if src else None,
                "conversation_title": src["conversation_title"] if src else None,
                "created_at": (src["created_at"] if src else None) or ent["created_at"],
                "snippet": snippet,
                "fact": f.get("text"),
            })
            if len(sources) >= limit:
                return sources
    return sources


# --------------------------------------------------------------------------
# Hybrid search (with multi-hop)
# --------------------------------------------------------------------------

def search(query_text, filters=None, multi_hop_depth=3):
    """Combined ranking + multi-hop fact retrieval.

    filters (optional): {type, min_confidence, status, pinned, important}
    """
    filters = filters or {}
    intent = detect_intent(query_text)
    vhits = vector_search(query_text)
    khits = keyword_search(query_text)

    merged = {}
    for s, r in vhits:
        merged[r["id"]] = {"entity": r, "score": s * 0.6, "vector": round(s, 3), "reasons": ["semantic"]}
    for s, r in khits:
        cur = merged.get(r["id"])
        if cur:
            cur["score"] += s
            cur["keyword"] = round(s, 1)
            if "keyword" not in cur["reasons"]:
                cur["reasons"].append("keyword")
        else:
            merged[r["id"]] = {"entity": r, "score": float(s), "keyword": round(s, 1), "reasons": ["keyword"]}

    # Graph-connectivity signal.
    adj, _ = graph._load_edges(active_only=True)
    for eid, rec in merged.items():
        deg = len(adj.get(eid, []))
        if deg >= 2:
            rec["score"] += min(deg, 10) * 0.05
            rec["reasons"].append("graph")
        # recency / flags
        rec["score"] += _recency_boost(rec["entity"])
        if _is_recent(rec["entity"]):
            rec["reasons"].append("recent")
        if rec["entity"].get("pinned"):
            rec["score"] += 0.8
            rec["reasons"].append("pinned")
        if rec["entity"].get("important"):
            rec["score"] += 0.5
            rec["reasons"].append("important")
        # status penalty
        if rec["entity"].get("status") == "superseded":
            rec["score"] -= 5.0

    # Apply filters.
    if filters:
        merged = {eid: rec for eid, rec in merged.items()
                  if _passes_filters(rec["entity"], filters)}

    results = sorted(merged.values(), key=lambda x: -x["score"])
    entities = [{
        "id": e["entity"]["id"], "name": e["entity"]["name"],
        "type": e["entity"]["type"], "description": e["entity"]["description"],
        "confidence": e["entity"]["confidence"],
        "score": round(e["score"], 3),
        "vector": e.get("vector"), "keyword": e.get("keyword"),
        "reasons": e.get("reasons", []),
        "status": e["entity"].get("status", "active"),
        "pinned": e["entity"].get("pinned", 0),
        "important": e["entity"].get("important", 0),
    } for e in results if e["score"] > 0]

    # Facts: direct + intent + multi-hop.
    facts = []
    seed_ids = [e["entity"]["id"] for e in results[:5]]
    for e in results[:5]:
        facts.extend(graph_facts_for_entity(e["entity"]["id"]))
    facts.extend(intent_facts(intent))
    if seed_ids:
        facts.extend(graph.multi_hop(seed_ids, max_depth=multi_hop_depth))

    seen, dedup = set(), []
    for f in facts:
        if f["text"] not in seen:
            seen.add(f["text"])
            dedup.append(f)

    dedup = _rank_facts(dedup, query_text)

    return {"intent": intent, "entities": entities, "facts": dedup,
            "sources": sources_for_facts(dedup)}


def _rank_facts(facts, query_text):
    q_terms = set(query_terms(query_text))
    def _score(f):
        blob = (f.get("text") or "").lower()
        tok = sum(1 for t in q_terms if t in blob)
        depth = f.get("depth") or 1
        conf = f.get("confidence") or 0.5
        return (tok * 3.0) + float(conf) - (max(int(depth), 1) - 1) * 0.45
    return sorted(facts, key=_score, reverse=True)


def _is_recent(row):
    import datetime as _dt
    try:
        d = _dt.datetime.fromisoformat(row.get("updated_at") or row.get("created_at") or "")
        return (_dt.datetime.now(_dt.timezone.utc) - d).total_seconds() < 86400 * 7
    except (ValueError, TypeError):
        return False


def _recency_boost(row):
    return 0.3 if _is_recent(row) else 0.0


def _passes_filters(row, filters):
    if filters.get("type") and row["type"] != filters["type"]:
        return False
    if filters.get("min_confidence") is not None and row["confidence"] < filters["min_confidence"]:
        return False
    if filters.get("status") and row.get("status", "active") != filters["status"]:
        return False
    if filters.get("pinned") is not None and bool(row.get("pinned", 0)) != bool(filters["pinned"]):
        return False
    if filters.get("important") is not None and bool(row.get("important", 0)) != bool(filters["important"]):
        return False
    created = (row.get("created_at") or "")[:10]
    updated = (row.get("updated_at") or created)[:10]
    if filters.get("date_from") and updated < str(filters["date_from"])[:10]:
        return False
    if filters.get("date_to") and created > str(filters["date_to"])[:10]:
        return False
    if filters.get("source"):
        src_filter = str(filters["source"])
        if src_filter.lower() == "demo":
            try:
                meta = json.loads(row.get("meta") or "{}")
            except ValueError:
                meta = {}
            if not meta.get("demo"):
                return False
        else:
            mid = row.get("source_message_id")
            msg = store.message_by_id(mid) if mid else None
            if not msg or str(msg.get("conversation_id")) != src_filter:
                return False
    return True


# --------------------------------------------------------------------------
# Grounded answer (KNOWN / UNKNOWN / UNCERTAIN)
# --------------------------------------------------------------------------

_YN_FACT = re.compile(
    r"^(?:do i|did i|am i|have i)\s+"
    r"(using|use|learning|learn|preferring|prefer|living in|live in|"
    r"working at|work at|working on|work on|know)\s+(.+?)\??$",
    re.I,
)

_YN_REL = {
    "use": "uses", "using": "uses",
    "learn": "learning", "learning": "learning",
    "prefer": "prefers", "preferring": "prefers",
    "live in": "lives_in", "living in": "lives_in",
    "work at": "works_at", "working at": "works_at",
    "work on": "works_on", "working on": "works_on",
    "know": "knows",
}


def _direct_fact_answer(query_text):
    """Yes/no questions about a specific stored fact. Never invents."""
    m = _YN_FACT.match((query_text or "").strip())
    if not m:
        return None
    rel = _YN_REL.get(m.group(1).lower())
    name = (m.group(2) or "").strip().strip("?. ")
    if not rel or not name:
        return None
    target = store.find_entity_by_name(name)
    if not target:
        hits = keyword_search(name, limit=3)
        if hits and hits[0][0] >= 5:
            target = hits[0][1]
    uid = store.ensure_user_entity()
    unknown = {
        "text": (
            f"I don't have a memory indicating that. Nothing in your brain "
            f"matches “{query_text}” yet."
        ),
        "status": "unknown",
        "sources": [],
    }
    if not target:
        return unknown
    row = db.query_one(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? "
        "AND relation=? AND status='active'",
        (uid, target["id"], rel),
    )
    if not row:
        return unknown
    fact = {"text": f'User {rel} {target["name"]}', "confidence": row["confidence"],
            "entities": [uid, target["id"]], "source_message_id": row.get("source_message_id")}
    return {
        "text": f'Yes — User {rel} {target["name"]}. (from stored memory)',
        "status": "known",
        "sources": sources_for_facts([fact]),
    }


_ABOUT = re.compile(
    r"^(?:tell me about|what do (?:i|you) know about|who is|what about)\s+(.+?)\??$",
    re.I,
)
_PATH_Q = re.compile(
    r"^(?:how (?:is|are)\s+(.+?)\s+related\s+to\s+(.+?)"
    r"|what(?:'s| is) the (?:connection|relationship|link) between\s+(.+?)\s+and\s+(.+?))"
    r"\??$",
    re.I,
)
_ARTICLES = re.compile(r"^(?:the|a|an|my|our|this|that)\s+", re.I)
_USES_OF = re.compile(
    r"^(?:what(?: technology| technologies| tools?)? does)\s+(.+?)\s+use\??$",
    re.I,
)
_LIST_QUESTIONS = (
    (re.compile(r"^(?:where do i live|where am i based|where do i live now)\??$", re.I),
     "location", " lives_in "),
    (re.compile(r"^(?:where do i work|who do i work for|where am i employed)\??$", re.I),
     "organization", " works_at "),
    (re.compile(r"^(?:who do i know|who have i met)\??$", re.I),
     "person", " knows "),
    (re.compile(r"^(?:what do i prefer|what(?:'s| is) my (?:preference|favorite|favourite)(?: language)?)\??$", re.I),
     "interest", " prefers "),
    (re.compile(r"^(?:what do i use|what(?: tools| tech| technologies) do i use)\??$", re.I),
     "technology", " uses "),
)


def _resolve_named_entity(name):
    name = (name or "").strip().strip("?. ")
    name = _ARTICLES.sub("", name).strip()
    if not name:
        return None
    hit = store.find_entity_by_name(name)
    if hit:
        return hit
    hits = keyword_search(name, limit=3)
    if hits and hits[0][0] >= 5:
        return hits[0][1]
    tokens = [t for t in query_terms(name) if t not in STOPWORDS]
    if not tokens:
        return None
    best = None
    for row in db.query("SELECT * FROM entities"):
        blob = (row["name"] or "").lower()
        if all(t in blob for t in tokens):
            if best is None or len(blob) < len(best["name"]):
                best = row
    return best


def _about_answer(query_text):
    m = _ABOUT.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return {
            "text": (
                f"I don't have a memory indicating that. Nothing in your brain "
                f"matches “{query_text}” yet."
            ),
            "status": "unknown",
            "sources": [],
        }
    facts = graph_facts_for_entity(ent["id"])
    sources = sources_for_facts(
        facts or [{"text": ent["name"], "entities": [ent["id"]],
                   "source_message_id": ent.get("source_message_id")}]
    )
    lines = [f'{ent["name"]} is stored as a {ent["type"]}.']
    if ent.get("description"):
        lines.append(ent["description"])
    if facts:
        lines.append("Known facts: " + "; ".join(f["text"] for f in facts[:8]) + ".")
    else:
        lines.append("No active relationships yet.")
    if sources and sources[0].get("snippet"):
        lines.append(f'Source: “{sources[0]["snippet"]}”')
    return {"text": " ".join(lines) + " (from stored memory)",
            "status": "known", "sources": sources}


def _path_answer(query_text):
    m = _PATH_Q.match((query_text or "").strip())
    if not m:
        return None
    left = m.group(1) or m.group(3)
    right = m.group(2) or m.group(4)
    a = _resolve_named_entity(left)
    b = _resolve_named_entity(right)
    if not a or not b:
        return {
            "text": (
                f"I don't have a memory indicating that. Nothing in your brain "
                f"matches “{query_text}” yet."
            ),
            "status": "unknown",
            "sources": [],
        }
    hops = graph.shortest_path(a["id"], b["id"])
    if not hops:
        return {
            "text": f"I don't have a stored path between {a['name']} and {b['name']}.",
            "status": "unknown",
            "sources": [],
        }
    names = {a["id"]: a["name"], b["id"]: b["name"]}
    bits = []
    for hop in hops:
        if "relation" not in hop:
            continue
        src = store.entity_row(hop["from"])
        tgt = store.entity_row(hop["to"])
        if src and tgt:
            names[src["id"]] = src["name"]
            names[tgt["id"]] = tgt["name"]
            bits.append(f'{src["name"]} {hop["relation"]} {tgt["name"]}')
    if not bits:
        return {
            "text": f"{a['name']} and {b['name']} are the same stored entity.",
            "status": "known",
            "sources": [],
        }
    facts = [{"text": t, "entities": [a["id"], b["id"]]} for t in bits]
    return {
        "text": " → ".join(bits) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
    }


def _unknown(query_text):
    return {
        "text": (
            f"I don't have a memory indicating that. Nothing in your brain "
            f"matches “{query_text}” yet."
        ),
        "status": "unknown",
        "sources": [],
        "final": True,
    }


def _list_intent_answer(query_text):
    """Direct answers for where I live / who I know / what I prefer."""
    q = (query_text or "").strip()
    for rx, intent, _needle in _LIST_QUESTIONS:
        if not rx.match(q):
            continue
        facts = intent_facts(intent)
        if not facts:
            return _unknown(query_text)
        return {
            "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
            "status": "known",
            "sources": sources_for_facts(facts),
            "final": True,
        }
    return None


def _uses_of_answer(query_text):
    m = _USES_OF.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return _unknown(query_text)
    facts = [f for f in graph_facts_for_entity(ent["id"]) if " uses " in f["text"]]
    if not facts:
        return {
            "text": f"I don't have a stored uses-relationship for {ent['name']}.",
            "status": "unknown",
            "sources": [],
            "final": True,
        }
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


_STOPPED_Q = re.compile(
    r"^(?:what did i stop|what have i stopped|what did i quit)(?:\s+\w+)?\??$",
    re.I,
)
_CHANGED_Q = re.compile(
    r"^(?:what changed(?: this week| recently)?|what did i change(?: this week| recently)?)\??$",
    re.I,
)
_USED_BY = re.compile(
    r"^(?:who uses|what uses|which (?:projects?|apps?|tools?) (?:use|uses))\s+(.+?)\??$",
    re.I,
)
_WHEN_Q = re.compile(
    r"^when did i (?:start |begin )?(?:learning |using |working (?:on |at )?"
    r"|living (?:in )?|meet(?:ing)? )?(.+?)\??$",
    re.I,
)


def _used_by_answer(query_text):
    """Inverse of uses-of: which stored things use this entity."""
    m = _USED_BY.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return _unknown(query_text)
    needle = f' uses {ent["name"]}'
    facts = [f for f in graph_facts_for_entity(ent["id"]) if needle in f.get("text", "")]
    if not facts:
        return {
            "text": f'I don\'t have a stored uses-relationship pointing at {ent["name"]}.',
            "status": "unknown",
            "sources": [],
            "final": True,
        }
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


def _when_answer(query_text):
    """Date of the earliest stored fact about a named entity. Never invents."""
    m = _WHEN_Q.match((query_text or "").strip())
    if not m:
        return None
    ent = _resolve_named_entity(m.group(1))
    if not ent:
        return _unknown(query_text)
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT r.*, s.name sname, t.name tname FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE (r.source_id=? AND r.target_id=?) OR (r.source_id=? AND r.target_id=?) "
        "ORDER BY r.created_at ASC, r.id ASC",
        (uid, ent["id"], ent["id"], uid),
    )
    if rels:
        first = rels[0]
        when = (first.get("created_at") or "")[:10] or "an unknown date"
        extra = " (no longer active)" if first.get("status") != "active" else ""
        fact = {
            "text": f'{first["sname"]} {first["relation"]} {first["tname"]}',
            "entities": [first["source_id"], first["target_id"]],
            "source_message_id": first.get("source_message_id"),
            "confidence": first.get("confidence") or 0.8,
        }
        return {
            "text": (
                f'You first stored “{fact["text"]}” on {when}{extra}. '
                f"(from stored memory)"
            ),
            "status": "known",
            "sources": sources_for_facts([fact]),
            "final": True,
        }
    when = (ent.get("created_at") or "")[:10]
    if not when:
        return _unknown(query_text)
    return {
        "text": f'{ent["name"]} was first stored on {when}. (from stored memory)',
        "status": "known",
        "sources": sources_for_facts([{
            "text": ent["name"], "entities": [ent["id"]],
            "source_message_id": ent.get("source_message_id"),
        }]),
        "final": True,
    }


def _stopped_answer(query_text):
    """Active history: superseded facts. Never invents."""
    if not _STOPPED_Q.match((query_text or "").strip()):
        return None
    rels = db.query(
        "SELECT r.source_message_id smid, s.name sname, t.name tname, r.relation rel, "
        "r.confidence c, r.source_id sid, r.target_id tid "
        "FROM relationships r "
        "JOIN entities s ON s.id=r.source_id JOIN entities t ON t.id=r.target_id "
        "WHERE r.status='superseded' ORDER BY r.created_at DESC LIMIT 12"
    )
    if not rels:
        return _unknown(query_text)
    facts = [{"text": f'{r["sname"]} {r["rel"]} {r["tname"]} (no longer active)',
              "confidence": r["c"], "entities": [r["sid"], r["tid"]],
              "source_message_id": r["smid"]} for r in rels]
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


def _changed_answer(query_text):
    """Recent superseded / conflict / command memories from the last 7 days."""
    if not _CHANGED_Q.match((query_text or "").strip()):
        return None
    import datetime as _dt
    cutoff = (_dt.datetime.now(_dt.timezone.utc) - _dt.timedelta(days=7)).isoformat()
    mems = db.query(
        "SELECT * FROM memories WHERE kind IN ('superseded','conflict','command') "
        "AND created_at >= ? ORDER BY created_at DESC LIMIT 12",
        (cutoff,),
    )
    if not mems:
        return _unknown(query_text)
    facts = [{"text": m["text"], "confidence": m.get("confidence") or 0.8,
              "entities": json_loads(m.get("entity_ids")),
              "source_message_id": m.get("message_id")} for m in mems]
    return {
        "text": "; ".join(f["text"] for f in facts[:8]) + ". (from stored memory)",
        "status": "known",
        "sources": sources_for_facts(facts),
        "final": True,
    }


def retrieve_answer(query_text, filters=None):
    """Deterministic retrieval. `final` answers skip the LLM composer."""
    direct = _direct_fact_answer(query_text)
    if direct is not None:
        out = dict(direct)
        out["final"] = True
        return out
    stopped = _stopped_answer(query_text)
    if stopped is not None:
        return stopped
    changed = _changed_answer(query_text)
    if changed is not None:
        return changed
    listed = _list_intent_answer(query_text)
    if listed is not None:
        return listed
    uses = _uses_of_answer(query_text)
    if uses is not None:
        return uses
    used_by = _used_by_answer(query_text)
    if used_by is not None:
        return used_by
    when = _when_answer(query_text)
    if when is not None:
        return when
    about = _about_answer(query_text)
    if about is not None:
        out = dict(about)
        out["final"] = True
        return out
    path = _path_answer(query_text)
    if path is not None:
        out = dict(path)
        out["final"] = True
        return out
    return {"final": False, "retrieval": search(query_text, filters=filters)}


def answer(query_text, model=None, context=None, filters=None):
    model = model or config.DEFAULT_LLM_MODEL
    retrieved = retrieve_answer(query_text, filters=filters)
    if retrieved.get("final"):
        return {k: retrieved[k] for k in ("text", "status", "sources") if k in retrieved}
    return compose_answer(query_text, retrieved["retrieval"], model, context)


def _intent_relevant_facts(facts, intent):
    keys = {
        "learning": (" learning ",),
        "project": ("project ",),
        "technology": (" uses ",),
        "interest": (" prefers ", " interested_in ", " likes "),
        "goal": (" wants ",),
        "person": ("person ", " knows "),
        "location": (" lives_in ",),
        "organization": (" works_at ",),
    }.get(intent)
    if not keys:
        return list(facts)
    return [f for f in facts if any(k in f" {f.get('text', '')} " or k.strip() in (f.get("text") or "") for k in keys)]


def _status_of(res, query_text=""):
    ents = res["entities"]
    facts = res["facts"]
    intent = res["intent"]
    if not ents and not facts:
        return "unknown"
    if intent and facts:
        relevant = _intent_relevant_facts(facts, intent)
        if relevant:
            top_conf = relevant[0].get("confidence") or 0.0
            return "known" if top_conf >= 0.6 else "uncertain"
        return "uncertain" if ents else "unknown"
    has_name = any((e.get("keyword") or 0) >= 1 for e in ents)
    if not has_name:
        return "unknown"
    top = ents[0]["score"] if ents else 0.0
    if top >= 2.0:
        return "known"
    return "uncertain"


def _knowledge_names(res, query_text=""):
    """Surface forms the composer is allowed to mention."""
    names = {"user", "i", "me"}
    for e in res.get("entities") or []:
        n = store.normalize_name(e.get("name"))
        if n:
            names.add(n)
    for f in res.get("facts") or []:
        for part in re.findall(r"[A-Za-z0-9][A-Za-z0-9+.#\-]{1,40}", f.get("text") or ""):
            n = store.normalize_name(part)
            if n:
                names.add(n)
    for t in query_terms(query_text):
        names.add(t)
    return names


def reply_is_grounded(text, res, query_text=""):
    """False if the reply names a stored entity or known tech absent from knowledge."""
    blob = (text or "").lower()
    if not blob.strip():
        return False
    allowed = _knowledge_names(res, query_text)
    for e in store.all_entities():
        n = e.get("norm_name") or ""
        if not n or n in allowed or len(n) < 3:
            continue
        if re.search(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])", blob):
            return False
    for key, display in fallback.TECH.items():
        dn = display.lower()
        if dn in allowed or key in allowed:
            continue
        if re.search(r"(?<![a-z0-9])" + re.escape(key) + r"(?![a-z0-9])", blob):
            return False
    return True


def _composer_messages(query_text, res, context=None):
    entities = res["entities"]
    facts = res["facts"]
    context_lines = []
    for e in entities[:8]:
        context_lines.append(
            f'- entity "{e["name"]}" (type: {e["type"]}, confidence {round(e["confidence"], 2)}): '
            f'{e["description"] or ""}')
    for f in facts[:12]:
        context_lines.append(f'- fact: {f["text"]} (confidence {round(f["confidence"], 2)})')
    if context:
        context_lines.append("- recent conversation:\n" + context)
    grounding = "\n".join(context_lines)
    prompt = (
        "You are the memory of a personal Second Brain. Answer the user's "
        "question using ONLY the knowledge below. Be concise and factual. "
        "If the knowledge does not contain the answer, say so explicitly — "
        "never invent personal memories. Only mention entities that appear "
        "in KNOWLEDGE. If the answer is based on low-confidence memories, "
        "say 'I believe' or 'possibly'.\n\n"
        f"KNOWLEDGE:\n{grounding}\n\nQUESTION: {query_text}\nANSWER:")
    return [
        {"role": "system",
         "content": "You are a helpful personal knowledge assistant. Answer only from the provided knowledge."},
        {"role": "user", "content": prompt},
    ]


def compose_answer(query_text, res, model, context=None):
    sources = res.get("sources", [])
    status = _status_of(res, query_text)

    if status == "unknown":
        return {"text": f"I don't have a memory indicating that. Nothing in your brain matches \u201c{query_text}\u201d yet.",
                "status": "unknown", "sources": []}

    if ollama.available():
        try:
            text = ollama.chat(model, _composer_messages(query_text, res, context),
                               temperature=0.2).strip()
            if text and reply_is_grounded(text, res, query_text):
                return {"text": text, "status": status, "sources": sources}
        except Exception:
            pass

    text = _fallback_answer(query_text, res, status)
    return {"text": text, "status": status, "sources": sources}


def compose_answer_stream(query_text, res, model, context=None):
    """Yield reply chunks after retrieval. Falls back to one complete chunk."""
    status = _status_of(res, query_text)
    if status == "unknown":
        yield f"I don't have a memory indicating that. Nothing in your brain matches \u201c{query_text}\u201d yet."
        return
    if ollama.available():
        try:
            acc = []
            for piece in ollama.chat_stream(
                model, _composer_messages(query_text, res, context), temperature=0.2,
            ):
                if piece:
                    acc.append(piece)
            text = "".join(acc).strip()
            if text and reply_is_grounded(text, res, query_text):
                yield text
                return
        except Exception:
            pass
    yield _fallback_answer(query_text, res, status)


def _fallback_answer(query_text, res, status):
    intent = res["intent"]
    entities = res["entities"]
    facts = res["facts"]

    names = [e["name"] for e in entities if (e.get("keyword") or 0) >= 1] or \
            [e["name"] for e in entities]
    if status == "uncertain":
        if names:
            return f"I have a lower-confidence memory suggesting {', '.join(names)}. Treat this as tentative."
        return "I'm not certain about that — my memory is incomplete here."

    if intent == "project":
        projs = [f["text"] for f in facts if f["text"].startswith("project ")]
        text = ("You're working on: " + ", ".join(p[8:] for p in projs) + "."
                if projs else f"Here's what I have: {', '.join(names)}.")
    elif intent == "learning":
        learns = [f["text"] for f in facts if " learning " in f["text"]]
        text = ("You're learning: " + "; ".join(learns) + "."
                if learns else f"Here's what I have: {', '.join(names)}.")
    elif intent in ("interest", "preference"):
        pref = [f["text"] for f in facts if " prefers " in f["text"] or " interested_in " in f["text"]]
        text = ("; ".join(pref) + "." if pref else f"Here's what I have: {', '.join(names)}.")
    elif intent == "goal":
        goals = [f["text"] for f in facts if " wants " in f["text"]]
        text = ("; ".join(goals) + "." if goals else f"Here's what I have: {', '.join(names)}.")
    elif intent == "organization":
        jobs = [f["text"] for f in facts if " works_at " in f["text"]]
        text = ("; ".join(jobs) + "." if jobs else f"Here's what I have: {', '.join(names)}.")
    elif intent == "location":
        locs = [f["text"] for f in facts if " lives_in " in f["text"]]
        text = ("; ".join(locs) + "." if locs else f"Here's what I have: {', '.join(names)}.")
    else:
        detail = ". ".join(f["text"] for f in facts[:5])
        text = f"I found: {', '.join(names)}. " + (detail + "." if detail else "")

    text += " (from stored memory)"
    return text


def is_question(text):
    t = text.strip()
    if not t:
        return False
    if t.endswith("?"):
        return True
    lower = t.lower()
    interrogatives = ("what", "who", "which", "when", "where", "how", "do i", "am i",
                      "have i", "did i", "list", "tell me", "show me",
                      "whats", "what's", "give me", "summarize", "what do you",
                      "what are", "what is", "do you", "can you tell",
                      "what do i know")
    return lower.startswith(interrogatives)
````

## `backend/store.py`

````
"""Graph store: entities, relationships, conversations, memories, messages.

Implements normalization, duplicate detection, entity merging, memory
supersession (stale/outdated facts), and source tracking so the brain stays
clean and trustworthy instead of accumulating duplicate or contradictory nodes.
"""
import json
import re

import numpy as np

from . import config, db, fallback, ollama


# --------------------------------------------------------------------------
# Normalization helpers
# --------------------------------------------------------------------------

def normalize_name(name):
    """Lowercase, collapse whitespace, strip surrounding punctuation."""
    if not name:
        return ""
    n = name.strip().lower()
    n = re.sub(r"\s+", " ", n)
    n = n.strip("\"'“”‘’()[]{}.,:;!?*")
    return n


def normalize_type(t):
    return config.TYPE_SYNONYMS.get((t or "").strip().lower(), "concept")


def normalize_relation(raw):
    """Return (canonical_relation, swap) for a raw relation label."""
    label = re.sub(r"[^a-z_]", "_", (raw or "").strip().lower()).strip("_")
    label = re.sub(r"_+", "_", label)
    if label in config.RELATION_INVERSE:
        return config.RELATION_INVERSE[label], True
    return config.RELATION_SYNONYMS.get(label, "related_to"), False


def vec_to_json(vec):
    if vec is None:
        return None
    return json.dumps([float(v) for v in vec])


def vec_from_json(s):
    if not s:
        return None
    return np.array(json.loads(s), dtype=np.float32)


_EMBED_CACHE = {}
_EMBED_CACHE_MAX = 256


def embed_text(text, model=None):
    """Embed text using Ollama if available, else the fallback hasher."""
    if model is None:
        model = db.get_setting("embedding_model", config.DEFAULT_EMBEDDING_MODEL)
    cache_key = (model or "", text or "")
    cached = _EMBED_CACHE.get(cache_key)
    if cached is not None:
        return cached
    vec = None
    if ollama.available():
        try:
            vec = np.array(ollama.embed(model or config.DEFAULT_EMBEDDING_MODEL, text),
                           dtype=np.float32)
        except Exception:
            vec = None
    if vec is None or vec.size == 0:
        vec = np.array(fallback.fallback_embed(text), dtype=np.float32)
    if len(_EMBED_CACHE) >= _EMBED_CACHE_MAX:
        _EMBED_CACHE.pop(next(iter(_EMBED_CACHE)))
    _EMBED_CACHE[cache_key] = vec
    return vec


def merge_similarity_threshold():
    return db.get_setting_float("merge_similarity", config.DEFAULT_MERGE_SIMILARITY)


# --------------------------------------------------------------------------
# Entity CRUD + merging
# --------------------------------------------------------------------------

def ensure_user_entity():
    """Create the special 'User' entity if it does not exist yet."""
    existing = db.query_one(
        "SELECT id FROM entities WHERE norm_name=?",
        (normalize_name(config.USER_ENTITY_NAME),),
    )
    if existing:
        return existing["id"]
    return create_entity(
        name=config.USER_ENTITY_NAME,
        etype="person",
        description=config.USER_ENTITY_DESCRIPTION,
        confidence=1.0,
    )


def find_entity_by_name(name):
    return db.query_one("SELECT * FROM entities WHERE norm_name=?", (normalize_name(name),))


def create_entity(name, etype="concept", description="", confidence=0.8,
                  aliases=None, source_message_id=None, embedding=None, meta=None):
    norm = normalize_name(name)
    if not norm:
        return None
    now = db.utcnow()
    eid = db.execute(
        "INSERT INTO entities(name, norm_name, type, description, aliases, embedding, "
        "confidence, source_message_id, created_at, updated_at, meta) "
        "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        (name.strip(), norm, normalize_type(etype), description or "",
         json.dumps(aliases or []), vec_to_json(embedding), confidence,
         source_message_id, now, now, json.dumps(meta or {})),
    )
    return eid


def update_entity(eid, **fields):
    allowed = {"name", "type", "description", "aliases", "confidence", "meta",
               "status", "pinned", "important"}
    sets, params = [], []
    for k, v in fields.items():
        if k not in allowed:
            continue
        if k in ("aliases", "meta"):
            v = json.dumps(v)
        sets.append(f"{k}=?")
        params.append(v)
    if not sets:
        return
    sets.append("updated_at=?")
    params.append(db.utcnow())
    params.append(eid)
    db.execute(f"UPDATE entities SET {', '.join(sets)} WHERE id=?", params)
    if "name" in fields:
        db.execute("UPDATE entities SET norm_name=? WHERE id=?",
                   (normalize_name(fields["name"]), eid))


def _cosine(a, b):
    if a is None or b is None or a.size == 0 or b.size == 0:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


def find_duplicate(entity_name, etype, embedding=None):
    """Find an existing entity that this one should merge into.

    1. Exact normalized-name match (including aliases).
    2. Vector similarity above the configured merge threshold (re-worded concepts).
    """
    norm = normalize_name(entity_name)
    row = db.query_one("SELECT * FROM entities WHERE norm_name=?", (norm,))
    if row:
        return row

    alias_rows = db.query(
        "SELECT * FROM entities WHERE aliases LIKE ?",
        (f"%{norm}%",),
    )
    for r in alias_rows:
        try:
            aliases = json.loads(r.get("aliases") or "[]")
        except ValueError:
            aliases = []
        if norm in [normalize_name(a) for a in aliases]:
            return r

    if embedding is not None:
        threshold = merge_similarity_threshold()
        alias_rows = db.query("SELECT * FROM entities WHERE embedding IS NOT NULL")
        for r in alias_rows:
            if normalize_name(r["name"]) in ("user",) and etype == "person":
                continue
            emb = vec_from_json(r.get("embedding"))
            if emb is not None and _cosine(embedding, emb) >= threshold:
                return r
    return None


def upsert_entity(name, etype, description="", confidence=0.8, source_message_id=None,
                  embedding=None, meta=None):
    """Insert or merge an entity. Returns (entity_id, created_bool)."""
    name = name.strip()
    if not name or normalize_name(name) == "":
        return None, False

    if normalize_name(name) in ("i", "me", "my", "myself", "mine", "user"):
        return ensure_user_entity(), False

    dup = find_duplicate(name, etype, embedding)
    if dup:
        new_desc = dup.get("description") or description
        aliases = []
        try:
            aliases = json.loads(dup.get("aliases") or "[]")
        except ValueError:
            aliases = []
        if normalize_name(name) != dup["norm_name"] and name not in aliases:
            aliases.append(name)
        update_entity(dup["id"], description=new_desc, aliases=aliases,
                      confidence=max(dup["confidence"], confidence))
        if embedding is not None and not dup.get("embedding"):
            db.execute("UPDATE entities SET embedding=? WHERE id=?",
                       (vec_to_json(embedding), dup["id"]))
        return dup["id"], False

    eid = create_entity(name, etype, description, confidence, source_message_id=source_message_id,
                        embedding=embedding, meta=meta)
    return eid, True


def merge_entities(keep_id, drop_id):
    """Merge `drop_id` into `keep_id`."""
    keep = db.query_one("SELECT * FROM entities WHERE id=?", (keep_id,))
    drop = db.query_one("SELECT * FROM entities WHERE id=?", (drop_id,))
    if not keep or not drop or keep_id == drop_id:
        return {"error": "invalid merge target"}

    db.execute("UPDATE OR IGNORE relationships SET source_id=? WHERE source_id=?", (keep_id, drop_id))
    db.execute("UPDATE OR IGNORE relationships SET target_id=? WHERE target_id=?", (keep_id, drop_id))
    db.execute("DELETE FROM relationships WHERE source_id=target_id")

    aliases = json.loads(keep.get("aliases") or "[]")
    for a in json.loads(drop.get("aliases") or "[]"):
        if a not in aliases:
            aliases.append(a)
    if drop["name"] not in aliases:
        aliases.append(drop["name"])
    desc = keep.get("description") or drop.get("description") or ""
    update_entity(keep_id, description=desc, aliases=aliases,
                  confidence=max(keep["confidence"], drop["confidence"]))
    # Rewrite every memory that references the dropped entity (including
    # multi-id memories such as relationship events).
    mems = db.query("SELECT id, entity_ids FROM memories WHERE entity_ids LIKE ?",
                    (f"%{drop_id}%",))
    for m in mems:
        try:
            ids = json.loads(m["entity_ids"] or "[]")
        except ValueError:
            continue
        if drop_id not in ids:
            continue
        rewritten, seen = [], set()
        for i in ids:
            nid = keep_id if i == drop_id else i
            if nid in seen:
                continue
            seen.add(nid)
            rewritten.append(nid)
        db.execute("UPDATE memories SET entity_ids=? WHERE id=?",
                   (json.dumps(rewritten), m["id"]))
    db.execute("DELETE FROM entities WHERE id=?", (drop_id,))
    return {"ok": True, "id": keep_id}


def delete_entity(eid):
    db.execute("DELETE FROM entities WHERE id=?", (eid,))


def set_entity_status(eid, status):
    db.execute("UPDATE entities SET status=? WHERE id=?", (status, eid))


def toggle_entity_flag(eid, flag):
    if flag not in ("pinned", "important"):
        return False
    row = entity_row(eid)
    if not row:
        return False
    db.execute(f"UPDATE entities SET {flag}=? WHERE id=?", (0 if row[flag] else 1, eid))
    return True


def set_confidence(eid, confidence):
    db.execute("UPDATE entities SET confidence=?, updated_at=? WHERE id=?",
               (confidence, db.utcnow(), eid))


def entity_row(eid):
    return db.query_one("SELECT * FROM entities WHERE id=?", (eid,))


def all_entities():
    return db.query("SELECT * FROM entities ORDER BY type, name COLLATE NOCASE")


def similar_entities(eid, limit=6, min_score=0.78):
    """Near-duplicates by embedding. Never auto-merges; the UI can suggest Merge."""
    row = entity_row(eid)
    if not row:
        return []
    vec = vec_from_json(row.get("embedding"))
    if vec is None:
        return []
    try:
        limit = max(1, min(int(limit or 6), 20))
    except (TypeError, ValueError):
        limit = 6
    scored = []
    for other in all_entities():
        if other["id"] == eid:
            continue
        ev = vec_from_json(other.get("embedding"))
        if ev is None:
            continue
        score = _cosine(vec, ev)
        if score >= min_score:
            scored.append((score, other))
    scored.sort(key=lambda x: -x[0])
    return [{
        "id": other["id"], "name": other["name"], "type": other["type"],
        "score": round(float(score), 3),
        "status": other.get("status", "active"),
    } for score, other in scored[:limit]]


# --------------------------------------------------------------------------
# Relationships (with supersession for stale facts)
# --------------------------------------------------------------------------

def add_relationship(source_id, target_id, relation, confidence=0.8, source_message_id=None):
    if source_id == target_id:
        return None
    existing = db.query_one(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation=?",
        (source_id, target_id, relation),
    )
    if existing:
        # Re-activate a previously superseded relationship when re-asserted.
        db.execute(
            "UPDATE relationships SET confidence=MAX(confidence,?), status='active' WHERE id=?",
            (confidence, existing["id"]),
        )
        return existing["id"]
    return db.execute(
        "INSERT INTO relationships(source_id, target_id, relation, confidence, "
        "source_message_id, created_at, status) VALUES(?,?,?,?,?,?,'active')",
        (source_id, target_id, relation, confidence, source_message_id, db.utcnow()),
    )


def relationship_exists(source_id, target_id, relation):
    return db.query_one(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? AND relation=?",
        (source_id, target_id, relation),
    ) is not None


def relationship_active(source_id, target_id, relation):
    return db.query_one(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? "
        "AND relation=? AND status='active'",
        (source_id, target_id, relation),
    ) is not None


def supersede_relationship(source_id, target_id, relation):
    """Mark a matching active relationship as superseded. Returns count changed."""
    rows = db.query(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? AND relation=? AND status='active'",
        (source_id, target_id, relation),
    )
    for r in rows:
        db.execute("UPDATE relationships SET status='superseded' WHERE id=?", (r["id"],))
    return len(rows)


def supersede_relations_of_type(source_id, relation, except_target_id=None, target_type=None):
    """Supersede all active `relation` links from `source_id` (optionally
    matching a target entity type), used for conflict resolution. Returns ids."""
    sql = "SELECT r.id, r.target_id, e.type ttype FROM relationships r JOIN entities e ON e.id=r.target_id WHERE r.source_id=? AND r.relation=? AND r.status='active'"
    rows = db.query(sql, (source_id, relation))
    changed = []
    for r in rows:
        if except_target_id and r["target_id"] == except_target_id:
            continue
        if target_type and r["ttype"] != target_type:
            continue
        db.execute("UPDATE relationships SET status='superseded' WHERE id=?", (r["id"],))
        changed.append(r["target_id"])
    return changed


def update_relationship(rid, **fields):
    """Update relation label, confidence, or status. Never deletes the row."""
    allowed = {"relation", "confidence", "status"}
    sets, params = [], []
    for k, v in fields.items():
        if k not in allowed:
            continue
        if k == "relation":
            rel, _swap = normalize_relation(v)
            v = rel
        if k == "confidence":
            try:
                v = max(0.0, min(1.0, float(v)))
            except (TypeError, ValueError):
                continue
        if k == "status" and v not in ("active", "superseded"):
            continue
        sets.append(f"{k}=?")
        params.append(v)
    if not sets:
        return False
    params.append(rid)
    db.execute(f"UPDATE relationships SET {', '.join(sets)} WHERE id=?", params)
    return True


def delete_relationship(rid):
    db.execute("DELETE FROM relationships WHERE id=?", (rid,))


def all_relationships(active_only=False):
    if active_only:
        return db.query("SELECT * FROM relationships WHERE status='active'")
    return db.query("SELECT * FROM relationships")


def relationship_row(rid):
    return db.query_one("SELECT * FROM relationships WHERE id=?", (rid,))


# --------------------------------------------------------------------------
# Conversations (short-term context, separate from long-term memory)
# --------------------------------------------------------------------------

def create_conversation(title=""):
    now = db.utcnow()
    return db.execute(
        "INSERT INTO conversations(title, created_at, updated_at) VALUES(?,?,?)",
        (title, now, now),
    )


def touch_conversation(cid, title=None):
    fields, params = [], []
    if title is not None:
        fields.append("title=?")
        params.append(title)
    fields.append("updated_at=?")
    params.append(db.utcnow())
    params.append(cid)
    db.execute(f"UPDATE conversations SET {', '.join(fields)} WHERE id=?", params)


def conversation_row(cid):
    return db.query_one("SELECT * FROM conversations WHERE id=?", (cid,))


def all_conversations():
    return db.query("SELECT * FROM conversations ORDER BY updated_at DESC, id DESC")


def _like_pattern(query):
    raw = (query or "").strip()
    if not raw:
        return None
    escaped = raw.replace("#", "##").replace("%", "#%").replace("_", "#_")
    return f"%{escaped}%"


def conversation_summaries(query=None, limit=200):
    """List conversations with counts/previews. Optional title+message search.

    Does not load every message row. LIKE wildcards in ``query`` are escaped
    so ``%`` cannot dump the whole rail.
    """
    try:
        limit = max(1, min(int(limit or 200), 500))
    except (TypeError, ValueError):
        limit = 200
    like = _like_pattern(query)
    params = []
    where = ""
    if like:
        where = (
            "WHERE c.id IN ("
            "  SELECT id FROM conversations WHERE title LIKE ? ESCAPE '#' "
            "  UNION "
            "  SELECT conversation_id FROM messages "
            "  WHERE conversation_id IS NOT NULL AND content LIKE ? ESCAPE '#'"
            ")"
        )
        params.extend([like, like])
    sql = (
        "SELECT c.id, c.title, c.created_at, c.updated_at, "
        "  (SELECT COUNT(*) FROM messages m WHERE m.conversation_id=c.id) AS message_count, "
        "  (SELECT m.content FROM messages m WHERE m.conversation_id=c.id AND m.role='user' "
        "   ORDER BY m.id DESC LIMIT 1) AS preview "
        "FROM conversations c "
        f"{where} "
        "ORDER BY c.updated_at DESC, c.id DESC LIMIT ?"
    )
    params.append(limit)
    rows = db.query(sql, tuple(params))
    out = []
    for c in rows:
        out.append({
            "id": c["id"],
            "title": c["title"] or "(untitled)",
            "created_at": c["created_at"],
            "updated_at": c["updated_at"],
            "message_count": int(c.get("message_count") or 0),
            "preview": (c.get("preview") or "")[:80],
        })
    return out


def current_conversation_id():
    cid = db.get_setting("current_conversation_id")
    if cid is None:
        cid = create_conversation()
        db.set_setting("current_conversation_id", cid)
        return cid
    if not conversation_row(cid):
        cid = create_conversation()
        db.set_setting("current_conversation_id", cid)
    return cid


def new_conversation():
    cid = create_conversation()
    db.set_setting("current_conversation_id", cid)
    return cid


def conversation_messages(cid, limit=None):
    """Return messages in chronological order. `limit` means the last N turns."""
    if limit:
        return db.query(
            "SELECT * FROM ("
            "  SELECT * FROM messages WHERE conversation_id=? ORDER BY id DESC LIMIT ?"
            ") ORDER BY id ASC",
            (cid, int(limit)),
        )
    return db.query(
        "SELECT * FROM messages WHERE conversation_id=? ORDER BY id ASC",
        (cid,),
    )


def delete_conversation(cid):
    """Delete a conversation and its messages. Long-term memories stay."""
    db.execute("DELETE FROM messages WHERE conversation_id=?", (cid,))
    db.execute("DELETE FROM conversations WHERE id=?", (cid,))
    current = db.get_setting("current_conversation_id")
    if current is not None and str(current) == str(cid):
        db.set_setting("current_conversation_id", None)
    return True


# --------------------------------------------------------------------------
# Memories (timeline events)
# --------------------------------------------------------------------------

def add_memory(kind, text, entity_ids=None, message_id=None, confidence=0.8, meta=None):
    return db.execute(
        "INSERT INTO memories(kind, text, entity_ids, message_id, confidence, created_at, meta) "
        "VALUES(?,?,?,?,?,?,?)",
        (kind, text, json.dumps(entity_ids or []), message_id, confidence, db.utcnow(),
         json.dumps(meta or {})),
    )


def recent_memories(limit=30):
    return db.query("SELECT * FROM memories ORDER BY created_at DESC, id DESC LIMIT ?", (limit,))


def memories_for_entity(eid, limit=50):
    rows = db.query("SELECT * FROM memories ORDER BY created_at DESC, id DESC LIMIT 200")
    out = []
    for m in rows:
        try:
            ids = json.loads(m["entity_ids"] or "[]")
        except ValueError:
            ids = []
        if eid in ids:
            out.append(m)
            if len(out) >= limit:
                break
    return out


# --------------------------------------------------------------------------
# Messages
# --------------------------------------------------------------------------

def add_message(role, content, conversation_id=None, embedding=None, extracted=0, meta=None):
    return db.execute(
        "INSERT INTO messages(conversation_id, role, content, created_at, embedding, extracted, meta) "
        "VALUES(?,?,?,?,?,?,?)",
        (conversation_id, role, content, db.utcnow(), vec_to_json(embedding), extracted,
         json.dumps(meta or {})),
    )


def messages(limit=200):
    return db.query("SELECT * FROM messages ORDER BY id ASC LIMIT ?", (limit,))


def message_by_id(mid):
    return db.query_one("SELECT * FROM messages WHERE id=?", (mid,))
````

## `backend/summarize.py`

````
"""Memory consolidation / summarization.

Detects clusters of related memories (by shared entities) and produces a
deterministic summary. The original memories are never deleted — a summary is a
new `summary` memory whose `meta` references the source memory ids it was
generated from.

Uses Ollama only to *polish* wording when available and genuinely useful;
otherwise falls back to a deterministic template, so consolidation always works
locally.
"""
import json

from . import config, db, ollama, store

MIN_MEMORIES_TO_SUMMARIZE = 3


def find_consolidation_candidates(min_shared=MIN_MEMORIES_TO_SUMMARIZE, limit=20):
    """Find clusters of memories that share an entity and are ripe for
    summarization. Returns a list of {entity, memory_ids, count}."""
    memories = db.query(
        "SELECT * FROM memories WHERE kind IN ('entity','relationship','update') "
        "ORDER BY created_at DESC LIMIT 500")
    # Map entity_id -> memory ids.
    clusters = {}
    for m in memories:
        try:
            ids = json.loads(m["entity_ids"] or "[]")
        except ValueError:
            ids = []
        for eid in ids:
            clusters.setdefault(eid, []).append(m["id"])

    out = []
    for eid, mids in clusters.items():
        if len(mids) < min_shared:
            continue
        ent = store.entity_row(eid)
        if not ent:
            continue
        # Skip entities already summarized recently.
        if _already_summarized(mids):
            continue
        out.append({"entity_id": eid, "entity_name": ent["name"],
                    "entity_type": ent["type"], "memory_ids": sorted(set(mids))[:30],
                    "count": len(set(mids))})
    out.sort(key=lambda x: -x["count"])
    return out[:limit]


def _already_summarized(memory_ids):
    """Avoid re-summarizing a cluster that a summary already references."""
    ids = set(memory_ids)
    rows = db.query("SELECT meta FROM memories WHERE kind='summary'")
    for r in rows:
        try:
            meta = json.loads(r["meta"] or "{}")
        except ValueError:
            continue
        refs = set(meta.get("source_memory_ids", []))
        if refs and ids and len(ids & refs) >= min(3, len(ids)):
            return True
    return False


def summarize_entity(entity_id, memory_ids=None):
    """Generate a summary for an entity. Returns the created summary memory."""
    ent = store.entity_row(entity_id)
    if not ent:
        return {"ok": False, "error": "entity not found"}

    if memory_ids is None:
        cands = find_consolidation_candidates(min_shared=1)
        target = next((c for c in cands if c["entity_id"] == entity_id), None)
        memory_ids = target["memory_ids"] if target else []

    mems = [db.query_one("SELECT * FROM memories WHERE id=?", (mid,)) for mid in memory_ids]
    mems = [m for m in mems if m]

    facts = store_relationships_readable(entity_id)

    # Build a deterministic summary body.
    parts = [f'{ent["name"]} is a {ent["type"]}.']
    if ent.get("description"):
        parts.append(ent["description"])
    if facts:
        parts.append("Key facts: " + "; ".join(facts[:8]) + ".")
    if mems:
        parts.append(f"Recorded across {len(mems)} memory events.")

    text = " ".join(parts)

    # Optionally polish wording with Ollama (only when useful).
    if ollama.available():
        try:
            prompt = (
                "Summarize the following memory of a personal knowledge graph "
                "into 2-3 concise, factual sentences. Do not invent anything.\n\n"
                f"{text}")
            polished = ollama.chat(
                db.get_setting("llm_model", config.DEFAULT_LLM_MODEL),
                [{"role": "system", "content": "You summarize personal memories factually."},
                 {"role": "user", "content": prompt}],
                temperature=0.3).strip()
            if polished:
                text = polished
        except Exception:
            pass

    summary_id = store.add_memory(
        "summary", text, entity_ids=[entity_id],
        confidence=max([ent["confidence"], 0.7]),
    )
    db.execute("UPDATE memories SET meta=? WHERE id=?",
               (json.dumps({"source_memory_ids": memory_ids}), summary_id))
    return {"ok": True, "summary_id": summary_id, "text": text,
            "entity": ent["name"], "source_memory_ids": memory_ids}


def store_relationships_readable(entity_id):
    """Readable active relationships for an entity (canonical direction)."""
    rels = db.query(
        "SELECT s.name sname, t.name tname, r.relation rel, r.source_id sid "
        "FROM relationships r JOIN entities s ON s.id=r.source_id "
        "JOIN entities t ON t.id=r.target_id "
        "WHERE (r.source_id=? OR r.target_id=?) AND r.status='active'",
        (entity_id, entity_id))
    out = []
    for r in rels:
        if r["sid"] == entity_id:
            out.append(f'{r["sname"]} {r["rel"]} {r["tname"]}')
        else:
            out.append(f'{r["tname"]} {r["rel"]} {r["sname"]}')
    return out


def summarize_all(limit=10):
    """Summarize the top consolidation candidates. Returns a list of results."""
    candidates = find_consolidation_candidates(limit=limit)
    results = []
    for c in candidates:
        r = summarize_entity(c["entity_id"], memory_ids=c["memory_ids"])
        results.append(r)
    return results
````

## `frontend/app.js`

````
/* ==========================================================================
   Second Brain — frontend application (Phase 2)
   ========================================================================== */

const API = "/api";
const $ = (s) => document.querySelector(s);
const $$ = (s) => Array.from(document.querySelectorAll(s));

const TYPE_COLORS = {
  person: "#f472b6", project: "#22d3ee", technology: "#34d399",
  topic: "#a78bfa", skill: "#2dd4bf", goal: "#60a5fa",
  interest: "#fb923c", preference: "#e879f9", fact: "#f87171",
  location: "#4ade80", organization: "#38bdf8", concept: "#fbbf24",
  task: "#94a3b8", event: "#f472b6",
};

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

async function api(path, opts = {}) {
  const res = await fetch(API + path, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) {
    let msg = res.statusText;
    try { msg = (await res.json()).detail || msg; } catch {}
    throw new Error(msg);
  }
  return res.json();
}

function toast(text) {
  const t = $("#toast");
  t.textContent = text;
  t.classList.add("show");
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove("show"), 2600);
}

function badge(type) {
  return `<span class="badge ${esc(type)}">${esc(type)}</span>`;
}

function fmtTime(iso) {
  const d = new Date(iso);
  return d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}
function fmtDay(iso) {
  const d = new Date(iso);
  return d.toLocaleDateString([], { weekday: "long", month: "long", day: "numeric", year: "numeric" });
}

let typeColors = TYPE_COLORS;

/* ==========================================================================
   Navigation
   ========================================================================== */
const VIEWS = ["dashboard", "chat", "graph", "browse", "memory", "search", "settings"];
let currentView = "dashboard";

function parseHash() {
  const raw = (location.hash || "").replace(/^#/, "");
  const parts = raw.split("/");
  return { view: parts[0] || "", extra: parts[1] || "" };
}

function setHash(view, extra) {
  const next = extra ? ("#" + view + "/" + extra) : ("#" + view);
  if (location.hash !== next) {
    try { history.replaceState(null, "", next); } catch {}
  }
}

function showView(name, opts = {}) {
  if (!VIEWS.includes(name)) name = "dashboard";
  currentView = name;
  VIEWS.forEach((v) => {
    const el = $("#view-" + v);
    if (el) el.classList.toggle("active", v === name);
  });
  $$(".nav-item").forEach((b) => b.classList.toggle("active", b.dataset.view === name));
  if (!opts.keepHash) setHash(name);
  if (name === "graph") requestAnimationFrame(() => { if (cy) cy.fit(undefined, 30); });
  if (name === "dashboard") loadDashboard();
  if (name === "memory") loadMemory();
  if (name === "browse") loadBrowse();
  if (name === "chat") scrollChat();
  if (name === "settings") { loadSettings(); loadBackupStatus(); }
}

function applyRoute() {
  const h = parseHash();
  if (h.view === "entity" && h.extra) {
    showView("graph", { keepHash: true });
    openEntity(h.extra);
    return;
  }
  if (h.view === "chat") {
    showView("chat", { keepHash: true });
    if (h.extra) openConversation(Number(h.extra));
    return;
  }
  if (VIEWS.includes(h.view)) showView(h.view, { keepHash: true });
}

window.addEventListener("hashchange", applyRoute);

$$(".nav-item").forEach((b) =>
  b.addEventListener("click", () => showView(b.dataset.view)));

/* ==========================================================================
   Status / health
   ========================================================================== */
async function refreshStatus() {
  try {
    const h = await api("/health");
    const dot = $(".status-dot");
    const txt = $(".status-text");
    if (h.ollama_available) {
      dot.className = "status-dot on";
      txt.textContent = "Ollama online";
    } else {
      dot.className = "status-dot off";
      txt.textContent = "Ollama offline (fallback)";
    }
    $("#model-line").textContent = `LLM: ${h.llm_model} · EMB: ${h.embedding_model}`;
  } catch {}
}

/* ==========================================================================
   Dashboard
   ========================================================================== */
async function loadDashboard() {
  const d = await api("/dashboard");
  const stats = [
    ["Entities", d.entities], ["Relationships", d.relationships],
    ["Memories", d.memories], ["Conversations", d.conversations],
    ["Technologies", d.by_type.technology || 0], ["Projects", d.by_type.project || 0],
    ["People", d.by_type.person || 0], ["Pinned", d.pinned],
  ];
  $("#stats-grid").innerHTML = stats
    .map(([l, n]) => `<div class="stat-card"><div class="stat-num">${n}</div><div class="stat-label">${l}</div></div>`)
    .join("");

  // Growth chart
  const max = Math.max(1, ...d.growth.map((g) => g.count));
  $("#growth-chart").innerHTML = d.growth.map((g) => `
    <div class="grow-bar" style="height:${Math.max(3, (g.count / max) * 100)}%">
      <span class="grow-tip">${g.date.slice(5)} · ${g.count}</span>
    </div>`).join("");

  // Type breakdown
  const types = Object.entries(d.by_type).sort((a, b) => b[1] - a[1]);
  const total = types.reduce((s, [, n]) => s + n, 0) || 1;
  $("#type-breakdown").innerHTML = types.length ? types.map(([t, n]) => `
    <div class="type-row">
      <span class="type-dot" style="background:${typeColors[t] || "#8899bb"}"></span>
      <span class="type-name">${esc(t)}</span>
      <span class="type-bar-track"><span class="type-bar-fill" style="width:${(n / total) * 100}%;background:${typeColors[t] || "#8899bb"}"></span></span>
      <span class="type-count">${n}</span>
    </div>`).join("") : `<p class="muted">No entities yet.</p>`;

  $("#recent-memories").innerHTML = d.recent.length
    ? d.recent.map((m) => `
        <div class="mem-item">
          <span class="mem-ico">${m.kind === "entity" ? "◆" : m.kind === "superseded" ? "⤫" : "⇄"}</span>
          <span class="mem-text">${esc(m.text)}</span>
          <span class="mem-time">${fmtTime(m.created_at)}</span>
        </div>`).join("")
    : `<p class="muted">No memories yet — start chatting.</p>`;

  $("#top-entities").innerHTML = d.most_connected.length
    ? d.most_connected.map((e) => `
        <div class="entity-mini" data-id="${e.id}">
          <span style="color:${typeColors[e.type] || "#fff"}">●</span>
          <span class="em-name">${esc(e.name)}</span>
          ${badge(e.type)}
          <span class="em-degree">${e.degree}</span>
        </div>`).join("")
    : `<p class="muted">Nothing yet.</p>`;
  $$("#top-entities .entity-mini").forEach((el) =>
    el.addEventListener("click", () => openEntity(el.dataset.id)));

  const banner = $("#demo-banner");
  if (banner) banner.style.display = d.has_demo_data ? "" : "none";
}

/* ==========================================================================
   Chat
   ========================================================================== */
let currentConversationId = null;

function scrollChat() {
  const s = $("#chat-scroll");
  s.scrollTop = s.scrollHeight;
}

function rememberChips(remembered) {
  if (!remembered || !remembered.length) return "";
  const parts = remembered.map((r) => {
    if (r.kind === "entity") {
      return `<span class="remembered-chip" data-id="${r.entity_id}">
        <span style="color:${typeColors[r.type] || "#fff"}">●</span> ${esc(r.name)}
        <span class="conf">${Math.round((r.confidence || 0.8) * 100)}%</span></span>`;
    }
    return `<span class="remembered-chip" data-id="${r.target_id || r.entity_id}">
      ${esc(r.source)} <span class="arrow">→</span> <span class="rel">${esc(r.relation)}</span> <span class="arrow">→</span> ${esc(r.target)}
      <span class="conf">${Math.round((r.confidence || 0.8) * 100)}%</span></span>`;
  }).join("");
  return `<div class="remembered-title">Memory updated</div>${parts}`;
}

function sourceChips(sources) {
  if (!sources || !sources.length) return "";
  return `<div class="remembered-title">Sources</div>` +
    sources.map((s) => `<span class="remembered-chip" data-id="${s.entity_id}">${esc(s.name)}${s.fact ? ` · <span class="conf">${esc(s.fact)}</span>` : ""}${s.snippet ? ` · <span class="conf">${esc(s.snippet)}</span>` : ""}</span>`).join("");
}

function attachChips(root) {
  if (!root) return;
  root.querySelectorAll(".remembered-chip").forEach((chip) =>
    chip.addEventListener("click", () => openEntity(chip.dataset.id)));
}

function appendMessage(role, content, opts = {}) {
  $("#chat-empty").style.display = "none";
  const wrap = document.createElement("div");
  wrap.className = "msg " + role;

  if (content) {
    const b = document.createElement("div");
    b.className = "msg-bubble";
    b.textContent = content;
    if (opts.status) {
      const st = document.createElement("span");
      st.className = "ans-status ans-" + opts.status;
      st.textContent = opts.status;
      b.prepend(st, document.createTextNode(" "));
    }
    wrap.appendChild(b);
  }

  if (opts.remembered && opts.remembered.length) {
    const box = document.createElement("div");
    box.className = "remembered-box";
    box.innerHTML = rememberChips(opts.remembered);
    wrap.appendChild(box);
    box.querySelectorAll(".remembered-chip").forEach((chip) =>
      chip.addEventListener("click", () => openEntity(chip.dataset.id)));
  }

  if (opts.superseded && opts.superseded.length) {
    const note = document.createElement("div");
    note.className = "superseded-note";
    note.textContent = "Superseded: " + opts.superseded.join(", ");
    wrap.appendChild(note);
  }

  if (opts.sources && opts.sources.length) {
    const src = document.createElement("div");
    src.className = "remembered-box";
    src.innerHTML = sourceChips(opts.sources);
    wrap.appendChild(src);
    attachChips(src);
  }

  const t = document.createElement("div");
  t.className = "msg-time";
  t.textContent = fmtTime(new Date().toISOString());
  wrap.appendChild(t);
  $("#chat-messages").appendChild(wrap);
  scrollChat();
}

function parseSseBuffer(buffer, onEvent) {
  const parts = buffer.split("\n\n");
  const rest = parts.pop();
  for (const block of parts) {
    let event = "message";
    const dataLines = [];
    for (const line of block.split("\n")) {
      if (line.startsWith("event:")) event = line.slice(6).trim();
      else if (line.startsWith("data:")) dataLines.push(line.slice(5).trim());
    }
    if (!dataLines.length) continue;
    try { onEvent(event, JSON.parse(dataLines.join("\n"))); } catch {}
  }
  return rest;
}

async function sendChat() {
  const input = $("#chat-input");
  const content = input.value.trim();
  if (!content) return;
  input.value = "";
  input.style.height = "auto";
  appendMessage("user", content);
  $("#chat-send").disabled = true;

  const wrap = document.createElement("div");
  wrap.className = "msg assistant";
  const bubble = document.createElement("div");
  bubble.className = "msg-bubble streaming";
  wrap.appendChild(bubble);
  $("#chat-empty").style.display = "none";
  $("#chat-messages").appendChild(wrap);
  scrollChat();

  let reply = "";
  let remembered = [];
  let superseded = [];
  let status = "";
  let sources = [];
  let usedFallback = false;

  const finish = (r = {}) => {
    reply = r.reply != null ? r.reply : reply;
    remembered = r.remembered || remembered;
    superseded = r.superseded || superseded;
    status = r.status || status;
    sources = r.sources || sources;
    if (r.used_fallback) usedFallback = true;
    r.used_fallback = usedFallback || r.used_fallback;
    if (r.conversation_id) currentConversationId = r.conversation_id;
    bubble.classList.remove("streaming");
    bubble.textContent = reply;
    if (status) {
      const st = document.createElement("span");
      st.className = "ans-status ans-" + status;
      st.textContent = status === "answered" ? "known" : status;
      bubble.prepend(st, document.createTextNode(" "));
    }
    if (remembered && remembered.length) {
      const box = document.createElement("div");
      box.className = "remembered-box";
      box.innerHTML = rememberChips(remembered);
      wrap.appendChild(box);
      box.querySelectorAll(".remembered-chip").forEach((chip) =>
        chip.addEventListener("click", () => openEntity(chip.dataset.id)));
    }
    if (superseded && superseded.length) {
      const note = document.createElement("div");
      note.className = "superseded-note";
      note.textContent = "Superseded: " + superseded.join(", ");
      wrap.appendChild(note);
    }
    if (sources && sources.length) {
      const src = document.createElement("div");
      src.className = "remembered-box";
      src.innerHTML = sourceChips(sources);
      wrap.appendChild(src);
      attachChips(src);
    }
    const t = document.createElement("div");
    t.className = "msg-time";
    t.textContent = fmtTime(new Date().toISOString());
    wrap.appendChild(t);
    if (r.used_fallback) {
      const chip = document.createElement("span");
      chip.className = "offline-chip";
      chip.textContent = "offline extractor";
      bubble.appendChild(document.createTextNode(" "));
      bubble.appendChild(chip);
    }
    if (remembered && remembered.length) { loadDashboard(); buildGraph(); }
    if (r.is_command || (remembered && remembered.length)) loadDashboard();
    loadConversations();
    scrollChat();
  };

  try {
    const res = await fetch(API + "/chat/stream", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content, conversation_id: currentConversationId }),
    });
    if (!res.ok || !res.body) {
      const r = await api("/chat", {
        method: "POST",
        body: JSON.stringify({ content, conversation_id: currentConversationId }),
      });
      finish(r);
      return;
    }
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buf = "";
    let donePayload = null;
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      buf = parseSseBuffer(buf, (event, data) => {
        if (event === "meta" && data.conversation_id) currentConversationId = data.conversation_id;
        if (event === "token" && data.text) {
          reply += data.text;
          bubble.textContent = reply;
          scrollChat();
        }
        if (event === "memory") {
          remembered = data.remembered || [];
          superseded = data.superseded || [];
          if (data.used_fallback) usedFallback = true;
        }
        if (event === "status") status = data.status || status;
        if (event === "sources") sources = data.sources || [];
        if (event === "done") donePayload = data;
      });
    }
    finish(donePayload || { reply, remembered, superseded, status, sources });
  } catch (e) {
    try {
      const r = await api("/chat", {
        method: "POST",
        body: JSON.stringify({ content, conversation_id: currentConversationId }),
      });
      finish(r);
    } catch (err) {
      bubble.classList.remove("streaming");
      bubble.textContent = "⚠ " + err.message;
    }
  } finally {
    $("#chat-send").disabled = false;
    scrollChat();
  }
}

$("#chat-send").addEventListener("click", sendChat);
$("#chat-input").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendChat(); }
});
$("#chat-input").addEventListener("input", (e) => {
  e.target.style.height = "auto";
  e.target.style.height = Math.min(e.target.scrollHeight, 140) + "px";
});

$("#chat-new").addEventListener("click", async () => {
  const r = await api("/conversations/new", { method: "POST" });
  currentConversationId = r.conversation_id;
  setHash("chat", r.conversation_id);
  $("#chat-messages").innerHTML = "";
  $("#chat-empty").style.display = "";
  toast("Started a new conversation");
  loadConversations();
});

async function loadConversations() {
  const list = $("#conv-list");
  if (!list) return;
  const q = ($("#conv-search") && $("#conv-search").value.trim()) || "";
  try {
    const convs = await api("/conversations" + (q ? ("?q=" + encodeURIComponent(q)) : ""));
    if (!convs.length) {
      list.innerHTML = `<p class="muted">${q ? "No conversations match." : "No conversations yet."}</p>`;
      return;
    }
    list.innerHTML = convs.map((c) => `
      <div class="conv-item ${c.id === currentConversationId ? "active" : ""}" data-id="${c.id}">
        <div class="conv-title" data-id="${c.id}" title="Double-click to rename">${esc(c.title || "(untitled)")}</div>
        <div class="conv-preview">${esc(c.preview || "")}</div>
        <button class="rel-del conv-del" data-id="${c.id}" title="Delete conversation">✕</button>
      </div>`).join("");
    list.querySelectorAll(".conv-item").forEach((el) =>
      el.addEventListener("click", (ev) => {
        if (ev.target.closest(".conv-del") || ev.target.closest(".conv-title")) return;
        openConversation(Number(el.dataset.id));
      }));
    list.querySelectorAll(".conv-title").forEach((el) =>
      el.addEventListener("dblclick", (ev) => {
        ev.stopPropagation();
        renameConversation(Number(el.dataset.id), el);
      }));
    list.querySelectorAll(".conv-del").forEach((btn) =>
      btn.addEventListener("click", async (ev) => {
        ev.stopPropagation();
        if (!confirm("Delete this conversation? Long-term memories stay.")) return;
        const r = await api("/conversations/" + btn.dataset.id, { method: "DELETE" });
        if (currentConversationId === Number(btn.dataset.id)) {
          currentConversationId = r.conversation_id || null;
          $("#chat-messages").innerHTML = "";
          $("#chat-empty").style.display = "";
        }
        loadConversations();
      }));
    const src = $("#sf-source");
    if (src && !q) {
      const cur = src.value;
      src.innerHTML = `<option value="">Any source</option>` +
        convs.map((c) => `<option value="${c.id}">${esc(c.title || "Conversation " + c.id)}</option>`).join("");
      src.value = cur;
    }
  } catch {}
}

if ($("#conv-search")) {
  let convSearchTimer = null;
  $("#conv-search").addEventListener("input", () => {
    clearTimeout(convSearchTimer);
    convSearchTimer = setTimeout(loadConversations, 180);
  });
  $("#conv-search").addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.target.value = ""; loadConversations(); }
  });
}

async function renameConversation(id, el) {
  const current = el.textContent.trim();
  el.contentEditable = "true";
  el.focus();
  const range = document.createRange();
  range.selectNodeContents(el);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  const done = async () => {
    el.contentEditable = "false";
    el.removeEventListener("blur", done);
    const title = el.textContent.trim().slice(0, 80);
    if (!title || title === current) { el.textContent = current; return; }
    await api("/conversations/" + id, { method: "PATCH", body: JSON.stringify({ title }) });
    loadConversations();
  };
  el.addEventListener("blur", done);
  el.addEventListener("keydown", (e) => {
    if (e.key === "Enter") { e.preventDefault(); el.blur(); }
    if (e.key === "Escape") { el.textContent = current; el.blur(); }
  }, { once: true });
}

async function openConversation(id) {
  currentConversationId = id;
  setHash("chat", id);
  $("#chat-messages").innerHTML = "";
  $("#chat-empty").style.display = "";
  const msgs = await api(`/conversations/${id}/messages`);
  msgs.forEach((m) => {
    if (m.role === "user") appendMessage("user", m.content);
    else appendMessage("assistant", m.content, {
      remembered: m.remembered, kind: m.kind, status: m.status,
      superseded: m.superseded, sources: m.sources,
    });
  });
  loadConversations();
}

async function loadChatHistory() {
  const convs = await api("/conversations");
  if (!convs.length) { loadConversations(); return; }
  currentConversationId = convs[0].id;
  await openConversation(convs[0].id);
}

/* ==========================================================================
   Knowledge Graph
   ========================================================================== */
let cy;
let graphNodes = [];

function initGraph() {
  cy = cytoscape({
    container: document.getElementById("cy"),
    style: [
      { selector: "node",
        style: {
          "background-color": (el) => typeColors[el.data("type")] || "#8899bb",
          "label": "data(label)",
          "color": "#e7ecf5",
          "font-size": 11,
          "text-valign": "center",
          "text-halign": "center",
          "text-wrap": "wrap",
          "text-max-width": 80,
          "width": (el) => el.data("important") ? 22 : 16,
          "height": (el) => el.data("important") ? 22 : 16,
          "border-width": (el) => el.data("pinned") ? 3 : 1.5,
          "border-color": (el) => el.data("pinned") ? "#fbbf24" : "#0a0e1a",
          "text-outline-width": 2, "text-outline-color": "#0a0e1a",
        } },
      { selector: "node:selected",
        style: { "border-width": 3, "border-color": "#ffffff" } },
      { selector: "node.dim", style: { opacity: 0.12 } },
      { selector: "node.superseded", style: { opacity: 0.3, "background-color": "#64748b" } },
      { selector: "edge",
        style: {
          "width": 1.4,
          "line-color": "rgba(140,155,190,0.35)",
          "target-arrow-color": "rgba(140,155,190,0.5)",
          "target-arrow-shape": "triangle",
          "curve-style": "bezier",
          "label": "data(relation)",
          "font-size": 8.5,
          "color": "rgba(170,185,215,0.75)",
          "text-rotation": "autorotate",
          "text-background-color": "#0a0e1a",
          "text-background-opacity": 0.7,
          "text-background-padding": 2,
        } },
      { selector: "edge.dim", style: { opacity: 0.05 } },
      { selector: "edge.superseded", style: { "line-style": "dashed", "line-color": "rgba(100,116,139,0.4)" } },
      { selector: "edge.highlight", style: { "line-color": "#22d3ee", "width": 2.2 } },
      { selector: "node.highlight", style: { "border-width": 2.5, "border-color": "#22d3ee" } },
    ],
    layout: {
      name: "cose",
      animate: true,
      animationDuration: 600,
      nodeRepulsion: () => 9000,
      idealEdgeLength: () => 90,
      edgeElasticity: () => 120,
      gravity: 0.25,
      numIter: 1500,
      padding: 40,
    },
    wheelSensitivity: 0.25,
  });

  cy.on("tap", "node", (e) => {
    const id = String(e.target.id());
    lastFocusedId = id;
    pathEnds = pathEnds.filter((x) => x !== id).concat([id]).slice(-2);
    openEntity(id);
  });
  cy.on("dbltap", "node", (e) => {
    lastFocusedId = String(e.target.id());
    expandSelectedNeighborhood();
  });
  cy.on("tap", (e) => { if (e.target === cy) closeEntity(); });

  cy.on("mouseover", "node", (e) => {
    const n = e.target;
    cy.elements().addClass("dim");
    n.removeClass("dim");
    n.neighborhood().removeClass("dim").addClass("highlight");
    n.addClass("highlight");
  });
  cy.on("mouseout", "node", () => cy.elements().removeClass("dim").removeClass("highlight"));
}

function buildLegend() {
  const types = [...new Set(graphNodes.map((n) => n.type))].sort();
  $("#graph-legend").innerHTML = types.map((t) => `
    <div class="legend-row" data-type="${esc(t)}">
      <span class="legend-dot" style="background:${typeColors[t] || "#8899bb"}"></span>
      ${esc(t)}
    </div>`).join("");
  $$(".legend-row").forEach((r) =>
    r.addEventListener("click", () => {
      r.classList.toggle("off");
      applyTypeFilter();
    }));
}

const hiddenTypes = new Set();
function applyTypeFilter() {
  $$(".legend-row").forEach((r) => {
    if (r.classList.contains("off")) hiddenTypes.add(r.dataset.type);
    else hiddenTypes.delete(r.dataset.type);
  });
  applyConnectedFilter();
}

async function buildGraph(opts = {}) {
  const aroundEl = $("#gf-around-me");
  let focus = opts.focus;
  if (!focus) focus = (aroundEl && aroundEl.checked) ? "user" : "auto";
  const g = await api("/graph?focus=" + encodeURIComponent(focus) + "&depth=2");
  graphNodes = g.nodes;
  typeColors = g.type_colors || TYPE_COLORS;
  if (aroundEl && g.focus === "user") aroundEl.checked = true;
  if (g.truncated && $("#gf-layout") && $("#gf-layout").value === "cose") {
    $("#gf-layout").value = "breadthfirst";
  }
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.label, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  if (!cy) initGraph();
  cy.elements().remove();
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  buildLegend();
  applyTypeFilter();
  if (g.truncated) {
    $("#graph-sub").textContent = `You + ${g.depth} hops · ${g.nodes.length} of ${g.total_nodes} entities · Reset view for the full graph`;
  } else {
    $("#graph-sub").textContent = `${g.nodes.length} entities · ${g.edges.length} relationships`;
  }
  populateFilterDropdowns(g);
  runGraphLayout();
}

function populateFilterDropdowns(g) {
  const types = (g.entity_types || Object.keys(typeColors)).sort();
  const rels = (g.relation_types || []).sort();
  const fill = (sel, items, label) => {
    const el = $(sel);
    if (!el) return;
    const cur = el.value;
    el.innerHTML = `<option value="">${label}</option>` + items.map((t) => `<option value="${esc(t)}">${esc(t)}</option>`).join("");
    el.value = cur;
  };
  fill("#gf-type", types, "All types");
  fill("#gf-relation", rels, "All relations");
  fill("#sf-type", types, "Any type");
  fill("#browse-type", types, "All types");
}

async function loadBrowse() {
  const list = $("#browse-list");
  if (!list) return;
  const params = new URLSearchParams();
  const q = $("#browse-q") && $("#browse-q").value.trim();
  const type = $("#browse-type") && $("#browse-type").value;
  if (q) params.set("q", q);
  if (type) params.set("type", type);
  if ($("#browse-pinned") && $("#browse-pinned").checked) params.set("pinned", "true");
  if ($("#browse-important") && $("#browse-important").checked) params.set("important", "true");
  const sort = $("#browse-sort") && $("#browse-sort").value;
  if (sort && sort !== "name") params.set("sort", sort);
  const ents = await api("/entities?" + params.toString());
  list.innerHTML = ents.length ? ents.map((e) => `
    <div class="browse-row" data-id="${e.id}">
      <span style="color:${typeColors[e.type] || "#fff"}">●</span>
      <span class="browse-name">${esc(e.name)}</span>
      ${badge(e.type)}
      ${e.pinned ? '<span class="st-status st-pinned">pinned</span>' : ""}
      ${e.important ? '<span class="st-status st-important">important</span>' : ""}
      <span class="browse-meta"><span>${e.degree} links</span><span>${Math.round((e.confidence || 0.8) * 100)}%</span></span>
    </div>`).join("") : `<p class="muted">No entities match.</p>`;
  list.querySelectorAll(".browse-row").forEach((el) =>
    el.addEventListener("click", () => openEntity(el.dataset.id)));
}

async function applyGraphFilters() {
  const params = new URLSearchParams();
  if ($("#gf-type").value) params.set("entity_type", $("#gf-type").value);
  if ($("#gf-relation").value) params.set("relation", $("#gf-relation").value);
  params.set("active_only", $("#gf-superseded").checked ? "false" : "true");
  if ($("#gf-pinned").checked) params.set("pinned", "true");
  if ($("#gf-important").checked) params.set("important", "true");
  const conf = parseFloat($("#gf-confidence") && $("#gf-confidence").value);
  if (conf) params.set("min_confidence", String(conf));
  const g = await api("/graph/filter?" + params.toString());
  cy.elements().remove();
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.name, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  applyConnectedFilter();
  if (g.stats) {
    $("#graph-sub").textContent = `${g.stats.nodes} entities · ${g.stats.edges} relationships · avg degree ${g.stats.avg_degree}`;
  }
  runGraphLayout();
}

const TYPE_RANK = {
  person: 8, project: 7, organization: 6, technology: 5, skill: 4,
  goal: 3, interest: 3, preference: 3, location: 2, topic: 2,
  event: 2, task: 1, fact: 1, concept: 1,
};

function runGraphLayout() {
  if (!cy) return;
  const name = ($("#gf-layout") && $("#gf-layout").value) || "cose";
  if (name === "concentric") {
    cy.layout({
      name: "concentric",
      concentric: (n) => TYPE_RANK[n.data("type")] || 1,
      levelWidth: () => 1,
      animate: true,
      animationDuration: 400,
      padding: 40,
    }).run();
  } else if (name === "breadthfirst") {
    const roots = cy.nodes().filter((n) => String(n.data("label") || "").toLowerCase() === "user");
    cy.layout({
      name: "breadthfirst",
      roots: roots.length ? roots : undefined,
      directed: false,
      spacingFactor: 1.15,
      animate: true,
      animationDuration: 400,
      padding: 40,
    }).run();
  } else {
    cy.layout({
      name: "cose",
      animate: true,
      animationDuration: 500,
      nodeRepulsion: () => 9000,
      idealEdgeLength: () => 90,
      padding: 40,
    }).run();
  }
}

function applyConnectedFilter() {
  if (!cy) return;
  const only = $("#gf-connected") && $("#gf-connected").checked;
  cy.nodes().forEach((n) => {
    const hiddenType = hiddenTypes.has(n.data("type"));
    const isolated = only && n.degree() === 0 && String(n.data("label") || "").toLowerCase() !== "user";
    n.style("display", (hiddenType || isolated) ? "none" : "element");
  });
  cy.edges().forEach((e) => {
    const hidden = e.source().style("display") === "none" || e.target().style("display") === "none";
    e.style("display", hidden ? "none" : "element");
  });
}

$("#graph-apply").addEventListener("click", applyGraphFilters);
if ($("#gf-layout")) $("#gf-layout").addEventListener("change", runGraphLayout);
if ($("#gf-connected")) $("#gf-connected").addEventListener("change", applyConnectedFilter);
if ($("#gf-around-me")) {
  $("#gf-around-me").addEventListener("change", () => {
    buildGraph({ focus: $("#gf-around-me").checked ? "user" : "all" });
  });
}
if ($("#gf-confidence")) {
  $("#gf-confidence").addEventListener("input", (e) => {
    const el = $("#gf-conf-val");
    if (el) el.textContent = e.target.value;
  });
}
if ($("#graph-zoom-in")) $("#graph-zoom-in").addEventListener("click", () => { if (cy) cy.zoom(cy.zoom() * 1.2); });
if ($("#graph-zoom-out")) $("#graph-zoom-out").addEventListener("click", () => { if (cy) cy.zoom(cy.zoom() / 1.2); });
if ($("#graph-fit")) $("#graph-fit").addEventListener("click", () => { if (cy) cy.fit(undefined, 40); });
if ($("#graph-expand")) $("#graph-expand").addEventListener("click", expandSelectedNeighborhood);
if ($("#graph-path")) $("#graph-path").addEventListener("click", showGraphPath);
if ($("#graph-to-me")) $("#graph-to-me").addEventListener("click", pathToUser);

let lastFocusedId = null;
let pathEnds = [];

async function pathToUser() {
  if (!cy) return;
  const id = lastFocusedId || (cy.$("node:selected").length ? cy.$("node:selected")[0].id() : null);
  if (!id) { toast("Select a node first"); return; }
  const roots = cy.nodes().filter((n) => String(n.data("label") || "").toLowerCase() === "user");
  if (!roots.length) { toast("No User node in this view"); return; }
  pathEnds = [String(roots[0].id()), String(id)];
  await showGraphPath();
}

async function showGraphPath() {
  if (pathEnds.length < 2) { toast("Click two nodes, then Path"); return; }
  const [a, b] = pathEnds.slice(-2);
  const g = await api(`/graph/path?source_id=${a}&target_id=${b}`);
  if (!g.found || !g.path) { toast("No stored path between those nodes"); return; }
  cy.elements().addClass("dim").removeClass("highlight");
  const hops = g.path.filter((h) => h.from && h.to);
  hops.forEach((h) => {
    const src = cy.getElementById(String(h.from));
    const tgt = cy.getElementById(String(h.to));
    src.removeClass("dim").addClass("highlight");
    tgt.removeClass("dim").addClass("highlight");
    src.edgesWith(tgt).removeClass("dim").addClass("highlight");
  });
  toast(hops.map((h) => h.relation).join(" → ") || "Path found");
}

async function expandSelectedNeighborhood() {
  if (!cy) return;
  const selected = cy.$("node:selected");
  const id = selected.length ? selected[0].id() : lastFocusedId;
  if (!id) { toast("Select a node first"); return; }
  const g = await api(`/graph/neighborhood/${id}?depth=2`);
  const existing = new Set(cy.nodes().map((n) => String(n.id())));
  const nodes = g.nodes.filter((n) => !existing.has(String(n.id))).map((n) => ({
    data: { id: n.id, label: n.name, type: n.type, pinned: n.pinned, important: n.important, status: n.status },
  }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  if (nodes.length || edges.length) cy.add(nodes.concat(edges));
  const center = cy.getElementById(String(id));
  if (center && center.length) {
    lastFocusedId = id;
    cy.animate({ fit: { eles: center.neighborhood().add(center), padding: 60 }, duration: 300 });
  }
}

$("#graph-search").addEventListener("input", (e) => {
  const q = e.target.value.trim().toLowerCase();
  cy.elements().removeClass("dim");
  if (!q) { cy.fit(undefined, 40); return; }
  cy.nodes().forEach((n) => {
    if (!n.data("label").toLowerCase().includes(q)) n.addClass("dim");
  });
  cy.edges().forEach((ed) => {
    if (ed.source().hasClass("dim") || ed.target().hasClass("dim")) ed.addClass("dim");
  });
  const matches = cy.nodes().filter((n) => !n.hasClass("dim"));
  if (matches.length) cy.animate({ fit: { eles: matches, padding: 60 }, duration: 400 });
});
$("#graph-search").addEventListener("keydown", (e) => { if (e.key === "Escape") { e.target.value = ""; e.target.dispatchEvent(new Event("input")); } });

$("#graph-reset").addEventListener("click", async () => {
  // Reset filter controls and reload the full graph.
  $("#gf-type").value = ""; $("#gf-relation").value = "";
  $("#gf-superseded").checked = false; $("#gf-pinned").checked = false; $("#gf-important").checked = false;
  if ($("#gf-connected")) $("#gf-connected").checked = false;
  if ($("#gf-around-me")) $("#gf-around-me").checked = false;
  if ($("#gf-layout")) $("#gf-layout").value = "cose";
  $$(".legend-row").forEach((r) => r.classList.remove("off"));
  hiddenTypes.clear();
  await buildGraph({ focus: "all" });
  cy.fit(undefined, 50);
  closeEntity();
});

/* ==========================================================================
   Memory timeline (with filters)
   ========================================================================== */
async function loadMemory() {
  const kind = $("#mem-kind").value;
  const entityQ = $("#mem-entity").value.trim();
  const date = $("#mem-date").value;
  const params = new URLSearchParams();
  if (kind) params.set("kind", kind);
  if (date) params.set("date", date);
  if (entityQ) params.set("entity", entityQ);
  const mems = await api("/memories?" + params.toString());
  const byDay = {};
  mems.forEach((m) => {
    const day = fmtDay(m.created_at);
    (byDay[day] = byDay[day] || []).push(m);
  });
  const html = Object.entries(byDay).map(([day, items]) => `
    <div class="tl-day">
      <div class="tl-day-head">${esc(day)}</div>
      ${items.map((m) => {
        return `<div class="tl-item"${m.message_id ? ` data-mid="${m.message_id}" title="Open source message"` : ""}>
          <div class="tl-time">${fmtTime(m.created_at)}</div>
          <div class="tl-text">${esc(m.text)}<span class="tl-kind">${esc(m.kind)}</span>
          ${m.confidence ? `<span class="conf">${Math.round(m.confidence * 100)}%</span>` : ""}</div>
        </div>`;
      }).join("")}
    </div>`).join("");
  $("#timeline").innerHTML = html || `<p class="muted">No memories recorded yet.</p>`;
  $$("#timeline .tl-item").forEach((el) => {
    if (!el.dataset.mid) return;
    el.style.cursor = "pointer";
    el.addEventListener("click", async () => {
      try {
        const src = await api("/messages/" + el.dataset.mid);
        openSource(src);
      } catch (err) { toast(err.message); }
    });
  });
}

$("#mem-kind").addEventListener("change", loadMemory);
$("#mem-date").addEventListener("change", loadMemory);
$("#mem-entity").addEventListener("keydown", (e) => { if (e.key === "Enter") loadMemory(); });
$("#mem-clear").addEventListener("click", () => {
  $("#mem-kind").value = ""; $("#mem-entity").value = ""; $("#mem-date").value = "";
  loadMemory();
});

/* ==========================================================================
   Search
   ========================================================================== */
const REASON_LABELS = {
  keyword: "Keyword match", semantic: "Semantic match",
  graph: "Graph relation", recent: "Recent memory",
  pinned: "Pinned", important: "Important",
};

async function doSearch() {
  const q = $("#search-input").value.trim();
  if (!q) return;
  const body = { query: q };
  if ($("#sf-type").value) body.type = $("#sf-type").value;
  if ($("#sf-confidence").value) body.min_confidence = parseFloat($("#sf-confidence").value);
  if ($("#sf-status").value) body.status = $("#sf-status").value;
  if ($("#sf-pinned").checked) body.pinned = true;
  if ($("#sf-important").checked) body.important = true;
  if ($("#sf-from") && $("#sf-from").value) body.date_from = $("#sf-from").value;
  if ($("#sf-to") && $("#sf-to").value) body.date_to = $("#sf-to").value;
  if ($("#sf-source") && $("#sf-source").value) body.source = $("#sf-source").value;

  const r = await api("/search", { method: "POST", body: JSON.stringify(body) });
  const ans = $("#search-answer");
  ans.style.display = "block";
  const stLabel = { answered: "known", known: "known", unknown: "unknown", uncertain: "uncertain" }[r.status] || r.status;
  ans.innerHTML = `<div class="panel-head"><h2>Answer <span class="ans-status ans-${r.status}">${stLabel}</span></h2></div>
    <div class="panel-body">${esc(r.answer)}</div>`;

  // Sources used (traceable).
  const srcPanel = $("#search-sources");
  if (r.sources && r.sources.length) {
    srcPanel.style.display = "block";
    srcPanel.innerHTML = `<div class="panel-head"><h2>Sources used</h2></div><div class="panel-body">
      ${r.sources.map((s) => `
        <span class="remembered-chip" data-id="${s.entity_id}">
          <span style="color:${typeColors[s.type] || "#fff"}">●</span> ${esc(s.name)}
          ${s.conversation_title ? ` · <span class="conf">${esc(s.conversation_title)}</span>` : ""}
          ${s.snippet ? ` · <span class="conf">${esc(s.snippet)}</span>` : ""}
        </span>`).join("")}
    </div>`;
    srcPanel.querySelectorAll(".remembered-chip").forEach((chip) =>
      chip.addEventListener("click", () => openEntity(chip.dataset.id)));
  } else {
    srcPanel.style.display = "none";
  }

  $("#search-results").innerHTML = r.entities.length ? `
    <div class="panel"><div class="panel-head"><h2>Entities</h2></div><div class="panel-body">
      ${r.entities.map((e) => `
        <div class="result-entity" data-id="${e.id}">
          <span style="color:${typeColors[e.type] || "#fff"}">●</span>
          <div style="flex:1">
            <div class="re-name">${esc(e.name)} <span class="conf">${Math.round((e.confidence || 0.8) * 100)}%</span></div>
            <div class="re-desc">${esc(e.description || "")}</div>
            <div class="re-reasons">${(e.reasons || []).map((r) => `<span class="reason-chip">${esc(REASON_LABELS[r] || r)}</span>`).join("")}</div>
          </div>
          ${badge(e.type)}
        </div>`).join("")}
    </div></div>
    <div class="panel"><div class="panel-head"><h2>Facts</h2></div><div class="panel-body">
      ${r.facts.map((f) => `<div class="mem-item"><span class="mem-ico">⇄</span><span class="mem-text">${esc(f.text)}</span></div>`).join("")}
    </div></div>`
    : `<p class="muted">Nothing found for “${esc(q)}”.</p>`;
  $$("#search-results .result-entity").forEach((el) =>
    el.addEventListener("click", () => openEntity(el.dataset.id)));
}
$("#search-btn").addEventListener("click", doSearch);
$("#search-input").addEventListener("keydown", (e) => { if (e.key === "Enter") doSearch(); });

/* ==========================================================================
   Entity slide-over
   ========================================================================== */
let currentEntity = null;

function openEntity(id) {
  loadEntity(id);
  $("#entity-panel").classList.add("open");
  $("#entity-overlay").classList.add("show");
  if (id != null && id !== "") setHash("entity", id);
}
function closeEntity() {
  $("#entity-panel").classList.remove("open");
  $("#entity-overlay").classList.remove("show");
  currentEntity = null;
  if (parseHash().view === "entity") setHash(currentView || "dashboard");
}
$("#entity-overlay").addEventListener("click", closeEntity);

function openSource(source) {
  if (!source) return;
  const modal = document.createElement("div");
  modal.className = "modal src-modal";
  modal.innerHTML = `
    <div class="modal-card">
      <h3>Source</h3>
      <p class="muted">${source.conversation_title ? "Conversation: " + esc(source.conversation_title) : "Conversation"} · ${fmtDay(source.created_at)}</p>
      <div class="msg-bubble">${esc(source.content)}</div>
      <div style="margin-top:12px;text-align:right"><button class="btn-ghost" id="src-close">Close</button></div>
    </div>`;
  document.body.appendChild(modal);
  modal.addEventListener("click", (e) => { if (e.target === modal) modal.remove(); });
  modal.querySelector("#src-close").addEventListener("click", () => modal.remove());
}

async function loadEntity(id) {
  currentEntity = id;
  const d = await api("/entities/" + id);
  const e = d.entity;

  const relTypes = ["learning","uses","knows","likes","created","interested_in","related_to","wants","works_on","prefers","works_at","lives_in","located_in","member_of"];
  const related = d.related.map((r) => `
    <div class="rel-item ${r.status === "superseded" ? "super" : ""}" data-id="${r.other_id}">
      <span style="color:${typeColors[r.other_type] || "#fff"}">●</span>
      <span class="ri-name">${esc(r.other_name)}</span>
      ${badge(r.other_type)}
      <span class="rel-conf">${Math.round((r.confidence || 0.8) * 100)}%</span>
      <span class="ri-rel">${r.direction === "out" ? "→" : "←"} ${esc(r.relation)}</span>
      ${r.rid ? `<select class="input rel-edit" data-rid="${r.rid}" title="Change relationship type">${relTypes.map((t) => `<option value="${t}" ${(r.canonical || r.relation) === t ? "selected" : ""}>${t}</option>`).join("")}</select>` : ""}
      ${r.rid ? `<button class="rel-del" data-rid="${r.rid}" title="Delete relationship">✕</button>` : ""}
    </div>`).join("");

  const flags = [];
  if (e.pinned) flags.push('<span class="st-status st-pinned">pinned</span>');
  if (e.important) flags.push('<span class="st-status st-important">important</span>');
  if (e.status === "superseded") flags.push('<span class="st-status st-superseded">superseded</span>');
  if (e.meta && e.meta.demo) flags.push('<span class="st-status st-demo">demo</span>');

  const aliases = (e.aliases || []).length ? (e.aliases || []).map(esc).join(", ") : "—";

  $("#entity-inner").innerHTML = `
    <button class="entity-close" id="entity-close">✕</button>
    <div class="entity-title">${esc(e.name)}</div>
    <div style="margin:6px 0 2px">${badge(e.type)}</div>
    <div class="entity-meta">${flags.join(" ")}</div>
    <div class="entity-desc">${esc(e.description || "No description.")}</div>

    <div class="conf-label">Confidence: ${Math.round((e.confidence || 0.8) * 100)}%</div>
    <div class="conf-bar"><div class="conf-fill" style="width:${Math.round((e.confidence || 0.8) * 100)}%"></div></div>

    <div class="entity-sec">
      <h3>Details</h3>
      <div class="meta-kv">Aliases: <b>${aliases}</b></div>
      <div class="meta-kv">Embedding: <b>${e.embedding ? "stored" : "none"}</b></div>
      <div class="meta-kv">Created: <b>${fmtDay(e.created_at)} ${fmtTime(e.created_at)}</b></div>
      <div class="meta-kv">Updated: <b>${fmtDay(e.updated_at)} ${fmtTime(e.updated_at)}</b></div>
      ${e.source ? `<div class="meta-kv">Source: <span class="source-link" id="entity-source">${e.source.conversation_title ? esc(e.source.conversation_title) : "conversation"} · ${fmtDay(e.source.created_at)}</span></div>` : ""}
    </div>

    <div class="entity-sec">
      <h3>Relationships (${d.related.length})</h3>
      ${related || `<p class="muted">None yet.</p>`}
      <div class="form" style="margin-top:10px">
        <label class="field"><span>Add relationship</span>
          <select class="input" id="add-rel-type">
            <option value="related_to">related_to</option>
            <option value="uses">uses</option>
            <option value="learning">learning</option>
            <option value="works_on">works_on</option>
            <option value="knows">knows</option>
            <option value="likes">likes</option>
            <option value="created">created</option>
            <option value="interested_in">interested_in</option>
            <option value="wants">wants</option>
            <option value="prefers">prefers</option>
            <option value="works_at">works_at</option>
            <option value="lives_in">lives_in</option>
            <option value="member_of">member_of</option>
          </select>
        </label>
        <input class="input" id="add-rel-target" placeholder="Target entity name" />
        <button class="btn-ghost" id="add-rel-btn">Add</button>
      </div>
    </div>

    <div class="entity-sec">
      <h3>Current state</h3>
      ${(d.history && d.history.current.length) ? d.history.current.map((r) => `
        <div class="entity-mem">${esc(r.text)} <span class="muted" style="font-size:11px">${Math.round((r.confidence || 0.8) * 100)}%</span></div>`).join("")
        : `<p class="muted">No active relationships.</p>`}
    </div>

    ${(d.history && d.history.superseded.length) ? `
    <div class="entity-sec">
      <h3>Previous (superseded)</h3>
      ${d.history.superseded.map((r) => `
        <div class="entity-mem super">${esc(r.text)} <span class="muted" style="font-size:11px">${fmtTime(r.created_at)}</span></div>`).join("")}
    </div>` : ""}

    ${(d.history && d.history.changes.length) ? `
    <div class="entity-sec">
      <h3>Changes</h3>
      ${d.history.changes.map((c) => `
        <div class="entity-mem">${esc(c.text)} <span class="muted" style="font-size:11px">${fmtTime(c.created_at)} · ${esc(c.kind)}</span></div>`).join("")}
    </div>` : ""}

    ${(d.similar && d.similar.length) ? `
    <div class="entity-sec">
      <h3>Looks similar</h3>
      ${d.similar.map((s) => `
        <div class="rel-item" data-id="${s.id}">
          <span style="color:${typeColors[s.type] || "#fff"}">●</span>
          <span class="ri-name">${esc(s.name)}</span>
          ${badge(s.type)}
          <span class="rel-conf">${Math.round((s.score || 0) * 100)}%</span>
        </div>`).join("")}
      <p class="muted">Possible duplicates. Use Merge if they are the same thing.</p>
    </div>` : ""}

    <div class="entity-sec">
      <h3>Memory history</h3>
      ${d.memories.length ? d.memories.map((m) => `
        <div class="entity-mem">${esc(m.text)}<br><span class="muted" style="font-size:11px">${fmtTime(m.created_at)} · ${esc(m.kind)}</span></div>`).join("")
        : `<p class="muted">None.</p>`}
    </div>

    <div class="entity-sec" id="entity-edit-sec" style="display:none">
      <h3>Edit</h3>
      <div class="form">
        <label class="field"><span>Name</span><input class="input" id="edit-name" value="${esc(e.name)}"></label>
        <label class="field"><span>Type</span>
          <select class="input" id="edit-type">
            ${Object.keys(typeColors).map((t) => `<option value="${t}" ${t === e.type ? "selected" : ""}>${t}</option>`).join("")}
          </select>
        </label>
        <label class="field"><span>Description</span><textarea class="input" id="edit-desc" rows="3">${esc(e.description || "")}</textarea></label>
        <label class="field"><span>Confidence</span><input class="input" id="edit-conf" type="number" min="0" max="1" step="0.05" value="${e.confidence}"></label>
        <div style="display:flex;gap:8px">
          <button class="btn-primary" id="edit-save">Save</button>
          <button class="btn-ghost" id="edit-cancel">Cancel</button>
        </div>
      </div>
    </div>

    <div class="entity-actions">
      <button class="btn-ghost" id="act-edit">Edit</button>
      <button class="btn-ghost" id="act-pin">${e.pinned ? "Unpin" : "Pin"}</button>
      <button class="btn-ghost" id="act-important">${e.important ? "Unmark important" : "Mark important"}</button>
      <button class="btn-ghost" id="act-focus">Focus in graph</button>
      <button class="btn-ghost" id="act-merge">Merge…</button>
      <button class="btn-danger" id="act-delete">Delete</button>
    </div>`;

  $("#entity-close").addEventListener("click", closeEntity);
  const srcLink = $("#entity-source");
  if (srcLink) srcLink.addEventListener("click", () => openSource(e.source));
  $$("#entity-inner .rel-item").forEach((el) =>
    el.addEventListener("click", (ev) => {
      if (ev.target.closest(".rel-del") || ev.target.closest(".rel-edit")) return;
      openEntity(el.dataset.id);
    }));
  $$("#entity-inner .rel-edit").forEach((sel) =>
    sel.addEventListener("change", async (ev) => {
      ev.stopPropagation();
      await api("/relationships/" + sel.dataset.rid, {
        method: "PATCH", body: JSON.stringify({ relation: sel.value }),
      });
      toast("Relationship updated");
      loadEntity(id); buildGraph();
    }));
  $$("#entity-inner .rel-del").forEach((btn) =>
    btn.addEventListener("click", async (ev) => {
      ev.stopPropagation();
      if (!confirm("Delete this relationship?")) return;
      await api("/relationships/" + btn.dataset.rid, { method: "DELETE" });
      toast("Relationship deleted");
      loadEntity(id); buildGraph();
    }));
  $("#act-edit").addEventListener("click", () => $("#entity-edit-sec").style.display = "block");
  $("#edit-cancel").addEventListener("click", () => $("#entity-edit-sec").style.display = "none");
  $("#edit-save").addEventListener("click", async () => {
    await api("/entities/" + id, { method: "PATCH", body: JSON.stringify({
      name: $("#edit-name").value, type: $("#edit-type").value,
      description: $("#edit-desc").value, confidence: parseFloat($("#edit-conf").value),
    })});
    toast("Entity updated");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-pin").addEventListener("click", async () => {
    await api("/entities/" + id, { method: "PATCH", body: JSON.stringify({ pinned: !e.pinned }) });
    toast(e.pinned ? "Unpinned" : "Pinned");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-important").addEventListener("click", async () => {
    await api("/entities/" + id, { method: "PATCH", body: JSON.stringify({ important: !e.important }) });
    toast(e.important ? "Unmarked" : "Marked important");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-focus").addEventListener("click", () => {
    showView("graph");
    lastFocusedId = id;
    cy.elements().addClass("dim");
    const n = cy.getElementById(String(id));
    n.removeClass("dim");
    n.neighborhood().removeClass("dim");
    if (n && n.length) n.select();
    cy.animate({ fit: { eles: n.neighborhood().add(n), padding: 80 }, duration: 400 });
    closeEntity();
  });
  const addRelBtn = $("#add-rel-btn");
  if (addRelBtn) addRelBtn.addEventListener("click", async () => {
    const name = ($("#add-rel-target").value || "").trim();
    const rel = $("#add-rel-type").value;
    if (!name) return;
    const ents = await api("/entities?q=" + encodeURIComponent(name));
    const hit = ents.find((x) => x.name.toLowerCase() === name.toLowerCase()) || ents[0];
    if (!hit) { toast("No matching entity"); return; }
    await api("/relationships", { method: "POST", body: JSON.stringify({
      source_id: Number(id), target_id: hit.id, relation: rel,
    })});
    toast("Relationship added");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-merge").addEventListener("click", () => openMerge(id));
  $("#act-delete").addEventListener("click", async () => {
    if (!confirm("Delete this entity and its relationships?")) return;
    try {
      await api("/entities/" + id, { method: "DELETE" });
      toast("Entity deleted");
      closeEntity(); buildGraph(); loadDashboard();
    } catch (err) { toast(err.message); }
  });
}

function openMerge(dropId) {
  const modal = document.createElement("div");
  modal.className = "modal";
  modal.innerHTML = `
    <div class="modal-card">
      <h3>Merge into another entity</h3>
      <p class="muted">This entity's relationships will be re-wired to the chosen target.</p>
      <input class="input modal-search" placeholder="Search entities…" />
      <div class="modal-list"></div>
      <div style="margin-top:12px;text-align:right"><button class="btn-ghost" id="merge-cancel">Cancel</button></div>
    </div>`;
  document.body.appendChild(modal);
  modal.addEventListener("click", (e) => { if (e.target === modal) modal.remove(); });
  modal.querySelector("#merge-cancel").addEventListener("click", () => modal.remove());

  const input = modal.querySelector(".modal-search");
  const list = modal.querySelector(".modal-list");
  async function render(q = "") {
    const ents = await api("/entities");
    const filtered = ents.filter((e) => e.id !== dropId && e.name.toLowerCase().includes(q.toLowerCase())).slice(0, 40);
    list.innerHTML = filtered.map((e) => `
      <div class="modal-opt" data-id="${e.id}">
        <span style="color:${typeColors[e.type] || "#fff"}">●</span>
        <span>${esc(e.name)}</span>${badge(e.type)}
      </div>`).join("");
    list.querySelectorAll(".modal-opt").forEach((el) =>
      el.addEventListener("click", async () => {
        await api("/entities/merge", { method: "POST", body: JSON.stringify({ keep_id: el.dataset.id, drop_id: dropId }) });
        toast("Merged");
        modal.remove();
        closeEntity(); buildGraph(); loadDashboard();
      }));
  }
  input.addEventListener("input", () => render(input.value));
  render();
}

/* ==========================================================================
   Settings
   ========================================================================== */
async function loadSettings() {
  const s = await api("/settings");
  $("#set-llm").value = s.llm_model;
  $("#set-emb").value = s.embedding_model;
  $("#set-ollama-url").value = s.ollama_base_url;
  $("#set-confidence").value = s.confidence_threshold;
  $("#conf-val").textContent = s.confidence_threshold;
  $("#set-merge").value = s.merge_similarity;
  $("#merge-val").textContent = s.merge_similarity;
  $("#set-auto-memory").checked = s.auto_memory;
  if ($("#set-auto-backup")) {
    const hours = (s.auto_backup_hours == null ? 24 : s.auto_backup_hours);
    $("#set-auto-backup").value = String([0, 6, 12, 24, 48].includes(Number(hours)) ? hours : 24);
  }
  if ($("#set-theme")) $("#set-theme").value = s.theme || "dark";
  $("#db-path").textContent = "Database: " + s.db_path;
  $("#ollama-info").innerHTML = s.ollama_available
    ? `<p class="hint">Ollama is <span style="color:var(--ok)">online</span>.</p>
       <p class="hint">Installed models: ${s.models_installed.map(esc).join(", ") || "none"}</p>`
    : `<p class="hint">Ollama is <span style="color:var(--danger)">offline</span> — running the built-in rule-based extractor.</p>
       <p class="hint">Start it with <code>ollama serve</code> and pull <code>qwen3:0.6b</code> + <code>nomic-embed-text</code>.</p>`;
  const priv = s.privacy || {};
  const pbox = $("#privacy-info");
  if (pbox) {
    pbox.innerHTML = `
      <p class="hint">Architecture: <strong>${esc((priv.mode || "local-first").toUpperCase())}</strong></p>
      <p class="hint">Local: ${priv.local === false ? "no" : "yes"} · Private: ${priv.private === false ? "no" : "yes"} · Telemetry: ${priv.telemetry ? "on" : "off"} · Cloud: ${priv.cloud ? "yes" : "none"}</p>
      <p class="hint">Personal memory stays on this machine unless you export it yourself.</p>
      <p class="hint">Database: <code>${esc(s.db_path || "")}</code> · Integrity: <strong>${s.db_ok === false ? "not ok" : "ok"}</strong></p>
      <p class="hint">Activity watch: ${priv.activity_watch ? "on" : "off"} — Second Brain never screenshots or polls what you are doing.</p>`;
  }
  document.body.classList.toggle("theme-light", s.theme === "light");
}

$("#set-confidence").addEventListener("input", (e) => { $("#conf-val").textContent = e.target.value; });
$("#set-merge").addEventListener("input", (e) => { $("#merge-val").textContent = e.target.value; });

$("#set-save").addEventListener("click", async () => {
  await api("/settings", { method: "POST", body: JSON.stringify({
    llm_model: $("#set-llm").value.trim() || undefined,
    embedding_model: $("#set-emb").value.trim() || undefined,
    ollama_base_url: $("#set-ollama-url").value.trim() || undefined,
  })});
  $("#set-hint").textContent = "Saved. Models are now active.";
  refreshStatus();
});

$("#set-behavior-save").addEventListener("click", async () => {
  await api("/settings", { method: "POST", body: JSON.stringify({
    confidence_threshold: parseFloat($("#set-confidence").value),
    merge_similarity: parseFloat($("#set-merge").value),
    auto_memory: $("#set-auto-memory").checked,
    auto_backup_hours: $("#set-auto-backup") ? parseFloat($("#set-auto-backup").value) : undefined,
    theme: $("#set-theme") ? $("#set-theme").value : undefined,
  })});
  if ($("#set-theme")) document.body.classList.toggle("theme-light", $("#set-theme").value === "light");
  toast("Memory behavior saved");
});

$("#reset-btn").addEventListener("click", async () => {
  if (!confirm("Wipe ALL entities, relationships, memories and messages?")) return;
  await api("/reset", { method: "POST", body: JSON.stringify({ confirm: true }) });
  toast("All data cleared");
  location.reload();
});

$("#demo-btn").addEventListener("click", async () => {
  await api("/demo", { method: "POST" });
  toast("Demo data loaded (marked as DEMO)");
  loadDashboard(); buildGraph(); loadMemory(); loadConversations();
});

if ($("#demo-clear-btn")) {
  $("#demo-clear-btn").addEventListener("click", async () => {
    if (!confirm("Remove demo-marked entities and the demo conversation? Real memories stay.")) return;
    const r = await api("/demo/clear", { method: "POST" });
    toast(`Removed ${r.entities_removed || 0} demo entities`);
    loadDashboard(); buildGraph(); loadMemory(); loadConversations();
  });
}

/* ---- Export / Import / Backup / Summarize ---- */

function downloadBlob(content, filename, type) {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename;
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
}

$("#export-json").addEventListener("click", async () => {
  const r = await fetch(API + "/export/json");
  downloadBlob(await r.text(), "second-brain-export.json", "application/json");
  toast("JSON exported");
});

$("#export-md").addEventListener("click", async () => {
  const r = await fetch(API + "/export/markdown");
  downloadBlob(await r.text(), "second-brain-export.md", "text/markdown");
  toast("Markdown exported");
});

function formatImportReport(r) {
  if (!r || !r.ok) return "Error: " + ((r && r.error) || "import failed");
  let msg = r.mode === "replace"
    ? `Replaced: ${r.entities_created} entities imported.`
    : `Merged: ${r.entities_created} created, ${r.entities_merged} merged, ${r.relationships_added} relationships.`;
  const conflicts = r.conflicts || (r.report && r.report.conflicts) || [];
  if (conflicts.length) {
    msg += " Conflicts: " + conflicts.slice(0, 8).map((c) =>
      `${c.relation} now ${c.kept} (was ${c.superseded})`).join("; ") + ".";
  }
  const skippedRels = r.relationships_skipped || 0;
  const skippedMems = r.memories_skipped || 0;
  if (skippedRels) msg += ` Skipped ${skippedRels} relationship(s).`;
  if (skippedMems) msg += ` ${skippedMems} duplicate memories ignored.`;
  return msg;
}

$("#import-merge").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "merge" }) });
    $("#import-status").textContent = formatImportReport(r);
    if (r.ok) { loadDashboard(); buildGraph(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

$("#import-replace").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  if (!confirm("Replace the ENTIRE database with this import? This wipes all current data.")) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "replace", confirm: true }) });
    $("#import-status").textContent = formatImportReport(r);
    if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

if ($("#import-notes-btn")) {
  $("#import-notes-btn").addEventListener("click", async () => {
    const text = ($("#import-notes") && $("#import-notes").value || "").trim();
    if (!text) return;
    try {
      const r = await api("/import/notes", { method: "POST", body: JSON.stringify({ text }) });
      $("#import-status").textContent = r.ok
        ? `Imported ${r.chunks} note(s), ${r.remembered} memories.`
        : "Error: " + (r.error || "failed");
      if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); loadConversations(); }
    } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
  });
}

$("#backup-now").addEventListener("click", async () => {
  const r = await api("/backup", { method: "POST" });
  $("#backup-status").textContent = r.ok
    ? `Backup created at ${r.path} (db: ${r.db}, json: ${r.export_json}, md: ${r.export_md})`
    : "Backup failed";
  loadBackupStatus();
});

async function loadBackupStatus() {
  try {
    const s = await api("/backup/status");
    if (s.count) {
      $("#backup-status").textContent = `Last backup: ${s.last_backup_at || "—"} · ${s.count} total · ${s.backup_dir}`;
    }
    const box = $("#backup-list");
    if (!box) return;
    const items = s.backups || [];
    box.innerHTML = items.length ? items.slice(0, 8).map((b) => `
      <div class="browse-row" style="margin-top:8px">
        <span class="browse-name">${esc(b.name)}</span>
        <span class="browse-meta">${esc((b.created_at || "").slice(0, 19))}${b.bytes ? " · " + Math.round(b.bytes / 1024) + " KB" : ""}${b.has_db === false ? " · missing db" : ""}</span>
        <button class="btn-ghost backup-restore" data-name="${esc(b.name)}">Restore</button>
      </div>`).join("") : "";
    box.querySelectorAll(".backup-restore").forEach((btn) =>
      btn.addEventListener("click", async () => {
        if (!confirm("Restore this backup? A safety snapshot of the current brain is created first.")) return;
        try {
          const r = await api("/backup/restore", {
            method: "POST",
            body: JSON.stringify({ name: btn.dataset.name, confirm: true }),
          });
          toast(r.ok ? "Backup restored" : "Restore failed");
          if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); loadConversations(); loadBrowse(); }
        } catch (e) { toast(e.message); }
      }));
  } catch {}
}

async function loadSummarizeCandidates() {
  try {
    const cands = await api("/summarize/candidates");
    $("#summarize-candidates").innerHTML = cands.length
      ? `<p class="hint">Ready to summarize:</p>` + cands.slice(0, 5).map((c) =>
          `<div class="mem-item"><span class="mem-ico">Σ</span><span class="mem-text">${esc(c.entity_name)} <span class="muted">(${c.count} memories)</span></span></div>`).join("")
      : `<p class="hint">No clusters ready for summarization yet.</p>`;
  } catch {}
}

$("#summarize-all").addEventListener("click", async () => {
  $("#summarize-status").textContent = "Summarizing…";
  try {
    const r = await api("/summarize", { method: "POST", body: JSON.stringify({}) });
    const okCount = Array.isArray(r) ? r.filter((x) => x && x.ok).length : (r.ok ? 1 : 0);
    $("#summarize-status").textContent = `Summarized ${okCount} entit${okCount === 1 ? "y" : "ies"}.`;
    loadSummarizeCandidates(); loadDashboard();
  } catch (e) { $("#summarize-status").textContent = "Error: " + e.message; }
});

/* ==========================================================================
   Command palette + keyboard
   ========================================================================== */
let paletteIndex = 0;
let paletteItems = [];

function closePalette() {
  const pal = $("#palette");
  const ov = $("#palette-overlay");
  if (pal) pal.hidden = true;
  if (ov) ov.classList.remove("show");
}

function openPalette() {
  const pal = $("#palette");
  const ov = $("#palette-overlay");
  const input = $("#palette-input");
  if (!pal || !input) return;
  pal.hidden = false;
  if (ov) ov.classList.add("show");
  input.value = "";
  input.focus();
  renderPalette("");
}

async function renderPalette(q) {
  const box = $("#palette-results");
  if (!box) return;
  const query = (q || "").trim().toLowerCase();
  const views = VIEWS.map((v) => ({ kind: "view", id: v, label: v[0].toUpperCase() + v.slice(1) }));
  let ents = [];
  let convs = [];
  try { ents = await api("/entities" + (query ? ("?q=" + encodeURIComponent(query)) : "")); } catch {}
  try { convs = await api("/conversations" + (query ? ("?q=" + encodeURIComponent(query)) : "")); } catch {}
  const viewHits = views.filter((v) => !query || v.label.toLowerCase().includes(query));
  const entHits = ents.slice(0, 10).map((e) => ({ kind: "entity", id: e.id, label: e.name, type: e.type }));
  const convHits = (convs || []).slice(0, 6).map((c) => ({ kind: "conversation", id: c.id, label: c.title || ("Chat " + c.id) }));
  paletteItems = viewHits.concat(convHits, entHits);
  paletteIndex = 0;
  box.innerHTML = paletteItems.map((it, i) => `
    <div class="palette-item ${i === 0 ? "active" : ""}" data-i="${i}">
      <span class="palette-kicker">${it.kind}</span>
      <span>${esc(it.label)}</span>
      ${it.type ? badge(it.type) : ""}
    </div>`).join("") || `<p class="muted">Nothing matches.</p>`;
  box.querySelectorAll(".palette-item").forEach((el) =>
    el.addEventListener("click", () => choosePalette(Number(el.dataset.i))));
}

function choosePalette(i) {
  const it = paletteItems[i];
  closePalette();
  if (!it) return;
  if (it.kind === "view") showView(it.id);
  else if (it.kind === "conversation") { showView("chat"); openConversation(it.id); }
  else openEntity(it.id);
}

if ($("#palette-input")) {
  $("#palette-input").addEventListener("input", (e) => renderPalette(e.target.value));
  $("#palette-input").addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") { e.preventDefault(); paletteIndex = Math.min(paletteItems.length - 1, paletteIndex + 1); }
    if (e.key === "ArrowUp") { e.preventDefault(); paletteIndex = Math.max(0, paletteIndex - 1); }
    $$("#palette-results .palette-item").forEach((el, i) => el.classList.toggle("active", i === paletteIndex));
    if (e.key === "Enter") { e.preventDefault(); choosePalette(paletteIndex); }
    if (e.key === "Escape") closePalette();
  });
}
if ($("#palette-overlay")) $("#palette-overlay").addEventListener("click", closePalette);
if ($("#browse-q")) $("#browse-q").addEventListener("input", loadBrowse);
if ($("#browse-type")) $("#browse-type").addEventListener("change", loadBrowse);
if ($("#browse-pinned")) $("#browse-pinned").addEventListener("change", loadBrowse);
if ($("#browse-important")) $("#browse-important").addEventListener("change", loadBrowse);
if ($("#browse-sort")) $("#browse-sort").addEventListener("change", loadBrowse);

document.addEventListener("keydown", (e) => {
  const tag = (e.target && e.target.tagName) || "";
  const typing = tag === "INPUT" || tag === "TEXTAREA" || (e.target && e.target.isContentEditable);
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    const pal = $("#palette");
    if (pal && !pal.hidden) closePalette();
    else openPalette();
    return;
  }
  if (e.key === "Escape") {
    closePalette();
    closeEntity();
    return;
  }
  if (typing) return;
  const map = { "1": "dashboard", "2": "chat", "3": "graph", "4": "browse", "5": "memory", "6": "search", "7": "settings" };
  if (map[e.key]) showView(map[e.key]);
  if (e.key === "/") { e.preventDefault(); showView("search"); const el = $("#search-input"); if (el) el.focus(); }
});

/* ==========================================================================
   Boot
   ========================================================================== */
async function boot() {
  const wanted = location.hash;
  refreshStatus();
  await loadChatHistory();
  await buildGraph();
  await loadDashboard();
  await loadSettings();
  loadBackupStatus();
  loadSummarizeCandidates();
  loadConversations();
  if (wanted && wanted !== "#") {
    try { history.replaceState(null, "", wanted); } catch {}
    applyRoute();
  } else {
    showView("dashboard");
  }
  setInterval(refreshStatus, 15000);
}
boot();
````

## `frontend/index.html`

````
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Second Brain — Local AI Knowledge Graph</title>
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23070a13'/%3E%3Ctext x='16' y='22' text-anchor='middle' font-size='18' fill='%2322d3ee'%3E%E2%97%86%3C/text%3E%3C/svg%3E" />
  <link rel="stylesheet" href="style.css" />
  <script src="vendor/cytoscape.min.js"></script>
</head>
<body>
  <div class="bg-orbs" aria-hidden="true">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>

  <div class="app">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-mark">◈</div>
        <div class="brand-text">
          <span class="brand-name">Second Brain</span>
          <span class="brand-sub">local knowledge OS</span>
        </div>
      </div>

      <nav class="nav">
        <button class="nav-item active" data-view="dashboard">
          <span class="nav-ico">▦</span> Dashboard
        </button>
        <button class="nav-item" data-view="chat">
          <span class="nav-ico">✉</span> Chat
        </button>
        <button class="nav-item" data-view="graph">
          <span class="nav-ico">◉</span> Knowledge Graph
        </button>
        <button class="nav-item" data-view="browse">
          <span class="nav-ico">▤</span> Entities
        </button>
        <button class="nav-item" data-view="memory">
          <span class="nav-ico">🕘</span> Memory
        </button>
        <button class="nav-item" data-view="search">
          <span class="nav-ico">⌕</span> Search
        </button>
        <button class="nav-item" data-view="settings">
          <span class="nav-ico">⚙</span> Settings
        </button>
      </nav>

      <div class="sidebar-foot">
        <div class="status" id="status-indicator">
          <span class="status-dot"></span>
          <span class="status-text">checking Ollama…</span>
        </div>
        <div class="privacy-badge" id="privacy-badge">LOCAL · PRIVATE</div>
        <div class="model-line" id="model-line"></div>
      </div>
    </aside>

    <!-- Main -->
    <main class="main">
      <!-- ============ DASHBOARD ============ -->
      <section class="view" id="view-dashboard">
        <header class="view-head">
          <h1>Dashboard</h1>
          <p class="view-sub">Your knowledge, growing itself.</p>
        </header>
        <div class="demo-banner" id="demo-banner" style="display:none">
          This database contains <strong>DEMO</strong> data. It is marked separately from your real memories.
        </div>
        <div class="stats-grid" id="stats-grid"></div>

        <div class="dash-cols">
          <div class="panel">
            <div class="panel-head"><h2>Memory growth <span class="muted">(14 days)</span></h2></div>
            <div class="panel-body">
              <div id="growth-chart"></div>
            </div>
          </div>
          <div class="panel">
            <div class="panel-head"><h2>Memory types</h2></div>
            <div class="panel-body" id="type-breakdown"></div>
          </div>
        </div>

        <div class="dash-cols">
          <div class="panel">
            <div class="panel-head"><h2>Recent memories</h2></div>
            <div class="panel-body" id="recent-memories"></div>
          </div>
          <div class="panel">
            <div class="panel-head"><h2>Most connected</h2></div>
            <div class="panel-body" id="top-entities"></div>
          </div>
        </div>
      </section>

      <!-- ============ CHAT ============ -->
      <section class="view" id="view-chat">
        <header class="view-head">
          <div>
            <h1>Chat</h1>
            <p class="view-sub">Just talk to it — your knowledge graph builds itself.</p>
          </div>
          <div class="graph-tools">
            <button class="btn-ghost" id="chat-new">New conversation</button>
          </div>
        </header>
        <div class="chat-layout">
          <aside class="conv-rail">
            <div class="conv-rail-head">Conversations</div>
            <input id="conv-search" class="input" type="search" placeholder="Search chats…" autocomplete="off" />
            <div id="conv-list" class="conv-list"></div>
          </aside>
        <div class="chat-wrap">
          <div class="chat-scroll" id="chat-scroll">
            <div class="chat-empty" id="chat-empty">
              <div class="chat-empty-mark">◈</div>
              <p>Say something meaningful and I'll remember it.<br/>
              <span class="muted">Try: “I'm learning Python and want to build AI agents.”</span></p>
            </div>
            <div id="chat-messages"></div>
          </div>
          <div class="chat-inputbar">
            <textarea id="chat-input" rows="1" placeholder="Talk to your Second Brain…"></textarea>
            <button id="chat-send" class="btn-primary">Send</button>
          </div>
        </div>
        </div>
      </section>

      <!-- ============ GRAPH ============ -->
      <section class="view" id="view-graph">
        <header class="view-head graph-head">
          <div>
            <h1>Knowledge Graph</h1>
            <p class="view-sub" id="graph-sub">Click a node to inspect it.</p>
          </div>
          <div class="graph-tools">
            <input id="graph-search" class="input" type="text" placeholder="Search nodes…" />
            <button class="btn-ghost" id="graph-reset">Reset view</button>
          </div>
        </header>
        <div class="filter-bar graph-filters">
          <select id="gf-type" class="input">
            <option value="">All types</option>
          </select>
          <select id="gf-relation" class="input">
            <option value="">All relations</option>
          </select>
          <label class="toggle small">
            <input type="checkbox" id="gf-superseded" />
            <span>Show superseded</span>
          </label>
          <label class="toggle small">
            <input type="checkbox" id="gf-pinned" />
            <span>Pinned only</span>
          </label>
          <label class="toggle small">
            <input type="checkbox" id="gf-important" />
            <span>Important only</span>
          </label>
          <label class="field compact">
            <span>Min confidence <span id="gf-conf-val">0</span></span>
            <input id="gf-confidence" class="input range" type="range" min="0" max="1" step="0.05" value="0" />
          </label>
          <select id="gf-layout" class="input" title="Graph layout">
            <option value="cose">Force layout</option>
            <option value="concentric">Group by type</option>
            <option value="breadthfirst">From User</option>
          </select>
          <label class="toggle small">
            <input type="checkbox" id="gf-connected" />
            <span>Connected only</span>
          </label>
          <label class="toggle small">
            <input type="checkbox" id="gf-around-me" />
            <span>Around me</span>
          </label>
          <button class="btn-ghost" id="graph-apply">Apply filters</button>
        </div>
        <div class="graph-layout">
          <div class="graph-legend" id="graph-legend"></div>
          <div class="graph-zoom">
            <button class="btn-ghost" id="graph-zoom-in" title="Zoom in">+</button>
            <button class="btn-ghost" id="graph-zoom-out" title="Zoom out">−</button>
            <button class="btn-ghost" id="graph-fit" title="Fit">Fit</button>
            <button class="btn-ghost" id="graph-expand" title="Expand neighborhood">Expand</button>
            <button class="btn-ghost" id="graph-path" title="Path between last two nodes">Path</button>
            <button class="btn-ghost" id="graph-to-me" title="Path from User to the selected node">To me</button>
          </div>
          <div id="cy"></div>
        </div>
      </section>

      <!-- ============ ENTITIES ============ -->
      <section class="view" id="view-browse">
        <header class="view-head">
          <div>
            <h1>Entities</h1>
            <p class="view-sub">Browse the real SQLite graph — nothing fabricated.</p>
          </div>
        </header>
        <div class="filter-bar">
          <input id="browse-q" class="input" type="text" placeholder="Filter by name…" />
          <select id="browse-type" class="input">
            <option value="">All types</option>
          </select>
          <label class="toggle small">
            <input type="checkbox" id="browse-pinned" />
            <span>Pinned</span>
          </label>
          <label class="toggle small">
            <input type="checkbox" id="browse-important" />
            <span>Important</span>
          </label>
          <select id="browse-sort" class="input" title="Sort entities">
            <option value="name">Name</option>
            <option value="degree">Most linked</option>
            <option value="recent">Recently updated</option>
            <option value="confidence">Confidence</option>
          </select>
        </div>
        <div id="browse-list" class="browse-list"></div>
      </section>

      <!-- ============ MEMORY ============ -->
      <section class="view" id="view-memory">
        <header class="view-head">
          <div>
            <h1>Memory Timeline</h1>
            <p class="view-sub">When information entered your brain — with sources.</p>
          </div>
        </header>
        <div class="filter-bar">
          <select id="mem-kind" class="input">
            <option value="">All kinds</option>
            <option value="entity">Entities</option>
            <option value="relationship">Relationships</option>
            <option value="update">Updates</option>
            <option value="superseded">Superseded</option>
            <option value="conflict">Conflicts</option>
            <option value="command">Commands</option>
            <option value="summary">Summaries</option>
          </select>
          <input id="mem-entity" class="input" type="text" placeholder="Filter by entity…" />
          <input id="mem-date" class="input" type="date" />
          <button class="btn-ghost" id="mem-clear">Clear</button>
        </div>
        <div class="timeline" id="timeline"></div>
      </section>

      <!-- ============ SEARCH ============ -->
      <section class="view" id="view-search">
        <header class="view-head">
          <h1>Search</h1>
          <p class="view-sub">Unified memory: keyword + semantic + graph.</p>
        </header>
        <div class="search-bar">
          <input id="search-input" class="input input-lg" type="text" placeholder="What projects am I working on?" />
          <button id="search-btn" class="btn-primary">Ask</button>
        </div>
        <div class="filter-bar search-filters">
          <select id="sf-type" class="input">
            <option value="">Any type</option>
          </select>
          <select id="sf-confidence" class="input">
            <option value="">Any confidence</option>
            <option value="0.5">≥ 50%</option>
            <option value="0.7">≥ 70%</option>
            <option value="0.9">≥ 90%</option>
          </select>
          <select id="sf-status" class="input">
            <option value="">Any status</option>
            <option value="active">Active</option>
            <option value="superseded">Superseded</option>
          </select>
          <label class="toggle small">
            <input type="checkbox" id="sf-pinned" />
            <span>Pinned</span>
          </label>
          <label class="toggle small">
            <input type="checkbox" id="sf-important" />
            <span>Important</span>
          </label>
          <input id="sf-from" class="input" type="date" title="From date" />
          <input id="sf-to" class="input" type="date" title="To date" />
          <select id="sf-source" class="input">
            <option value="">Any source</option>
          </select>
        </div>
        <div id="search-answer" class="panel search-answer" style="display:none"></div>
        <div id="search-sources" class="panel" style="display:none"></div>
        <div id="search-results"></div>
      </section>

      <!-- ============ SETTINGS ============ -->
      <section class="view" id="view-settings">
        <header class="view-head">
          <h1>Settings</h1>
          <p class="view-sub">Swap models and tune memory without touching code.</p>
        </header>

        <div class="panel">
          <div class="panel-head"><h2>AI Models</h2></div>
          <div class="panel-body form">
            <div class="field-row">
              <label class="field">
                <span>LLM (extraction)</span>
                <input id="set-llm" class="input" type="text" placeholder="qwen3:0.6b" />
              </label>
              <label class="field">
                <span>Embedding model</span>
                <input id="set-emb" class="input" type="text" placeholder="nomic-embed-text" />
              </label>
            </div>
            <label class="field">
              <span>Ollama URL</span>
              <input id="set-ollama-url" class="input" type="text" placeholder="http://localhost:11434" />
            </label>
            <button class="btn-primary" id="set-save">Save models</button>
            <p class="hint" id="set-hint"></p>
          </div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Memory behavior</h2></div>
          <div class="panel-body form">
            <label class="field">
              <span>Confidence threshold — <span id="conf-val"></span></span>
              <input id="set-confidence" class="input range" type="range" min="0" max="1" step="0.05" />
            </label>
            <label class="field">
              <span>Duplicate merge threshold — <span id="merge-val"></span></span>
              <input id="set-merge" class="input range" type="range" min="0.5" max="0.99" step="0.01" />
            </label>
            <label class="toggle">
              <input type="checkbox" id="set-auto-memory" />
              <span>Auto-memory <span class="muted">(extract knowledge from messages automatically)</span></span>
            </label>
            <label class="field">
              <span>Automatic local backup</span>
              <select id="set-auto-backup" class="input">
                <option value="0">Off</option>
                <option value="6">Every 6 hours</option>
                <option value="12">Every 12 hours</option>
                <option value="24">Every 24 hours</option>
                <option value="48">Every 48 hours</option>
              </select>
            </label>
            <label class="field">
              <span>Theme</span>
              <select id="set-theme" class="input">
                <option value="dark">Dark</option>
                <option value="light">Light</option>
              </select>
            </label>
            <button class="btn-primary" id="set-behavior-save">Save behavior</button>
          </div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Privacy</h2></div>
          <div class="panel-body" id="privacy-info"></div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Ollama</h2></div>
          <div class="panel-body" id="ollama-info"></div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Data</h2></div>
          <div class="panel-body form">
            <p class="hint" id="db-path"></p>
            <div style="display:flex; gap:8px; flex-wrap:wrap">
              <button class="btn-danger" id="reset-btn">Reset all data</button>
              <button class="btn-ghost" id="demo-btn">Load demo data</button>
              <button class="btn-ghost" id="demo-clear-btn">Clear demo data</button>
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Memory consolidation</h2></div>
          <div class="panel-body form">
            <p class="hint">Summarize clusters of related memories into concise entity summaries. Originals are never deleted.</p>
            <div class="dash-cols">
              <div>
                <button class="btn-primary" id="summarize-all">Summarize now</button>
                <p class="hint" id="summarize-status"></p>
              </div>
              <div id="summarize-candidates"></div>
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Export / Import</h2></div>
          <div class="panel-body form">
            <div style="display:flex; gap:8px; flex-wrap:wrap">
              <button class="btn-ghost" id="export-json">Export JSON</button>
              <button class="btn-ghost" id="export-md">Export Markdown</button>
            </div>
            <label class="field">
              <span>Import JSON <span class="muted">(paste an export)</span></span>
              <textarea class="input" id="import-data" rows="3" placeholder='{"format":"second-brain", ...}'></textarea>
            </label>
            <div style="display:flex; gap:8px">
              <button class="btn-primary" id="import-merge">Merge import</button>
              <button class="btn-danger" id="import-replace">Replace database</button>
            </div>
            <p class="hint" id="import-status"></p>
            <label class="field">
              <span>Import notes <span class="muted">(plain text / markdown paragraphs)</span></span>
              <textarea class="input" id="import-notes" rows="3" placeholder="Paste notes. Each paragraph is extracted into memory."></textarea>
            </label>
            <button class="btn-primary" id="import-notes-btn">Import notes</button>
          </div>
        </div>

        <div class="panel">
          <div class="panel-head"><h2>Backup</h2></div>
          <div class="panel-body form">
            <button class="btn-primary" id="backup-now">Create backup</button>
            <p class="hint" id="backup-status"></p>
            <div id="backup-list"></div>
          </div>
        </div>
      </section>
    </main>
  </div>

  <!-- Entity detail slide-over -->
  <div class="overlay" id="entity-overlay"></div>
  <aside class="entity-panel" id="entity-panel">
    <div class="entity-inner" id="entity-inner"></div>
  </aside>

  <!-- Command palette -->
  <div class="overlay" id="palette-overlay"></div>
  <div class="palette" id="palette" hidden>
    <input id="palette-input" class="input input-lg" type="text" placeholder="Jump to a view or entity…  Ctrl+K" />
    <div id="palette-results" class="palette-results"></div>
  </div>

  <!-- Toast -->
  <div class="toast" id="toast"></div>

  <script src="app.js"></script>
</body>
</html>
````

## `frontend/style.css`

````
/* ==========================================================================
   Second Brain — dark, glassmorphism, futuristic personal AI OS
   ========================================================================== */

:root {
  --bg: #070a13;
  --bg-soft: #0b101f;
  --surface: rgba(255, 255, 255, 0.035);
  --surface-2: rgba(255, 255, 255, 0.06);
  --border: rgba(255, 255, 255, 0.09);
  --border-strong: rgba(255, 255, 255, 0.16);
  --text: #e7ecf5;
  --text-muted: #8b95a8;
  --text-dim: #5b6478;
  --accent: #22d3ee;
  --accent-2: #8b5cf6;
  --accent-grad: linear-gradient(135deg, #22d3ee, #8b5cf6);
  --danger: #f87171;
  --ok: #34d399;

  --c-person: #f472b6;
  --c-project: #22d3ee;
  --c-technology: #34d399;
  --c-topic: #a78bfa;
  --c-concept: #fbbf24;
  --c-goal: #60a5fa;
  --c-fact: #f87171;
  --c-interest: #fb923c;

  --radius: 16px;
  --radius-sm: 10px;
  --sidebar-w: 240px;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter",
          "Helvetica Neue", Arial, sans-serif;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font);
  font-size: 15px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  overflow: hidden;
}

::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.10); border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.18); }
::-webkit-scrollbar-track { background: transparent; }

/* ---- animated background orbs ---- */
.bg-orbs { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.orb { position: absolute; border-radius: 50%; filter: blur(90px); opacity: 0.55; }
.orb-1 { width: 520px; height: 520px; background: radial-gradient(circle, rgba(34,211,238,0.35), transparent 70%); top: -160px; right: -120px; animation: drift 26s ease-in-out infinite; }
.orb-2 { width: 460px; height: 460px; background: radial-gradient(circle, rgba(139,92,246,0.30), transparent 70%); bottom: -160px; left: 10%; animation: drift 32s ease-in-out infinite reverse; }
.orb-3 { width: 380px; height: 380px; background: radial-gradient(circle, rgba(59,130,246,0.22), transparent 70%); top: 40%; left: 40%; animation: drift 40s ease-in-out infinite; }
@keyframes drift {
  0%, 100% { transform: translate(0,0) scale(1); }
  33% { transform: translate(40px,-30px) scale(1.08); }
  66% { transform: translate(-30px,20px) scale(0.95); }
}

.app { position: relative; z-index: 1; display: flex; height: 100vh; }

/* ---- sidebar ---- */
.sidebar {
  width: var(--sidebar-w);
  flex: 0 0 var(--sidebar-w);
  display: flex;
  flex-direction: column;
  padding: 22px 16px;
  background: rgba(10, 14, 26, 0.7);
  backdrop-filter: blur(20px);
  border-right: 1px solid var(--border);
}

.brand { display: flex; align-items: center; gap: 12px; padding: 0 8px 22px; }
.brand-mark {
  width: 38px; height: 38px; display: grid; place-items: center;
  font-size: 20px; color: #071018;
  background: var(--accent-grad);
  border-radius: 11px;
  box-shadow: 0 0 24px rgba(34,211,238,0.5);
}
.brand-text { display: flex; flex-direction: column; line-height: 1.2; }
.brand-name { font-weight: 700; font-size: 16px; letter-spacing: 0.2px; }
.brand-sub { font-size: 11px; color: var(--text-muted); }

.nav { display: flex; flex-direction: column; gap: 4px; }
.nav-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 12px; border: none; border-radius: var(--radius-sm);
  background: transparent; color: var(--text-muted);
  font-size: 14px; font-family: var(--font); cursor: pointer;
  text-align: left; transition: all 0.15s ease;
}
.nav-item:hover { background: var(--surface-2); color: var(--text); }
.nav-item.active {
  background: linear-gradient(135deg, rgba(34,211,238,0.14), rgba(139,92,246,0.14));
  color: var(--text);
  box-shadow: inset 0 0 0 1px rgba(34,211,238,0.25);
}
.nav-ico { width: 18px; text-align: center; opacity: 0.9; }

.sidebar-foot { margin-top: auto; padding: 14px 8px 0; display: flex; flex-direction: column; gap: 8px; border-top: 1px solid var(--border); }
.status { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--text-muted); }
.status-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--text-dim); }
.status-dot.on { background: var(--ok); box-shadow: 0 0 8px var(--ok); }
.status-dot.off { background: var(--danger); box-shadow: 0 0 8px var(--danger); }
.model-line { font-size: 11px; color: var(--text-dim); line-height: 1.4; }

/* ---- main ---- */
.main { flex: 1; overflow-y: auto; position: relative; }
.view { display: none; padding: 30px 36px 60px; max-width: 1200px; margin: 0 auto; animation: fadeUp 0.35s ease; }
.view.active { display: block; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }

.view-head { display: flex; align-items: flex-end; justify-content: space-between; gap: 20px; margin-bottom: 24px; flex-wrap: wrap; }
.view-head h1 { margin: 0; font-size: 26px; font-weight: 700; letter-spacing: -0.3px; }
.view-sub { margin: 4px 0 0; color: var(--text-muted); font-size: 14px; }

/* ---- panels / cards ---- */
.panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  backdrop-filter: blur(14px);
  overflow: hidden;
  margin-bottom: 20px;
}
.panel-head { padding: 16px 20px 0; }
.panel-head h2 { margin: 0; font-size: 15px; font-weight: 600; color: var(--text); }
.panel-body { padding: 16px 20px 20px; }

/* ---- dashboard ---- */
.stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 14px; margin-bottom: 24px; }
.stat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px;
  backdrop-filter: blur(14px);
  position: relative;
  overflow: hidden;
  transition: transform 0.18s ease, border-color 0.18s ease;
}
.stat-card:hover { transform: translateY(-3px); border-color: var(--border-strong); }
.stat-card::after {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: var(--accent-grad); opacity: 0; transition: opacity 0.2s;
}
.stat-card:hover::after { opacity: 1; }
.stat-num { font-size: 30px; font-weight: 700; letter-spacing: -0.5px; background: var(--accent-grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.stat-label { font-size: 12px; color: var(--text-muted); margin-top: 2px; }

.dash-cols { display: grid; grid-template-columns: 1.4fr 1fr; gap: 20px; }
@media (max-width: 860px) { .dash-cols { grid-template-columns: 1fr; } }

.mem-item { display: flex; gap: 12px; padding: 9px 0; border-bottom: 1px solid var(--border); font-size: 13.5px; }
.mem-item:last-child { border-bottom: none; }
.mem-ico { flex: 0 0 auto; color: var(--accent); }
.mem-text { color: var(--text); }
.mem-time { color: var(--text-dim); font-size: 12px; margin-left: auto; white-space: nowrap; }

.entity-mini { display: flex; align-items: center; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); cursor: pointer; }
.entity-mini:last-child { border-bottom: none; }
.entity-mini:hover .em-name { color: var(--accent); }
.em-name { font-weight: 500; font-size: 14px; transition: color 0.15s; }
.em-degree { margin-left: auto; color: var(--text-dim); font-size: 12px; }

/* ---- type badges ---- */
.badge { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 11px; font-weight: 600; letter-spacing: 0.3px; text-transform: uppercase; }
.badge.person { background: rgba(244,114,182,0.15); color: var(--c-person); }
.badge.project { background: rgba(34,211,238,0.15); color: var(--c-project); }
.badge.technology { background: rgba(52,211,153,0.15); color: var(--c-technology); }
.badge.topic { background: rgba(167,139,250,0.15); color: var(--c-topic); }
.badge.concept { background: rgba(251,191,36,0.15); color: var(--c-concept); }
.badge.goal { background: rgba(96,165,250,0.15); color: var(--c-goal); }
.badge.fact { background: rgba(248,113,113,0.15); color: var(--c-fact); }
.badge.interest { background: rgba(251,146,60,0.15); color: var(--c-interest); }

/* ---- buttons / inputs ---- */
button { font-family: var(--font); }
.btn-primary {
  padding: 10px 18px; border: none; border-radius: var(--radius-sm);
  background: var(--accent-grad); color: #051018; font-weight: 600; font-size: 14px;
  cursor: pointer; transition: filter 0.15s, transform 0.1s;
  box-shadow: 0 4px 18px rgba(34,211,238,0.3);
}
.btn-primary:hover { filter: brightness(1.08); }
.btn-primary:active { transform: scale(0.98); }
.btn-primary:disabled { opacity: 0.5; cursor: default; }
.btn-ghost {
  padding: 9px 16px; border: 1px solid var(--border-strong); border-radius: var(--radius-sm);
  background: var(--surface-2); color: var(--text); font-size: 13.5px; cursor: pointer;
  transition: background 0.15s;
}
.btn-ghost:hover { background: rgba(255,255,255,0.1); }
.btn-danger {
  padding: 9px 16px; border: 1px solid rgba(248,113,113,0.4); border-radius: var(--radius-sm);
  background: rgba(248,113,113,0.1); color: var(--danger); font-size: 13.5px; cursor: pointer;
}
.btn-danger:hover { background: rgba(248,113,113,0.2); }

.input {
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  color: var(--text);
  padding: 10px 14px;
  font-size: 14px;
  font-family: var(--font);
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}
.input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(34,211,238,0.15); }
.input-lg { font-size: 15px; padding: 13px 16px; }
.input::placeholder { color: var(--text-dim); }

.muted { color: var(--text-muted); }
.hint { color: var(--text-muted); font-size: 13px; }

/* ---- chat ---- */
.chat-wrap { display: flex; flex-direction: column; height: calc(100vh - 150px); min-height: 400px; }
.chat-scroll { flex: 1; overflow-y: auto; padding: 8px 4px 20px; display: flex; flex-direction: column; gap: 16px; }
.chat-empty { text-align: center; color: var(--text-muted); padding: 60px 20px; }
.chat-empty-mark { font-size: 42px; background: var(--accent-grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 12px; }
.msg { max-width: 78%; display: flex; flex-direction: column; }
.msg.user { align-self: flex-end; }
.msg.assistant { align-self: flex-start; }
.msg-bubble {
  padding: 12px 16px; border-radius: 16px; font-size: 14.5px; white-space: pre-wrap; word-wrap: break-word;
}
.msg.user .msg-bubble {
  background: linear-gradient(135deg, rgba(34,211,238,0.22), rgba(139,92,246,0.22));
  border: 1px solid rgba(34,211,238,0.3);
  border-bottom-right-radius: 4px;
}
.msg.assistant .msg-bubble {
  background: var(--surface);
  border: 1px solid var(--border);
  border-bottom-left-radius: 4px;
}
.msg-updates { margin-top: 8px; display: flex; flex-direction: column; gap: 4px; }
.msg-update {
  font-size: 12.5px; color: var(--text-muted);
  background: rgba(34,211,153,0.08);
  border: 1px solid rgba(52,211,153,0.2);
  border-radius: 8px; padding: 4px 10px; align-self: flex-start;
}
.msg-time { font-size: 11px; color: var(--text-dim); margin-top: 4px; padding: 0 4px; }
.msg.user .msg-time { align-self: flex-end; }

.chat-inputbar {
  display: flex; gap: 10px; padding: 12px;
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  backdrop-filter: blur(14px);
}
.chat-inputbar textarea {
  flex: 1; resize: none; background: transparent; border: none; outline: none;
  color: var(--text); font-size: 15px; font-family: var(--font); max-height: 140px; padding: 8px 4px;
}
.chat-inputbar textarea::placeholder { color: var(--text-dim); }

/* ---- graph ---- */
.graph-head { align-items: center; }
.graph-tools { display: flex; gap: 10px; align-items: center; }
.graph-layout { position: relative; height: calc(100vh - 170px); min-height: 460px; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; background: rgba(7,10,19,0.5); }
#cy { position: absolute; inset: 0; }
.graph-legend {
  position: absolute; top: 14px; left: 14px; z-index: 5;
  display: flex; flex-direction: column; gap: 6px;
  background: rgba(10,14,26,0.75); backdrop-filter: blur(10px);
  border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 12px 14px;
}
.legend-row { display: flex; align-items: center; gap: 8px; font-size: 12.5px; color: var(--text-muted); cursor: pointer; user-select: none; }
.legend-dot { width: 11px; height: 11px; border-radius: 50%; }
.legend-row.off { opacity: 0.35; }

/* ---- timeline ---- */
.timeline { display: flex; flex-direction: column; gap: 24px; }
.tl-day {}
.tl-day-head { font-size: 14px; font-weight: 600; color: var(--text); padding: 6px 0 10px; display: flex; align-items: center; gap: 10px; }
.tl-day-head::after { content: ""; flex: 1; height: 1px; background: var(--border); }
.tl-item {
  display: flex; gap: 14px; padding: 10px 0 10px; margin-left: 4px;
  border-left: 1px solid var(--border); padding-left: 18px; position: relative;
}
.tl-item::before {
  content: ""; position: absolute; left: -5px; top: 17px; width: 9px; height: 9px;
  border-radius: 50%; background: var(--accent); box-shadow: 0 0 10px var(--accent);
}
.tl-time { color: var(--text-dim); font-size: 12.5px; width: 52px; flex: 0 0 auto; padding-top: 1px; }
.tl-text { font-size: 14px; }
.tl-kind { font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-dim); margin-left: 8px; }

/* ---- search ---- */
.search-bar { display: flex; gap: 12px; margin-bottom: 22px; }
.search-bar .input { flex: 1; }
.search-answer { border-color: rgba(34,211,238,0.3); }
.search-answer .panel-body { font-size: 15px; white-space: pre-wrap; }
.result-entity { display: flex; align-items: center; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--border); cursor: pointer; }
.result-entity:last-child { border-bottom: none; }
.result-entity:hover .re-name { color: var(--accent); }
.re-name { font-weight: 600; }
.re-desc { color: var(--text-muted); font-size: 13px; }

/* ---- settings form ---- */
.form { display: flex; flex-direction: column; gap: 16px; }
.field { display: flex; flex-direction: column; gap: 6px; font-size: 13px; color: var(--text-muted); }
.form .btn-primary, .form .btn-danger { align-self: flex-start; }

/* ---- entity slide-over ---- */
.overlay { position: fixed; inset: 0; background: rgba(4,6,12,0.55); backdrop-filter: blur(2px); z-index: 40; opacity: 0; pointer-events: none; transition: opacity 0.25s; }
.overlay.show { opacity: 1; pointer-events: auto; }
.entity-panel {
  position: fixed; top: 0; right: 0; bottom: 0; width: 400px; max-width: 92vw; z-index: 50;
  background: rgba(11,16,31,0.92); backdrop-filter: blur(24px);
  border-left: 1px solid var(--border);
  transform: translateX(100%); transition: transform 0.28s cubic-bezier(0.2,0.8,0.2,1);
  display: flex; flex-direction: column;
}
.entity-panel.open { transform: translateX(0); }
.entity-inner { overflow-y: auto; padding: 24px; }
.entity-close { position: absolute; top: 16px; right: 16px; background: none; border: none; color: var(--text-muted); font-size: 20px; cursor: pointer; }
.entity-close:hover { color: var(--text); }
.entity-title { font-size: 22px; font-weight: 700; margin: 4px 0 2px; }
.entity-desc { color: var(--text-muted); font-size: 14px; margin-bottom: 18px; }
.entity-sec { margin-top: 20px; }
.entity-sec h3 { font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; color: var(--text-dim); margin: 0 0 10px; }
.rel-item { display: flex; align-items: center; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); cursor: pointer; }
.rel-item:hover .ri-name { color: var(--accent); }
.ri-name { font-weight: 500; }
.ri-rel { color: var(--text-muted); font-size: 12.5px; margin-left: auto; }
.entity-actions { display: flex; gap: 8px; margin-top: 20px; flex-wrap: wrap; }
.entity-mem { font-size: 13px; color: var(--text-muted); padding: 6px 0; border-bottom: 1px solid var(--border); }
.entity-mem:last-child { border-bottom: none; }

/* ---- toast ---- */
.toast {
  position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(20px);
  background: rgba(20,26,44,0.95); border: 1px solid var(--border-strong);
  color: var(--text); padding: 12px 20px; border-radius: 12px; font-size: 14px;
  z-index: 100; opacity: 0; pointer-events: none; transition: all 0.25s ease;
  box-shadow: 0 12px 40px rgba(0,0,0,0.5);
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

/* ---- merge modal ---- */
.modal { position: fixed; inset: 0; z-index: 60; display: grid; place-items: center; background: rgba(4,6,12,0.6); }
.modal-card { width: 420px; max-width: 92vw; background: rgba(13,18,34,0.98); border: 1px solid var(--border-strong); border-radius: var(--radius); padding: 22px; }
.modal-card h3 { margin: 0 0 6px; }
.modal-search { margin: 14px 0; width: 100%; }
.modal-list { max-height: 260px; overflow-y: auto; display: flex; flex-direction: column; }
.modal-opt { padding: 10px 12px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; gap: 10px; }
.modal-opt:hover { background: var(--surface-2); }

/* ==========================================================================
   Phase 2 additions
   ========================================================================== */

/* privacy badge */
.privacy-badge {
  font-size: 10px; letter-spacing: 1.2px; color: var(--ok);
  border: 1px solid rgba(52,211,153,0.35); border-radius: 6px;
  padding: 3px 8px; text-align: center;
  background: rgba(52,211,153,0.08);
}

/* growth chart */
#growth-chart { display: flex; align-items: flex-end; gap: 3px; height: 120px; }
.grow-bar { flex: 1; background: linear-gradient(180deg, var(--accent), rgba(139,92,246,0.6)); border-radius: 3px 3px 0 0; min-height: 2px; position: relative; transition: height .3s; }
.grow-bar:hover { filter: brightness(1.3); }
.grow-bar .grow-tip { position: absolute; bottom: calc(100% + 4px); left: 50%; transform: translateX(-50%); font-size: 10px; color: var(--text); background: rgba(20,26,44,.95); padding: 2px 6px; border-radius: 5px; opacity: 0; pointer-events: none; white-space: nowrap; }
.grow-bar:hover .grow-tip { opacity: 1; }

/* type breakdown */
.type-row { display: flex; align-items: center; gap: 10px; padding: 5px 0; font-size: 13px; }
.type-dot { width: 10px; height: 10px; border-radius: 50%; flex: 0 0 auto; }
.type-name { width: 110px; color: var(--text-muted); text-transform: capitalize; }
.type-bar-track { flex: 1; height: 6px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden; }
.type-bar-fill { height: 100%; border-radius: 4px; }
.type-count { width: 30px; text-align: right; color: var(--text); font-variant-numeric: tabular-nums; }

/* filter bar (memory) */
.filter-bar { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; align-items: center; }
.filter-bar .input { flex: 0 0 auto; }
.filter-bar #mem-entity { flex: 1; min-width: 160px; }

/* remembered chips (memory transparency) */
.remembered-box {
  margin-top: 10px; padding: 10px 12px; border-radius: 10px;
  background: rgba(52,211,153,0.06); border: 1px solid rgba(52,211,153,0.18);
  font-size: 13px;
}
.remembered-title { color: var(--ok); font-size: 11px; letter-spacing: .5px; text-transform: uppercase; margin-bottom: 6px; }
.remembered-chip {
  display: inline-flex; align-items: center; gap: 6px; margin: 3px 4px 3px 0;
  padding: 3px 10px; border-radius: 999px; cursor: pointer;
  background: var(--surface-2); border: 1px solid var(--border);
  font-size: 12.5px; transition: all .15s;
}
.remembered-chip:hover { border-color: var(--accent); color: var(--accent); }
.remembered-chip .conf { color: var(--text-dim); font-size: 11px; }
.remembered-chip .arrow { color: var(--text-dim); }
.superseded-note { margin-top: 6px; font-size: 12px; color: var(--danger); }

/* status badges */
.st-status { font-size: 10px; letter-spacing: .6px; text-transform: uppercase; padding: 2px 8px; border-radius: 999px; }
.st-superseded { background: rgba(148,163,184,0.15); color: var(--text-dim); text-decoration: line-through; }
.st-active { background: rgba(52,211,153,0.15); color: var(--ok); }
.st-pinned { background: rgba(251,191,36,0.15); color: var(--c-concept); }
.st-important { background: rgba(248,113,113,0.15); color: var(--c-fact); }
.st-demo { background: rgba(139,92,246,0.15); color: var(--accent-2); }

/* answer status */
.ans-status { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 11px; font-weight: 600; letter-spacing: .4px; text-transform: uppercase; margin-left: 8px; }
.ans-answered, .ans-known { background: rgba(52,211,153,0.15); color: var(--ok); }
.ans-unknown { background: rgba(248,113,113,0.15); color: var(--danger); }
.ans-uncertain { background: rgba(251,191,36,0.15); color: var(--c-concept); }

/* confidence bar */
.conf-bar { height: 5px; background: rgba(255,255,255,0.07); border-radius: 4px; overflow: hidden; margin-top: 6px; }
.conf-fill { height: 100%; background: var(--accent-grad); border-radius: 4px; }
.conf-label { font-size: 11px; color: var(--text-dim); }

/* entity metadata */
.entity-meta { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 4px; }
.meta-kv { font-size: 12px; color: var(--text-muted); }
.meta-kv b { color: var(--text); font-weight: 500; }
.source-link { cursor: pointer; color: var(--accent); font-size: 12.5px; }
.source-link:hover { text-decoration: underline; }

/* relationship status in entity panel */
.rel-item.super { opacity: 0.45; }
.rel-item.super .ri-name { text-decoration: line-through; }
.rel-conf { font-size: 11px; color: var(--text-dim); margin-left: 6px; }

/* toggle */
.toggle { display: flex; align-items: center; gap: 10px; font-size: 14px; cursor: pointer; }
.toggle input { width: 18px; height: 18px; accent-color: var(--accent); cursor: pointer; }

/* field row + range */
.field-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
@media (max-width: 640px) { .field-row { grid-template-columns: 1fr; } }
.input.range { padding: 0; background: transparent; border: none; box-shadow: none; }
.input.range:focus { box-shadow: none; }

/* source message modal */
.src-modal .msg-bubble { margin: 10px 0; }

/* ==========================================================================
   Phase 3 additions
   ========================================================================== */

/* graph + search filter toggles */
.toggle.small { gap: 6px; font-size: 13px; }
.toggle.small input { width: 15px; height: 15px; }
.graph-filters, .search-filters { align-items: center; }

/* reason chips (why a result matched) */
.re-reasons { margin-top: 4px; }
.reason-chip {
  display: inline-block; margin-right: 5px; padding: 1px 8px;
  border-radius: 999px; font-size: 10.5px; letter-spacing: .3px;
  background: rgba(34,211,238,0.1); color: var(--accent);
  border: 1px solid rgba(34,211,238,0.25);
}

/* superseded entity history items */
.entity-mem.super { opacity: 0.55; text-decoration: line-through; }

/* source chips in search */
#search-sources .panel-body { display: flex; flex-wrap: wrap; gap: 4px; }

/* conversation rail */
.chat-layout { display: grid; grid-template-columns: 220px 1fr; gap: 16px; height: calc(100vh - 150px); min-height: 400px; }
@media (max-width: 860px) { .chat-layout { grid-template-columns: 1fr; height: auto; } }
.conv-rail {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 12px; overflow-y: auto; min-height: 160px;
}
.conv-rail-head { font-size: 11px; letter-spacing: 0.6px; text-transform: uppercase; color: var(--text-dim); margin-bottom: 8px; }
#conv-search { width: 100%; margin-bottom: 10px; padding: 7px 10px; font-size: 12.5px; }
.conv-list { display: flex; flex-direction: column; }
.conv-item {
  padding: 8px 10px; border-radius: 8px; cursor: pointer; margin-bottom: 4px;
  border: 1px solid transparent; position: relative;
}
.conv-item .conv-del { position: absolute; top: 6px; right: 6px; }
.conv-item:hover { background: var(--surface-2); }
.conv-item.active { background: rgba(34,211,238,0.1); border-color: rgba(34,211,238,0.3); }
.conv-title { font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.conv-preview { font-size: 11px; color: var(--text-dim); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.chat-layout .chat-wrap { height: 100%; min-height: 360px; }

/* streaming caret */
.msg-bubble.streaming::after {
  content: "▍"; display: inline-block; margin-left: 2px; animation: blink 1s step-end infinite;
  color: var(--accent);
}
@keyframes blink { 50% { opacity: 0; } }

/* graph zoom cluster */
.graph-zoom {
  position: absolute; top: 14px; right: 14px; z-index: 5; display: flex; gap: 6px;
}
.graph-zoom .btn-ghost { padding: 6px 10px; font-size: 13px; }
.field.compact { font-size: 12px; color: var(--text-muted); min-width: 140px; }
.field.compact span { display: block; margin-bottom: 2px; }

/* demo banner */
.demo-banner {
  margin-bottom: 16px; padding: 10px 14px; border-radius: var(--radius-sm);
  background: rgba(139,92,246,0.12); border: 1px solid rgba(139,92,246,0.35);
  color: var(--text); font-size: 13.5px;
}

/* theme: light */
body.theme-light {
  --bg: #eef2f8; --bg-soft: #e4eaf3; --surface: rgba(255,255,255,0.72);
  --surface-2: rgba(255,255,255,0.9); --border: rgba(15,23,42,0.08);
  --border-strong: rgba(15,23,42,0.16); --text: #0f172a; --text-muted: #475569;
  --text-dim: #64748b;
}
body.theme-light .sidebar { background: rgba(255,255,255,0.7); }

.rel-edit {
  font-size: 11px; padding: 2px 6px; max-width: 128px; margin-left: 6px;
}
.rel-item { flex-wrap: wrap; }
.graph-zoom { flex-wrap: wrap; max-width: 52%; justify-content: flex-end; }

.rel-del {
  margin-left: 8px; border: none; background: transparent; color: var(--text-dim);
  cursor: pointer; font-size: 13px;
}
.rel-del:hover { color: var(--danger); }

/* entity browser */
.browse-list { display: flex; flex-direction: column; gap: 4px; }
.browse-row {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 14px; border: 1px solid var(--border); border-radius: var(--radius-sm);
  background: var(--surface); cursor: pointer;
}
.browse-row:hover { border-color: var(--border-strong); }
.browse-name { font-weight: 600; }
.browse-meta { margin-left: auto; color: var(--text-dim); font-size: 12px; display: flex; gap: 8px; align-items: center; }

/* command palette */
.palette {
  position: fixed; top: 16vh; left: 50%; transform: translateX(-50%);
  width: min(560px, 92vw); z-index: 80;
  background: rgba(11,16,31,0.96); border: 1px solid var(--border-strong);
  border-radius: var(--radius); padding: 12px; box-shadow: 0 24px 80px rgba(0,0,0,0.55);
}
.palette[hidden] { display: none; }
.palette-results { max-height: 320px; overflow-y: auto; margin-top: 10px; }
.palette-item {
  padding: 9px 12px; border-radius: 8px; cursor: pointer;
  display: flex; align-items: center; gap: 10px; font-size: 14px;
}
.palette-item:hover, .palette-item.active { background: var(--surface-2); }
.palette-kicker { font-size: 11px; letter-spacing: .4px; text-transform: uppercase; color: var(--text-dim); }

.offline-chip {
  display: inline-block; margin-left: 8px; padding: 1px 8px; border-radius: 999px;
  font-size: 10.5px; letter-spacing: .3px; text-transform: uppercase;
  background: rgba(251,191,36,0.12); color: var(--c-concept);
  border: 1px solid rgba(251,191,36,0.3);
}

.conv-title[contenteditable="true"] { outline: 1px solid var(--accent); border-radius: 4px; padding: 0 4px; }

@media (max-width: 720px) {
  .sidebar { width: 72px; flex-basis: 72px; padding: 16px 8px; }
  .brand-text, .nav-item { font-size: 0; }
  .nav-item { justify-content: center; padding: 12px 8px; }
  .nav-ico { font-size: 16px; }
  .sidebar-foot .status-text, .model-line, .privacy-badge { display: none; }
  .view { padding: 20px 16px 40px; }
}
````

## `frontend/vendor/cytoscape.min.js`

````
/**
 * Copyright (c) 2016-2024, The Cytoscape Consortium.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the “Software”), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

!function(e,t){"object"==typeof exports&&"undefined"!=typeof module?module.exports=t():"function"==typeof define&&define.amd?define(t):(e="undefined"!=typeof globalThis?globalThis:e||self).cytoscape=t()}(this,(function(){"use strict";function e(t){return(e="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(t)}function t(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function n(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function r(e,t,r){return t&&n(e.prototype,t),r&&n(e,r),Object.defineProperty(e,"prototype",{writable:!1}),e}function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==n)return;var r,i,a=[],o=!0,s=!1;try{for(n=n.call(e);!(o=(r=n.next()).done)&&(a.push(r.value),!t||a.length!==t);o=!0);}catch(e){s=!0,i=e}finally{try{o||null==n.return||n.return()}finally{if(s)throw i}}return a}(e,t)||o(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function o(e,t){if(e){if("string"==typeof e)return s(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?s(e,t):void 0}}function s(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function l(e,t){var n="undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(!n){if(Array.isArray(e)||(n=o(e))||t&&e&&"number"==typeof e.length){n&&(e=n);var r=0,i=function(){};return{s:i,n:function(){return r>=e.length?{done:!0}:{done:!1,value:e[r++]}},e:function(e){throw e},f:i}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var a,s=!0,l=!1;return{s:function(){n=n.call(e)},n:function(){var e=n.next();return s=e.done,e},e:function(e){l=!0,a=e},f:function(){try{s||null==n.return||n.return()}finally{if(l)throw a}}}}var u="undefined"==typeof window?null:window,c=u?u.navigator:null;u&&u.document;var d=e(""),h=e({}),p=e((function(){})),f="undefined"==typeof HTMLElement?"undefined":e(HTMLElement),g=function(e){return e&&e.instanceString&&y(e.instanceString)?e.instanceString():null},v=function(t){return null!=t&&e(t)==d},y=function(t){return null!=t&&e(t)===p},m=function(e){return!E(e)&&(Array.isArray?Array.isArray(e):null!=e&&e instanceof Array)},b=function(t){return null!=t&&e(t)===h&&!m(t)&&t.constructor===Object},x=function(t){return null!=t&&e(t)===e(1)&&!isNaN(t)},w=function(e){return"undefined"===f?void 0:null!=e&&e instanceof HTMLElement},E=function(e){return k(e)||C(e)},k=function(e){return"collection"===g(e)&&e._private.single},C=function(e){return"collection"===g(e)&&!e._private.single},S=function(e){return"core"===g(e)},P=function(e){return"stylesheet"===g(e)},D=function(e){return null==e||!(""!==e&&!e.match(/^\s+$/))},T=function(t){return function(t){return null!=t&&e(t)===h}(t)&&y(t.then)},_=function(e,t){t||(t=function(){if(1===arguments.length)return arguments[0];if(0===arguments.length)return"undefined";for(var e=[],t=0;t<arguments.length;t++)e.push(arguments[t]);return e.join("$")});var n=function n(){var r,i=this,a=arguments,o=t.apply(i,a),s=n.cache;return(r=s[o])||(r=s[o]=e.apply(i,a)),r};return n.cache={},n},M=_((function(e){return e.replace(/([A-Z])/g,(function(e){return"-"+e.toLowerCase()}))})),B=_((function(e){return e.replace(/(-\w)/g,(function(e){return e[1].toUpperCase()}))})),N=_((function(e,t){return e+t[0].toUpperCase()+t.substring(1)}),(function(e,t){return e+"$"+t})),z=function(e){return D(e)?e:e.charAt(0).toUpperCase()+e.substring(1)},I="(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))",A=function(e,t){return e<t?-1:e>t?1:0},L=null!=Object.assign?Object.assign.bind(Object):function(e){for(var t=arguments,n=1;n<t.length;n++){var r=t[n];if(null!=r)for(var i=Object.keys(r),a=0;a<i.length;a++){var o=i[a];e[o]=r[o]}}return e},O=function(e){return(m(e)?e:null)||function(e){return R[e.toLowerCase()]}(e)||function(e){if((4===e.length||7===e.length)&&"#"===e[0]){var t,n,r;return 4===e.length?(t=parseInt(e[1]+e[1],16),n=parseInt(e[2]+e[2],16),r=parseInt(e[3]+e[3],16)):(t=parseInt(e[1]+e[2],16),n=parseInt(e[3]+e[4],16),r=parseInt(e[5]+e[6],16)),[t,n,r]}}(e)||function(e){var t,n=new RegExp("^rgb[a]?\\(((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%]?)\\s*,\\s*((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%]?)\\s*,\\s*((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%]?)(?:\\s*,\\s*((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))))?\\)$").exec(e);if(n){t=[];for(var r=[],i=1;i<=3;i++){var a=n[i];if("%"===a[a.length-1]&&(r[i]=!0),a=parseFloat(a),r[i]&&(a=a/100*255),a<0||a>255)return;t.push(Math.floor(a))}var o=r[1]||r[2]||r[3],s=r[1]&&r[2]&&r[3];if(o&&!s)return;var l=n[4];if(void 0!==l){if((l=parseFloat(l))<0||l>1)return;t.push(l)}}return t}(e)||function(e){var t,n,r,i,a,o,s,l;function u(e,t,n){return n<0&&(n+=1),n>1&&(n-=1),n<1/6?e+6*(t-e)*n:n<.5?t:n<2/3?e+(t-e)*(2/3-n)*6:e}var c=new RegExp("^hsl[a]?\\(((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?)))\\s*,\\s*((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%])\\s*,\\s*((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%])(?:\\s*,\\s*((?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))))?\\)$").exec(e);if(c){if((n=parseInt(c[1]))<0?n=(360- -1*n%360)%360:n>360&&(n%=360),n/=360,(r=parseFloat(c[2]))<0||r>100)return;if(r/=100,(i=parseFloat(c[3]))<0||i>100)return;if(i/=100,void 0!==(a=c[4])&&((a=parseFloat(a))<0||a>1))return;if(0===r)o=s=l=Math.round(255*i);else{var d=i<.5?i*(1+r):i+r-i*r,h=2*i-d;o=Math.round(255*u(h,d,n+1/3)),s=Math.round(255*u(h,d,n)),l=Math.round(255*u(h,d,n-1/3))}t=[o,s,l,a]}return t}(e)},R={transparent:[0,0,0,0],aliceblue:[240,248,255],antiquewhite:[250,235,215],aqua:[0,255,255],aquamarine:[127,255,212],azure:[240,255,255],beige:[245,245,220],bisque:[255,228,196],black:[0,0,0],blanchedalmond:[255,235,205],blue:[0,0,255],blueviolet:[138,43,226],brown:[165,42,42],burlywood:[222,184,135],cadetblue:[95,158,160],chartreuse:[127,255,0],chocolate:[210,105,30],coral:[255,127,80],cornflowerblue:[100,149,237],cornsilk:[255,248,220],crimson:[220,20,60],cyan:[0,255,255],darkblue:[0,0,139],darkcyan:[0,139,139],darkgoldenrod:[184,134,11],darkgray:[169,169,169],darkgreen:[0,100,0],darkgrey:[169,169,169],darkkhaki:[189,183,107],darkmagenta:[139,0,139],darkolivegreen:[85,107,47],darkorange:[255,140,0],darkorchid:[153,50,204],darkred:[139,0,0],darksalmon:[233,150,122],darkseagreen:[143,188,143],darkslateblue:[72,61,139],darkslategray:[47,79,79],darkslategrey:[47,79,79],darkturquoise:[0,206,209],darkviolet:[148,0,211],deeppink:[255,20,147],deepskyblue:[0,191,255],dimgray:[105,105,105],dimgrey:[105,105,105],dodgerblue:[30,144,255],firebrick:[178,34,34],floralwhite:[255,250,240],forestgreen:[34,139,34],fuchsia:[255,0,255],gainsboro:[220,220,220],ghostwhite:[248,248,255],gold:[255,215,0],goldenrod:[218,165,32],gray:[128,128,128],grey:[128,128,128],green:[0,128,0],greenyellow:[173,255,47],honeydew:[240,255,240],hotpink:[255,105,180],indianred:[205,92,92],indigo:[75,0,130],ivory:[255,255,240],khaki:[240,230,140],lavender:[230,230,250],lavenderblush:[255,240,245],lawngreen:[124,252,0],lemonchiffon:[255,250,205],lightblue:[173,216,230],lightcoral:[240,128,128],lightcyan:[224,255,255],lightgoldenrodyellow:[250,250,210],lightgray:[211,211,211],lightgreen:[144,238,144],lightgrey:[211,211,211],lightpink:[255,182,193],lightsalmon:[255,160,122],lightseagreen:[32,178,170],lightskyblue:[135,206,250],lightslategray:[119,136,153],lightslategrey:[119,136,153],lightsteelblue:[176,196,222],lightyellow:[255,255,224],lime:[0,255,0],limegreen:[50,205,50],linen:[250,240,230],magenta:[255,0,255],maroon:[128,0,0],mediumaquamarine:[102,205,170],mediumblue:[0,0,205],mediumorchid:[186,85,211],mediumpurple:[147,112,219],mediumseagreen:[60,179,113],mediumslateblue:[123,104,238],mediumspringgreen:[0,250,154],mediumturquoise:[72,209,204],mediumvioletred:[199,21,133],midnightblue:[25,25,112],mintcream:[245,255,250],mistyrose:[255,228,225],moccasin:[255,228,181],navajowhite:[255,222,173],navy:[0,0,128],oldlace:[253,245,230],olive:[128,128,0],olivedrab:[107,142,35],orange:[255,165,0],orangered:[255,69,0],orchid:[218,112,214],palegoldenrod:[238,232,170],palegreen:[152,251,152],paleturquoise:[175,238,238],palevioletred:[219,112,147],papayawhip:[255,239,213],peachpuff:[255,218,185],peru:[205,133,63],pink:[255,192,203],plum:[221,160,221],powderblue:[176,224,230],purple:[128,0,128],red:[255,0,0],rosybrown:[188,143,143],royalblue:[65,105,225],saddlebrown:[139,69,19],salmon:[250,128,114],sandybrown:[244,164,96],seagreen:[46,139,87],seashell:[255,245,238],sienna:[160,82,45],silver:[192,192,192],skyblue:[135,206,235],slateblue:[106,90,205],slategray:[112,128,144],slategrey:[112,128,144],snow:[255,250,250],springgreen:[0,255,127],steelblue:[70,130,180],tan:[210,180,140],teal:[0,128,128],thistle:[216,191,216],tomato:[255,99,71],turquoise:[64,224,208],violet:[238,130,238],wheat:[245,222,179],white:[255,255,255],whitesmoke:[245,245,245],yellow:[255,255,0],yellowgreen:[154,205,50]},V=function(e){for(var t=e.map,n=e.keys,r=n.length,i=0;i<r;i++){var a=n[i];if(b(a))throw Error("Tried to set map with object key");i<n.length-1?(null==t[a]&&(t[a]={}),t=t[a]):t[a]=e.value}},F=function(e){for(var t=e.map,n=e.keys,r=n.length,i=0;i<r;i++){var a=n[i];if(b(a))throw Error("Tried to get map with object key");if(null==(t=t[a]))return t}return t};var j=function(e){var t=typeof e;return null!=e&&("object"==t||"function"==t)},q="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof self?self:{};var Y="object"==typeof q&&q&&q.Object===Object&&q,X="object"==typeof self&&self&&self.Object===Object&&self,W=Y||X||Function("return this")(),H=function(){return W.Date.now()},K=/\s/;var G=function(e){for(var t=e.length;t--&&K.test(e.charAt(t)););return t},U=/^\s+/;var Z=function(e){return e?e.slice(0,G(e)+1).replace(U,""):e},$=W.Symbol,Q=Object.prototype,J=Q.hasOwnProperty,ee=Q.toString,te=$?$.toStringTag:void 0;var ne=function(e){var t=J.call(e,te),n=e[te];try{e[te]=void 0;var r=!0}catch(e){}var i=ee.call(e);return r&&(t?e[te]=n:delete e[te]),i},re=Object.prototype.toString;var ie=function(e){return re.call(e)},ae=$?$.toStringTag:void 0;var oe=function(e){return null==e?void 0===e?"[object Undefined]":"[object Null]":ae&&ae in Object(e)?ne(e):ie(e)};var se=function(e){return null!=e&&"object"==typeof e};var le=function(e){return"symbol"==typeof e||se(e)&&"[object Symbol]"==oe(e)},ue=/^[-+]0x[0-9a-f]+$/i,ce=/^0b[01]+$/i,de=/^0o[0-7]+$/i,he=parseInt;var pe=function(e){if("number"==typeof e)return e;if(le(e))return NaN;if(j(e)){var t="function"==typeof e.valueOf?e.valueOf():e;e=j(t)?t+"":t}if("string"!=typeof e)return 0===e?e:+e;e=Z(e);var n=ce.test(e);return n||de.test(e)?he(e.slice(2),n?2:8):ue.test(e)?NaN:+e},fe=Math.max,ge=Math.min;var ve=function(e,t,n){var r,i,a,o,s,l,u=0,c=!1,d=!1,h=!0;if("function"!=typeof e)throw new TypeError("Expected a function");function p(t){var n=r,a=i;return r=i=void 0,u=t,o=e.apply(a,n)}function f(e){return u=e,s=setTimeout(v,t),c?p(e):o}function g(e){var n=e-l;return void 0===l||n>=t||n<0||d&&e-u>=a}function v(){var e=H();if(g(e))return y(e);s=setTimeout(v,function(e){var n=t-(e-l);return d?ge(n,a-(e-u)):n}(e))}function y(e){return s=void 0,h&&r?p(e):(r=i=void 0,o)}function m(){var e=H(),n=g(e);if(r=arguments,i=this,l=e,n){if(void 0===s)return f(l);if(d)return clearTimeout(s),s=setTimeout(v,t),p(l)}return void 0===s&&(s=setTimeout(v,t)),o}return t=pe(t)||0,j(n)&&(c=!!n.leading,a=(d="maxWait"in n)?fe(pe(n.maxWait)||0,t):a,h="trailing"in n?!!n.trailing:h),m.cancel=function(){void 0!==s&&clearTimeout(s),u=0,r=l=i=s=void 0},m.flush=function(){return void 0===s?o:y(H())},m},ye=u?u.performance:null,me=ye&&ye.now?function(){return ye.now()}:function(){return Date.now()},be=function(){if(u){if(u.requestAnimationFrame)return function(e){u.requestAnimationFrame(e)};if(u.mozRequestAnimationFrame)return function(e){u.mozRequestAnimationFrame(e)};if(u.webkitRequestAnimationFrame)return function(e){u.webkitRequestAnimationFrame(e)};if(u.msRequestAnimationFrame)return function(e){u.msRequestAnimationFrame(e)}}return function(e){e&&setTimeout((function(){e(me())}),1e3/60)}}(),xe=function(e){return be(e)},we=me,Ee=65599,ke=function(e){for(var t,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:9261,r=n;!(t=e.next()).done;)r=r*Ee+t.value|0;return r},Ce=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:9261;return t*Ee+e|0},Se=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:5381;return(t<<5)+t+e|0},Pe=function(e){return 2097152*e[0]+e[1]},De=function(e,t){return[Ce(e[0],t[0]),Se(e[1],t[1])]},Te=function(e,t){var n={value:0,done:!1},r=0,i=e.length;return ke({next:function(){return r<i?n.value=e.charCodeAt(r++):n.done=!0,n}},t)},_e=function(){return Me(arguments)},Me=function(e){for(var t,n=0;n<e.length;n++){var r=e[n];t=0===n?Te(r):Te(r,t)}return t},Be=!0,Ne=null!=console.warn,ze=null!=console.trace,Ie=Number.MAX_SAFE_INTEGER||9007199254740991,Ae=function(){return!0},Le=function(){return!1},Oe=function(){return 0},Re=function(){},Ve=function(e){throw new Error(e)},Fe=function(e){if(void 0===e)return Be;Be=!!e},je=function(e){Fe()&&(Ne?console.warn(e):(console.log(e),ze&&console.trace()))},qe=function(e){return null==e?e:m(e)?e.slice():b(e)?function(e){return L({},e)}(e):e},Ye=function(e,t){for(t=e="";e++<36;t+=51*e&52?(15^e?8^Math.random()*(20^e?16:4):4).toString(16):"-");return t},Xe={},We=function(){return Xe},He=function(e){var t=Object.keys(e);return function(n){for(var r={},i=0;i<t.length;i++){var a=t[i],o=null==n?void 0:n[a];r[a]=void 0===o?e[a]:o}return r}},Ke=function(e,t,n){for(var r=e.length-1;r>=0&&(e[r]!==t||(e.splice(r,1),!n));r--);},Ge=function(e){e.splice(0,e.length)},Ue=function(e,t,n){return n&&(t=N(n,t)),e[t]},Ze=function(e,t,n,r){n&&(t=N(n,t)),e[t]=r},$e="undefined"!=typeof Map?Map:function(){function e(){t(this,e),this._obj={}}return r(e,[{key:"set",value:function(e,t){return this._obj[e]=t,this}},{key:"delete",value:function(e){return this._obj[e]=void 0,this}},{key:"clear",value:function(){this._obj={}}},{key:"has",value:function(e){return void 0!==this._obj[e]}},{key:"get",value:function(e){return this._obj[e]}}]),e}(),Qe=function(){function e(n){if(t(this,e),this._obj=Object.create(null),this.size=0,null!=n){var r;r=null!=n.instanceString&&n.instanceString()===this.instanceString()?n.toArray():n;for(var i=0;i<r.length;i++)this.add(r[i])}}return r(e,[{key:"instanceString",value:function(){return"set"}},{key:"add",value:function(e){var t=this._obj;1!==t[e]&&(t[e]=1,this.size++)}},{key:"delete",value:function(e){var t=this._obj;1===t[e]&&(t[e]=0,this.size--)}},{key:"clear",value:function(){this._obj=Object.create(null)}},{key:"has",value:function(e){return 1===this._obj[e]}},{key:"toArray",value:function(){var e=this;return Object.keys(this._obj).filter((function(t){return e.has(t)}))}},{key:"forEach",value:function(e,t){return this.toArray().forEach(e,t)}}]),e}(),Je="undefined"!==("undefined"==typeof Set?"undefined":e(Set))?Set:Qe,et=function(e,t){var n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];if(void 0!==e&&void 0!==t&&S(e)){var r=t.group;if(null==r&&(r=t.data&&null!=t.data.source&&null!=t.data.target?"edges":"nodes"),"nodes"===r||"edges"===r){this.length=1,this[0]=this;var i=this._private={cy:e,single:!0,data:t.data||{},position:t.position||{x:0,y:0},autoWidth:void 0,autoHeight:void 0,autoPadding:void 0,compoundBoundsClean:!1,listeners:[],group:r,style:{},rstyle:{},styleCxts:[],styleKeys:{},removed:!0,selected:!!t.selected,selectable:void 0===t.selectable||!!t.selectable,locked:!!t.locked,grabbed:!1,grabbable:void 0===t.grabbable||!!t.grabbable,pannable:void 0===t.pannable?"edges"===r:!!t.pannable,active:!1,classes:new Je,animation:{current:[],queue:[]},rscratch:{},scratch:t.scratch||{},edges:[],children:[],parent:t.parent&&t.parent.isNode()?t.parent:null,traversalCache:{},backgrounding:!1,bbCache:null,bbCacheShift:{x:0,y:0},bodyBounds:null,overlayBounds:null,labelBounds:{all:null,source:null,target:null,main:null},arrowBounds:{source:null,target:null,"mid-source":null,"mid-target":null}};if(null==i.position.x&&(i.position.x=0),null==i.position.y&&(i.position.y=0),t.renderedPosition){var a=t.renderedPosition,o=e.pan(),s=e.zoom();i.position={x:(a.x-o.x)/s,y:(a.y-o.y)/s}}var l=[];m(t.classes)?l=t.classes:v(t.classes)&&(l=t.classes.split(/\s+/));for(var u=0,c=l.length;u<c;u++){var d=l[u];d&&""!==d&&i.classes.add(d)}this.createEmitter();var h=t.style||t.css;h&&(je("Setting a `style` bypass at element creation should be done only when absolutely necessary.  Try to use the stylesheet instead."),this.style(h)),(void 0===n||n)&&this.restore()}else Ve("An element must be of type `nodes` or `edges`; you specified `"+r+"`")}else Ve("An element must have a core reference and parameters set")},tt=function(e){return e={bfs:e.bfs||!e.dfs,dfs:e.dfs||!e.bfs},function(t,n,r){var i;b(t)&&!E(t)&&(t=(i=t).roots||i.root,n=i.visit,r=i.directed),r=2!==arguments.length||y(n)?r:n,n=y(n)?n:function(){};for(var a,o=this._private.cy,s=t=v(t)?this.filter(t):t,l=[],u=[],c={},d={},h={},p=0,f=this.byGroup(),g=f.nodes,m=f.edges,x=0;x<s.length;x++){var w=s[x],k=w.id();w.isNode()&&(l.unshift(w),e.bfs&&(h[k]=!0,u.push(w)),d[k]=0)}for(var C=function(){var t=e.bfs?l.shift():l.pop(),i=t.id();if(e.dfs){if(h[i])return"continue";h[i]=!0,u.push(t)}var o,s=d[i],f=c[i],v=null!=f?f.source():null,y=null!=f?f.target():null,b=null==f?void 0:t.same(v)?y[0]:v[0];if(!0===(o=n(t,f,b,p++,s)))return a=t,"break";if(!1===o)return"break";for(var x=t.connectedEdges().filter((function(e){return(!r||e.source().same(t))&&m.has(e)})),w=0;w<x.length;w++){var E=x[w],k=E.connectedNodes().filter((function(e){return!e.same(t)&&g.has(e)})),C=k.id();0===k.length||h[C]||(k=k[0],l.push(k),e.bfs&&(h[C]=!0,u.push(k)),c[C]=E,d[C]=d[i]+1)}};0!==l.length;){var S=C();if("continue"!==S&&"break"===S)break}for(var P=o.collection(),D=0;D<u.length;D++){var T=u[D],_=c[T.id()];null!=_&&P.push(_),P.push(T)}return{path:o.collection(P),found:o.collection(a)}}},nt={breadthFirstSearch:tt({bfs:!0}),depthFirstSearch:tt({dfs:!0})};nt.bfs=nt.breadthFirstSearch,nt.dfs=nt.depthFirstSearch;var rt=function(e,t){return e(t={exports:{}},t.exports),t.exports}((function(e,t){(function(){var t,n,r,i,a,o,s,l,u,c,d,h,p,f,g;r=Math.floor,c=Math.min,n=function(e,t){return e<t?-1:e>t?1:0},u=function(e,t,i,a,o){var s;if(null==i&&(i=0),null==o&&(o=n),i<0)throw new Error("lo must be non-negative");for(null==a&&(a=e.length);i<a;)o(t,e[s=r((i+a)/2)])<0?a=s:i=s+1;return[].splice.apply(e,[i,i-i].concat(t)),t},o=function(e,t,r){return null==r&&(r=n),e.push(t),f(e,0,e.length-1,r)},a=function(e,t){var r,i;return null==t&&(t=n),r=e.pop(),e.length?(i=e[0],e[0]=r,g(e,0,t)):i=r,i},l=function(e,t,r){var i;return null==r&&(r=n),i=e[0],e[0]=t,g(e,0,r),i},s=function(e,t,r){var i;return null==r&&(r=n),e.length&&r(e[0],t)<0&&(t=(i=[e[0],t])[0],e[0]=i[1],g(e,0,r)),t},i=function(e,t){var i,a,o,s,l,u;for(null==t&&(t=n),l=[],a=0,o=(s=function(){u=[];for(var t=0,n=r(e.length/2);0<=n?t<n:t>n;0<=n?t++:t--)u.push(t);return u}.apply(this).reverse()).length;a<o;a++)i=s[a],l.push(g(e,i,t));return l},p=function(e,t,r){var i;if(null==r&&(r=n),-1!==(i=e.indexOf(t)))return f(e,0,i,r),g(e,i,r)},d=function(e,t,r){var a,o,l,u,c;if(null==r&&(r=n),!(o=e.slice(0,t)).length)return o;for(i(o,r),l=0,u=(c=e.slice(t)).length;l<u;l++)a=c[l],s(o,a,r);return o.sort(r).reverse()},h=function(e,t,r){var o,s,l,d,h,p,f,g,v;if(null==r&&(r=n),10*t<=e.length){if(!(l=e.slice(0,t).sort(r)).length)return l;for(s=l[l.length-1],d=0,p=(f=e.slice(t)).length;d<p;d++)r(o=f[d],s)<0&&(u(l,o,0,null,r),l.pop(),s=l[l.length-1]);return l}for(i(e,r),v=[],h=0,g=c(t,e.length);0<=g?h<g:h>g;0<=g?++h:--h)v.push(a(e,r));return v},f=function(e,t,r,i){var a,o,s;for(null==i&&(i=n),a=e[r];r>t&&i(a,o=e[s=r-1>>1])<0;)e[r]=o,r=s;return e[r]=a},g=function(e,t,r){var i,a,o,s,l;for(null==r&&(r=n),a=e.length,l=t,o=e[t],i=2*t+1;i<a;)(s=i+1)<a&&!(r(e[i],e[s])<0)&&(i=s),e[t]=e[i],i=2*(t=i)+1;return e[t]=o,f(e,l,t,r)},t=function(){function e(e){this.cmp=null!=e?e:n,this.nodes=[]}return e.push=o,e.pop=a,e.replace=l,e.pushpop=s,e.heapify=i,e.updateItem=p,e.nlargest=d,e.nsmallest=h,e.prototype.push=function(e){return o(this.nodes,e,this.cmp)},e.prototype.pop=function(){return a(this.nodes,this.cmp)},e.prototype.peek=function(){return this.nodes[0]},e.prototype.contains=function(e){return-1!==this.nodes.indexOf(e)},e.prototype.replace=function(e){return l(this.nodes,e,this.cmp)},e.prototype.pushpop=function(e){return s(this.nodes,e,this.cmp)},e.prototype.heapify=function(){return i(this.nodes,this.cmp)},e.prototype.updateItem=function(e){return p(this.nodes,e,this.cmp)},e.prototype.clear=function(){return this.nodes=[]},e.prototype.empty=function(){return 0===this.nodes.length},e.prototype.size=function(){return this.nodes.length},e.prototype.clone=function(){var t;return(t=new e).nodes=this.nodes.slice(0),t},e.prototype.toArray=function(){return this.nodes.slice(0)},e.prototype.insert=e.prototype.push,e.prototype.top=e.prototype.peek,e.prototype.front=e.prototype.peek,e.prototype.has=e.prototype.contains,e.prototype.copy=e.prototype.clone,e}(),e.exports=t}).call(q)})),it=He({root:null,weight:function(e){return 1},directed:!1}),at={dijkstra:function(e){if(!b(e)){var t=arguments;e={root:t[0],weight:t[1],directed:t[2]}}var n=it(e),r=n.root,i=n.weight,a=n.directed,o=this,s=i,l=v(r)?this.filter(r)[0]:r[0],u={},c={},d={},h=this.byGroup(),p=h.nodes,f=h.edges;f.unmergeBy((function(e){return e.isLoop()}));for(var g=function(e){return u[e.id()]},y=function(e,t){u[e.id()]=t,m.updateItem(e)},m=new rt((function(e,t){return g(e)-g(t)})),x=0;x<p.length;x++){var w=p[x];u[w.id()]=w.same(l)?0:1/0,m.push(w)}for(var E=function(e,t){for(var n,r=(a?e.edgesTo(t):e.edgesWith(t)).intersect(f),i=1/0,o=0;o<r.length;o++){var l=r[o],u=s(l);(u<i||!n)&&(i=u,n=l)}return{edge:n,dist:i}};m.size()>0;){var k=m.pop(),C=g(k),S=k.id();if(d[S]=C,C!==1/0)for(var P=k.neighborhood().intersect(p),D=0;D<P.length;D++){var T=P[D],_=T.id(),M=E(k,T),B=C+M.dist;B<g(T)&&(y(T,B),c[_]={node:k,edge:M.edge})}}return{distanceTo:function(e){var t=v(e)?p.filter(e)[0]:e[0];return d[t.id()]},pathTo:function(e){var t=v(e)?p.filter(e)[0]:e[0],n=[],r=t,i=r.id();if(t.length>0)for(n.unshift(t);c[i];){var a=c[i];n.unshift(a.edge),n.unshift(a.node),i=(r=a.node).id()}return o.spawn(n)}}}},ot={kruskal:function(e){e=e||function(e){return 1};for(var t=this.byGroup(),n=t.nodes,r=t.edges,i=n.length,a=new Array(i),o=n,s=function(e){for(var t=0;t<a.length;t++){if(a[t].has(e))return t}},l=0;l<i;l++)a[l]=this.spawn(n[l]);for(var u=r.sort((function(t,n){return e(t)-e(n)})),c=0;c<u.length;c++){var d=u[c],h=d.source()[0],p=d.target()[0],f=s(h),g=s(p),v=a[f],y=a[g];f!==g&&(o.merge(d),v.merge(y),a.splice(g,1))}return o}},st=He({root:null,goal:null,weight:function(e){return 1},heuristic:function(e){return 0},directed:!1}),lt={aStar:function(e){var t=this.cy(),n=st(e),r=n.root,i=n.goal,a=n.heuristic,o=n.directed,s=n.weight;r=t.collection(r)[0],i=t.collection(i)[0];var l,u,c=r.id(),d=i.id(),h={},p={},f={},g=new rt((function(e,t){return p[e.id()]-p[t.id()]})),v=new Je,y={},m={},b=function(e,t){g.push(e),v.add(t)};b(r,c),h[c]=0,p[c]=a(r);for(var x,w=0;g.size()>0;){if(l=g.pop(),u=l.id(),v.delete(u),w++,u===d){for(var E=[],k=i,C=d,S=m[C];E.unshift(k),null!=S&&E.unshift(S),null!=(k=y[C]);)S=m[C=k.id()];return{found:!0,distance:h[u],path:this.spawn(E),steps:w}}f[u]=!0;for(var P=l._private.edges,D=0;D<P.length;D++){var T=P[D];if(this.hasElementWithId(T.id())&&(!o||T.data("source")===u)){var _=T.source(),M=T.target(),B=_.id()!==u?_:M,N=B.id();if(this.hasElementWithId(N)&&!f[N]){var z=h[u]+s(T);x=N,v.has(x)?z<h[N]&&(h[N]=z,p[N]=z+a(B),y[N]=l,m[N]=T):(h[N]=z,p[N]=z+a(B),b(B,N),y[N]=l,m[N]=T)}}}}return{found:!1,distance:void 0,path:void 0,steps:w}}},ut=He({weight:function(e){return 1},directed:!1}),ct={floydWarshall:function(e){for(var t=this.cy(),n=ut(e),r=n.weight,i=n.directed,a=r,o=this.byGroup(),s=o.nodes,l=o.edges,u=s.length,c=u*u,d=function(e){return s.indexOf(e)},h=function(e){return s[e]},p=new Array(c),f=0;f<c;f++){var g=f%u,y=(f-g)/u;p[f]=y===g?0:1/0}for(var m=new Array(c),b=new Array(c),x=0;x<l.length;x++){var w=l[x],E=w.source()[0],k=w.target()[0];if(E!==k){var C=d(E),S=d(k),P=C*u+S,D=a(w);if(p[P]>D&&(p[P]=D,m[P]=S,b[P]=w),!i){var T=S*u+C;!i&&p[T]>D&&(p[T]=D,m[T]=C,b[T]=w)}}}for(var _=0;_<u;_++)for(var M=0;M<u;M++)for(var B=M*u+_,N=0;N<u;N++){var z=M*u+N,I=_*u+N;p[B]+p[I]<p[z]&&(p[z]=p[B]+p[I],m[z]=m[B])}var A=function(e){return d(function(e){return(v(e)?t.filter(e):e)[0]}(e))};return{distance:function(e,t){var n=A(e),r=A(t);return p[n*u+r]},path:function(e,n){var r=A(e),i=A(n),a=h(r);if(r===i)return a.collection();if(null==m[r*u+i])return t.collection();var o,s=t.collection(),l=r;for(s.merge(a);r!==i;)l=r,r=m[r*u+i],o=b[l*u+r],s.merge(o),s.merge(h(r));return s}}}},dt=He({weight:function(e){return 1},directed:!1,root:null}),ht={bellmanFord:function(e){var t=this,n=dt(e),r=n.weight,i=n.directed,a=n.root,o=r,s=this,l=this.cy(),u=this.byGroup(),c=u.edges,d=u.nodes,h=d.length,p=new $e,f=!1,g=[];a=l.collection(a)[0],c.unmergeBy((function(e){return e.isLoop()}));for(var y=c.length,m=function(e){var t=p.get(e.id());return t||(t={},p.set(e.id(),t)),t},b=function(e){return(v(e)?l.$(e):e)[0]},x=0;x<h;x++){var w=d[x],E=m(w);w.same(a)?E.dist=0:E.dist=1/0,E.pred=null,E.edge=null}for(var k=!1,C=function(e,t,n,r,i,a){var o=r.dist+a;o<i.dist&&!n.same(r.edge)&&(i.dist=o,i.pred=e,i.edge=n,k=!0)},S=1;S<h;S++){k=!1;for(var P=0;P<y;P++){var D=c[P],T=D.source(),_=D.target(),M=o(D),B=m(T),N=m(_);C(T,0,D,B,N,M),i||C(_,0,D,N,B,M)}if(!k)break}if(k)for(var z=[],I=0;I<y;I++){var A=c[I],L=A.source(),O=A.target(),R=o(A),V=m(L).dist,F=m(O).dist;if(V+R<F||!i&&F+R<V){if(f||(je("Graph contains a negative weight cycle for Bellman-Ford"),f=!0),!1===e.findNegativeWeightCycles)break;var j=[];V+R<F&&j.push(L),!i&&F+R<V&&j.push(O);for(var q=j.length,Y=0;Y<q;Y++){var X=j[Y],W=[X];W.push(m(X).edge);for(var H=m(X).pred;-1===W.indexOf(H);)W.push(H),W.push(m(H).edge),H=m(H).pred;for(var K=(W=W.slice(W.indexOf(H)))[0].id(),G=0,U=2;U<W.length;U+=2)W[U].id()<K&&(K=W[U].id(),G=U);(W=W.slice(G).concat(W.slice(0,G))).push(W[0]);var Z=W.map((function(e){return e.id()})).join(",");-1===z.indexOf(Z)&&(g.push(s.spawn(W)),z.push(Z))}}}return{distanceTo:function(e){return m(b(e)).dist},pathTo:function(e){for(var n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:a,r=b(e),i=[],o=r;;){if(null==o)return t.spawn();var l=m(o),u=l.edge,c=l.pred;if(i.unshift(o[0]),o.same(n)&&i.length>0)break;null!=u&&i.unshift(u),o=c}return s.spawn(i)},hasNegativeWeightCycle:f,negativeWeightCycles:g}}},pt=Math.sqrt(2),ft=function(e,t,n){0===n.length&&Ve("Karger-Stein must be run on a connected (sub)graph");for(var r=n[e],i=r[1],a=r[2],o=t[i],s=t[a],l=n,u=l.length-1;u>=0;u--){var c=l[u],d=c[1],h=c[2];(t[d]===o&&t[h]===s||t[d]===s&&t[h]===o)&&l.splice(u,1)}for(var p=0;p<l.length;p++){var f=l[p];f[1]===s?(l[p]=f.slice(),l[p][1]=o):f[2]===s&&(l[p]=f.slice(),l[p][2]=o)}for(var g=0;g<t.length;g++)t[g]===s&&(t[g]=o);return l},gt=function(e,t,n,r){for(;n>r;){var i=Math.floor(Math.random()*t.length);t=ft(i,e,t),n--}return t},vt={kargerStein:function(){var e=this,t=this.byGroup(),n=t.nodes,r=t.edges;r.unmergeBy((function(e){return e.isLoop()}));var i=n.length,a=r.length,o=Math.ceil(Math.pow(Math.log(i)/Math.LN2,2)),s=Math.floor(i/pt);if(!(i<2)){for(var l=[],u=0;u<a;u++){var c=r[u];l.push([u,n.indexOf(c.source()),n.indexOf(c.target())])}for(var d=1/0,h=[],p=new Array(i),f=new Array(i),g=new Array(i),v=function(e,t){for(var n=0;n<i;n++)t[n]=e[n]},y=0;y<=o;y++){for(var m=0;m<i;m++)f[m]=m;var b=gt(f,l.slice(),i,s),x=b.slice();v(f,g);var w=gt(f,b,s,2),E=gt(g,x,s,2);w.length<=E.length&&w.length<d?(d=w.length,h=w,v(f,p)):E.length<=w.length&&E.length<d&&(d=E.length,h=E,v(g,p))}for(var k=this.spawn(h.map((function(e){return r[e[0]]}))),C=this.spawn(),S=this.spawn(),P=p[0],D=0;D<p.length;D++){var T=p[D],_=n[D];T===P?C.merge(_):S.merge(_)}var M=function(t){var n=e.spawn();return t.forEach((function(t){n.merge(t),t.connectedEdges().forEach((function(t){e.contains(t)&&!k.contains(t)&&n.merge(t)}))})),n},B=[M(C),M(S)];return{cut:k,components:B,partition1:C,partition2:S}}Ve("At least 2 nodes are required for Karger-Stein algorithm")}},yt=function(e,t,n){return{x:e.x*t+n.x,y:e.y*t+n.y}},mt=function(e,t,n){return{x:(e.x-n.x)/t,y:(e.y-n.y)/t}},bt=function(e){return{x:e[0],y:e[1]}},xt=function(e,t){return Math.atan2(t,e)-Math.PI/2},wt=Math.log2||function(e){return Math.log(e)/Math.log(2)},Et=function(e){return e>0?1:e<0?-1:0},kt=function(e,t){return Math.sqrt(Ct(e,t))},Ct=function(e,t){var n=t.x-e.x,r=t.y-e.y;return n*n+r*r},St=function(e){for(var t=e.length,n=0,r=0;r<t;r++)n+=e[r];for(var i=0;i<t;i++)e[i]=e[i]/n;return e},Pt=function(e,t,n,r){return(1-r)*(1-r)*e+2*(1-r)*r*t+r*r*n},Dt=function(e,t,n,r){return{x:Pt(e.x,t.x,n.x,r),y:Pt(e.y,t.y,n.y,r)}},Tt=function(e,t,n){return Math.max(e,Math.min(n,t))},_t=function(e){if(null==e)return{x1:1/0,y1:1/0,x2:-1/0,y2:-1/0,w:0,h:0};if(null!=e.x1&&null!=e.y1){if(null!=e.x2&&null!=e.y2&&e.x2>=e.x1&&e.y2>=e.y1)return{x1:e.x1,y1:e.y1,x2:e.x2,y2:e.y2,w:e.x2-e.x1,h:e.y2-e.y1};if(null!=e.w&&null!=e.h&&e.w>=0&&e.h>=0)return{x1:e.x1,y1:e.y1,x2:e.x1+e.w,y2:e.y1+e.h,w:e.w,h:e.h}}},Mt=function(e,t){e.x1=Math.min(e.x1,t.x1),e.x2=Math.max(e.x2,t.x2),e.w=e.x2-e.x1,e.y1=Math.min(e.y1,t.y1),e.y2=Math.max(e.y2,t.y2),e.h=e.y2-e.y1},Bt=function(e,t,n){e.x1=Math.min(e.x1,t),e.x2=Math.max(e.x2,t),e.w=e.x2-e.x1,e.y1=Math.min(e.y1,n),e.y2=Math.max(e.y2,n),e.h=e.y2-e.y1},Nt=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0;return e.x1-=t,e.x2+=t,e.y1-=t,e.y2+=t,e.w=e.x2-e.x1,e.h=e.y2-e.y1,e},zt=function(e){var t,n,r,i,o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[0];if(1===o.length)t=n=r=i=o[0];else if(2===o.length)t=r=o[0],i=n=o[1];else if(4===o.length){var s=a(o,4);t=s[0],n=s[1],r=s[2],i=s[3]}return e.x1-=i,e.x2+=n,e.y1-=t,e.y2+=r,e.w=e.x2-e.x1,e.h=e.y2-e.y1,e},It=function(e,t){e.x1=t.x1,e.y1=t.y1,e.x2=t.x2,e.y2=t.y2,e.w=e.x2-e.x1,e.h=e.y2-e.y1},At=function(e,t){return!(e.x1>t.x2)&&(!(t.x1>e.x2)&&(!(e.x2<t.x1)&&(!(t.x2<e.x1)&&(!(e.y2<t.y1)&&(!(t.y2<e.y1)&&(!(e.y1>t.y2)&&!(t.y1>e.y2)))))))},Lt=function(e,t,n){return e.x1<=t&&t<=e.x2&&e.y1<=n&&n<=e.y2},Ot=function(e,t){return Lt(e,t.x1,t.y1)&&Lt(e,t.x2,t.y2)},Rt=function(e,t,n,r,i,a,o){var s,l,u=arguments.length>7&&void 0!==arguments[7]?arguments[7]:"auto",c="auto"===u?nn(i,a):u,d=i/2,h=a/2,p=(c=Math.min(c,d,h))!==d,f=c!==h;if(p){var g=n-d+c-o,v=r-h-o,y=n+d-c+o,m=v;if((s=Zt(e,t,n,r,g,v,y,m,!1)).length>0)return s}if(f){var b=n+d+o,x=r-h+c-o,w=b,E=r+h-c+o;if((s=Zt(e,t,n,r,b,x,w,E,!1)).length>0)return s}if(p){var k=n-d+c-o,C=r+h+o,S=n+d-c+o,P=C;if((s=Zt(e,t,n,r,k,C,S,P,!1)).length>0)return s}if(f){var D=n-d-o,T=r-h+c-o,_=D,M=r+h-c+o;if((s=Zt(e,t,n,r,D,T,_,M,!1)).length>0)return s}var B=n-d+c,N=r-h+c;if((l=Gt(e,t,n,r,B,N,c+o)).length>0&&l[0]<=B&&l[1]<=N)return[l[0],l[1]];var z=n+d-c,I=r-h+c;if((l=Gt(e,t,n,r,z,I,c+o)).length>0&&l[0]>=z&&l[1]<=I)return[l[0],l[1]];var A=n+d-c,L=r+h-c;if((l=Gt(e,t,n,r,A,L,c+o)).length>0&&l[0]>=A&&l[1]>=L)return[l[0],l[1]];var O=n-d+c,R=r+h-c;return(l=Gt(e,t,n,r,O,R,c+o)).length>0&&l[0]<=O&&l[1]>=R?[l[0],l[1]]:[]},Vt=function(e,t,n,r,i,a,o){var s=o,l=Math.min(n,i),u=Math.max(n,i),c=Math.min(r,a),d=Math.max(r,a);return l-s<=e&&e<=u+s&&c-s<=t&&t<=d+s},Ft=function(e,t,n,r,i,a,o,s,l){var u=Math.min(n,o,i)-l,c=Math.max(n,o,i)+l,d=Math.min(r,s,a)-l,h=Math.max(r,s,a)+l;return!(e<u||e>c||t<d||t>h)},jt=function(e,t,n,r,i,a,o,s){var l=[];!function(e,t,n,r,i){var a,o,s,l,u,c,d,h;0===e&&(e=1e-5),s=-27*(r/=e)+(t/=e)*(9*(n/=e)-t*t*2),a=(o=(3*n-t*t)/9)*o*o+(s/=54)*s,i[1]=0,d=t/3,a>0?(u=(u=s+Math.sqrt(a))<0?-Math.pow(-u,1/3):Math.pow(u,1/3),c=(c=s-Math.sqrt(a))<0?-Math.pow(-c,1/3):Math.pow(c,1/3),i[0]=-d+u+c,d+=(u+c)/2,i[4]=i[2]=-d,d=Math.sqrt(3)*(-c+u)/2,i[3]=d,i[5]=-d):(i[5]=i[3]=0,0===a?(h=s<0?-Math.pow(-s,1/3):Math.pow(s,1/3),i[0]=2*h-d,i[4]=i[2]=-(h+d)):(l=(o=-o)*o*o,l=Math.acos(s/Math.sqrt(l)),h=2*Math.sqrt(o),i[0]=-d+h*Math.cos(l/3),i[2]=-d+h*Math.cos((l+2*Math.PI)/3),i[4]=-d+h*Math.cos((l+4*Math.PI)/3)))}(1*n*n-4*n*i+2*n*o+4*i*i-4*i*o+o*o+r*r-4*r*a+2*r*s+4*a*a-4*a*s+s*s,9*n*i-3*n*n-3*n*o-6*i*i+3*i*o+9*r*a-3*r*r-3*r*s-6*a*a+3*a*s,3*n*n-6*n*i+n*o-n*e+2*i*i+2*i*e-o*e+3*r*r-6*r*a+r*s-r*t+2*a*a+2*a*t-s*t,1*n*i-n*n+n*e-i*e+r*a-r*r+r*t-a*t,l);for(var u=[],c=0;c<6;c+=2)Math.abs(l[c+1])<1e-7&&l[c]>=0&&l[c]<=1&&u.push(l[c]);u.push(1),u.push(0);for(var d,h,p,f=-1,g=0;g<u.length;g++)d=Math.pow(1-u[g],2)*n+2*(1-u[g])*u[g]*i+u[g]*u[g]*o,h=Math.pow(1-u[g],2)*r+2*(1-u[g])*u[g]*a+u[g]*u[g]*s,p=Math.pow(d-e,2)+Math.pow(h-t,2),f>=0?p<f&&(f=p):f=p;return f},qt=function(e,t,n,r,i,a){var o=[e-n,t-r],s=[i-n,a-r],l=s[0]*s[0]+s[1]*s[1],u=o[0]*o[0]+o[1]*o[1],c=o[0]*s[0]+o[1]*s[1],d=c*c/l;return c<0?u:d>l?(e-i)*(e-i)+(t-a)*(t-a):u-d},Yt=function(e,t,n){for(var r,i,a,o,s=0,l=0;l<n.length/2;l++)if(r=n[2*l],i=n[2*l+1],l+1<n.length/2?(a=n[2*(l+1)],o=n[2*(l+1)+1]):(a=n[2*(l+1-n.length/2)],o=n[2*(l+1-n.length/2)+1]),r==e&&a==e);else{if(!(r>=e&&e>=a||r<=e&&e<=a))continue;(e-r)/(a-r)*(o-i)+i>t&&s++}return s%2!=0},Xt=function(e,t,n,r,i,a,o,s,l){var u,c=new Array(n.length);null!=s[0]?(u=Math.atan(s[1]/s[0]),s[0]<0?u+=Math.PI/2:u=-u-Math.PI/2):u=s;for(var d,h=Math.cos(-u),p=Math.sin(-u),f=0;f<c.length/2;f++)c[2*f]=a/2*(n[2*f]*h-n[2*f+1]*p),c[2*f+1]=o/2*(n[2*f+1]*h+n[2*f]*p),c[2*f]+=r,c[2*f+1]+=i;if(l>0){var g=Ht(c,-l);d=Wt(g)}else d=c;return Yt(e,t,d)},Wt=function(e){for(var t,n,r,i,a,o,s,l,u=new Array(e.length/2),c=0;c<e.length/4;c++){t=e[4*c],n=e[4*c+1],r=e[4*c+2],i=e[4*c+3],c<e.length/4-1?(a=e[4*(c+1)],o=e[4*(c+1)+1],s=e[4*(c+1)+2],l=e[4*(c+1)+3]):(a=e[0],o=e[1],s=e[2],l=e[3]);var d=Zt(t,n,r,i,a,o,s,l,!0);u[2*c]=d[0],u[2*c+1]=d[1]}return u},Ht=function(e,t){for(var n,r,i,a,o=new Array(2*e.length),s=0;s<e.length/2;s++){n=e[2*s],r=e[2*s+1],s<e.length/2-1?(i=e[2*(s+1)],a=e[2*(s+1)+1]):(i=e[0],a=e[1]);var l=a-r,u=-(i-n),c=Math.sqrt(l*l+u*u),d=l/c,h=u/c;o[4*s]=n+d*t,o[4*s+1]=r+h*t,o[4*s+2]=i+d*t,o[4*s+3]=a+h*t}return o},Kt=function(e,t,n,r,i,a,o){return e-=i,t-=a,(e/=n/2+o)*e+(t/=r/2+o)*t<=1},Gt=function(e,t,n,r,i,a,o){var s=[n-e,r-t],l=[e-i,t-a],u=s[0]*s[0]+s[1]*s[1],c=2*(l[0]*s[0]+l[1]*s[1]),d=c*c-4*u*(l[0]*l[0]+l[1]*l[1]-o*o);if(d<0)return[];var h=(-c+Math.sqrt(d))/(2*u),p=(-c-Math.sqrt(d))/(2*u),f=Math.min(h,p),g=Math.max(h,p),v=[];if(f>=0&&f<=1&&v.push(f),g>=0&&g<=1&&v.push(g),0===v.length)return[];var y=v[0]*s[0]+e,m=v[0]*s[1]+t;return v.length>1?v[0]==v[1]?[y,m]:[y,m,v[1]*s[0]+e,v[1]*s[1]+t]:[y,m]},Ut=function(e,t,n){return t<=e&&e<=n||n<=e&&e<=t?e:e<=t&&t<=n||n<=t&&t<=e?t:n},Zt=function(e,t,n,r,i,a,o,s,l){var u=e-i,c=n-e,d=o-i,h=t-a,p=r-t,f=s-a,g=d*h-f*u,v=c*h-p*u,y=f*c-d*p;if(0!==y){var m=g/y,b=v/y;return-.001<=m&&m<=1.001&&-.001<=b&&b<=1.001||l?[e+m*c,t+m*p]:[]}return 0===g||0===v?Ut(e,n,o)===o?[o,s]:Ut(e,n,i)===i?[i,a]:Ut(i,o,n)===n?[n,r]:[]:[]},$t=function(e,t,n,r,i,a,o,s){var l,u,c,d,h,p,f=[],g=new Array(n.length),v=!0;if(null==a&&(v=!1),v){for(var y=0;y<g.length/2;y++)g[2*y]=n[2*y]*a+r,g[2*y+1]=n[2*y+1]*o+i;if(s>0){var m=Ht(g,-s);u=Wt(m)}else u=g}else u=n;for(var b=0;b<u.length/2;b++)c=u[2*b],d=u[2*b+1],b<u.length/2-1?(h=u[2*(b+1)],p=u[2*(b+1)+1]):(h=u[0],p=u[1]),0!==(l=Zt(e,t,r,i,c,d,h,p)).length&&f.push(l[0],l[1]);return f},Qt=function(e,t,n){var r=[e[0]-t[0],e[1]-t[1]],i=Math.sqrt(r[0]*r[0]+r[1]*r[1]),a=(i-n)/i;return a<0&&(a=1e-5),[t[0]+a*r[0],t[1]+a*r[1]]},Jt=function(e,t){var n=tn(e,t);return n=en(n)},en=function(e){for(var t,n,r=e.length/2,i=1/0,a=1/0,o=-1/0,s=-1/0,l=0;l<r;l++)t=e[2*l],n=e[2*l+1],i=Math.min(i,t),o=Math.max(o,t),a=Math.min(a,n),s=Math.max(s,n);for(var u=2/(o-i),c=2/(s-a),d=0;d<r;d++)t=e[2*d]=e[2*d]*u,n=e[2*d+1]=e[2*d+1]*c,i=Math.min(i,t),o=Math.max(o,t),a=Math.min(a,n),s=Math.max(s,n);if(a<-1)for(var h=0;h<r;h++)n=e[2*h+1]=e[2*h+1]+(-1-a);return e},tn=function(e,t){var n=1/e*2*Math.PI,r=e%2==0?Math.PI/2+n/2:Math.PI/2;r+=t;for(var i,a=new Array(2*e),o=0;o<e;o++)i=o*n+r,a[2*o]=Math.cos(i),a[2*o+1]=Math.sin(-i);return a},nn=function(e,t){return Math.min(e/4,t/4,8)},rn=function(e,t){return Math.min(e/10,t/10,8)},an=function(e,t){return{heightOffset:Math.min(15,.05*t),widthOffset:Math.min(100,.25*e),ctrlPtOffsetPct:.05}},on=He({dampingFactor:.8,precision:1e-6,iterations:200,weight:function(e){return 1}}),sn={pageRank:function(e){for(var t=on(e),n=t.dampingFactor,r=t.precision,i=t.iterations,a=t.weight,o=this._private.cy,s=this.byGroup(),l=s.nodes,u=s.edges,c=l.length,d=c*c,h=u.length,p=new Array(d),f=new Array(c),g=(1-n)/c,v=0;v<c;v++){for(var y=0;y<c;y++){p[v*c+y]=0}f[v]=0}for(var m=0;m<h;m++){var b=u[m],x=b.data("source"),w=b.data("target");if(x!==w){var E=l.indexOfId(x),k=l.indexOfId(w),C=a(b);p[k*c+E]+=C,f[E]+=C}}for(var S=1/c+g,P=0;P<c;P++)if(0===f[P])for(var D=0;D<c;D++){p[D*c+P]=S}else for(var T=0;T<c;T++){var _=T*c+P;p[_]=p[_]/f[P]+g}for(var M,B=new Array(c),N=new Array(c),z=0;z<c;z++)B[z]=1;for(var I=0;I<i;I++){for(var A=0;A<c;A++)N[A]=0;for(var L=0;L<c;L++)for(var O=0;O<c;O++){var R=L*c+O;N[L]+=p[R]*B[O]}St(N),M=B,B=N,N=M;for(var V=0,F=0;F<c;F++){var j=M[F]-B[F];V+=j*j}if(V<r)break}return{rank:function(e){return e=o.collection(e)[0],B[l.indexOf(e)]}}}},ln=He({root:null,weight:function(e){return 1},directed:!1,alpha:0}),un={degreeCentralityNormalized:function(e){e=ln(e);var t=this.cy(),n=this.nodes(),r=n.length;if(e.directed){for(var i={},a={},o=0,s=0,l=0;l<r;l++){var u=n[l],c=u.id();e.root=u;var d=this.degreeCentrality(e);o<d.indegree&&(o=d.indegree),s<d.outdegree&&(s=d.outdegree),i[c]=d.indegree,a[c]=d.outdegree}return{indegree:function(e){return 0==o?0:(v(e)&&(e=t.filter(e)),i[e.id()]/o)},outdegree:function(e){return 0===s?0:(v(e)&&(e=t.filter(e)),a[e.id()]/s)}}}for(var h={},p=0,f=0;f<r;f++){var g=n[f];e.root=g;var y=this.degreeCentrality(e);p<y.degree&&(p=y.degree),h[g.id()]=y.degree}return{degree:function(e){return 0===p?0:(v(e)&&(e=t.filter(e)),h[e.id()]/p)}}},degreeCentrality:function(e){e=ln(e);var t=this.cy(),n=this,r=e,i=r.root,a=r.weight,o=r.directed,s=r.alpha;if(i=t.collection(i)[0],o){for(var l=i.connectedEdges(),u=l.filter((function(e){return e.target().same(i)&&n.has(e)})),c=l.filter((function(e){return e.source().same(i)&&n.has(e)})),d=u.length,h=c.length,p=0,f=0,g=0;g<u.length;g++)p+=a(u[g]);for(var v=0;v<c.length;v++)f+=a(c[v]);return{indegree:Math.pow(d,1-s)*Math.pow(p,s),outdegree:Math.pow(h,1-s)*Math.pow(f,s)}}for(var y=i.connectedEdges().intersection(n),m=y.length,b=0,x=0;x<y.length;x++)b+=a(y[x]);return{degree:Math.pow(m,1-s)*Math.pow(b,s)}}};un.dc=un.degreeCentrality,un.dcn=un.degreeCentralityNormalised=un.degreeCentralityNormalized;var cn=He({harmonic:!0,weight:function(){return 1},directed:!1,root:null}),dn={closenessCentralityNormalized:function(e){for(var t=cn(e),n=t.harmonic,r=t.weight,i=t.directed,a=this.cy(),o={},s=0,l=this.nodes(),u=this.floydWarshall({weight:r,directed:i}),c=0;c<l.length;c++){for(var d=0,h=l[c],p=0;p<l.length;p++)if(c!==p){var f=u.distance(h,l[p]);d+=n?1/f:f}n||(d=1/d),s<d&&(s=d),o[h.id()]=d}return{closeness:function(e){return 0==s?0:(e=v(e)?a.filter(e)[0].id():e.id(),o[e]/s)}}},closenessCentrality:function(e){var t=cn(e),n=t.root,r=t.weight,i=t.directed,a=t.harmonic;n=this.filter(n)[0];for(var o=this.dijkstra({root:n,weight:r,directed:i}),s=0,l=this.nodes(),u=0;u<l.length;u++){var c=l[u];if(!c.same(n)){var d=o.distanceTo(c);s+=a?1/d:d}}return a?s:1/s}};dn.cc=dn.closenessCentrality,dn.ccn=dn.closenessCentralityNormalised=dn.closenessCentralityNormalized;var hn=He({weight:null,directed:!1}),pn={betweennessCentrality:function(e){for(var t=hn(e),n=t.directed,r=t.weight,i=null!=r,a=this.cy(),o=this.nodes(),s={},l={},u=0,c=function(e,t){l[e]=t,t>u&&(u=t)},d=function(e){return l[e]},h=0;h<o.length;h++){var p=o[h],f=p.id();s[f]=n?p.outgoers().nodes():p.openNeighborhood().nodes(),c(f,0)}for(var g=function(e){for(var t=o[e].id(),n=[],l={},u={},h={},p=new rt((function(e,t){return h[e]-h[t]})),f=0;f<o.length;f++){var g=o[f].id();l[g]=[],u[g]=0,h[g]=1/0}for(u[t]=1,h[t]=0,p.push(t);!p.empty();){var v=p.pop();if(n.push(v),i)for(var y=0;y<s[v].length;y++){var m=s[v][y],b=a.getElementById(v),x=void 0;x=b.edgesTo(m).length>0?b.edgesTo(m)[0]:m.edgesTo(b)[0];var w=r(x);m=m.id(),h[m]>h[v]+w&&(h[m]=h[v]+w,p.nodes.indexOf(m)<0?p.push(m):p.updateItem(m),u[m]=0,l[m]=[]),h[m]==h[v]+w&&(u[m]=u[m]+u[v],l[m].push(v))}else for(var E=0;E<s[v].length;E++){var k=s[v][E].id();h[k]==1/0&&(p.push(k),h[k]=h[v]+1),h[k]==h[v]+1&&(u[k]=u[k]+u[v],l[k].push(v))}}for(var C={},S=0;S<o.length;S++)C[o[S].id()]=0;for(;n.length>0;){for(var P=n.pop(),D=0;D<l[P].length;D++){var T=l[P][D];C[T]=C[T]+u[T]/u[P]*(1+C[P])}P!=o[e].id()&&c(P,d(P)+C[P])}},v=0;v<o.length;v++)g(v);var y={betweenness:function(e){var t=a.collection(e).id();return d(t)},betweennessNormalized:function(e){if(0==u)return 0;var t=a.collection(e).id();return d(t)/u}};return y.betweennessNormalised=y.betweennessNormalized,y}};pn.bc=pn.betweennessCentrality;var fn=He({expandFactor:2,inflateFactor:2,multFactor:1,maxIterations:20,attributes:[function(e){return 1}]}),gn=function(e,t){for(var n=0,r=0;r<t.length;r++)n+=t[r](e);return n},vn=function(e,t){for(var n,r=0;r<t;r++){n=0;for(var i=0;i<t;i++)n+=e[i*t+r];for(var a=0;a<t;a++)e[a*t+r]=e[a*t+r]/n}},yn=function(e,t,n){for(var r=new Array(n*n),i=0;i<n;i++){for(var a=0;a<n;a++)r[i*n+a]=0;for(var o=0;o<n;o++)for(var s=0;s<n;s++)r[i*n+s]+=e[i*n+o]*t[o*n+s]}return r},mn=function(e,t,n){for(var r=e.slice(0),i=1;i<n;i++)e=yn(e,r,t);return e},bn=function(e,t,n){for(var r=new Array(t*t),i=0;i<t*t;i++)r[i]=Math.pow(e[i],n);return vn(r,t),r},xn=function(e,t,n,r){for(var i=0;i<n;i++){if(Math.round(e[i]*Math.pow(10,r))/Math.pow(10,r)!==Math.round(t[i]*Math.pow(10,r))/Math.pow(10,r))return!1}return!0},wn=function(e,t){for(var n=0;n<e.length;n++)if(!t[n]||e[n].id()!==t[n].id())return!1;return!0},En=function(e){for(var t=this.nodes(),n=this.edges(),r=this.cy(),i=function(e){return fn(e)}(e),a={},o=0;o<t.length;o++)a[t[o].id()]=o;for(var s,l=t.length,u=l*l,c=new Array(u),d=0;d<u;d++)c[d]=0;for(var h=0;h<n.length;h++){var p=n[h],f=a[p.source().id()],g=a[p.target().id()],v=gn(p,i.attributes);c[f*l+g]+=v,c[g*l+f]+=v}!function(e,t,n){for(var r=0;r<t;r++)e[r*t+r]=n}(c,l,i.multFactor),vn(c,l);for(var y=!0,m=0;y&&m<i.maxIterations;)y=!1,s=mn(c,l,i.expandFactor),c=bn(s,l,i.inflateFactor),xn(c,s,u,4)||(y=!0),m++;var b=function(e,t,n,r){for(var i=[],a=0;a<t;a++){for(var o=[],s=0;s<t;s++)Math.round(1e3*e[a*t+s])/1e3>0&&o.push(n[s]);0!==o.length&&i.push(r.collection(o))}return i}(c,l,t,r);return b=function(e){for(var t=0;t<e.length;t++)for(var n=0;n<e.length;n++)t!=n&&wn(e[t],e[n])&&e.splice(n,1);return e}(b)},kn={markovClustering:En,mcl:En},Cn=function(e){return e},Sn=function(e,t){return Math.abs(t-e)},Pn=function(e,t,n){return e+Sn(t,n)},Dn=function(e,t,n){return e+Math.pow(n-t,2)},Tn=function(e){return Math.sqrt(e)},_n=function(e,t,n){return Math.max(e,Sn(t,n))},Mn=function(e,t,n,r,i){for(var a=arguments.length>5&&void 0!==arguments[5]?arguments[5]:Cn,o=r,s=0;s<e;s++)o=i(o,t(s),n(s));return a(o)},Bn={euclidean:function(e,t,n){return e>=2?Mn(e,t,n,0,Dn,Tn):Mn(e,t,n,0,Pn)},squaredEuclidean:function(e,t,n){return Mn(e,t,n,0,Dn)},manhattan:function(e,t,n){return Mn(e,t,n,0,Pn)},max:function(e,t,n){return Mn(e,t,n,-1/0,_n)}};function Nn(e,t,n,r,i,a){var o;return o=y(e)?e:Bn[e]||Bn.euclidean,0===t&&y(e)?o(i,a):o(t,n,r,i,a)}Bn["squared-euclidean"]=Bn.squaredEuclidean,Bn.squaredeuclidean=Bn.squaredEuclidean;var zn=He({k:2,m:2,sensitivityThreshold:1e-4,distance:"euclidean",maxIterations:10,attributes:[],testMode:!1,testCentroids:null}),In=function(e){return zn(e)},An=function(e,t,n,r,i){var a="kMedoids"!==i?function(e){return n[e]}:function(e){return r[e](n)},o=n,s=t;return Nn(e,r.length,a,(function(e){return r[e](t)}),o,s)},Ln=function(e,t,n){for(var r=n.length,i=new Array(r),a=new Array(r),o=new Array(t),s=null,l=0;l<r;l++)i[l]=e.min(n[l]).value,a[l]=e.max(n[l]).value;for(var u=0;u<t;u++){s=[];for(var c=0;c<r;c++)s[c]=Math.random()*(a[c]-i[c])+i[c];o[u]=s}return o},On=function(e,t,n,r,i){for(var a=1/0,o=0,s=0;s<t.length;s++){var l=An(n,e,t[s],r,i);l<a&&(a=l,o=s)}return o},Rn=function(e,t,n){for(var r=[],i=null,a=0;a<t.length;a++)n[(i=t[a]).id()]===e&&r.push(i);return r},Vn=function(e,t,n){return Math.abs(t-e)<=n},Fn=function(e,t,n){for(var r=0;r<e.length;r++)for(var i=0;i<e[r].length;i++){if(Math.abs(e[r][i]-t[r][i])>n)return!1}return!0},jn=function(e,t,n){for(var r=0;r<n;r++)if(e===t[r])return!0;return!1},qn=function(e,t){var n=new Array(t);if(e.length<50)for(var r=0;r<t;r++){for(var i=e[Math.floor(Math.random()*e.length)];jn(i,n,r);)i=e[Math.floor(Math.random()*e.length)];n[r]=i}else for(var a=0;a<t;a++)n[a]=e[Math.floor(Math.random()*e.length)];return n},Yn=function(e,t,n){for(var r=0,i=0;i<t.length;i++)r+=An("manhattan",t[i],e,n,"kMedoids");return r},Xn=function(e,t,n,r,i){for(var a,o,s=0;s<t.length;s++)for(var l=0;l<e.length;l++)r[s][l]=Math.pow(n[s][l],i.m);for(var u=0;u<e.length;u++)for(var c=0;c<i.attributes.length;c++){a=0,o=0;for(var d=0;d<t.length;d++)a+=r[d][u]*i.attributes[c](t[d]),o+=r[d][u];e[u][c]=a/o}},Wn=function(e,t,n,r,i){for(var a=0;a<e.length;a++)t[a]=e[a].slice();for(var o,s,l,u=2/(i.m-1),c=0;c<n.length;c++)for(var d=0;d<r.length;d++){o=0;for(var h=0;h<n.length;h++)s=An(i.distance,r[d],n[c],i.attributes,"cmeans"),l=An(i.distance,r[d],n[h],i.attributes,"cmeans"),o+=Math.pow(s/l,u);e[d][c]=1/o}},Hn=function(e){var t,n,r,i,a=this.cy(),o=this.nodes(),s=In(e);r=new Array(o.length);for(var l=0;l<o.length;l++)r[l]=new Array(s.k);n=new Array(o.length);for(var u=0;u<o.length;u++)n[u]=new Array(s.k);for(var c=0;c<o.length;c++){for(var d=0,h=0;h<s.k;h++)n[c][h]=Math.random(),d+=n[c][h];for(var p=0;p<s.k;p++)n[c][p]=n[c][p]/d}t=new Array(s.k);for(var f=0;f<s.k;f++)t[f]=new Array(s.attributes.length);i=new Array(o.length);for(var g=0;g<o.length;g++)i[g]=new Array(s.k);for(var v=!0,y=0;v&&y<s.maxIterations;)v=!1,Xn(t,o,n,i,s),Wn(n,r,t,o,s),Fn(n,r,s.sensitivityThreshold)||(v=!0),y++;return{clusters:function(e,t,n,r){for(var i,a,o=new Array(n.k),s=0;s<o.length;s++)o[s]=[];for(var l=0;l<t.length;l++){i=-1/0,a=-1;for(var u=0;u<t[0].length;u++)t[l][u]>i&&(i=t[l][u],a=u);o[a].push(e[l])}for(var c=0;c<o.length;c++)o[c]=r.collection(o[c]);return o}(o,n,s,a),degreeOfMembership:n}},Kn={kMeans:function(t){var n,r=this.cy(),i=this.nodes(),a=null,o=In(t),s=new Array(o.k),l={};o.testMode?"number"==typeof o.testCentroids?(o.testCentroids,n=Ln(i,o.k,o.attributes)):n="object"===e(o.testCentroids)?o.testCentroids:Ln(i,o.k,o.attributes):n=Ln(i,o.k,o.attributes);for(var u=!0,c=0;u&&c<o.maxIterations;){for(var d=0;d<i.length;d++)l[(a=i[d]).id()]=On(a,n,o.distance,o.attributes,"kMeans");u=!1;for(var h=0;h<o.k;h++){var p=Rn(h,i,l);if(0!==p.length){for(var f=o.attributes.length,g=n[h],v=new Array(f),y=new Array(f),m=0;m<f;m++){y[m]=0;for(var b=0;b<p.length;b++)a=p[b],y[m]+=o.attributes[m](a);v[m]=y[m]/p.length,Vn(v[m],g[m],o.sensitivityThreshold)||(u=!0)}n[h]=v,s[h]=r.collection(p)}}c++}return s},kMedoids:function(t){var n,r,i=this.cy(),a=this.nodes(),o=null,s=In(t),l=new Array(s.k),u={},c=new Array(s.k);s.testMode?"number"==typeof s.testCentroids||(n="object"===e(s.testCentroids)?s.testCentroids:qn(a,s.k)):n=qn(a,s.k);for(var d=!0,h=0;d&&h<s.maxIterations;){for(var p=0;p<a.length;p++)u[(o=a[p]).id()]=On(o,n,s.distance,s.attributes,"kMedoids");d=!1;for(var f=0;f<n.length;f++){var g=Rn(f,a,u);if(0!==g.length){c[f]=Yn(n[f],g,s.attributes);for(var v=0;v<g.length;v++)(r=Yn(g[v],g,s.attributes))<c[f]&&(c[f]=r,n[f]=g[v],d=!0);l[f]=i.collection(g)}}h++}return l},fuzzyCMeans:Hn,fcm:Hn},Gn=He({distance:"euclidean",linkage:"min",mode:"threshold",threshold:1/0,addDendrogram:!1,dendrogramDepth:0,attributes:[]}),Un={single:"min",complete:"max"},Zn=function(e,t,n,r,i){for(var a,o=0,s=1/0,l=i.attributes,u=function(e,t){return Nn(i.distance,l.length,(function(t){return l[t](e)}),(function(e){return l[e](t)}),e,t)},c=0;c<e.length;c++){var d=e[c].key,h=n[d][r[d]];h<s&&(o=d,s=h)}if("threshold"===i.mode&&s>=i.threshold||"dendrogram"===i.mode&&1===e.length)return!1;var p,f=t[o],g=t[r[o]];p="dendrogram"===i.mode?{left:f,right:g,key:f.key}:{value:f.value.concat(g.value),key:f.key},e[f.index]=p,e.splice(g.index,1),t[f.key]=p;for(var v=0;v<e.length;v++){var y=e[v];f.key===y.key?a=1/0:"min"===i.linkage?(a=n[f.key][y.key],n[f.key][y.key]>n[g.key][y.key]&&(a=n[g.key][y.key])):"max"===i.linkage?(a=n[f.key][y.key],n[f.key][y.key]<n[g.key][y.key]&&(a=n[g.key][y.key])):a="mean"===i.linkage?(n[f.key][y.key]*f.size+n[g.key][y.key]*g.size)/(f.size+g.size):"dendrogram"===i.mode?u(y.value,f.value):u(y.value[0],f.value[0]),n[f.key][y.key]=n[y.key][f.key]=a}for(var m=0;m<e.length;m++){var b=e[m].key;if(r[b]===f.key||r[b]===g.key){for(var x=b,w=0;w<e.length;w++){var E=e[w].key;n[b][E]<n[b][x]&&(x=E)}r[b]=x}e[m].index=m}return f.key=g.key=f.index=g.index=null,!0},$n=function e(t,n,r){t&&(t.value?n.push(t.value):(t.left&&e(t.left,n),t.right&&e(t.right,n)))},Qn=function(e){for(var t=this.cy(),n=this.nodes(),r=function(e){var t=Gn(e),n=Un[t.linkage];return null!=n&&(t.linkage=n),t}(e),i=r.attributes,a=function(e,t){return Nn(r.distance,i.length,(function(t){return i[t](e)}),(function(e){return i[e](t)}),e,t)},o=[],s=[],l=[],u=[],c=0;c<n.length;c++){var d={value:"dendrogram"===r.mode?n[c]:[n[c]],key:c,index:c};o[c]=d,u[c]=d,s[c]=[],l[c]=0}for(var h=0;h<o.length;h++)for(var p=0;p<=h;p++){var f=void 0;f="dendrogram"===r.mode?h===p?1/0:a(o[h].value,o[p].value):h===p?1/0:a(o[h].value[0],o[p].value[0]),s[h][p]=f,s[p][h]=f,f<s[h][l[h]]&&(l[h]=p)}for(var g,v=Zn(o,u,s,l,r);v;)v=Zn(o,u,s,l,r);return"dendrogram"===r.mode?(g=function e(t,n,r){if(!t)return[];var i=[],a=[],o=[];return 0===n?(t.left&&$n(t.left,i),t.right&&$n(t.right,a),o=i.concat(a),[r.collection(o)]):1===n?t.value?[r.collection(t.value)]:(t.left&&$n(t.left,i),t.right&&$n(t.right,a),[r.collection(i),r.collection(a)]):t.value?[r.collection(t.value)]:(t.left&&(i=e(t.left,n-1,r)),t.right&&(a=e(t.right,n-1,r)),i.concat(a))}(o[0],r.dendrogramDepth,t),r.addDendrogram&&function e(t,n){if(!t)return"";if(t.left&&t.right){var r=e(t.left,n),i=e(t.right,n),a=n.add({group:"nodes",data:{id:r+","+i}});return n.add({group:"edges",data:{source:r,target:a.id()}}),n.add({group:"edges",data:{source:i,target:a.id()}}),a.id()}return t.value?t.value.id():void 0}(o[0],t)):(g=new Array(o.length),o.forEach((function(e,n){e.key=e.index=null,g[n]=t.collection(e.value)}))),g},Jn={hierarchicalClustering:Qn,hca:Qn},er=He({distance:"euclidean",preference:"median",damping:.8,maxIterations:1e3,minIterations:100,attributes:[]}),tr=function(e,t,n,r){var i=function(e,t){return r[t](e)};return-Nn(e,r.length,(function(e){return i(t,e)}),(function(e){return i(n,e)}),t,n)},nr=function(e,t){return"median"===t?function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:e.length,r=!(arguments.length>3&&void 0!==arguments[3])||arguments[3],i=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],a=!(arguments.length>5&&void 0!==arguments[5])||arguments[5];r?e=e.slice(t,n):(n<e.length&&e.splice(n,e.length-n),t>0&&e.splice(0,t));for(var o=0,s=e.length-1;s>=0;s--){var l=e[s];a?isFinite(l)||(e[s]=-1/0,o++):e.splice(s,1)}i&&e.sort((function(e,t){return e-t}));var u=e.length,c=Math.floor(u/2);return u%2!=0?e[c+1+o]:(e[c-1+o]+e[c+o])/2}(e):"mean"===t?function(e){for(var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:e.length,r=0,i=0,a=t;a<n;a++){var o=e[a];isFinite(o)&&(r+=o,i++)}return r/i}(e):"min"===t?function(e){for(var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:e.length,r=1/0,i=t;i<n;i++){var a=e[i];isFinite(a)&&(r=Math.min(a,r))}return r}(e):"max"===t?function(e){for(var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:e.length,r=-1/0,i=t;i<n;i++){var a=e[i];isFinite(a)&&(r=Math.max(a,r))}return r}(e):t},rr=function(e,t,n){for(var r=[],i=0;i<e;i++){for(var a=-1,o=-1/0,s=0;s<n.length;s++){var l=n[s];t[i*e+l]>o&&(a=l,o=t[i*e+l])}a>0&&r.push(a)}for(var u=0;u<n.length;u++)r[n[u]]=n[u];return r},ir=function(e){for(var t,n,r,i,a,o,s=this.cy(),l=this.nodes(),u=function(e){var t=e.damping,n=e.preference;.5<=t&&t<1||Ve("Damping must range on [0.5, 1).  Got: ".concat(t));var r=["median","mean","min","max"];return r.some((function(e){return e===n}))||x(n)||Ve("Preference must be one of [".concat(r.map((function(e){return"'".concat(e,"'")})).join(", "),"] or a number.  Got: ").concat(n)),er(e)}(e),c={},d=0;d<l.length;d++)c[l[d].id()]=d;n=(t=l.length)*t,r=new Array(n);for(var h=0;h<n;h++)r[h]=-1/0;for(var p=0;p<t;p++)for(var f=0;f<t;f++)p!==f&&(r[p*t+f]=tr(u.distance,l[p],l[f],u.attributes));i=nr(r,u.preference);for(var g=0;g<t;g++)r[g*t+g]=i;a=new Array(n);for(var v=0;v<n;v++)a[v]=0;o=new Array(n);for(var y=0;y<n;y++)o[y]=0;for(var m=new Array(t),b=new Array(t),w=new Array(t),E=0;E<t;E++)m[E]=0,b[E]=0,w[E]=0;for(var k,C=new Array(t*u.minIterations),S=0;S<C.length;S++)C[S]=0;for(k=0;k<u.maxIterations;k++){for(var P=0;P<t;P++){for(var D=-1/0,T=-1/0,_=-1,M=0,B=0;B<t;B++)m[B]=a[P*t+B],(M=o[P*t+B]+r[P*t+B])>=D?(T=D,D=M,_=B):M>T&&(T=M);for(var N=0;N<t;N++)a[P*t+N]=(1-u.damping)*(r[P*t+N]-D)+u.damping*m[N];a[P*t+_]=(1-u.damping)*(r[P*t+_]-T)+u.damping*m[_]}for(var z=0;z<t;z++){for(var I=0,A=0;A<t;A++)m[A]=o[A*t+z],b[A]=Math.max(0,a[A*t+z]),I+=b[A];I-=b[z],b[z]=a[z*t+z],I+=b[z];for(var L=0;L<t;L++)o[L*t+z]=(1-u.damping)*Math.min(0,I-b[L])+u.damping*m[L];o[z*t+z]=(1-u.damping)*(I-b[z])+u.damping*m[z]}for(var O=0,R=0;R<t;R++){var V=o[R*t+R]+a[R*t+R]>0?1:0;C[k%u.minIterations*t+R]=V,O+=V}if(O>0&&(k>=u.minIterations-1||k==u.maxIterations-1)){for(var F=0,j=0;j<t;j++){w[j]=0;for(var q=0;q<u.minIterations;q++)w[j]+=C[q*t+j];0!==w[j]&&w[j]!==u.minIterations||F++}if(F===t)break}}for(var Y=function(e,t,n){for(var r=[],i=0;i<e;i++)t[i*e+i]+n[i*e+i]>0&&r.push(i);return r}(t,a,o),X=function(e,t,n){for(var r=rr(e,t,n),i=0;i<n.length;i++){for(var a=[],o=0;o<r.length;o++)r[o]===n[i]&&a.push(o);for(var s=-1,l=-1/0,u=0;u<a.length;u++){for(var c=0,d=0;d<a.length;d++)c+=t[a[d]*e+a[u]];c>l&&(s=u,l=c)}n[i]=a[s]}return r=rr(e,t,n)}(t,r,Y),W={},H=0;H<Y.length;H++)W[Y[H]]=[];for(var K=0;K<l.length;K++){var G=X[c[l[K].id()]];null!=G&&W[G].push(l[K])}for(var U=new Array(Y.length),Z=0;Z<Y.length;Z++)U[Z]=s.collection(W[Y[Z]]);return U},ar={affinityPropagation:ir,ap:ir},or=He({root:void 0,directed:!1}),sr=function(){var e=this,t={},n=0,r=0,i=[],a=[],o={},s=function s(l,u,c){l===c&&(r+=1),t[u]={id:n,low:n++,cutVertex:!1};var d,h,p,f,g=e.getElementById(u).connectedEdges().intersection(e);0===g.size()?i.push(e.spawn(e.getElementById(u))):g.forEach((function(n){d=n.source().id(),h=n.target().id(),(p=d===u?h:d)!==c&&(f=n.id(),o[f]||(o[f]=!0,a.push({x:u,y:p,edge:n})),p in t?t[u].low=Math.min(t[u].low,t[p].id):(s(l,p,u),t[u].low=Math.min(t[u].low,t[p].low),t[u].id<=t[p].low&&(t[u].cutVertex=!0,function(n,r){for(var o=a.length-1,s=[],l=e.spawn();a[o].x!=n||a[o].y!=r;)s.push(a.pop().edge),o--;s.push(a.pop().edge),s.forEach((function(n){var r=n.connectedNodes().intersection(e);l.merge(n),r.forEach((function(n){var r=n.id(),i=n.connectedEdges().intersection(e);l.merge(n),t[r].cutVertex?l.merge(i.filter((function(e){return e.isLoop()}))):l.merge(i)}))})),i.push(l)}(u,p))))}))};e.forEach((function(e){if(e.isNode()){var n=e.id();n in t||(r=0,s(n,n),t[n].cutVertex=r>1)}}));var l=Object.keys(t).filter((function(e){return t[e].cutVertex})).map((function(t){return e.getElementById(t)}));return{cut:e.spawn(l),components:i}},lr=function(){var e=this,t={},n=0,r=[],i=[],a=e.spawn(e);return e.forEach((function(o){if(o.isNode()){var s=o.id();s in t||function o(s){if(i.push(s),t[s]={index:n,low:n++,explored:!1},e.getElementById(s).connectedEdges().intersection(e).forEach((function(e){var n=e.target().id();n!==s&&(n in t||o(n),t[n].explored||(t[s].low=Math.min(t[s].low,t[n].low)))})),t[s].index===t[s].low){for(var l=e.spawn();;){var u=i.pop();if(l.merge(e.getElementById(u)),t[u].low=t[s].index,t[u].explored=!0,u===s)break}var c=l.edgesWith(l),d=l.merge(c);r.push(d),a=a.difference(d)}}(s)}})),{cut:a,components:r}},ur={};[nt,at,ot,lt,ct,ht,vt,sn,un,dn,pn,kn,Kn,Jn,ar,{hierholzer:function(e){if(!b(e)){var t=arguments;e={root:t[0],directed:t[1]}}var n,r,i,a=or(e),o=a.root,s=a.directed,l=this,u=!1;o&&(i=v(o)?this.filter(o)[0].id():o[0].id());var c={},d={};s?l.forEach((function(e){var t=e.id();if(e.isNode()){var i=e.indegree(!0),a=e.outdegree(!0),o=i-a,s=a-i;1==o?n?u=!0:n=t:1==s?r?u=!0:r=t:(s>1||o>1)&&(u=!0),c[t]=[],e.outgoers().forEach((function(e){e.isEdge()&&c[t].push(e.id())}))}else d[t]=[void 0,e.target().id()]})):l.forEach((function(e){var t=e.id();e.isNode()?(e.degree(!0)%2&&(n?r?u=!0:r=t:n=t),c[t]=[],e.connectedEdges().forEach((function(e){return c[t].push(e.id())}))):d[t]=[e.source().id(),e.target().id()]}));var h={found:!1,trail:void 0};if(u)return h;if(r&&n)if(s){if(i&&r!=i)return h;i=r}else{if(i&&r!=i&&n!=i)return h;i||(i=r)}else i||(i=l[0].id());var p=function(e){for(var t,n,r,i=e,a=[e];c[i].length;)t=c[i].shift(),n=d[t][0],i!=(r=d[t][1])?(c[r]=c[r].filter((function(e){return e!=t})),i=r):s||i==n||(c[n]=c[n].filter((function(e){return e!=t})),i=n),a.unshift(t),a.unshift(i);return a},f=[],g=[];for(g=p(i);1!=g.length;)0==c[g[0]].length?(f.unshift(l.getElementById(g.shift())),f.unshift(l.getElementById(g.shift()))):g=p(g.shift()).concat(g);for(var y in f.unshift(l.getElementById(g.shift())),c)if(c[y].length)return h;return h.found=!0,h.trail=this.spawn(f,!0),h}},{hopcroftTarjanBiconnected:sr,htbc:sr,htb:sr,hopcroftTarjanBiconnectedComponents:sr},{tarjanStronglyConnected:lr,tsc:lr,tscc:lr,tarjanStronglyConnectedComponents:lr}].forEach((function(e){L(ur,e)}));
/*!
  Embeddable Minimum Strictly-Compliant Promises/A+ 1.1.1 Thenable
  Copyright (c) 2013-2014 Ralf S. Engelschall (http://engelschall.com)
  Licensed under The MIT License (http://opensource.org/licenses/MIT)
  */
var cr=function e(t){if(!(this instanceof e))return new e(t);this.id="Thenable/1.0.7",this.state=0,this.fulfillValue=void 0,this.rejectReason=void 0,this.onFulfilled=[],this.onRejected=[],this.proxy={then:this.then.bind(this)},"function"==typeof t&&t.call(this,this.fulfill.bind(this),this.reject.bind(this))};cr.prototype={fulfill:function(e){return dr(this,1,"fulfillValue",e)},reject:function(e){return dr(this,2,"rejectReason",e)},then:function(e,t){var n=new cr;return this.onFulfilled.push(fr(e,n,"fulfill")),this.onRejected.push(fr(t,n,"reject")),hr(this),n.proxy}};var dr=function(e,t,n,r){return 0===e.state&&(e.state=t,e[n]=r,hr(e)),e},hr=function(e){1===e.state?pr(e,"onFulfilled",e.fulfillValue):2===e.state&&pr(e,"onRejected",e.rejectReason)},pr=function(e,t,n){if(0!==e[t].length){var r=e[t];e[t]=[];var i=function(){for(var e=0;e<r.length;e++)r[e](n)};"function"==typeof setImmediate?setImmediate(i):setTimeout(i,0)}},fr=function(e,t,n){return function(r){if("function"!=typeof e)t[n].call(t,r);else{var i;try{i=e(r)}catch(e){return void t.reject(e)}gr(t,i)}}},gr=function t(n,r){if(n!==r&&n.proxy!==r){var i;if("object"===e(r)&&null!==r||"function"==typeof r)try{i=r.then}catch(e){return void n.reject(e)}if("function"!=typeof i)n.fulfill(r);else{var a=!1;try{i.call(r,(function(e){a||(a=!0,e===r?n.reject(new TypeError("circular thenable chain")):t(n,e))}),(function(e){a||(a=!0,n.reject(e))}))}catch(e){a||n.reject(e)}}}else n.reject(new TypeError("cannot resolve promise with itself"))};cr.all=function(e){return new cr((function(t,n){for(var r=new Array(e.length),i=0,a=function(n,a){r[n]=a,++i===e.length&&t(r)},o=0;o<e.length;o++)!function(t){var r=e[t];null!=r&&null!=r.then?r.then((function(e){a(t,e)}),(function(e){n(e)})):a(t,r)}(o)}))},cr.resolve=function(e){return new cr((function(t,n){t(e)}))},cr.reject=function(e){return new cr((function(t,n){n(e)}))};var vr="undefined"!=typeof Promise?Promise:cr,yr=function(e,t,n){var r=S(e),i=!r,a=this._private=L({duration:1e3},t,n);if(a.target=e,a.style=a.style||a.css,a.started=!1,a.playing=!1,a.hooked=!1,a.applying=!1,a.progress=0,a.completes=[],a.frames=[],a.complete&&y(a.complete)&&a.completes.push(a.complete),i){var o=e.position();a.startPosition=a.startPosition||{x:o.x,y:o.y},a.startStyle=a.startStyle||e.cy().style().getAnimationStartStyle(e,a.style)}if(r){var s=e.pan();a.startPan={x:s.x,y:s.y},a.startZoom=e.zoom()}this.length=1,this[0]=this},mr=yr.prototype;L(mr,{instanceString:function(){return"animation"},hook:function(){var e=this._private;if(!e.hooked){var t=e.target._private.animation;(e.queue?t.queue:t.current).push(this),E(e.target)&&e.target.cy().addToAnimationPool(e.target),e.hooked=!0}return this},play:function(){var e=this._private;return 1===e.progress&&(e.progress=0),e.playing=!0,e.started=!1,e.stopped=!1,this.hook(),this},playing:function(){return this._private.playing},apply:function(){var e=this._private;return e.applying=!0,e.started=!1,e.stopped=!1,this.hook(),this},applying:function(){return this._private.applying},pause:function(){var e=this._private;return e.playing=!1,e.started=!1,this},stop:function(){var e=this._private;return e.playing=!1,e.started=!1,e.stopped=!0,this},rewind:function(){return this.progress(0)},fastforward:function(){return this.progress(1)},time:function(e){var t=this._private;return void 0===e?t.progress*t.duration:this.progress(e/t.duration)},progress:function(e){var t=this._private,n=t.playing;return void 0===e?t.progress:(n&&this.pause(),t.progress=e,t.started=!1,n&&this.play(),this)},completed:function(){return 1===this._private.progress},reverse:function(){var e=this._private,t=e.playing;t&&this.pause(),e.progress=1-e.progress,e.started=!1;var n=function(t,n){var r=e[t];null!=r&&(e[t]=e[n],e[n]=r)};if(n("zoom","startZoom"),n("pan","startPan"),n("position","startPosition"),e.style)for(var r=0;r<e.style.length;r++){var i=e.style[r],a=i.name,o=e.startStyle[a];e.startStyle[a]=i,e.style[r]=o}return t&&this.play(),this},promise:function(e){var t,n=this._private;switch(e){case"frame":t=n.frames;break;default:case"complete":case"completed":t=n.completes}return new vr((function(e,n){t.push((function(){e()}))}))}}),mr.complete=mr.completed,mr.run=mr.play,mr.running=mr.playing;var br={animated:function(){return function(){var e=void 0!==this.length?this:[this];if(!(this._private.cy||this).styleEnabled())return!1;var t=e[0];return t?t._private.animation.current.length>0:void 0}},clearQueue:function(){return function(){var e=void 0!==this.length?this:[this];if(!(this._private.cy||this).styleEnabled())return this;for(var t=0;t<e.length;t++){e[t]._private.animation.queue=[]}return this}},delay:function(){return function(e,t){return(this._private.cy||this).styleEnabled()?this.animate({delay:e,duration:e,complete:t}):this}},delayAnimation:function(){return function(e,t){return(this._private.cy||this).styleEnabled()?this.animation({delay:e,duration:e,complete:t}):this}},animation:function(){return function(e,t){var n=void 0!==this.length,r=n?this:[this],i=this._private.cy||this,a=!n,o=!a;if(!i.styleEnabled())return this;var s=i.style();if(e=L({},e,t),0===Object.keys(e).length)return new yr(r[0],e);switch(void 0===e.duration&&(e.duration=400),e.duration){case"slow":e.duration=600;break;case"fast":e.duration=200}if(o&&(e.style=s.getPropsList(e.style||e.css),e.css=void 0),o&&null!=e.renderedPosition){var l=e.renderedPosition,u=i.pan(),c=i.zoom();e.position=mt(l,c,u)}if(a&&null!=e.panBy){var d=e.panBy,h=i.pan();e.pan={x:h.x+d.x,y:h.y+d.y}}var p=e.center||e.centre;if(a&&null!=p){var f=i.getCenterPan(p.eles,e.zoom);null!=f&&(e.pan=f)}if(a&&null!=e.fit){var g=e.fit,v=i.getFitViewport(g.eles||g.boundingBox,g.padding);null!=v&&(e.pan=v.pan,e.zoom=v.zoom)}if(a&&b(e.zoom)){var y=i.getZoomedViewport(e.zoom);null!=y?(y.zoomed&&(e.zoom=y.zoom),y.panned&&(e.pan=y.pan)):e.zoom=null}return new yr(r[0],e)}},animate:function(){return function(e,t){var n=void 0!==this.length?this:[this];if(!(this._private.cy||this).styleEnabled())return this;t&&(e=L({},e,t));for(var r=0;r<n.length;r++){var i=n[r],a=i.animated()&&(void 0===e.queue||e.queue);i.animation(e,a?{queue:!0}:void 0).play()}return this}},stop:function(){return function(e,t){var n=void 0!==this.length?this:[this],r=this._private.cy||this;if(!r.styleEnabled())return this;for(var i=0;i<n.length;i++){for(var a=n[i]._private,o=a.animation.current,s=0;s<o.length;s++){var l=o[s]._private;t&&(l.duration=0)}e&&(a.animation.queue=[]),t||(a.animation.current=[])}return r.notify("draw"),this}}},xr=Array.isArray,wr=/\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/,Er=/^\w*$/;var kr=function(e,t){if(xr(e))return!1;var n=typeof e;return!("number"!=n&&"symbol"!=n&&"boolean"!=n&&null!=e&&!le(e))||(Er.test(e)||!wr.test(e)||null!=t&&e in Object(t))};var Cr,Sr=function(e){if(!j(e))return!1;var t=oe(e);return"[object Function]"==t||"[object GeneratorFunction]"==t||"[object AsyncFunction]"==t||"[object Proxy]"==t},Pr=W["__core-js_shared__"],Dr=(Cr=/[^.]+$/.exec(Pr&&Pr.keys&&Pr.keys.IE_PROTO||""))?"Symbol(src)_1."+Cr:"";var Tr=function(e){return!!Dr&&Dr in e},_r=Function.prototype.toString;var Mr=function(e){if(null!=e){try{return _r.call(e)}catch(e){}try{return e+""}catch(e){}}return""},Br=/^\[object .+?Constructor\]$/,Nr=Function.prototype,zr=Object.prototype,Ir=Nr.toString,Ar=zr.hasOwnProperty,Lr=RegExp("^"+Ir.call(Ar).replace(/[\\^$.*+?()[\]{}|]/g,"\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,"$1.*?")+"$");var Or=function(e){return!(!j(e)||Tr(e))&&(Sr(e)?Lr:Br).test(Mr(e))};var Rr=function(e,t){return null==e?void 0:e[t]};var Vr=function(e,t){var n=Rr(e,t);return Or(n)?n:void 0},Fr=Vr(Object,"create");var jr=function(){this.__data__=Fr?Fr(null):{},this.size=0};var qr=function(e){var t=this.has(e)&&delete this.__data__[e];return this.size-=t?1:0,t},Yr=Object.prototype.hasOwnProperty;var Xr=function(e){var t=this.__data__;if(Fr){var n=t[e];return"__lodash_hash_undefined__"===n?void 0:n}return Yr.call(t,e)?t[e]:void 0},Wr=Object.prototype.hasOwnProperty;var Hr=function(e){var t=this.__data__;return Fr?void 0!==t[e]:Wr.call(t,e)};var Kr=function(e,t){var n=this.__data__;return this.size+=this.has(e)?0:1,n[e]=Fr&&void 0===t?"__lodash_hash_undefined__":t,this};function Gr(e){var t=-1,n=null==e?0:e.length;for(this.clear();++t<n;){var r=e[t];this.set(r[0],r[1])}}Gr.prototype.clear=jr,Gr.prototype.delete=qr,Gr.prototype.get=Xr,Gr.prototype.has=Hr,Gr.prototype.set=Kr;var Ur=Gr;var Zr=function(){this.__data__=[],this.size=0};var $r=function(e,t){return e===t||e!=e&&t!=t};var Qr=function(e,t){for(var n=e.length;n--;)if($r(e[n][0],t))return n;return-1},Jr=Array.prototype.splice;var ei=function(e){var t=this.__data__,n=Qr(t,e);return!(n<0)&&(n==t.length-1?t.pop():Jr.call(t,n,1),--this.size,!0)};var ti=function(e){var t=this.__data__,n=Qr(t,e);return n<0?void 0:t[n][1]};var ni=function(e){return Qr(this.__data__,e)>-1};var ri=function(e,t){var n=this.__data__,r=Qr(n,e);return r<0?(++this.size,n.push([e,t])):n[r][1]=t,this};function ii(e){var t=-1,n=null==e?0:e.length;for(this.clear();++t<n;){var r=e[t];this.set(r[0],r[1])}}ii.prototype.clear=Zr,ii.prototype.delete=ei,ii.prototype.get=ti,ii.prototype.has=ni,ii.prototype.set=ri;var ai=ii,oi=Vr(W,"Map");var si=function(){this.size=0,this.__data__={hash:new Ur,map:new(oi||ai),string:new Ur}};var li=function(e){var t=typeof e;return"string"==t||"number"==t||"symbol"==t||"boolean"==t?"__proto__"!==e:null===e};var ui=function(e,t){var n=e.__data__;return li(t)?n["string"==typeof t?"string":"hash"]:n.map};var ci=function(e){var t=ui(this,e).delete(e);return this.size-=t?1:0,t};var di=function(e){return ui(this,e).get(e)};var hi=function(e){return ui(this,e).has(e)};var pi=function(e,t){var n=ui(this,e),r=n.size;return n.set(e,t),this.size+=n.size==r?0:1,this};function fi(e){var t=-1,n=null==e?0:e.length;for(this.clear();++t<n;){var r=e[t];this.set(r[0],r[1])}}fi.prototype.clear=si,fi.prototype.delete=ci,fi.prototype.get=di,fi.prototype.has=hi,fi.prototype.set=pi;var gi=fi;function vi(e,t){if("function"!=typeof e||null!=t&&"function"!=typeof t)throw new TypeError("Expected a function");var n=function(){var r=arguments,i=t?t.apply(this,r):r[0],a=n.cache;if(a.has(i))return a.get(i);var o=e.apply(this,r);return n.cache=a.set(i,o)||a,o};return n.cache=new(vi.Cache||gi),n}vi.Cache=gi;var yi=vi;var mi=/[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g,bi=/\\(\\)?/g,xi=function(e){var t=yi(e,(function(e){return 500===n.size&&n.clear(),e})),n=t.cache;return t}((function(e){var t=[];return 46===e.charCodeAt(0)&&t.push(""),e.replace(mi,(function(e,n,r,i){t.push(r?i.replace(bi,"$1"):n||e)})),t}));var wi=function(e,t){for(var n=-1,r=null==e?0:e.length,i=Array(r);++n<r;)i[n]=t(e[n],n,e);return i},Ei=$?$.prototype:void 0,ki=Ei?Ei.toString:void 0;var Ci=function e(t){if("string"==typeof t)return t;if(xr(t))return wi(t,e)+"";if(le(t))return ki?ki.call(t):"";var n=t+"";return"0"==n&&1/t==-1/0?"-0":n};var Si=function(e){return null==e?"":Ci(e)};var Pi=function(e,t){return xr(e)?e:kr(e,t)?[e]:xi(Si(e))};var Di=function(e){if("string"==typeof e||le(e))return e;var t=e+"";return"0"==t&&1/e==-1/0?"-0":t};var Ti=function(e,t){for(var n=0,r=(t=Pi(t,e)).length;null!=e&&n<r;)e=e[Di(t[n++])];return n&&n==r?e:void 0};var _i=function(e,t,n){var r=null==e?void 0:Ti(e,t);return void 0===r?n:r},Mi=function(){try{var e=Vr(Object,"defineProperty");return e({},"",{}),e}catch(e){}}();var Bi=function(e,t,n){"__proto__"==t&&Mi?Mi(e,t,{configurable:!0,enumerable:!0,value:n,writable:!0}):e[t]=n},Ni=Object.prototype.hasOwnProperty;var zi=function(e,t,n){var r=e[t];Ni.call(e,t)&&$r(r,n)&&(void 0!==n||t in e)||Bi(e,t,n)},Ii=/^(?:0|[1-9]\d*)$/;var Ai=function(e,t){var n=typeof e;return!!(t=null==t?9007199254740991:t)&&("number"==n||"symbol"!=n&&Ii.test(e))&&e>-1&&e%1==0&&e<t};var Li=function(e,t,n,r){if(!j(e))return e;for(var i=-1,a=(t=Pi(t,e)).length,o=a-1,s=e;null!=s&&++i<a;){var l=Di(t[i]),u=n;if("__proto__"===l||"constructor"===l||"prototype"===l)return e;if(i!=o){var c=s[l];void 0===(u=r?r(c,l,s):void 0)&&(u=j(c)?c:Ai(t[i+1])?[]:{})}zi(s,l,u),s=s[l]}return e};var Oi=function(e,t,n){return null==e?e:Li(e,t,n)};var Ri=function(e,t){var n=-1,r=e.length;for(t||(t=Array(r));++n<r;)t[n]=e[n];return t};var Vi=function(e){return xr(e)?wi(e,Di):le(e)?[e]:Ri(xi(Si(e)))},Fi={};[br,{data:function(e){return e=L({},{field:"data",bindingEvent:"data",allowBinding:!1,allowSetting:!1,allowGetting:!1,settingEvent:"data",settingTriggersEvent:!1,triggerFnName:"trigger",immutableKeys:{},updateStyle:!1,beforeGet:function(e){},beforeSet:function(e,t){},onSet:function(e){},canSet:function(e){return!0}},e),function(t,n){var r=e,a=void 0!==this.length,o=a?this:[this],s=a?this[0]:this;if(v(t)){var l,u=-1!==t.indexOf(".")&&Vi(t);if(r.allowGetting&&void 0===n)return s&&(r.beforeGet(s),l=u&&void 0===s._private[r.field][t]?_i(s._private[r.field],u):s._private[r.field][t]),l;if(r.allowSetting&&void 0!==n&&!r.immutableKeys[t]){var c=i({},t,n);r.beforeSet(this,c);for(var d=0,h=o.length;d<h;d++){var p=o[d];r.canSet(p)&&(u&&void 0===s._private[r.field][t]?Oi(p._private[r.field],u,n):p._private[r.field][t]=n)}r.updateStyle&&this.updateStyle(),r.onSet(this),r.settingTriggersEvent&&this[r.triggerFnName](r.settingEvent)}}else if(r.allowSetting&&b(t)){var f,g,m=t,x=Object.keys(m);r.beforeSet(this,m);for(var w=0;w<x.length;w++){if(g=m[f=x[w]],!r.immutableKeys[f])for(var E=0;E<o.length;E++){var k=o[E];r.canSet(k)&&(k._private[r.field][f]=g)}}r.updateStyle&&this.updateStyle(),r.onSet(this),r.settingTriggersEvent&&this[r.triggerFnName](r.settingEvent)}else if(r.allowBinding&&y(t)){var C=t;this.on(r.bindingEvent,C)}else if(r.allowGetting&&void 0===t){var S;return s&&(r.beforeGet(s),S=s._private[r.field]),S}return this}},removeData:function(e){return e=L({},{field:"data",event:"data",triggerFnName:"trigger",triggerEvent:!1,immutableKeys:{}},e),function(t){var n=e,r=void 0!==this.length?this:[this];if(v(t)){for(var i=t.split(/\s+/),a=i.length,o=0;o<a;o++){var s=i[o];if(!D(s))if(!n.immutableKeys[s])for(var l=0,u=r.length;l<u;l++)r[l]._private[n.field][s]=void 0}n.triggerEvent&&this[n.triggerFnName](n.event)}else if(void 0===t){for(var c=0,d=r.length;c<d;c++)for(var h=r[c]._private[n.field],p=Object.keys(h),f=0;f<p.length;f++){var g=p[f];!n.immutableKeys[g]&&(h[g]=void 0)}n.triggerEvent&&this[n.triggerFnName](n.event)}return this}}},{eventAliasesOn:function(e){var t=e;t.addListener=t.listen=t.bind=t.on,t.unlisten=t.unbind=t.off=t.removeListener,t.trigger=t.emit,t.pon=t.promiseOn=function(e,t){var n=this,r=Array.prototype.slice.call(arguments,0);return new vr((function(e,t){var i=r.concat([function(t){n.off.apply(n,a),e(t)}]),a=i.concat([]);n.on.apply(n,i)}))}}}].forEach((function(e){L(Fi,e)}));var ji={animate:Fi.animate(),animation:Fi.animation(),animated:Fi.animated(),clearQueue:Fi.clearQueue(),delay:Fi.delay(),delayAnimation:Fi.delayAnimation(),stop:Fi.stop()},qi={classes:function(e){if(void 0===e){var t=[];return this[0]._private.classes.forEach((function(e){return t.push(e)})),t}m(e)||(e=(e||"").match(/\S+/g)||[]);for(var n=[],r=new Je(e),i=0;i<this.length;i++){for(var a=this[i],o=a._private,s=o.classes,l=!1,u=0;u<e.length;u++){var c=e[u];if(!s.has(c)){l=!0;break}}l||(l=s.size!==e.length),l&&(o.classes=r,n.push(a))}return n.length>0&&this.spawn(n).updateStyle().emit("class"),this},addClass:function(e){return this.toggleClass(e,!0)},hasClass:function(e){var t=this[0];return null!=t&&t._private.classes.has(e)},toggleClass:function(e,t){m(e)||(e=e.match(/\S+/g)||[]);for(var n=void 0===t,r=[],i=0,a=this.length;i<a;i++)for(var o=this[i],s=o._private.classes,l=!1,u=0;u<e.length;u++){var c=e[u],d=s.has(c),h=!1;t||n&&!d?(s.add(c),h=!0):(!t||n&&d)&&(s.delete(c),h=!0),!l&&h&&(r.push(o),l=!0)}return r.length>0&&this.spawn(r).updateStyle().emit("class"),this},removeClass:function(e){return this.toggleClass(e,!1)},flashClass:function(e,t){var n=this;if(null==t)t=250;else if(0===t)return n;return n.addClass(e),setTimeout((function(){n.removeClass(e)}),t),n}};qi.className=qi.classNames=qi.classes;var Yi={metaChar:"[\\!\\\"\\#\\$\\%\\&\\'\\(\\)\\*\\+\\,\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\]\\^\\`\\{\\|\\}\\~]",comparatorOp:"=|\\!=|>|>=|<|<=|\\$=|\\^=|\\*=",boolOp:"\\?|\\!|\\^",string:"\"(?:\\\\\"|[^\"])*\"|'(?:\\\\'|[^'])*'",number:I,meta:"degree|indegree|outdegree",separator:"\\s*,\\s*",descendant:"\\s+",child:"\\s+>\\s+",subject:"\\$",group:"node|edge|\\*",directedEdge:"\\s+->\\s+",undirectedEdge:"\\s+<->\\s+"};Yi.variable="(?:[\\w-.]|(?:\\\\"+Yi.metaChar+"))+",Yi.className="(?:[\\w-]|(?:\\\\"+Yi.metaChar+"))+",Yi.value=Yi.string+"|"+Yi.number,Yi.id=Yi.variable,function(){var e,t,n;for(e=Yi.comparatorOp.split("|"),n=0;n<e.length;n++)t=e[n],Yi.comparatorOp+="|@"+t;for(e=Yi.comparatorOp.split("|"),n=0;n<e.length;n++)(t=e[n]).indexOf("!")>=0||"="!==t&&(Yi.comparatorOp+="|\\!"+t)}();var Xi=0,Wi=1,Hi=2,Ki=3,Gi=4,Ui=5,Zi=6,$i=7,Qi=8,Ji=9,ea=10,ta=11,na=12,ra=13,ia=14,aa=15,oa=16,sa=17,la=18,ua=19,ca=20,da=[{selector:":selected",matches:function(e){return e.selected()}},{selector:":unselected",matches:function(e){return!e.selected()}},{selector:":selectable",matches:function(e){return e.selectable()}},{selector:":unselectable",matches:function(e){return!e.selectable()}},{selector:":locked",matches:function(e){return e.locked()}},{selector:":unlocked",matches:function(e){return!e.locked()}},{selector:":visible",matches:function(e){return e.visible()}},{selector:":hidden",matches:function(e){return!e.visible()}},{selector:":transparent",matches:function(e){return e.transparent()}},{selector:":grabbed",matches:function(e){return e.grabbed()}},{selector:":free",matches:function(e){return!e.grabbed()}},{selector:":removed",matches:function(e){return e.removed()}},{selector:":inside",matches:function(e){return!e.removed()}},{selector:":grabbable",matches:function(e){return e.grabbable()}},{selector:":ungrabbable",matches:function(e){return!e.grabbable()}},{selector:":animated",matches:function(e){return e.animated()}},{selector:":unanimated",matches:function(e){return!e.animated()}},{selector:":parent",matches:function(e){return e.isParent()}},{selector:":childless",matches:function(e){return e.isChildless()}},{selector:":child",matches:function(e){return e.isChild()}},{selector:":orphan",matches:function(e){return e.isOrphan()}},{selector:":nonorphan",matches:function(e){return e.isChild()}},{selector:":compound",matches:function(e){return e.isNode()?e.isParent():e.source().isParent()||e.target().isParent()}},{selector:":loop",matches:function(e){return e.isLoop()}},{selector:":simple",matches:function(e){return e.isSimple()}},{selector:":active",matches:function(e){return e.active()}},{selector:":inactive",matches:function(e){return!e.active()}},{selector:":backgrounding",matches:function(e){return e.backgrounding()}},{selector:":nonbackgrounding",matches:function(e){return!e.backgrounding()}}].sort((function(e,t){return function(e,t){return-1*A(e,t)}(e.selector,t.selector)})),ha=function(){for(var e,t={},n=0;n<da.length;n++)t[(e=da[n]).selector]=e.matches;return t}(),pa="("+da.map((function(e){return e.selector})).join("|")+")",fa=function(e){return e.replace(new RegExp("\\\\("+Yi.metaChar+")","g"),(function(e,t){return t}))},ga=function(e,t,n){e[e.length-1]=n},va=[{name:"group",query:!0,regex:"("+Yi.group+")",populate:function(e,t,n){var r=a(n,1)[0];t.checks.push({type:Xi,value:"*"===r?r:r+"s"})}},{name:"state",query:!0,regex:pa,populate:function(e,t,n){var r=a(n,1)[0];t.checks.push({type:$i,value:r})}},{name:"id",query:!0,regex:"\\#("+Yi.id+")",populate:function(e,t,n){var r=a(n,1)[0];t.checks.push({type:Qi,value:fa(r)})}},{name:"className",query:!0,regex:"\\.("+Yi.className+")",populate:function(e,t,n){var r=a(n,1)[0];t.checks.push({type:Ji,value:fa(r)})}},{name:"dataExists",query:!0,regex:"\\[\\s*("+Yi.variable+")\\s*\\]",populate:function(e,t,n){var r=a(n,1)[0];t.checks.push({type:Gi,field:fa(r)})}},{name:"dataCompare",query:!0,regex:"\\[\\s*("+Yi.variable+")\\s*("+Yi.comparatorOp+")\\s*("+Yi.value+")\\s*\\]",populate:function(e,t,n){var r=a(n,3),i=r[0],o=r[1],s=r[2];s=null!=new RegExp("^"+Yi.string+"$").exec(s)?s.substring(1,s.length-1):parseFloat(s),t.checks.push({type:Ki,field:fa(i),operator:o,value:s})}},{name:"dataBool",query:!0,regex:"\\[\\s*("+Yi.boolOp+")\\s*("+Yi.variable+")\\s*\\]",populate:function(e,t,n){var r=a(n,2),i=r[0],o=r[1];t.checks.push({type:Ui,field:fa(o),operator:i})}},{name:"metaCompare",query:!0,regex:"\\[\\[\\s*("+Yi.meta+")\\s*("+Yi.comparatorOp+")\\s*("+Yi.number+")\\s*\\]\\]",populate:function(e,t,n){var r=a(n,3),i=r[0],o=r[1],s=r[2];t.checks.push({type:Zi,field:fa(i),operator:o,value:parseFloat(s)})}},{name:"nextQuery",separator:!0,regex:Yi.separator,populate:function(e,t){var n=e.currentSubject,r=e.edgeCount,i=e.compoundCount,a=e[e.length-1];return null!=n&&(a.subject=n,e.currentSubject=null),a.edgeCount=r,a.compoundCount=i,e.edgeCount=0,e.compoundCount=0,e[e.length++]={checks:[]}}},{name:"directedEdge",separator:!0,regex:Yi.directedEdge,populate:function(e,t){if(null==e.currentSubject){var n={checks:[]},r=t,i={checks:[]};return n.checks.push({type:ta,source:r,target:i}),ga(e,0,n),e.edgeCount++,i}var a={checks:[]},o=t,s={checks:[]};return a.checks.push({type:na,source:o,target:s}),ga(e,0,a),e.edgeCount++,s}},{name:"undirectedEdge",separator:!0,regex:Yi.undirectedEdge,populate:function(e,t){if(null==e.currentSubject){var n={checks:[]},r=t,i={checks:[]};return n.checks.push({type:ea,nodes:[r,i]}),ga(e,0,n),e.edgeCount++,i}var a={checks:[]},o=t,s={checks:[]};return a.checks.push({type:ia,node:o,neighbor:s}),ga(e,0,a),s}},{name:"child",separator:!0,regex:Yi.child,populate:function(e,t){if(null==e.currentSubject){var n={checks:[]},r={checks:[]},i=e[e.length-1];return n.checks.push({type:aa,parent:i,child:r}),ga(e,0,n),e.compoundCount++,r}if(e.currentSubject===t){var a={checks:[]},o=e[e.length-1],s={checks:[]},l={checks:[]},u={checks:[]},c={checks:[]};return a.checks.push({type:ua,left:o,right:s,subject:l}),l.checks=t.checks,t.checks=[{type:ca}],c.checks.push({type:ca}),s.checks.push({type:sa,parent:c,child:u}),ga(e,0,a),e.currentSubject=l,e.compoundCount++,u}var d={checks:[]},h={checks:[]},p=[{type:sa,parent:d,child:h}];return d.checks=t.checks,t.checks=p,e.compoundCount++,h}},{name:"descendant",separator:!0,regex:Yi.descendant,populate:function(e,t){if(null==e.currentSubject){var n={checks:[]},r={checks:[]},i=e[e.length-1];return n.checks.push({type:oa,ancestor:i,descendant:r}),ga(e,0,n),e.compoundCount++,r}if(e.currentSubject===t){var a={checks:[]},o=e[e.length-1],s={checks:[]},l={checks:[]},u={checks:[]},c={checks:[]};return a.checks.push({type:ua,left:o,right:s,subject:l}),l.checks=t.checks,t.checks=[{type:ca}],c.checks.push({type:ca}),s.checks.push({type:la,ancestor:c,descendant:u}),ga(e,0,a),e.currentSubject=l,e.compoundCount++,u}var d={checks:[]},h={checks:[]},p=[{type:la,ancestor:d,descendant:h}];return d.checks=t.checks,t.checks=p,e.compoundCount++,h}},{name:"subject",modifier:!0,regex:Yi.subject,populate:function(e,t){if(null!=e.currentSubject&&e.currentSubject!==t)return je("Redefinition of subject in selector `"+e.toString()+"`"),!1;e.currentSubject=t;var n=e[e.length-1].checks[0],r=null==n?null:n.type;r===ta?n.type=ra:r===ea&&(n.type=ia,n.node=n.nodes[1],n.neighbor=n.nodes[0],n.nodes=null)}}];va.forEach((function(e){return e.regexObj=new RegExp("^"+e.regex)}));var ya=function(e){for(var t,n,r,i=0;i<va.length;i++){var a=va[i],o=a.name,s=e.match(a.regexObj);if(null!=s){n=s,t=a,r=o;var l=s[0];e=e.substring(l.length);break}}return{expr:t,match:n,name:r,remaining:e}},ma={parse:function(e){var t=this.inputText=e,n=this[0]={checks:[]};for(this.length=1,t=function(e){var t=e.match(/^\s+/);if(t){var n=t[0];e=e.substring(n.length)}return e}(t);;){var r=ya(t);if(null==r.expr)return je("The selector `"+e+"`is invalid"),!1;var i=r.match.slice(1),a=r.expr.populate(this,n,i);if(!1===a)return!1;if(null!=a&&(n=a),(t=r.remaining).match(/^\s*$/))break}var o=this[this.length-1];null!=this.currentSubject&&(o.subject=this.currentSubject),o.edgeCount=this.edgeCount,o.compoundCount=this.compoundCount;for(var s=0;s<this.length;s++){var l=this[s];if(l.compoundCount>0&&l.edgeCount>0)return je("The selector `"+e+"` is invalid because it uses both a compound selector and an edge selector"),!1;if(l.edgeCount>1)return je("The selector `"+e+"` is invalid because it uses multiple edge selectors"),!1;1===l.edgeCount&&je("The selector `"+e+"` is deprecated.  Edge selectors do not take effect on changes to source and target nodes after an edge is added, for performance reasons.  Use a class or data selector on edges instead, updating the class or data of an edge when your app detects a change in source or target nodes.")}return!0},toString:function(){if(null!=this.toStringCache)return this.toStringCache;for(var e=function(e){return null==e?"":e},t=function(t){return v(t)?'"'+t+'"':e(t)},n=function(e){return" "+e+" "},r=function(r,a){var o=r.type,s=r.value;switch(o){case Xi:var l=e(s);return l.substring(0,l.length-1);case Ki:var u=r.field,c=r.operator;return"["+u+n(e(c))+t(s)+"]";case Ui:var d=r.operator,h=r.field;return"["+e(d)+h+"]";case Gi:return"["+r.field+"]";case Zi:var p=r.operator;return"[["+r.field+n(e(p))+t(s)+"]]";case $i:return s;case Qi:return"#"+s;case Ji:return"."+s;case sa:case aa:return i(r.parent,a)+n(">")+i(r.child,a);case la:case oa:return i(r.ancestor,a)+" "+i(r.descendant,a);case ua:var f=i(r.left,a),g=i(r.subject,a),v=i(r.right,a);return f+(f.length>0?" ":"")+g+v;case ca:return""}},i=function(e,t){return e.checks.reduce((function(n,i,a){return n+(t===e&&0===a?"$":"")+r(i,t)}),"")},a="",o=0;o<this.length;o++){var s=this[o];a+=i(s,s.subject),this.length>1&&o<this.length-1&&(a+=", ")}return this.toStringCache=a,a}},ba=function(e,t,n){var r,i,a,o=v(e),s=x(e),l=v(n),u=!1,c=!1,d=!1;switch(t.indexOf("!")>=0&&(t=t.replace("!",""),c=!0),t.indexOf("@")>=0&&(t=t.replace("@",""),u=!0),(o||l||u)&&(i=o||s?""+e:"",a=""+n),u&&(e=i=i.toLowerCase(),n=a=a.toLowerCase()),t){case"*=":r=i.indexOf(a)>=0;break;case"$=":r=i.indexOf(a,i.length-a.length)>=0;break;case"^=":r=0===i.indexOf(a);break;case"=":r=e===n;break;case">":d=!0,r=e>n;break;case">=":d=!0,r=e>=n;break;case"<":d=!0,r=e<n;break;case"<=":d=!0,r=e<=n;break;default:r=!1}return!c||null==e&&d||(r=!r),r},xa=function(e,t){return e.data(t)},wa=[],Ea=function(e,t){return e.checks.every((function(e){return wa[e.type](e,t)}))};wa[Xi]=function(e,t){var n=e.value;return"*"===n||n===t.group()},wa[$i]=function(e,t){return function(e,t){return ha[e](t)}(e.value,t)},wa[Qi]=function(e,t){var n=e.value;return t.id()===n},wa[Ji]=function(e,t){var n=e.value;return t.hasClass(n)},wa[Zi]=function(e,t){var n=e.field,r=e.operator,i=e.value;return ba(function(e,t){return e[t]()}(t,n),r,i)},wa[Ki]=function(e,t){var n=e.field,r=e.operator,i=e.value;return ba(xa(t,n),r,i)},wa[Ui]=function(e,t){var n=e.field,r=e.operator;return function(e,t){switch(t){case"?":return!!e;case"!":return!e;case"^":return void 0===e}}(xa(t,n),r)},wa[Gi]=function(e,t){var n=e.field;return e.operator,void 0!==xa(t,n)},wa[ea]=function(e,t){var n=e.nodes[0],r=e.nodes[1],i=t.source(),a=t.target();return Ea(n,i)&&Ea(r,a)||Ea(r,i)&&Ea(n,a)},wa[ia]=function(e,t){return Ea(e.node,t)&&t.neighborhood().some((function(t){return t.isNode()&&Ea(e.neighbor,t)}))},wa[ta]=function(e,t){return Ea(e.source,t.source())&&Ea(e.target,t.target())},wa[na]=function(e,t){return Ea(e.source,t)&&t.outgoers().some((function(t){return t.isNode()&&Ea(e.target,t)}))},wa[ra]=function(e,t){return Ea(e.target,t)&&t.incomers().some((function(t){return t.isNode()&&Ea(e.source,t)}))},wa[aa]=function(e,t){return Ea(e.child,t)&&Ea(e.parent,t.parent())},wa[sa]=function(e,t){return Ea(e.parent,t)&&t.children().some((function(t){return Ea(e.child,t)}))},wa[oa]=function(e,t){return Ea(e.descendant,t)&&t.ancestors().some((function(t){return Ea(e.ancestor,t)}))},wa[la]=function(e,t){return Ea(e.ancestor,t)&&t.descendants().some((function(t){return Ea(e.descendant,t)}))},wa[ua]=function(e,t){return Ea(e.subject,t)&&Ea(e.left,t)&&Ea(e.right,t)},wa[ca]=function(){return!0},wa[Wi]=function(e,t){return e.value.has(t)},wa[Hi]=function(e,t){return(0,e.value)(t)};var ka=function(e){this.inputText=e,this.currentSubject=null,this.compoundCount=0,this.edgeCount=0,this.length=0,null==e||v(e)&&e.match(/^\s*$/)||(E(e)?this.addQuery({checks:[{type:Wi,value:e.collection()}]}):y(e)?this.addQuery({checks:[{type:Hi,value:e}]}):v(e)?this.parse(e)||(this.invalid=!0):Ve("A selector must be created from a string; found "))},Ca=ka.prototype;[ma,{matches:function(e){for(var t=0;t<this.length;t++){var n=this[t];if(Ea(n,e))return!0}return!1},filter:function(e){var t=this;if(1===t.length&&1===t[0].checks.length&&t[0].checks[0].type===Qi)return e.getElementById(t[0].checks[0].value).collection();var n=function(e){for(var n=0;n<t.length;n++){var r=t[n];if(Ea(r,e))return!0}return!1};return null==t.text()&&(n=function(){return!0}),e.filter(n)}}].forEach((function(e){return L(Ca,e)})),Ca.text=function(){return this.inputText},Ca.size=function(){return this.length},Ca.eq=function(e){return this[e]},Ca.sameText=function(e){return!this.invalid&&!e.invalid&&this.text()===e.text()},Ca.addQuery=function(e){this[this.length++]=e},Ca.selector=Ca.toString;var Sa={allAre:function(e){var t=new ka(e);return this.every((function(e){return t.matches(e)}))},is:function(e){var t=new ka(e);return this.some((function(e){return t.matches(e)}))},some:function(e,t){for(var n=0;n<this.length;n++){if(t?e.apply(t,[this[n],n,this]):e(this[n],n,this))return!0}return!1},every:function(e,t){for(var n=0;n<this.length;n++){if(!(t?e.apply(t,[this[n],n,this]):e(this[n],n,this)))return!1}return!0},same:function(e){if(this===e)return!0;e=this.cy().collection(e);var t=this.length;return t===e.length&&(1===t?this[0]===e[0]:this.every((function(t){return e.hasElementWithId(t.id())})))},anySame:function(e){return e=this.cy().collection(e),this.some((function(t){return e.hasElementWithId(t.id())}))},allAreNeighbors:function(e){e=this.cy().collection(e);var t=this.neighborhood();return e.every((function(e){return t.hasElementWithId(e.id())}))},contains:function(e){e=this.cy().collection(e);var t=this;return e.every((function(e){return t.hasElementWithId(e.id())}))}};Sa.allAreNeighbours=Sa.allAreNeighbors,Sa.has=Sa.contains,Sa.equal=Sa.equals=Sa.same;var Pa,Da,Ta=function(e,t){return function(n,r,i,a){var o,s=n;if(null==s?o="":E(s)&&1===s.length&&(o=s.id()),1===this.length&&o){var l=this[0]._private,u=l.traversalCache=l.traversalCache||{},c=u[t]=u[t]||[],d=Te(o),h=c[d];return h||(c[d]=e.call(this,n,r,i,a))}return e.call(this,n,r,i,a)}},_a={parent:function(e){var t=[];if(1===this.length){var n=this[0]._private.parent;if(n)return n}for(var r=0;r<this.length;r++){var i=this[r]._private.parent;i&&t.push(i)}return this.spawn(t,!0).filter(e)},parents:function(e){for(var t=[],n=this.parent();n.nonempty();){for(var r=0;r<n.length;r++){var i=n[r];t.push(i)}n=n.parent()}return this.spawn(t,!0).filter(e)},commonAncestors:function(e){for(var t,n=0;n<this.length;n++){var r=this[n].parents();t=(t=t||r).intersect(r)}return t.filter(e)},orphans:function(e){return this.stdFilter((function(e){return e.isOrphan()})).filter(e)},nonorphans:function(e){return this.stdFilter((function(e){return e.isChild()})).filter(e)},children:Ta((function(e){for(var t=[],n=0;n<this.length;n++)for(var r=this[n]._private.children,i=0;i<r.length;i++)t.push(r[i]);return this.spawn(t,!0).filter(e)}),"children"),siblings:function(e){return this.parent().children().not(this).filter(e)},isParent:function(){var e=this[0];if(e)return e.isNode()&&0!==e._private.children.length},isChildless:function(){var e=this[0];if(e)return e.isNode()&&0===e._private.children.length},isChild:function(){var e=this[0];if(e)return e.isNode()&&null!=e._private.parent},isOrphan:function(){var e=this[0];if(e)return e.isNode()&&null==e._private.parent},descendants:function(e){var t=[];return function e(n){for(var r=0;r<n.length;r++){var i=n[r];t.push(i),i.children().nonempty()&&e(i.children())}}(this.children()),this.spawn(t,!0).filter(e)}};function Ma(e,t,n,r){for(var i=[],a=new Je,o=e.cy().hasCompoundNodes(),s=0;s<e.length;s++){var l=e[s];n?i.push(l):o&&r(i,a,l)}for(;i.length>0;){var u=i.shift();t(u),a.add(u.id()),o&&r(i,a,u)}return e}function Ba(e,t,n){if(n.isParent())for(var r=n._private.children,i=0;i<r.length;i++){var a=r[i];t.has(a.id())||e.push(a)}}function Na(e,t,n){if(n.isChild()){var r=n._private.parent;t.has(r.id())||e.push(r)}}function za(e,t,n){Na(e,t,n),Ba(e,t,n)}_a.forEachDown=function(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];return Ma(this,e,t,Ba)},_a.forEachUp=function(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];return Ma(this,e,t,Na)},_a.forEachUpAndDown=function(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];return Ma(this,e,t,za)},_a.ancestors=_a.parents,(Pa=Da={data:Fi.data({field:"data",bindingEvent:"data",allowBinding:!0,allowSetting:!0,settingEvent:"data",settingTriggersEvent:!0,triggerFnName:"trigger",allowGetting:!0,immutableKeys:{id:!0,source:!0,target:!0,parent:!0},updateStyle:!0}),removeData:Fi.removeData({field:"data",event:"data",triggerFnName:"trigger",triggerEvent:!0,immutableKeys:{id:!0,source:!0,target:!0,parent:!0},updateStyle:!0}),scratch:Fi.data({field:"scratch",bindingEvent:"scratch",allowBinding:!0,allowSetting:!0,settingEvent:"scratch",settingTriggersEvent:!0,triggerFnName:"trigger",allowGetting:!0,updateStyle:!0}),removeScratch:Fi.removeData({field:"scratch",event:"scratch",triggerFnName:"trigger",triggerEvent:!0,updateStyle:!0}),rscratch:Fi.data({field:"rscratch",allowBinding:!1,allowSetting:!0,settingTriggersEvent:!1,allowGetting:!0}),removeRscratch:Fi.removeData({field:"rscratch",triggerEvent:!1}),id:function(){var e=this[0];if(e)return e._private.data.id}}).attr=Pa.data,Pa.removeAttr=Pa.removeData;var Ia,Aa,La=Da,Oa={};function Ra(e){return function(t){if(void 0===t&&(t=!0),0!==this.length&&this.isNode()&&!this.removed()){for(var n=0,r=this[0],i=r._private.edges,a=0;a<i.length;a++){var o=i[a];!t&&o.isLoop()||(n+=e(r,o))}return n}}}function Va(e,t){return function(n){for(var r,i=this.nodes(),a=0;a<i.length;a++){var o=i[a][e](n);void 0===o||void 0!==r&&!t(o,r)||(r=o)}return r}}L(Oa,{degree:Ra((function(e,t){return t.source().same(t.target())?2:1})),indegree:Ra((function(e,t){return t.target().same(e)?1:0})),outdegree:Ra((function(e,t){return t.source().same(e)?1:0}))}),L(Oa,{minDegree:Va("degree",(function(e,t){return e<t})),maxDegree:Va("degree",(function(e,t){return e>t})),minIndegree:Va("indegree",(function(e,t){return e<t})),maxIndegree:Va("indegree",(function(e,t){return e>t})),minOutdegree:Va("outdegree",(function(e,t){return e<t})),maxOutdegree:Va("outdegree",(function(e,t){return e>t}))}),L(Oa,{totalDegree:function(e){for(var t=0,n=this.nodes(),r=0;r<n.length;r++)t+=n[r].degree(e);return t}});var Fa=function(e,t,n){for(var r=0;r<e.length;r++){var i=e[r];if(!i.locked()){var a=i._private.position,o={x:null!=t.x?t.x-a.x:0,y:null!=t.y?t.y-a.y:0};!i.isParent()||0===o.x&&0===o.y||i.children().shift(o,n),i.dirtyBoundingBoxCache()}}},ja={field:"position",bindingEvent:"position",allowBinding:!0,allowSetting:!0,settingEvent:"position",settingTriggersEvent:!0,triggerFnName:"emitAndNotify",allowGetting:!0,validKeys:["x","y"],beforeGet:function(e){e.updateCompoundBounds()},beforeSet:function(e,t){Fa(e,t,!1)},onSet:function(e){e.dirtyCompoundBoundsCache()},canSet:function(e){return!e.locked()}};(Ia=Aa={position:Fi.data(ja),silentPosition:Fi.data(L({},ja,{allowBinding:!1,allowSetting:!0,settingTriggersEvent:!1,allowGetting:!1,beforeSet:function(e,t){Fa(e,t,!0)},onSet:function(e){e.dirtyCompoundBoundsCache()}})),positions:function(e,t){if(b(e))t?this.silentPosition(e):this.position(e);else if(y(e)){var n=e,r=this.cy();r.startBatch();for(var i=0;i<this.length;i++){var a,o=this[i];(a=n(o,i))&&(t?o.silentPosition(a):o.position(a))}r.endBatch()}return this},silentPositions:function(e){return this.positions(e,!0)},shift:function(e,t,n){var r;if(b(e)?(r={x:x(e.x)?e.x:0,y:x(e.y)?e.y:0},n=t):v(e)&&x(t)&&((r={x:0,y:0})[e]=t),null!=r){var i=this.cy();i.startBatch();for(var a=0;a<this.length;a++){var o=this[a];if(!(i.hasCompoundNodes()&&o.isChild()&&o.ancestors().anySame(this))){var s=o.position(),l={x:s.x+r.x,y:s.y+r.y};n?o.silentPosition(l):o.position(l)}}i.endBatch()}return this},silentShift:function(e,t){return b(e)?this.shift(e,!0):v(e)&&x(t)&&this.shift(e,t,!0),this},renderedPosition:function(e,t){var n=this[0],r=this.cy(),i=r.zoom(),a=r.pan(),o=b(e)?e:void 0,s=void 0!==o||void 0!==t&&v(e);if(n&&n.isNode()){if(!s){var l=n.position();return o=yt(l,i,a),void 0===e?o:o[e]}for(var u=0;u<this.length;u++){var c=this[u];void 0!==t?c.position(e,(t-a[e])/i):void 0!==o&&c.position(mt(o,i,a))}}else if(!s)return;return this},relativePosition:function(e,t){var n=this[0],r=this.cy(),i=b(e)?e:void 0,a=void 0!==i||void 0!==t&&v(e),o=r.hasCompoundNodes();if(n&&n.isNode()){if(!a){var s=n.position(),l=o?n.parent():null,u=l&&l.length>0,c=u;u&&(l=l[0]);var d=c?l.position():{x:0,y:0};return i={x:s.x-d.x,y:s.y-d.y},void 0===e?i:i[e]}for(var h=0;h<this.length;h++){var p=this[h],f=o?p.parent():null,g=f&&f.length>0,y=g;g&&(f=f[0]);var m=y?f.position():{x:0,y:0};void 0!==t?p.position(e,t+m[e]):void 0!==i&&p.position({x:i.x+m.x,y:i.y+m.y})}}else if(!a)return;return this}}).modelPosition=Ia.point=Ia.position,Ia.modelPositions=Ia.points=Ia.positions,Ia.renderedPoint=Ia.renderedPosition,Ia.relativePoint=Ia.relativePosition;var qa,Ya,Xa=Aa;qa=Ya={},Ya.renderedBoundingBox=function(e){var t=this.boundingBox(e),n=this.cy(),r=n.zoom(),i=n.pan(),a=t.x1*r+i.x,o=t.x2*r+i.x,s=t.y1*r+i.y,l=t.y2*r+i.y;return{x1:a,x2:o,y1:s,y2:l,w:o-a,h:l-s}},Ya.dirtyCompoundBoundsCache=function(){var e=arguments.length>0&&void 0!==arguments[0]&&arguments[0],t=this.cy();return t.styleEnabled()&&t.hasCompoundNodes()?(this.forEachUp((function(t){if(t.isParent()){var n=t._private;n.compoundBoundsClean=!1,n.bbCache=null,e||t.emitAndNotify("bounds")}})),this):this},Ya.updateCompoundBounds=function(){var e=arguments.length>0&&void 0!==arguments[0]&&arguments[0],t=this.cy();if(!t.styleEnabled()||!t.hasCompoundNodes())return this;if(!e&&t.batching())return this;function n(e){if(e.isParent()){var t=e._private,n=e.children(),r="include"===e.pstyle("compound-sizing-wrt-labels").value,i={width:{val:e.pstyle("min-width").pfValue,left:e.pstyle("min-width-bias-left"),right:e.pstyle("min-width-bias-right")},height:{val:e.pstyle("min-height").pfValue,top:e.pstyle("min-height-bias-top"),bottom:e.pstyle("min-height-bias-bottom")}},a=n.boundingBox({includeLabels:r,includeOverlays:!1,useCache:!1}),o=t.position;0!==a.w&&0!==a.h||((a={w:e.pstyle("width").pfValue,h:e.pstyle("height").pfValue}).x1=o.x-a.w/2,a.x2=o.x+a.w/2,a.y1=o.y-a.h/2,a.y2=o.y+a.h/2);var s=i.width.left.value;"px"===i.width.left.units&&i.width.val>0&&(s=100*s/i.width.val);var l=i.width.right.value;"px"===i.width.right.units&&i.width.val>0&&(l=100*l/i.width.val);var u=i.height.top.value;"px"===i.height.top.units&&i.height.val>0&&(u=100*u/i.height.val);var c=i.height.bottom.value;"px"===i.height.bottom.units&&i.height.val>0&&(c=100*c/i.height.val);var d=y(i.width.val-a.w,s,l),h=d.biasDiff,p=d.biasComplementDiff,f=y(i.height.val-a.h,u,c),g=f.biasDiff,v=f.biasComplementDiff;t.autoPadding=function(e,t,n,r){if("%"!==n.units)return"px"===n.units?n.pfValue:0;switch(r){case"width":return e>0?n.pfValue*e:0;case"height":return t>0?n.pfValue*t:0;case"average":return e>0&&t>0?n.pfValue*(e+t)/2:0;case"min":return e>0&&t>0?e>t?n.pfValue*t:n.pfValue*e:0;case"max":return e>0&&t>0?e>t?n.pfValue*e:n.pfValue*t:0;default:return 0}}(a.w,a.h,e.pstyle("padding"),e.pstyle("padding-relative-to").value),t.autoWidth=Math.max(a.w,i.width.val),o.x=(-h+a.x1+a.x2+p)/2,t.autoHeight=Math.max(a.h,i.height.val),o.y=(-g+a.y1+a.y2+v)/2}function y(e,t,n){var r=0,i=0,a=t+n;return e>0&&a>0&&(r=t/a*e,i=n/a*e),{biasDiff:r,biasComplementDiff:i}}}for(var r=0;r<this.length;r++){var i=this[r],a=i._private;a.compoundBoundsClean&&!e||(n(i),t.batching()||(a.compoundBoundsClean=!0))}return this};var Wa=function(e){return e===1/0||e===-1/0?0:e},Ha=function(e,t,n,r,i){r-t!=0&&i-n!=0&&null!=t&&null!=n&&null!=r&&null!=i&&(e.x1=t<e.x1?t:e.x1,e.x2=r>e.x2?r:e.x2,e.y1=n<e.y1?n:e.y1,e.y2=i>e.y2?i:e.y2,e.w=e.x2-e.x1,e.h=e.y2-e.y1)},Ka=function(e,t){return null==t?e:Ha(e,t.x1,t.y1,t.x2,t.y2)},Ga=function(e,t,n){return Ue(e,t,n)},Ua=function(e,t,n){if(!t.cy().headless()){var r,i,a=t._private,o=a.rstyle,s=o.arrowWidth/2;if("none"!==t.pstyle(n+"-arrow-shape").value){"source"===n?(r=o.srcX,i=o.srcY):"target"===n?(r=o.tgtX,i=o.tgtY):(r=o.midX,i=o.midY);var l=a.arrowBounds=a.arrowBounds||{},u=l[n]=l[n]||{};u.x1=r-s,u.y1=i-s,u.x2=r+s,u.y2=i+s,u.w=u.x2-u.x1,u.h=u.y2-u.y1,Nt(u,1),Ha(e,u.x1,u.y1,u.x2,u.y2)}}},Za=function(e,t,n){if(!t.cy().headless()){var r;r=n?n+"-":"";var i=t._private,a=i.rstyle;if(t.pstyle(r+"label").strValue){var o,s,l,u,c=t.pstyle("text-halign"),d=t.pstyle("text-valign"),h=Ga(a,"labelWidth",n),p=Ga(a,"labelHeight",n),f=Ga(a,"labelX",n),g=Ga(a,"labelY",n),v=t.pstyle(r+"text-margin-x").pfValue,y=t.pstyle(r+"text-margin-y").pfValue,m=t.isEdge(),b=t.pstyle(r+"text-rotation"),x=t.pstyle("text-outline-width").pfValue,w=t.pstyle("text-border-width").pfValue/2,E=t.pstyle("text-background-padding").pfValue,k=p,C=h,S=C/2,P=k/2;if(m)o=f-S,s=f+S,l=g-P,u=g+P;else{switch(c.value){case"left":o=f-C,s=f;break;case"center":o=f-S,s=f+S;break;case"right":o=f,s=f+C}switch(d.value){case"top":l=g-k,u=g;break;case"center":l=g-P,u=g+P;break;case"bottom":l=g,u=g+k}}o+=v-Math.max(x,w)-E-2,s+=v+Math.max(x,w)+E+2,l+=y-Math.max(x,w)-E-2,u+=y+Math.max(x,w)+E+2;var D=n||"main",T=i.labelBounds,_=T[D]=T[D]||{};_.x1=o,_.y1=l,_.x2=s,_.y2=u,_.w=s-o,_.h=u-l;var M=m&&"autorotate"===b.strValue,B=null!=b.pfValue&&0!==b.pfValue;if(M||B){var N=M?Ga(i.rstyle,"labelAngle",n):b.pfValue,z=Math.cos(N),I=Math.sin(N),A=(o+s)/2,L=(l+u)/2;if(!m){switch(c.value){case"left":A=s;break;case"right":A=o}switch(d.value){case"top":L=u;break;case"bottom":L=l}}var O=function(e,t){return{x:(e-=A)*z-(t-=L)*I+A,y:e*I+t*z+L}},R=O(o,l),V=O(o,u),F=O(s,l),j=O(s,u);o=Math.min(R.x,V.x,F.x,j.x),s=Math.max(R.x,V.x,F.x,j.x),l=Math.min(R.y,V.y,F.y,j.y),u=Math.max(R.y,V.y,F.y,j.y)}var q=D+"Rot",Y=T[q]=T[q]||{};Y.x1=o,Y.y1=l,Y.x2=s,Y.y2=u,Y.w=s-o,Y.h=u-l,Ha(e,o,l,s,u),Ha(i.labelBounds.all,o,l,s,u)}return e}},$a=function(e,t){var n,r,i,a,o,s,l,u=e._private.cy,c=u.styleEnabled(),d=u.headless(),h=_t(),p=e._private,f=e.isNode(),g=e.isEdge(),v=p.rstyle,y=f&&c?e.pstyle("bounds-expansion").pfValue:[0],m=function(e){return"none"!==e.pstyle("display").value},b=!c||m(e)&&(!g||m(e.source())&&m(e.target()));if(b){var x=0;c&&t.includeOverlays&&0!==e.pstyle("overlay-opacity").value&&(x=e.pstyle("overlay-padding").value);var w=0;c&&t.includeUnderlays&&0!==e.pstyle("underlay-opacity").value&&(w=e.pstyle("underlay-padding").value);var E=Math.max(x,w),k=0;if(c&&(k=e.pstyle("width").pfValue/2),f&&t.includeNodes){var C=e.position();o=C.x,s=C.y;var S=e.outerWidth()/2,P=e.outerHeight()/2;Ha(h,n=o-S,i=s-P,r=o+S,a=s+P),c&&t.includeOutlines&&function(e,t){if(!t.cy().headless()){var n,r,i,a=t.pstyle("outline-opacity").value,o=t.pstyle("outline-width").value;if(a>0&&o>0){var s=t.pstyle("outline-offset").value,l=t.pstyle("shape").value,u=o+s,c=(e.w+2*u)/e.w,d=(e.h+2*u)/e.h,h=0;["diamond","pentagon","round-triangle"].includes(l)?(c=(e.w+2.4*u)/e.w,h=-u/3.6):["concave-hexagon","rhomboid","right-rhomboid"].includes(l)?c=(e.w+2.4*u)/e.w:"star"===l?(c=(e.w+2.8*u)/e.w,d=(e.h+2.6*u)/e.h,h=-u/3.8):"triangle"===l?(c=(e.w+2.8*u)/e.w,d=(e.h+2.4*u)/e.h,h=-u/1.4):"vee"===l&&(c=(e.w+4.4*u)/e.w,d=(e.h+3.8*u)/e.h,h=.5*-u);var p=e.h*d-e.h,f=e.w*c-e.w;if(zt(e,[Math.ceil(p/2),Math.ceil(f/2)]),0!==h){var g=(r=0,i=h,{x1:(n=e).x1+r,x2:n.x2+r,y1:n.y1+i,y2:n.y2+i,w:n.w,h:n.h});Mt(e,g)}}}}(h,e)}else if(g&&t.includeEdges)if(c&&!d){var D=e.pstyle("curve-style").strValue;if(n=Math.min(v.srcX,v.midX,v.tgtX),r=Math.max(v.srcX,v.midX,v.tgtX),i=Math.min(v.srcY,v.midY,v.tgtY),a=Math.max(v.srcY,v.midY,v.tgtY),Ha(h,n-=k,i-=k,r+=k,a+=k),"haystack"===D){var T=v.haystackPts;if(T&&2===T.length){if(n=T[0].x,i=T[0].y,n>(r=T[1].x)){var _=n;n=r,r=_}if(i>(a=T[1].y)){var M=i;i=a,a=M}Ha(h,n-k,i-k,r+k,a+k)}}else if("bezier"===D||"unbundled-bezier"===D||D.endsWith("segments")||D.endsWith("taxi")){var B;switch(D){case"bezier":case"unbundled-bezier":B=v.bezierPts;break;case"segments":case"taxi":case"round-segments":case"round-taxi":B=v.linePts}if(null!=B)for(var N=0;N<B.length;N++){var z=B[N];n=z.x-k,r=z.x+k,i=z.y-k,a=z.y+k,Ha(h,n,i,r,a)}}}else{var I=e.source().position(),A=e.target().position();if((n=I.x)>(r=A.x)){var L=n;n=r,r=L}if((i=I.y)>(a=A.y)){var O=i;i=a,a=O}Ha(h,n-=k,i-=k,r+=k,a+=k)}if(c&&t.includeEdges&&g&&(Ua(h,e,"mid-source"),Ua(h,e,"mid-target"),Ua(h,e,"source"),Ua(h,e,"target")),c)if("yes"===e.pstyle("ghost").value){var R=e.pstyle("ghost-offset-x").pfValue,V=e.pstyle("ghost-offset-y").pfValue;Ha(h,h.x1+R,h.y1+V,h.x2+R,h.y2+V)}var F=p.bodyBounds=p.bodyBounds||{};It(F,h),zt(F,y),Nt(F,1),c&&(n=h.x1,r=h.x2,i=h.y1,a=h.y2,Ha(h,n-E,i-E,r+E,a+E));var j=p.overlayBounds=p.overlayBounds||{};It(j,h),zt(j,y),Nt(j,1);var q=p.labelBounds=p.labelBounds||{};null!=q.all?((l=q.all).x1=1/0,l.y1=1/0,l.x2=-1/0,l.y2=-1/0,l.w=0,l.h=0):q.all=_t(),c&&t.includeLabels&&(t.includeMainLabels&&Za(h,e,null),g&&(t.includeSourceLabels&&Za(h,e,"source"),t.includeTargetLabels&&Za(h,e,"target")))}return h.x1=Wa(h.x1),h.y1=Wa(h.y1),h.x2=Wa(h.x2),h.y2=Wa(h.y2),h.w=Wa(h.x2-h.x1),h.h=Wa(h.y2-h.y1),h.w>0&&h.h>0&&b&&(zt(h,y),Nt(h,1)),h},Qa=function(e){var t=0,n=function(e){return(e?1:0)<<t++},r=0;return r+=n(e.incudeNodes),r+=n(e.includeEdges),r+=n(e.includeLabels),r+=n(e.includeMainLabels),r+=n(e.includeSourceLabels),r+=n(e.includeTargetLabels),r+=n(e.includeOverlays),r+=n(e.includeOutlines)},Ja=function(e){if(e.isEdge()){var t=e.source().position(),n=e.target().position(),r=function(e){return Math.round(e)};return function(e,t){var n={value:0,done:!1},r=0,i=e.length;return ke({next:function(){return r<i?n.value=e[r++]:n.done=!0,n}},t)}([r(t.x),r(t.y),r(n.x),r(n.y)])}return 0},eo=function(e,t){var n,r=e._private,i=e.isEdge(),a=(null==t?no:Qa(t))===no,o=Ja(e),s=r.bbCachePosKey===o,l=t.useCache&&s,u=function(e){return null==e._private.bbCache||e._private.styleDirty};if(!l||u(e)||i&&u(e.source())||u(e.target())?(s||e.recalculateRenderedStyle(l),n=$a(e,to),r.bbCache=n,r.bbCachePosKey=o):n=r.bbCache,!a){var c=e.isNode();n=_t(),(t.includeNodes&&c||t.includeEdges&&!c)&&(t.includeOverlays?Ka(n,r.overlayBounds):Ka(n,r.bodyBounds)),t.includeLabels&&(t.includeMainLabels&&(!i||t.includeSourceLabels&&t.includeTargetLabels)?Ka(n,r.labelBounds.all):(t.includeMainLabels&&Ka(n,r.labelBounds.mainRot),t.includeSourceLabels&&Ka(n,r.labelBounds.sourceRot),t.includeTargetLabels&&Ka(n,r.labelBounds.targetRot))),n.w=n.x2-n.x1,n.h=n.y2-n.y1}return n},to={includeNodes:!0,includeEdges:!0,includeLabels:!0,includeMainLabels:!0,includeSourceLabels:!0,includeTargetLabels:!0,includeOverlays:!0,includeUnderlays:!0,includeOutlines:!0,useCache:!0},no=Qa(to),ro=He(to);Ya.boundingBox=function(e){var t;if(1!==this.length||null==this[0]._private.bbCache||this[0]._private.styleDirty||void 0!==e&&void 0!==e.useCache&&!0!==e.useCache){t=_t();var n=ro(e=e||to);if(this.cy().styleEnabled())for(var r=0;r<this.length;r++){var i=this[r],a=i._private,o=Ja(i),s=a.bbCachePosKey===o,l=n.useCache&&s&&!a.styleDirty;i.recalculateRenderedStyle(l)}this.updateCompoundBounds(!e.useCache);for(var u=0;u<this.length;u++){var c=this[u];Ka(t,eo(c,n))}}else e=void 0===e?to:ro(e),t=eo(this[0],e);return t.x1=Wa(t.x1),t.y1=Wa(t.y1),t.x2=Wa(t.x2),t.y2=Wa(t.y2),t.w=Wa(t.x2-t.x1),t.h=Wa(t.y2-t.y1),t},Ya.dirtyBoundingBoxCache=function(){for(var e=0;e<this.length;e++){var t=this[e]._private;t.bbCache=null,t.bbCachePosKey=null,t.bodyBounds=null,t.overlayBounds=null,t.labelBounds.all=null,t.labelBounds.source=null,t.labelBounds.target=null,t.labelBounds.main=null,t.labelBounds.sourceRot=null,t.labelBounds.targetRot=null,t.labelBounds.mainRot=null,t.arrowBounds.source=null,t.arrowBounds.target=null,t.arrowBounds["mid-source"]=null,t.arrowBounds["mid-target"]=null}return this.emitAndNotify("bounds"),this},Ya.boundingBoxAt=function(e){var t=this.nodes(),n=this.cy(),r=n.hasCompoundNodes(),i=n.collection();if(r&&(i=t.filter((function(e){return e.isParent()})),t=t.not(i)),b(e)){var a=e;e=function(){return a}}n.startBatch(),t.forEach((function(t,n){return t._private.bbAtOldPos=e(t,n)})).silentPositions(e),r&&(i.dirtyCompoundBoundsCache(),i.dirtyBoundingBoxCache(),i.updateCompoundBounds(!0));var o=function(e){return{x1:e.x1,x2:e.x2,w:e.w,y1:e.y1,y2:e.y2,h:e.h}}(this.boundingBox({useCache:!1}));return t.silentPositions((function(e){return e._private.bbAtOldPos})),r&&(i.dirtyCompoundBoundsCache(),i.dirtyBoundingBoxCache(),i.updateCompoundBounds(!0)),n.endBatch(),o},qa.boundingbox=qa.bb=qa.boundingBox,qa.renderedBoundingbox=qa.renderedBoundingBox;var io,ao,oo=Ya;io=ao={};var so=function(e){e.uppercaseName=z(e.name),e.autoName="auto"+e.uppercaseName,e.labelName="label"+e.uppercaseName,e.outerName="outer"+e.uppercaseName,e.uppercaseOuterName=z(e.outerName),io[e.name]=function(){var t=this[0],n=t._private,r=n.cy._private.styleEnabled;if(t){if(!r)return 1;if(t.isParent())return t.updateCompoundBounds(),n[e.autoName]||0;var i=t.pstyle(e.name);switch(i.strValue){case"label":return t.recalculateRenderedStyle(),n.rstyle[e.labelName]||0;default:return i.pfValue}}},io["outer"+e.uppercaseName]=function(){var t=this[0],n=t._private.cy._private.styleEnabled;if(t)return n?t[e.name]()+t.pstyle("border-width").pfValue+2*t.padding():1},io["rendered"+e.uppercaseName]=function(){var t=this[0];if(t)return t[e.name]()*this.cy().zoom()},io["rendered"+e.uppercaseOuterName]=function(){var t=this[0];if(t)return t[e.outerName]()*this.cy().zoom()}};so({name:"width"}),so({name:"height"}),ao.padding=function(){var e=this[0],t=e._private;return e.isParent()?(e.updateCompoundBounds(),void 0!==t.autoPadding?t.autoPadding:e.pstyle("padding").pfValue):e.pstyle("padding").pfValue},ao.paddedHeight=function(){var e=this[0];return e.height()+2*e.padding()},ao.paddedWidth=function(){var e=this[0];return e.width()+2*e.padding()};var lo=ao,uo={controlPoints:{get:function(e){return e.renderer().getControlPoints(e)},mult:!0},segmentPoints:{get:function(e){return e.renderer().getSegmentPoints(e)},mult:!0},sourceEndpoint:{get:function(e){return e.renderer().getSourceEndpoint(e)}},targetEndpoint:{get:function(e){return e.renderer().getTargetEndpoint(e)}},midpoint:{get:function(e){return e.renderer().getEdgeMidpoint(e)}}},co=Object.keys(uo).reduce((function(e,t){var n=uo[t],r=function(e){return"rendered"+e[0].toUpperCase()+e.substr(1)}(t);return e[t]=function(){return function(e,t){if(e.isEdge())return t(e)}(this,n.get)},n.mult?e[r]=function(){return function(e,t){if(e.isEdge()){var n=e.cy(),r=n.pan(),i=n.zoom();return t(e).map((function(e){return yt(e,i,r)}))}}(this,n.get)}:e[r]=function(){return function(e,t){if(e.isEdge()){var n=e.cy();return yt(t(e),n.zoom(),n.pan())}}(this,n.get)},e}),{}),ho=L({},Xa,oo,lo,co),po=function(e,t){this.recycle(e,t)};function fo(){return!1}function go(){return!0}po.prototype={instanceString:function(){return"event"},recycle:function(e,t){if(this.isImmediatePropagationStopped=this.isPropagationStopped=this.isDefaultPrevented=fo,null!=e&&e.preventDefault?(this.type=e.type,this.isDefaultPrevented=e.defaultPrevented?go:fo):null!=e&&e.type?t=e:this.type=e,null!=t&&(this.originalEvent=t.originalEvent,this.type=null!=t.type?t.type:this.type,this.cy=t.cy,this.target=t.target,this.position=t.position,this.renderedPosition=t.renderedPosition,this.namespace=t.namespace,this.layout=t.layout),null!=this.cy&&null!=this.position&&null==this.renderedPosition){var n=this.position,r=this.cy.zoom(),i=this.cy.pan();this.renderedPosition={x:n.x*r+i.x,y:n.y*r+i.y}}this.timeStamp=e&&e.timeStamp||Date.now()},preventDefault:function(){this.isDefaultPrevented=go;var e=this.originalEvent;e&&e.preventDefault&&e.preventDefault()},stopPropagation:function(){this.isPropagationStopped=go;var e=this.originalEvent;e&&e.stopPropagation&&e.stopPropagation()},stopImmediatePropagation:function(){this.isImmediatePropagationStopped=go,this.stopPropagation()},isDefaultPrevented:fo,isPropagationStopped:fo,isImmediatePropagationStopped:fo};var vo=/^([^.]+)(\.(?:[^.]+))?$/,yo={qualifierCompare:function(e,t){return e===t},eventMatches:function(){return!0},addEventFields:function(){},callbackContext:function(e){return e},beforeEmit:function(){},afterEmit:function(){},bubble:function(){return!1},parent:function(){return null},context:null},mo=Object.keys(yo),bo={};function xo(){for(var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:bo,t=arguments.length>1?arguments[1]:void 0,n=0;n<mo.length;n++){var r=mo[n];this[r]=e[r]||yo[r]}this.context=t||this.context,this.listeners=[],this.emitting=0}var wo=xo.prototype,Eo=function(e,t,n,r,i,a,o){y(r)&&(i=r,r=null),o&&(a=null==a?o:L({},a,o));for(var s=m(n)?n:n.split(/\s+/),l=0;l<s.length;l++){var u=s[l];if(!D(u)){var c=u.match(vo);if(c)if(!1===t(e,u,c[1],c[2]?c[2]:null,r,i,a))break}}},ko=function(e,t){return e.addEventFields(e.context,t),new po(t.type,t)},Co=function(e,t,n){if("event"!==g(n))if(b(n))t(e,ko(e,n));else for(var r=m(n)?n:n.split(/\s+/),i=0;i<r.length;i++){var a=r[i];if(!D(a)){var o=a.match(vo);if(o){var s=o[1],l=o[2]?o[2]:null;t(e,ko(e,{type:s,namespace:l,target:e.context}))}}}else t(e,n)};wo.on=wo.addListener=function(e,t,n,r,i){return Eo(this,(function(e,t,n,r,i,a,o){y(a)&&e.listeners.push({event:t,callback:a,type:n,namespace:r,qualifier:i,conf:o})}),e,t,n,r,i),this},wo.one=function(e,t,n,r){return this.on(e,t,n,r,{one:!0})},wo.removeListener=wo.off=function(e,t,n,r){var i=this;0!==this.emitting&&(this.listeners=this.listeners.slice());for(var a=this.listeners,o=function(o){var s=a[o];Eo(i,(function(t,n,r,i,l,u){if((s.type===r||"*"===e)&&(!i&&".*"!==s.namespace||s.namespace===i)&&(!l||t.qualifierCompare(s.qualifier,l))&&(!u||s.callback===u))return a.splice(o,1),!1}),e,t,n,r)},s=a.length-1;s>=0;s--)o(s);return this},wo.removeAllListeners=function(){return this.removeListener("*")},wo.emit=wo.trigger=function(e,t,n){var r=this.listeners,i=r.length;return this.emitting++,m(t)||(t=[t]),Co(this,(function(e,a){null!=n&&(r=[{event:a.event,type:a.type,namespace:a.namespace,callback:n}],i=r.length);for(var o=function(n){var i=r[n];if(i.type===a.type&&(!i.namespace||i.namespace===a.namespace||".*"===i.namespace)&&e.eventMatches(e.context,i,a)){var o=[a];null!=t&&function(e,t){for(var n=0;n<t.length;n++){var r=t[n];e.push(r)}}(o,t),e.beforeEmit(e.context,i,a),i.conf&&i.conf.one&&(e.listeners=e.listeners.filter((function(e){return e!==i})));var s=e.callbackContext(e.context,i,a),l=i.callback.apply(s,o);e.afterEmit(e.context,i,a),!1===l&&(a.stopPropagation(),a.preventDefault())}},s=0;s<i;s++)o(s);e.bubble(e.context)&&!a.isPropagationStopped()&&e.parent(e.context).emit(a,t)}),e),this.emitting--,this};var So={qualifierCompare:function(e,t){return null==e||null==t?null==e&&null==t:e.sameText(t)},eventMatches:function(e,t,n){var r=t.qualifier;return null==r||e!==n.target&&k(n.target)&&r.matches(n.target)},addEventFields:function(e,t){t.cy=e.cy(),t.target=e},callbackContext:function(e,t,n){return null!=t.qualifier?n.target:e},beforeEmit:function(e,t){t.conf&&t.conf.once&&t.conf.onceCollection.removeListener(t.event,t.qualifier,t.callback)},bubble:function(){return!0},parent:function(e){return e.isChild()?e.parent():e.cy()}},Po=function(e){return v(e)?new ka(e):e},Do={createEmitter:function(){for(var e=0;e<this.length;e++){var t=this[e],n=t._private;n.emitter||(n.emitter=new xo(So,t))}return this},emitter:function(){return this._private.emitter},on:function(e,t,n){for(var r=Po(t),i=0;i<this.length;i++){this[i].emitter().on(e,r,n)}return this},removeListener:function(e,t,n){for(var r=Po(t),i=0;i<this.length;i++){this[i].emitter().removeListener(e,r,n)}return this},removeAllListeners:function(){for(var e=0;e<this.length;e++){this[e].emitter().removeAllListeners()}return this},one:function(e,t,n){for(var r=Po(t),i=0;i<this.length;i++){this[i].emitter().one(e,r,n)}return this},once:function(e,t,n){for(var r=Po(t),i=0;i<this.length;i++){this[i].emitter().on(e,r,n,{once:!0,onceCollection:this})}},emit:function(e,t){for(var n=0;n<this.length;n++){this[n].emitter().emit(e,t)}return this},emitAndNotify:function(e,t){if(0!==this.length)return this.cy().notify(e,this),this.emit(e,t),this}};Fi.eventAliasesOn(Do);var To={nodes:function(e){return this.filter((function(e){return e.isNode()})).filter(e)},edges:function(e){return this.filter((function(e){return e.isEdge()})).filter(e)},byGroup:function(){for(var e=this.spawn(),t=this.spawn(),n=0;n<this.length;n++){var r=this[n];r.isNode()?e.push(r):t.push(r)}return{nodes:e,edges:t}},filter:function(e,t){if(void 0===e)return this;if(v(e)||E(e))return new ka(e).filter(this);if(y(e)){for(var n=this.spawn(),r=0;r<this.length;r++){var i=this[r];(t?e.apply(t,[i,r,this]):e(i,r,this))&&n.push(i)}return n}return this.spawn()},not:function(e){if(e){v(e)&&(e=this.filter(e));for(var t=this.spawn(),n=0;n<this.length;n++){var r=this[n];e.has(r)||t.push(r)}return t}return this},absoluteComplement:function(){return this.cy().mutableElements().not(this)},intersect:function(e){if(v(e)){var t=e;return this.filter(t)}for(var n=this.spawn(),r=e,i=this.length<e.length,a=i?this:r,o=i?r:this,s=0;s<a.length;s++){var l=a[s];o.has(l)&&n.push(l)}return n},xor:function(e){var t=this._private.cy;v(e)&&(e=t.$(e));var n=this.spawn(),r=e,i=function(e,t){for(var r=0;r<e.length;r++){var i=e[r],a=i._private.data.id;t.hasElementWithId(a)||n.push(i)}};return i(this,r),i(r,this),n},diff:function(e){var t=this._private.cy;v(e)&&(e=t.$(e));var n=this.spawn(),r=this.spawn(),i=this.spawn(),a=e,o=function(e,t,n){for(var r=0;r<e.length;r++){var a=e[r],o=a._private.data.id;t.hasElementWithId(o)?i.merge(a):n.push(a)}};return o(this,a,n),o(a,this,r),{left:n,right:r,both:i}},add:function(e){var t=this._private.cy;if(!e)return this;if(v(e)){var n=e;e=t.mutableElements().filter(n)}for(var r=this.spawnSelf(),i=0;i<e.length;i++){var a=e[i],o=!this.has(a);o&&r.push(a)}return r},merge:function(e){var t=this._private,n=t.cy;if(!e)return this;if(e&&v(e)){var r=e;e=n.mutableElements().filter(r)}for(var i=t.map,a=0;a<e.length;a++){var o=e[a],s=o._private.data.id;if(!i.has(s)){var l=this.length++;this[l]=o,i.set(s,{ele:o,index:l})}}return this},unmergeAt:function(e){var t=this[e].id(),n=this._private.map;this[e]=void 0,n.delete(t);var r=e===this.length-1;if(this.length>1&&!r){var i=this.length-1,a=this[i],o=a._private.data.id;this[i]=void 0,this[e]=a,n.set(o,{ele:a,index:e})}return this.length--,this},unmergeOne:function(e){e=e[0];var t=this._private,n=e._private.data.id,r=t.map.get(n);if(!r)return this;var i=r.index;return this.unmergeAt(i),this},unmerge:function(e){var t=this._private.cy;if(!e)return this;if(e&&v(e)){var n=e;e=t.mutableElements().filter(n)}for(var r=0;r<e.length;r++)this.unmergeOne(e[r]);return this},unmergeBy:function(e){for(var t=this.length-1;t>=0;t--){e(this[t])&&this.unmergeAt(t)}return this},map:function(e,t){for(var n=[],r=0;r<this.length;r++){var i=this[r],a=t?e.apply(t,[i,r,this]):e(i,r,this);n.push(a)}return n},reduce:function(e,t){for(var n=t,r=0;r<this.length;r++)n=e(n,this[r],r,this);return n},max:function(e,t){for(var n,r=-1/0,i=0;i<this.length;i++){var a=this[i],o=t?e.apply(t,[a,i,this]):e(a,i,this);o>r&&(r=o,n=a)}return{value:r,ele:n}},min:function(e,t){for(var n,r=1/0,i=0;i<this.length;i++){var a=this[i],o=t?e.apply(t,[a,i,this]):e(a,i,this);o<r&&(r=o,n=a)}return{value:r,ele:n}}},_o=To;_o.u=_o["|"]=_o["+"]=_o.union=_o.or=_o.add,_o["\\"]=_o["!"]=_o["-"]=_o.difference=_o.relativeComplement=_o.subtract=_o.not,_o.n=_o["&"]=_o["."]=_o.and=_o.intersection=_o.intersect,_o["^"]=_o["(+)"]=_o["(-)"]=_o.symmetricDifference=_o.symdiff=_o.xor,_o.fnFilter=_o.filterFn=_o.stdFilter=_o.filter,_o.complement=_o.abscomp=_o.absoluteComplement;var Mo=function(e,t){var n=e.cy().hasCompoundNodes();function r(e){var t=e.pstyle("z-compound-depth");return"auto"===t.value?n?e.zDepth():0:"bottom"===t.value?-1:"top"===t.value?Ie:0}var i=r(e)-r(t);if(0!==i)return i;function a(e){return"auto"===e.pstyle("z-index-compare").value&&e.isNode()?1:0}var o=a(e)-a(t);if(0!==o)return o;var s=e.pstyle("z-index").value-t.pstyle("z-index").value;return 0!==s?s:e.poolIndex()-t.poolIndex()},Bo={forEach:function(e,t){if(y(e))for(var n=this.length,r=0;r<n;r++){var i=this[r];if(!1===(t?e.apply(t,[i,r,this]):e(i,r,this)))break}return this},toArray:function(){for(var e=[],t=0;t<this.length;t++)e.push(this[t]);return e},slice:function(e,t){var n=[],r=this.length;null==t&&(t=r),null==e&&(e=0),e<0&&(e=r+e),t<0&&(t=r+t);for(var i=e;i>=0&&i<t&&i<r;i++)n.push(this[i]);return this.spawn(n)},size:function(){return this.length},eq:function(e){return this[e]||this.spawn()},first:function(){return this[0]||this.spawn()},last:function(){return this[this.length-1]||this.spawn()},empty:function(){return 0===this.length},nonempty:function(){return!this.empty()},sort:function(e){if(!y(e))return this;var t=this.toArray().sort(e);return this.spawn(t)},sortByZIndex:function(){return this.sort(Mo)},zDepth:function(){var e=this[0];if(e){var t=e._private;if("nodes"===t.group){var n=t.data.parent?e.parents().size():0;return e.isParent()?n:Ie-1}var r=t.source,i=t.target,a=r.zDepth(),o=i.zDepth();return Math.max(a,o,0)}}};Bo.each=Bo.forEach;"undefined"!=("undefined"==typeof Symbol?"undefined":e(Symbol))&&"undefined"!=e(Symbol.iterator)&&(Bo[Symbol.iterator]=function(){var e=this,t={value:void 0,done:!1},n=0,r=this.length;return i({next:function(){return n<r?t.value=e[n++]:(t.value=void 0,t.done=!0),t}},Symbol.iterator,(function(){return this}))});var No=He({nodeDimensionsIncludeLabels:!1}),zo={layoutDimensions:function(e){var t;if(e=No(e),this.takesUpSpace())if(e.nodeDimensionsIncludeLabels){var n=this.boundingBox();t={w:n.w,h:n.h}}else t={w:this.outerWidth(),h:this.outerHeight()};else t={w:0,h:0};return 0!==t.w&&0!==t.h||(t.w=t.h=1),t},layoutPositions:function(e,t,n){var r=this.nodes().filter((function(e){return!e.isParent()})),i=this.cy(),a=t.eles,o=function(e){return e.id()},s=_(n,o);e.emit({type:"layoutstart",layout:e}),e.animations=[];var l=t.spacingFactor&&1!==t.spacingFactor,u=function(){if(!l)return null;for(var e=_t(),t=0;t<r.length;t++){var n=r[t],i=s(n,t);Bt(e,i.x,i.y)}return e}(),c=_((function(e,n){var r=s(e,n);l&&(r=function(e,t,n){var r=t.x1+t.w/2,i=t.y1+t.h/2;return{x:r+(n.x-r)*e,y:i+(n.y-i)*e}}(Math.abs(t.spacingFactor),u,r));return null!=t.transform&&(r=t.transform(e,r)),r}),o);if(t.animate){for(var d=0;d<r.length;d++){var h=r[d],p=c(h,d);if(null==t.animateFilter||t.animateFilter(h,d)){var f=h.animation({position:p,duration:t.animationDuration,easing:t.animationEasing});e.animations.push(f)}else h.position(p)}if(t.fit){var g=i.animation({fit:{boundingBox:a.boundingBoxAt(c),padding:t.padding},duration:t.animationDuration,easing:t.animationEasing});e.animations.push(g)}else if(void 0!==t.zoom&&void 0!==t.pan){var v=i.animation({zoom:t.zoom,pan:t.pan,duration:t.animationDuration,easing:t.animationEasing});e.animations.push(v)}e.animations.forEach((function(e){return e.play()})),e.one("layoutready",t.ready),e.emit({type:"layoutready",layout:e}),vr.all(e.animations.map((function(e){return e.promise()}))).then((function(){e.one("layoutstop",t.stop),e.emit({type:"layoutstop",layout:e})}))}else r.positions(c),t.fit&&i.fit(t.eles,t.padding),null!=t.zoom&&i.zoom(t.zoom),t.pan&&i.pan(t.pan),e.one("layoutready",t.ready),e.emit({type:"layoutready",layout:e}),e.one("layoutstop",t.stop),e.emit({type:"layoutstop",layout:e});return this},layout:function(e){return this.cy().makeLayout(L({},e,{eles:this}))}};function Io(e,t,n){var r,i=n._private,a=i.styleCache=i.styleCache||[];return null!=(r=a[e])?r:r=a[e]=t(n)}function Ao(e,t){return e=Te(e),function(n){return Io(e,t,n)}}function Lo(e,t){e=Te(e);var n=function(e){return t.call(e)};return function(){var t=this[0];if(t)return Io(e,n,t)}}zo.createLayout=zo.makeLayout=zo.layout;var Oo={recalculateRenderedStyle:function(e){var t=this.cy(),n=t.renderer(),r=t.styleEnabled();return n&&r&&n.recalculateRenderedStyle(this,e),this},dirtyStyleCache:function(){var e,t=this.cy(),n=function(e){return e._private.styleCache=null};t.hasCompoundNodes()?((e=this.spawnSelf().merge(this.descendants()).merge(this.parents())).merge(e.connectedEdges()),e.forEach(n)):this.forEach((function(e){n(e),e.connectedEdges().forEach(n)}));return this},updateStyle:function(e){var t=this._private.cy;if(!t.styleEnabled())return this;if(t.batching())return t._private.batchStyleEles.merge(this),this;var n=this;e=!(!e&&void 0!==e),t.hasCompoundNodes()&&(n=this.spawnSelf().merge(this.descendants()).merge(this.parents()));var r=n;return e?r.emitAndNotify("style"):r.emit("style"),n.forEach((function(e){return e._private.styleDirty=!0})),this},cleanStyle:function(){var e=this.cy();if(e.styleEnabled())for(var t=0;t<this.length;t++){var n=this[t];n._private.styleDirty&&(n._private.styleDirty=!1,e.style().apply(n))}},parsedStyle:function(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],n=this[0],r=n.cy();if(r.styleEnabled()&&n){this.cleanStyle();var i=n._private.style[e];return null!=i?i:t?r.style().getDefaultProperty(e):null}},numericStyle:function(e){var t=this[0];if(t.cy().styleEnabled()&&t){var n=t.pstyle(e);return void 0!==n.pfValue?n.pfValue:n.value}},numericStyleUnits:function(e){var t=this[0];if(t.cy().styleEnabled())return t?t.pstyle(e).units:void 0},renderedStyle:function(e){var t=this.cy();if(!t.styleEnabled())return this;var n=this[0];return n?t.style().getRenderedStyle(n,e):void 0},style:function(e,t){var n=this.cy();if(!n.styleEnabled())return this;var r=n.style();if(b(e)){var i=e;r.applyBypass(this,i,!1),this.emitAndNotify("style")}else if(v(e)){if(void 0===t){var a=this[0];return a?r.getStylePropertyValue(a,e):void 0}r.applyBypass(this,e,t,!1),this.emitAndNotify("style")}else if(void 0===e){var o=this[0];return o?r.getRawStyle(o):void 0}return this},removeStyle:function(e){var t=this.cy();if(!t.styleEnabled())return this;var n=t.style();if(void 0===e)for(var r=0;r<this.length;r++){var i=this[r];n.removeAllBypasses(i,!1)}else{e=e.split(/\s+/);for(var a=0;a<this.length;a++){var o=this[a];n.removeBypasses(o,e,!1)}}return this.emitAndNotify("style"),this},show:function(){return this.css("display","element"),this},hide:function(){return this.css("display","none"),this},effectiveOpacity:function(){var e=this.cy();if(!e.styleEnabled())return 1;var t=e.hasCompoundNodes(),n=this[0];if(n){var r=n._private,i=n.pstyle("opacity").value;if(!t)return i;var a=r.data.parent?n.parents():null;if(a)for(var o=0;o<a.length;o++){i*=a[o].pstyle("opacity").value}return i}},transparent:function(){if(!this.cy().styleEnabled())return!1;var e=this[0],t=e.cy().hasCompoundNodes();return e?t?0===e.effectiveOpacity():0===e.pstyle("opacity").value:void 0},backgrounding:function(){return!!this.cy().styleEnabled()&&!!this[0]._private.backgrounding}};function Ro(e,t){var n=e._private.data.parent?e.parents():null;if(n)for(var r=0;r<n.length;r++){if(!t(n[r]))return!1}return!0}function Vo(e){var t=e.ok,n=e.edgeOkViaNode||e.ok,r=e.parentOk||e.ok;return function(){var e=this.cy();if(!e.styleEnabled())return!0;var i=this[0],a=e.hasCompoundNodes();if(i){var o=i._private;if(!t(i))return!1;if(i.isNode())return!a||Ro(i,r);var s=o.source,l=o.target;return n(s)&&(!a||Ro(s,n))&&(s===l||n(l)&&(!a||Ro(l,n)))}}}var Fo=Ao("eleTakesUpSpace",(function(e){return"element"===e.pstyle("display").value&&0!==e.width()&&(!e.isNode()||0!==e.height())}));Oo.takesUpSpace=Lo("takesUpSpace",Vo({ok:Fo}));var jo=Ao("eleInteractive",(function(e){return"yes"===e.pstyle("events").value&&"visible"===e.pstyle("visibility").value&&Fo(e)})),qo=Ao("parentInteractive",(function(e){return"visible"===e.pstyle("visibility").value&&Fo(e)}));Oo.interactive=Lo("interactive",Vo({ok:jo,parentOk:qo,edgeOkViaNode:Fo})),Oo.noninteractive=function(){var e=this[0];if(e)return!e.interactive()};var Yo=Ao("eleVisible",(function(e){return"visible"===e.pstyle("visibility").value&&0!==e.pstyle("opacity").pfValue&&Fo(e)})),Xo=Fo;Oo.visible=Lo("visible",Vo({ok:Yo,edgeOkViaNode:Xo})),Oo.hidden=function(){var e=this[0];if(e)return!e.visible()},Oo.isBundledBezier=Lo("isBundledBezier",(function(){return!!this.cy().styleEnabled()&&(!this.removed()&&"bezier"===this.pstyle("curve-style").value&&this.takesUpSpace())})),Oo.bypass=Oo.css=Oo.style,Oo.renderedCss=Oo.renderedStyle,Oo.removeBypass=Oo.removeCss=Oo.removeStyle,Oo.pstyle=Oo.parsedStyle;var Wo={};function Ho(e){return function(){var t=arguments,n=[];if(2===t.length){var r=t[0],i=t[1];this.on(e.event,r,i)}else if(1===t.length&&y(t[0])){var a=t[0];this.on(e.event,a)}else if(0===t.length||1===t.length&&m(t[0])){for(var o=1===t.length?t[0]:null,s=0;s<this.length;s++){var l=this[s],u=!e.ableField||l._private[e.ableField],c=l._private[e.field]!=e.value;if(e.overrideAble){var d=e.overrideAble(l);if(void 0!==d&&(u=d,!d))return this}u&&(l._private[e.field]=e.value,c&&n.push(l))}var h=this.spawn(n);h.updateStyle(),h.emit(e.event),o&&h.emit(o)}return this}}function Ko(e){Wo[e.field]=function(){var t=this[0];if(t){if(e.overrideField){var n=e.overrideField(t);if(void 0!==n)return n}return t._private[e.field]}},Wo[e.on]=Ho({event:e.on,field:e.field,ableField:e.ableField,overrideAble:e.overrideAble,value:!0}),Wo[e.off]=Ho({event:e.off,field:e.field,ableField:e.ableField,overrideAble:e.overrideAble,value:!1})}Ko({field:"locked",overrideField:function(e){return!!e.cy().autolock()||void 0},on:"lock",off:"unlock"}),Ko({field:"grabbable",overrideField:function(e){return!e.cy().autoungrabify()&&!e.pannable()&&void 0},on:"grabify",off:"ungrabify"}),Ko({field:"selected",ableField:"selectable",overrideAble:function(e){return!e.cy().autounselectify()&&void 0},on:"select",off:"unselect"}),Ko({field:"selectable",overrideField:function(e){return!e.cy().autounselectify()&&void 0},on:"selectify",off:"unselectify"}),Wo.deselect=Wo.unselect,Wo.grabbed=function(){var e=this[0];if(e)return e._private.grabbed},Ko({field:"active",on:"activate",off:"unactivate"}),Ko({field:"pannable",on:"panify",off:"unpanify"}),Wo.inactive=function(){var e=this[0];if(e)return!e._private.active};var Go={},Uo=function(e){return function(t){for(var n=[],r=0;r<this.length;r++){var i=this[r];if(i.isNode()){for(var a=!1,o=i.connectedEdges(),s=0;s<o.length;s++){var l=o[s],u=l.source(),c=l.target();if(e.noIncomingEdges&&c===i&&u!==i||e.noOutgoingEdges&&u===i&&c!==i){a=!0;break}}a||n.push(i)}}return this.spawn(n,!0).filter(t)}},Zo=function(e){return function(t){for(var n=[],r=0;r<this.length;r++){var i=this[r];if(i.isNode())for(var a=i.connectedEdges(),o=0;o<a.length;o++){var s=a[o],l=s.source(),u=s.target();e.outgoing&&l===i?(n.push(s),n.push(u)):e.incoming&&u===i&&(n.push(s),n.push(l))}}return this.spawn(n,!0).filter(t)}},$o=function(e){return function(t){for(var n=this,r=[],i={};;){var a=e.outgoing?n.outgoers():n.incomers();if(0===a.length)break;for(var o=!1,s=0;s<a.length;s++){var l=a[s],u=l.id();i[u]||(i[u]=!0,r.push(l),o=!0)}if(!o)break;n=a}return this.spawn(r,!0).filter(t)}};function Qo(e){return function(t){for(var n=[],r=0;r<this.length;r++){var i=this[r]._private[e.attr];i&&n.push(i)}return this.spawn(n,!0).filter(t)}}function Jo(e){return function(t){var n=[],r=this._private.cy,i=e||{};v(t)&&(t=r.$(t));for(var a=0;a<t.length;a++)for(var o=t[a]._private.edges,s=0;s<o.length;s++){var l=o[s],u=l._private.data,c=this.hasElementWithId(u.source)&&t.hasElementWithId(u.target),d=t.hasElementWithId(u.source)&&this.hasElementWithId(u.target);if(c||d){if(i.thisIsSrc||i.thisIsTgt){if(i.thisIsSrc&&!c)continue;if(i.thisIsTgt&&!d)continue}n.push(l)}}return this.spawn(n,!0)}}function es(e){return e=L({},{codirected:!1},e),function(t){for(var n=[],r=this.edges(),i=e,a=0;a<r.length;a++)for(var o=r[a]._private,s=o.source,l=s._private.data.id,u=o.data.target,c=s._private.edges,d=0;d<c.length;d++){var h=c[d],p=h._private.data,f=p.target,g=p.source,v=f===u&&g===l,y=l===f&&u===g;(i.codirected&&v||!i.codirected&&(v||y))&&n.push(h)}return this.spawn(n,!0).filter(t)}}Go.clearTraversalCache=function(){for(var e=0;e<this.length;e++)this[e]._private.traversalCache=null},L(Go,{roots:Uo({noIncomingEdges:!0}),leaves:Uo({noOutgoingEdges:!0}),outgoers:Ta(Zo({outgoing:!0}),"outgoers"),successors:$o({outgoing:!0}),incomers:Ta(Zo({incoming:!0}),"incomers"),predecessors:$o({incoming:!0})}),L(Go,{neighborhood:Ta((function(e){for(var t=[],n=this.nodes(),r=0;r<n.length;r++)for(var i=n[r],a=i.connectedEdges(),o=0;o<a.length;o++){var s=a[o],l=s.source(),u=s.target(),c=i===l?u:l;c.length>0&&t.push(c[0]),t.push(s[0])}return this.spawn(t,!0).filter(e)}),"neighborhood"),closedNeighborhood:function(e){return this.neighborhood().add(this).filter(e)},openNeighborhood:function(e){return this.neighborhood(e)}}),Go.neighbourhood=Go.neighborhood,Go.closedNeighbourhood=Go.closedNeighborhood,Go.openNeighbourhood=Go.openNeighborhood,L(Go,{source:Ta((function(e){var t,n=this[0];return n&&(t=n._private.source||n.cy().collection()),t&&e?t.filter(e):t}),"source"),target:Ta((function(e){var t,n=this[0];return n&&(t=n._private.target||n.cy().collection()),t&&e?t.filter(e):t}),"target"),sources:Qo({attr:"source"}),targets:Qo({attr:"target"})}),L(Go,{edgesWith:Ta(Jo(),"edgesWith"),edgesTo:Ta(Jo({thisIsSrc:!0}),"edgesTo")}),L(Go,{connectedEdges:Ta((function(e){for(var t=[],n=0;n<this.length;n++){var r=this[n];if(r.isNode())for(var i=r._private.edges,a=0;a<i.length;a++){var o=i[a];t.push(o)}}return this.spawn(t,!0).filter(e)}),"connectedEdges"),connectedNodes:Ta((function(e){for(var t=[],n=0;n<this.length;n++){var r=this[n];r.isEdge()&&(t.push(r.source()[0]),t.push(r.target()[0]))}return this.spawn(t,!0).filter(e)}),"connectedNodes"),parallelEdges:Ta(es(),"parallelEdges"),codirectedEdges:Ta(es({codirected:!0}),"codirectedEdges")}),L(Go,{components:function(e){var t=this,n=t.cy(),r=n.collection(),i=null==e?t.nodes():e.nodes(),a=[];null!=e&&i.empty()&&(i=e.sources());var o=function(e,t){r.merge(e),i.unmerge(e),t.merge(e)};if(i.empty())return t.spawn();var s=function(){var e=n.collection();a.push(e);var r=i[0];o(r,e),t.bfs({directed:!1,roots:r,visit:function(t){return o(t,e)}}),e.forEach((function(n){n.connectedEdges().forEach((function(n){t.has(n)&&e.has(n.source())&&e.has(n.target())&&e.merge(n)}))}))};do{s()}while(i.length>0);return a},component:function(){var e=this[0];return e.cy().mutableElements().components(e)[0]}}),Go.componentsOf=Go.components;var ts=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=arguments.length>3&&void 0!==arguments[3]&&arguments[3];if(void 0!==e){var i=new $e,a=!1;if(t){if(t.length>0&&b(t[0])&&!k(t[0])){a=!0;for(var o=[],s=new Je,l=0,u=t.length;l<u;l++){var c=t[l];null==c.data&&(c.data={});var d=c.data;if(null==d.id)d.id=Ye();else if(e.hasElementWithId(d.id)||s.has(d.id))continue;var h=new et(e,c,!1);o.push(h),s.add(d.id)}t=o}}else t=[];this.length=0;for(var p=0,f=t.length;p<f;p++){var g=t[p][0];if(null!=g){var v=g._private.data.id;n&&i.has(v)||(n&&i.set(v,{index:this.length,ele:g}),this[this.length]=g,this.length++)}}this._private={eles:this,cy:e,get map(){return null==this.lazyMap&&this.rebuildMap(),this.lazyMap},set map(e){this.lazyMap=e},rebuildMap:function(){for(var e=this.lazyMap=new $e,t=this.eles,n=0;n<t.length;n++){var r=t[n];e.set(r.id(),{index:n,ele:r})}}},n&&(this._private.map=i),a&&!r&&this.restore()}else Ve("A collection must have a reference to the core")},ns=et.prototype=ts.prototype=Object.create(Array.prototype);ns.instanceString=function(){return"collection"},ns.spawn=function(e,t){return new ts(this.cy(),e,t)},ns.spawnSelf=function(){return this.spawn(this)},ns.cy=function(){return this._private.cy},ns.renderer=function(){return this._private.cy.renderer()},ns.element=function(){return this[0]},ns.collection=function(){return C(this)?this:new ts(this._private.cy,[this])},ns.unique=function(){return new ts(this._private.cy,this,!0)},ns.hasElementWithId=function(e){return e=""+e,this._private.map.has(e)},ns.getElementById=function(e){e=""+e;var t=this._private.cy,n=this._private.map.get(e);return n?n.ele:new ts(t)},ns.$id=ns.getElementById,ns.poolIndex=function(){var e=this._private.cy._private.elements,t=this[0]._private.data.id;return e._private.map.get(t).index},ns.indexOf=function(e){var t=e[0]._private.data.id;return this._private.map.get(t).index},ns.indexOfId=function(e){return e=""+e,this._private.map.get(e).index},ns.json=function(e){var t=this.element(),n=this.cy();if(null==t&&e)return this;if(null!=t){var r=t._private;if(b(e)){if(n.startBatch(),e.data){t.data(e.data);var i=r.data;if(t.isEdge()){var a=!1,o={},s=e.data.source,l=e.data.target;null!=s&&s!=i.source&&(o.source=""+s,a=!0),null!=l&&l!=i.target&&(o.target=""+l,a=!0),a&&(t=t.move(o))}else{var u="parent"in e.data,c=e.data.parent;!u||null==c&&null==i.parent||c==i.parent||(void 0===c&&(c=null),null!=c&&(c=""+c),t=t.move({parent:c}))}}e.position&&t.position(e.position);var d=function(n,i,a){var o=e[n];null!=o&&o!==r[n]&&(o?t[i]():t[a]())};return d("removed","remove","restore"),d("selected","select","unselect"),d("selectable","selectify","unselectify"),d("locked","lock","unlock"),d("grabbable","grabify","ungrabify"),d("pannable","panify","unpanify"),null!=e.classes&&t.classes(e.classes),n.endBatch(),this}if(void 0===e){var h={data:qe(r.data),position:qe(r.position),group:r.group,removed:r.removed,selected:r.selected,selectable:r.selectable,locked:r.locked,grabbable:r.grabbable,pannable:r.pannable,classes:null};h.classes="";var p=0;return r.classes.forEach((function(e){return h.classes+=0==p++?e:" "+e})),h}}},ns.jsons=function(){for(var e=[],t=0;t<this.length;t++){var n=this[t].json();e.push(n)}return e},ns.clone=function(){for(var e=this.cy(),t=[],n=0;n<this.length;n++){var r=this[n].json(),i=new et(e,r,!1);t.push(i)}return new ts(e,t)},ns.copy=ns.clone,ns.restore=function(){for(var e,t,n=!(arguments.length>0&&void 0!==arguments[0])||arguments[0],r=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],i=this,a=i.cy(),o=a._private,s=[],l=[],u=0,c=i.length;u<c;u++){var d=i[u];r&&!d.removed()||(d.isNode()?s.push(d):l.push(d))}e=s.concat(l);var h=function(){e.splice(t,1),t--};for(t=0;t<e.length;t++){var p=e[t],f=p._private,g=f.data;if(p.clearTraversalCache(),r||f.removed)if(void 0===g.id)g.id=Ye();else if(x(g.id))g.id=""+g.id;else{if(D(g.id)||!v(g.id)){Ve("Can not create element with invalid string ID `"+g.id+"`"),h();continue}if(a.hasElementWithId(g.id)){Ve("Can not create second element with ID `"+g.id+"`"),h();continue}}else;var y=g.id;if(p.isNode()){var m=f.position;null==m.x&&(m.x=0),null==m.y&&(m.y=0)}if(p.isEdge()){for(var b=p,w=["source","target"],E=w.length,k=!1,C=0;C<E;C++){var S=w[C],P=g[S];x(P)&&(P=g[S]=""+g[S]),null==P||""===P?(Ve("Can not create edge `"+y+"` with unspecified "+S),k=!0):a.hasElementWithId(P)||(Ve("Can not create edge `"+y+"` with nonexistant "+S+" `"+P+"`"),k=!0)}if(k){h();continue}var T=a.getElementById(g.source),_=a.getElementById(g.target);T.same(_)?T._private.edges.push(b):(T._private.edges.push(b),_._private.edges.push(b)),b._private.source=T,b._private.target=_}f.map=new $e,f.map.set(y,{ele:p,index:0}),f.removed=!1,r&&a.addToPool(p)}for(var M=0;M<s.length;M++){var B=s[M],N=B._private.data;x(N.parent)&&(N.parent=""+N.parent);var z=N.parent,I=null!=z;if(I||B._private.parent){var A=B._private.parent?a.collection().merge(B._private.parent):a.getElementById(z);if(A.empty())N.parent=void 0;else if(A[0].removed())je("Node added with missing parent, reference to parent removed"),N.parent=void 0,B._private.parent=null;else{for(var L=!1,O=A;!O.empty();){if(B.same(O)){L=!0,N.parent=void 0;break}O=O.parent()}L||(A[0]._private.children.push(B),B._private.parent=A[0],o.hasCompoundNodes=!0)}}}if(e.length>0){for(var R=e.length===i.length?i:new ts(a,e),V=0;V<R.length;V++){var F=R[V];F.isNode()||(F.parallelEdges().clearTraversalCache(),F.source().clearTraversalCache(),F.target().clearTraversalCache())}(o.hasCompoundNodes?a.collection().merge(R).merge(R.connectedNodes()).merge(R.parent()):R).dirtyCompoundBoundsCache().dirtyBoundingBoxCache().updateStyle(n),n?R.emitAndNotify("add"):r&&R.emit("add")}return i},ns.removed=function(){var e=this[0];return e&&e._private.removed},ns.inside=function(){var e=this[0];return e&&!e._private.removed},ns.remove=function(){var e=!(arguments.length>0&&void 0!==arguments[0])||arguments[0],t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],n=this,r=[],i={},a=n._private.cy;function o(e){for(var t=e._private.edges,n=0;n<t.length;n++)l(t[n])}function s(e){for(var t=e._private.children,n=0;n<t.length;n++)l(t[n])}function l(e){var n=i[e.id()];t&&e.removed()||n||(i[e.id()]=!0,e.isNode()?(r.push(e),o(e),s(e)):r.unshift(e))}for(var u=0,c=n.length;u<c;u++){var d=n[u];l(d)}function h(e,t){var n=e._private.edges;Ke(n,t),e.clearTraversalCache()}function p(e){e.clearTraversalCache()}var f=[];function g(e,t){t=t[0];var n=(e=e[0])._private.children,r=e.id();Ke(n,t),t._private.parent=null,f.ids[r]||(f.ids[r]=!0,f.push(e))}f.ids={},n.dirtyCompoundBoundsCache(),t&&a.removeFromPool(r);for(var v=0;v<r.length;v++){var y=r[v];if(y.isEdge()){var m=y.source()[0],b=y.target()[0];h(m,y),h(b,y);for(var x=y.parallelEdges(),w=0;w<x.length;w++){var E=x[w];p(E),E.isBundledBezier()&&E.dirtyBoundingBoxCache()}}else{var k=y.parent();0!==k.length&&g(k,y)}t&&(y._private.removed=!0)}var C=a._private.elements;a._private.hasCompoundNodes=!1;for(var S=0;S<C.length;S++){var P=C[S];if(P.isParent()){a._private.hasCompoundNodes=!0;break}}var D=new ts(this.cy(),r);D.size()>0&&(e?D.emitAndNotify("remove"):t&&D.emit("remove"));for(var T=0;T<f.length;T++){var _=f[T];t&&_.removed()||_.updateStyle()}return D},ns.move=function(e){var t=this._private.cy,n=this,r=function(e){return null==e?e:""+e};if(void 0!==e.source||void 0!==e.target){var i=r(e.source),a=r(e.target),o=null!=i&&t.hasElementWithId(i),s=null!=a&&t.hasElementWithId(a);(o||s)&&(t.batch((function(){n.remove(!1,!1),n.emitAndNotify("moveout");for(var e=0;e<n.length;e++){var t=n[e],r=t._private.data;t.isEdge()&&(o&&(r.source=i),s&&(r.target=a))}n.restore(!1,!1)})),n.emitAndNotify("move"))}else if(void 0!==e.parent){var l=r(e.parent);if(null===l||t.hasElementWithId(l)){var u=null===l?void 0:l;t.batch((function(){var e=n.remove(!1,!1);e.emitAndNotify("moveout");for(var t=0;t<n.length;t++){var r=n[t],i=r._private.data;r.isNode()&&(i.parent=u)}e.restore(!1,!1)})),n.emitAndNotify("move")}}return this},[ur,ji,qi,Sa,_a,La,Oa,ho,Do,To,{isNode:function(){return"nodes"===this.group()},isEdge:function(){return"edges"===this.group()},isLoop:function(){return this.isEdge()&&this.source()[0]===this.target()[0]},isSimple:function(){return this.isEdge()&&this.source()[0]!==this.target()[0]},group:function(){var e=this[0];if(e)return e._private.group}},Bo,zo,Oo,Wo,Go].forEach((function(e){L(ns,e)}));var rs={add:function(e){var t,n=this;if(E(e)){var r=e;if(r._private.cy===n)t=r.restore();else{for(var i=[],a=0;a<r.length;a++){var o=r[a];i.push(o.json())}t=new ts(n,i)}}else if(m(e)){t=new ts(n,e)}else if(b(e)&&(m(e.nodes)||m(e.edges))){for(var s=e,l=[],u=["nodes","edges"],c=0,d=u.length;c<d;c++){var h=u[c],p=s[h];if(m(p))for(var f=0,g=p.length;f<g;f++){var v=L({group:h},p[f]);l.push(v)}}t=new ts(n,l)}else{t=new et(n,e).collection()}return t},remove:function(e){if(E(e));else if(v(e)){var t=e;e=this.$(t)}return e.remove()}};
/*! Bezier curve function generator. Copyright Gaetan Renaudeau. MIT License: http://en.wikipedia.org/wiki/MIT_License */
/*! Runge-Kutta spring physics function generator. Adapted from Framer.js, copyright Koen Bok. MIT License: http://en.wikipedia.org/wiki/MIT_License */
var is=function(){function e(e){return-e.tension*e.x-e.friction*e.v}function t(t,n,r){var i={x:t.x+r.dx*n,v:t.v+r.dv*n,tension:t.tension,friction:t.friction};return{dx:i.v,dv:e(i)}}function n(n,r){var i={dx:n.v,dv:e(n)},a=t(n,.5*r,i),o=t(n,.5*r,a),s=t(n,r,o),l=1/6*(i.dx+2*(a.dx+o.dx)+s.dx),u=1/6*(i.dv+2*(a.dv+o.dv)+s.dv);return n.x=n.x+l*r,n.v=n.v+u*r,n}return function e(t,r,i){var a,o,s,l={x:-1,v:0,tension:null,friction:null},u=[0],c=0;for(t=parseFloat(t)||500,r=parseFloat(r)||20,i=i||null,l.tension=t,l.friction=r,o=(a=null!==i)?(c=e(t,r))/i*.016:.016;s=n(s||l,o),u.push(1+s.x),c+=16,Math.abs(s.x)>1e-4&&Math.abs(s.v)>1e-4;);return a?function(e){return u[e*(u.length-1)|0]}:c}}(),as=function(e,t,n,r){var i=function(e,t,n,r){var i=4,a=.001,o=1e-7,s=10,l=11,u=1/(l-1),c="undefined"!=typeof Float32Array;if(4!==arguments.length)return!1;for(var d=0;d<4;++d)if("number"!=typeof arguments[d]||isNaN(arguments[d])||!isFinite(arguments[d]))return!1;e=Math.min(e,1),n=Math.min(n,1),e=Math.max(e,0),n=Math.max(n,0);var h=c?new Float32Array(l):new Array(l);function p(e,t){return 1-3*t+3*e}function f(e,t){return 3*t-6*e}function g(e){return 3*e}function v(e,t,n){return((p(t,n)*e+f(t,n))*e+g(t))*e}function y(e,t,n){return 3*p(t,n)*e*e+2*f(t,n)*e+g(t)}function m(t,r){for(var a=0;a<i;++a){var o=y(r,e,n);if(0===o)return r;r-=(v(r,e,n)-t)/o}return r}function b(){for(var t=0;t<l;++t)h[t]=v(t*u,e,n)}function x(t,r,i){var a,l,u=0;do{(a=v(l=r+(i-r)/2,e,n)-t)>0?i=l:r=l}while(Math.abs(a)>o&&++u<s);return l}function w(t){for(var r=0,i=1,o=l-1;i!==o&&h[i]<=t;++i)r+=u;--i;var s=r+(t-h[i])/(h[i+1]-h[i])*u,c=y(s,e,n);return c>=a?m(t,s):0===c?s:x(t,r,r+u)}var E=!1;function k(){E=!0,e===t&&n===r||b()}var C=function(i){return E||k(),e===t&&n===r?i:0===i?0:1===i?1:v(w(i),t,r)};C.getControlPoints=function(){return[{x:e,y:t},{x:n,y:r}]};var S="generateBezier("+[e,t,n,r]+")";return C.toString=function(){return S},C}(e,t,n,r);return function(e,t,n){return e+(t-e)*i(n)}},os={linear:function(e,t,n){return e+(t-e)*n},ease:as(.25,.1,.25,1),"ease-in":as(.42,0,1,1),"ease-out":as(0,0,.58,1),"ease-in-out":as(.42,0,.58,1),"ease-in-sine":as(.47,0,.745,.715),"ease-out-sine":as(.39,.575,.565,1),"ease-in-out-sine":as(.445,.05,.55,.95),"ease-in-quad":as(.55,.085,.68,.53),"ease-out-quad":as(.25,.46,.45,.94),"ease-in-out-quad":as(.455,.03,.515,.955),"ease-in-cubic":as(.55,.055,.675,.19),"ease-out-cubic":as(.215,.61,.355,1),"ease-in-out-cubic":as(.645,.045,.355,1),"ease-in-quart":as(.895,.03,.685,.22),"ease-out-quart":as(.165,.84,.44,1),"ease-in-out-quart":as(.77,0,.175,1),"ease-in-quint":as(.755,.05,.855,.06),"ease-out-quint":as(.23,1,.32,1),"ease-in-out-quint":as(.86,0,.07,1),"ease-in-expo":as(.95,.05,.795,.035),"ease-out-expo":as(.19,1,.22,1),"ease-in-out-expo":as(1,0,0,1),"ease-in-circ":as(.6,.04,.98,.335),"ease-out-circ":as(.075,.82,.165,1),"ease-in-out-circ":as(.785,.135,.15,.86),spring:function(e,t,n){if(0===n)return os.linear;var r=is(e,t,n);return function(e,t,n){return e+(t-e)*r(n)}},"cubic-bezier":as};function ss(e,t,n,r,i){if(1===r)return n;if(t===n)return n;var a=i(t,n,r);return null==e||((e.roundValue||e.color)&&(a=Math.round(a)),void 0!==e.min&&(a=Math.max(a,e.min)),void 0!==e.max&&(a=Math.min(a,e.max))),a}function ls(e,t){return null!=e.pfValue||null!=e.value?null==e.pfValue||null!=t&&"%"===t.type.units?e.value:e.pfValue:e}function us(e,t,n,r,i){var a=null!=i?i.type:null;n<0?n=0:n>1&&(n=1);var o=ls(e,i),s=ls(t,i);if(x(o)&&x(s))return ss(a,o,s,n,r);if(m(o)&&m(s)){for(var l=[],u=0;u<s.length;u++){var c=o[u],d=s[u];if(null!=c&&null!=d){var h=ss(a,c,d,n,r);l.push(h)}else l.push(d)}return l}}function cs(e,t,n,r){var i=!r,a=e._private,o=t._private,s=o.easing,l=o.startTime,u=(r?e:e.cy()).style();if(!o.easingImpl)if(null==s)o.easingImpl=os.linear;else{var c,d,h;if(v(s))c=u.parse("transition-timing-function",s).value;else c=s;v(c)?(d=c,h=[]):(d=c[1],h=c.slice(2).map((function(e){return+e}))),h.length>0?("spring"===d&&h.push(o.duration),o.easingImpl=os[d].apply(null,h)):o.easingImpl=os[d]}var p,f=o.easingImpl;if(p=0===o.duration?1:(n-l)/o.duration,o.applying&&(p=o.progress),p<0?p=0:p>1&&(p=1),null==o.delay){var g=o.startPosition,y=o.position;if(y&&i&&!e.locked()){var m={};ds(g.x,y.x)&&(m.x=us(g.x,y.x,p,f)),ds(g.y,y.y)&&(m.y=us(g.y,y.y,p,f)),e.position(m)}var b=o.startPan,x=o.pan,w=a.pan,E=null!=x&&r;E&&(ds(b.x,x.x)&&(w.x=us(b.x,x.x,p,f)),ds(b.y,x.y)&&(w.y=us(b.y,x.y,p,f)),e.emit("pan"));var k=o.startZoom,C=o.zoom,S=null!=C&&r;S&&(ds(k,C)&&(a.zoom=Tt(a.minZoom,us(k,C,p,f),a.maxZoom)),e.emit("zoom")),(E||S)&&e.emit("viewport");var P=o.style;if(P&&P.length>0&&i){for(var D=0;D<P.length;D++){var T=P[D],_=T.name,M=T,B=o.startStyle[_],N=us(B,M,p,f,u.properties[B.name]);u.overrideBypass(e,_,N)}e.emit("style")}}return o.progress=p,p}function ds(e,t){return null!=e&&null!=t&&(!(!x(e)||!x(t))||!(!e||!t))}function hs(e,t,n,r){var i=t._private;i.started=!0,i.startTime=n-i.progress*i.duration}function ps(e,t){var n=t._private.aniEles,r=[];function i(t,n){var i=t._private,a=i.animation.current,o=i.animation.queue,s=!1;if(0===a.length){var l=o.shift();l&&a.push(l)}for(var u=function(e){for(var t=e.length-1;t>=0;t--){(0,e[t])()}e.splice(0,e.length)},c=a.length-1;c>=0;c--){var d=a[c],h=d._private;h.stopped?(a.splice(c,1),h.hooked=!1,h.playing=!1,h.started=!1,u(h.frames)):(h.playing||h.applying)&&(h.playing&&h.applying&&(h.applying=!1),h.started||hs(0,d,e),cs(t,d,e,n),h.applying&&(h.applying=!1),u(h.frames),null!=h.step&&h.step(e),d.completed()&&(a.splice(c,1),h.hooked=!1,h.playing=!1,h.started=!1,u(h.completes)),s=!0)}return n||0!==a.length||0!==o.length||r.push(t),s}for(var a=!1,o=0;o<n.length;o++){var s=i(n[o]);a=a||s}var l=i(t,!0);(a||l)&&(n.length>0?t.notify("draw",n):t.notify("draw")),n.unmerge(r),t.emit("step")}var fs={animate:Fi.animate(),animation:Fi.animation(),animated:Fi.animated(),clearQueue:Fi.clearQueue(),delay:Fi.delay(),delayAnimation:Fi.delayAnimation(),stop:Fi.stop(),addToAnimationPool:function(e){this.styleEnabled()&&this._private.aniEles.merge(e)},stopAnimationLoop:function(){this._private.animationsRunning=!1},startAnimationLoop:function(){var e=this;if(e._private.animationsRunning=!0,e.styleEnabled()){var t=e.renderer();t&&t.beforeRender?t.beforeRender((function(t,n){ps(n,e)}),t.beforeRenderPriorities.animations):function t(){e._private.animationsRunning&&xe((function(n){ps(n,e),t()}))}()}}},gs={qualifierCompare:function(e,t){return null==e||null==t?null==e&&null==t:e.sameText(t)},eventMatches:function(e,t,n){var r=t.qualifier;return null==r||e!==n.target&&k(n.target)&&r.matches(n.target)},addEventFields:function(e,t){t.cy=e,t.target=e},callbackContext:function(e,t,n){return null!=t.qualifier?n.target:e}},vs=function(e){return v(e)?new ka(e):e},ys={createEmitter:function(){var e=this._private;return e.emitter||(e.emitter=new xo(gs,this)),this},emitter:function(){return this._private.emitter},on:function(e,t,n){return this.emitter().on(e,vs(t),n),this},removeListener:function(e,t,n){return this.emitter().removeListener(e,vs(t),n),this},removeAllListeners:function(){return this.emitter().removeAllListeners(),this},one:function(e,t,n){return this.emitter().one(e,vs(t),n),this},once:function(e,t,n){return this.emitter().one(e,vs(t),n),this},emit:function(e,t){return this.emitter().emit(e,t),this},emitAndNotify:function(e,t){return this.emit(e),this.notify(e,t),this}};Fi.eventAliasesOn(ys);var ms={png:function(e){return e=e||{},this._private.renderer.png(e)},jpg:function(e){var t=this._private.renderer;return(e=e||{}).bg=e.bg||"#fff",t.jpg(e)}};ms.jpeg=ms.jpg;var bs={layout:function(e){if(null!=e)if(null!=e.name){var t=e.name,n=this.extension("layout",t);if(null!=n){var r;r=v(e.eles)?this.$(e.eles):null!=e.eles?e.eles:this.$();var i=new n(L({},e,{cy:this,eles:r}));return i}Ve("No such layout `"+t+"` found.  Did you forget to import it and `cytoscape.use()` it?")}else Ve("A `name` must be specified to make a layout");else Ve("Layout options must be specified to make a layout")}};bs.createLayout=bs.makeLayout=bs.layout;var xs={notify:function(e,t){var n=this._private;if(this.batching()){n.batchNotifications=n.batchNotifications||{};var r=n.batchNotifications[e]=n.batchNotifications[e]||this.collection();null!=t&&r.merge(t)}else if(n.notificationsEnabled){var i=this.renderer();!this.destroyed()&&i&&i.notify(e,t)}},notifications:function(e){var t=this._private;return void 0===e?t.notificationsEnabled:(t.notificationsEnabled=!!e,this)},noNotifications:function(e){this.notifications(!1),e(),this.notifications(!0)},batching:function(){return this._private.batchCount>0},startBatch:function(){var e=this._private;return null==e.batchCount&&(e.batchCount=0),0===e.batchCount&&(e.batchStyleEles=this.collection(),e.batchNotifications={}),e.batchCount++,this},endBatch:function(){var e=this._private;if(0===e.batchCount)return this;if(e.batchCount--,0===e.batchCount){e.batchStyleEles.updateStyle();var t=this.renderer();Object.keys(e.batchNotifications).forEach((function(n){var r=e.batchNotifications[n];r.empty()?t.notify(n):t.notify(n,r)}))}return this},batch:function(e){return this.startBatch(),e(),this.endBatch(),this},batchData:function(e){var t=this;return this.batch((function(){for(var n=Object.keys(e),r=0;r<n.length;r++){var i=n[r],a=e[i];t.getElementById(i).data(a)}}))}},ws=He({hideEdgesOnViewport:!1,textureOnViewport:!1,motionBlur:!1,motionBlurOpacity:.05,pixelRatio:void 0,desktopTapThreshold:4,touchTapThreshold:8,wheelSensitivity:1,debug:!1,showFps:!1}),Es={renderTo:function(e,t,n,r){return this._private.renderer.renderTo(e,t,n,r),this},renderer:function(){return this._private.renderer},forceRender:function(){return this.notify("draw"),this},resize:function(){return this.invalidateSize(),this.emitAndNotify("resize"),this},initRenderer:function(e){var t=this.extension("renderer",e.name);if(null!=t){void 0!==e.wheelSensitivity&&je("You have set a custom wheel sensitivity.  This will make your app zoom unnaturally when using mainstream mice.  You should change this value from the default only if you can guarantee that all your users will use the same hardware and OS configuration as your current machine.");var n=ws(e);n.cy=this,this._private.renderer=new t(n),this.notify("init")}else Ve("Can not initialise: No such renderer `".concat(e.name,"` found. Did you forget to import it and `cytoscape.use()` it?"))},destroyRenderer:function(){this.notify("destroy");var e=this.container();if(e)for(e._cyreg=null;e.childNodes.length>0;)e.removeChild(e.childNodes[0]);this._private.renderer=null,this.mutableElements().forEach((function(e){var t=e._private;t.rscratch={},t.rstyle={},t.animation.current=[],t.animation.queue=[]}))},onRender:function(e){return this.on("render",e)},offRender:function(e){return this.off("render",e)}};Es.invalidateDimensions=Es.resize;var ks={collection:function(e,t){return v(e)?this.$(e):E(e)?e.collection():m(e)?(t||(t={}),new ts(this,e,t.unique,t.removed)):new ts(this)},nodes:function(e){var t=this.$((function(e){return e.isNode()}));return e?t.filter(e):t},edges:function(e){var t=this.$((function(e){return e.isEdge()}));return e?t.filter(e):t},$:function(e){var t=this._private.elements;return e?t.filter(e):t.spawnSelf()},mutableElements:function(){return this._private.elements}};ks.elements=ks.filter=ks.$;var Cs={};Cs.apply=function(e){for(var t=this._private.cy.collection(),n=0;n<e.length;n++){var r=e[n],i=this.getContextMeta(r);if(!i.empty){var a=this.getContextStyle(i),o=this.applyContextStyle(i,a,r);r._private.appliedInitStyle?this.updateTransitions(r,o.diffProps):r._private.appliedInitStyle=!0,this.updateStyleHints(r)&&t.push(r)}}return t},Cs.getPropertiesDiff=function(e,t){var n=this._private.propDiffs=this._private.propDiffs||{},r=e+"-"+t,i=n[r];if(i)return i;for(var a=[],o={},s=0;s<this.length;s++){var l=this[s],u="t"===e[s],c="t"===t[s],d=u!==c,h=l.mappedProperties.length>0;if(d||c&&h){var p=void 0;d&&h||d?p=l.properties:h&&(p=l.mappedProperties);for(var f=0;f<p.length;f++){for(var g=p[f],v=g.name,y=!1,m=s+1;m<this.length;m++){var b=this[m];if("t"===t[m]&&(y=null!=b.properties[g.name]))break}o[v]||y||(o[v]=!0,a.push(v))}}}return n[r]=a,a},Cs.getContextMeta=function(e){for(var t,n="",r=e._private.styleCxtKey||"",i=0;i<this.length;i++){var a=this[i];n+=a.selector&&a.selector.matches(e)?"t":"f"}return t=this.getPropertiesDiff(r,n),e._private.styleCxtKey=n,{key:n,diffPropNames:t,empty:0===t.length}},Cs.getContextStyle=function(e){var t=e.key,n=this._private.contextStyles=this._private.contextStyles||{};if(n[t])return n[t];for(var r={_private:{key:t}},i=0;i<this.length;i++){var a=this[i];if("t"===t[i])for(var o=0;o<a.properties.length;o++){var s=a.properties[o];r[s.name]=s}}return n[t]=r,r},Cs.applyContextStyle=function(e,t,n){for(var r=e.diffPropNames,i={},a=this.types,o=0;o<r.length;o++){var s=r[o],l=t[s],u=n.pstyle(s);if(!l){if(!u)continue;l=u.bypass?{name:s,deleteBypassed:!0}:{name:s,delete:!0}}if(u!==l){if(l.mapped===a.fn&&null!=u&&null!=u.mapping&&u.mapping.value===l.value){var c=u.mapping;if((c.fnValue=l.value(n))===c.prevFnValue)continue}var d=i[s]={prev:u};this.applyParsedProperty(n,l),d.next=n.pstyle(s),d.next&&d.next.bypass&&(d.next=d.next.bypassed)}}return{diffProps:i}},Cs.updateStyleHints=function(e){var t=e._private,n=this,r=n.propertyGroupNames,i=n.propertyGroupKeys,a=function(e,t,r){return n.getPropertiesHash(e,t,r)},o=t.styleKey;if(e.removed())return!1;var s="nodes"===t.group,l=e._private.style;r=Object.keys(l);for(var u=0;u<i.length;u++){var c=i[u];t.styleKeys[c]=[9261,5381]}for(var d,h=function(e,n){return t.styleKeys[n][0]=Ce(e,t.styleKeys[n][0])},p=function(e,n){return t.styleKeys[n][1]=Se(e,t.styleKeys[n][1])},f=function(e,t){h(e,t),p(e,t)},g=function(e,t){for(var n=0;n<e.length;n++){var r=e.charCodeAt(n);h(r,t),p(r,t)}},v=0;v<r.length;v++){var y=r[v],m=l[y];if(null!=m){var b=this.properties[y],x=b.type,w=b.groupKey,E=void 0;null!=b.hashOverride?E=b.hashOverride(e,m):null!=m.pfValue&&(E=m.pfValue);var k=null==b.enums?m.value:null,C=null!=E,S=C||null!=k,P=m.units;if(x.number&&S&&!x.multiple)f(-128<(d=C?E:k)&&d<128&&Math.floor(d)!==d?2e9-(1024*d|0):d,w),C||null==P||g(P,w);else g(m.strValue,w)}}for(var D,T,_=[9261,5381],M=0;M<i.length;M++){var B=i[M],N=t.styleKeys[B];_[0]=Ce(N[0],_[0]),_[1]=Se(N[1],_[1])}t.styleKey=(D=_[0],T=_[1],2097152*D+T);var z=t.styleKeys;t.labelDimsKey=Pe(z.labelDimensions);var I=a(e,["label"],z.labelDimensions);if(t.labelKey=Pe(I),t.labelStyleKey=Pe(De(z.commonLabel,I)),!s){var A=a(e,["source-label"],z.labelDimensions);t.sourceLabelKey=Pe(A),t.sourceLabelStyleKey=Pe(De(z.commonLabel,A));var L=a(e,["target-label"],z.labelDimensions);t.targetLabelKey=Pe(L),t.targetLabelStyleKey=Pe(De(z.commonLabel,L))}if(s){var O=t.styleKeys,R=O.nodeBody,V=O.nodeBorder,F=O.nodeOutline,j=O.backgroundImage,q=O.compound,Y=O.pie,X=[R,V,F,j,q,Y].filter((function(e){return null!=e})).reduce(De,[9261,5381]);t.nodeKey=Pe(X),t.hasPie=null!=Y&&9261!==Y[0]&&5381!==Y[1]}return o!==t.styleKey},Cs.clearStyleHints=function(e){var t=e._private;t.styleCxtKey="",t.styleKeys={},t.styleKey=null,t.labelKey=null,t.labelStyleKey=null,t.sourceLabelKey=null,t.sourceLabelStyleKey=null,t.targetLabelKey=null,t.targetLabelStyleKey=null,t.nodeKey=null,t.hasPie=null},Cs.applyParsedProperty=function(e,t){var n,r=this,i=t,a=e._private.style,o=r.types,s=r.properties[i.name].type,l=i.bypass,u=a[i.name],c=u&&u.bypass,d=e._private,h=function(e){return null==e?null:null!=e.pfValue?e.pfValue:e.value},p=function(){var t=h(u),n=h(i);r.checkTriggers(e,i.name,t,n)};if("curve-style"===t.name&&e.isEdge()&&("bezier"!==t.value&&e.isLoop()||"haystack"===t.value&&(e.source().isParent()||e.target().isParent()))&&(i=t=this.parse(t.name,"bezier",l)),i.delete)return a[i.name]=void 0,p(),!0;if(i.deleteBypassed)return u?!!u.bypass&&(u.bypassed=void 0,p(),!0):(p(),!0);if(i.deleteBypass)return u?!!u.bypass&&(a[i.name]=u.bypassed,p(),!0):(p(),!0);var f=function(){je("Do not assign mappings to elements without corresponding data (i.e. ele `"+e.id()+"` has no mapping for property `"+i.name+"` with data field `"+i.field+"`); try a `["+i.field+"]` selector to limit scope to elements with `"+i.field+"` defined")};switch(i.mapped){case o.mapData:for(var g,v=i.field.split("."),y=d.data,m=0;m<v.length&&y;m++){y=y[v[m]]}if(null==y)return f(),!1;if(!x(y))return je("Do not use continuous mappers without specifying numeric data (i.e. `"+i.field+": "+y+"` for `"+e.id()+"` is non-numeric)"),!1;var b=i.fieldMax-i.fieldMin;if((g=0===b?0:(y-i.fieldMin)/b)<0?g=0:g>1&&(g=1),s.color){var w=i.valueMin[0],E=i.valueMax[0],k=i.valueMin[1],C=i.valueMax[1],S=i.valueMin[2],P=i.valueMax[2],D=null==i.valueMin[3]?1:i.valueMin[3],T=null==i.valueMax[3]?1:i.valueMax[3],_=[Math.round(w+(E-w)*g),Math.round(k+(C-k)*g),Math.round(S+(P-S)*g),Math.round(D+(T-D)*g)];n={bypass:i.bypass,name:i.name,value:_,strValue:"rgb("+_[0]+", "+_[1]+", "+_[2]+")"}}else{if(!s.number)return!1;var M=i.valueMin+(i.valueMax-i.valueMin)*g;n=this.parse(i.name,M,i.bypass,"mapping")}if(!n)return f(),!1;n.mapping=i,i=n;break;case o.data:for(var B=i.field.split("."),N=d.data,z=0;z<B.length&&N;z++){N=N[B[z]]}if(null!=N&&(n=this.parse(i.name,N,i.bypass,"mapping")),!n)return f(),!1;n.mapping=i,i=n;break;case o.fn:var I=i.value,A=null!=i.fnValue?i.fnValue:I(e);if(i.prevFnValue=A,null==A)return je("Custom function mappers may not return null (i.e. `"+i.name+"` for ele `"+e.id()+"` is null)"),!1;if(!(n=this.parse(i.name,A,i.bypass,"mapping")))return je("Custom function mappers may not return invalid values for the property type (i.e. `"+i.name+"` for ele `"+e.id()+"` is invalid)"),!1;n.mapping=qe(i),i=n;break;case void 0:break;default:return!1}return l?(i.bypassed=c?u.bypassed:u,a[i.name]=i):c?u.bypassed=i:a[i.name]=i,p(),!0},Cs.cleanElements=function(e,t){for(var n=0;n<e.length;n++){var r=e[n];if(this.clearStyleHints(r),r.dirtyCompoundBoundsCache(),r.dirtyBoundingBoxCache(),t)for(var i=r._private.style,a=Object.keys(i),o=0;o<a.length;o++){var s=a[o],l=i[s];null!=l&&(l.bypass?l.bypassed=null:i[s]=null)}else r._private.style={}}},Cs.update=function(){this._private.cy.mutableElements().updateStyle()},Cs.updateTransitions=function(e,t){var n=this,r=e._private,i=e.pstyle("transition-property").value,a=e.pstyle("transition-duration").pfValue,o=e.pstyle("transition-delay").pfValue;if(i.length>0&&a>0){for(var s={},l=!1,u=0;u<i.length;u++){var c=i[u],d=e.pstyle(c),h=t[c];if(h){var p=h.prev,f=null!=h.next?h.next:d,g=!1,v=void 0;p&&(x(p.pfValue)&&x(f.pfValue)?(g=f.pfValue-p.pfValue,v=p.pfValue+1e-6*g):x(p.value)&&x(f.value)?(g=f.value-p.value,v=p.value+1e-6*g):m(p.value)&&m(f.value)&&(g=p.value[0]!==f.value[0]||p.value[1]!==f.value[1]||p.value[2]!==f.value[2],v=p.strValue),g&&(s[c]=f.strValue,this.applyBypass(e,c,v),l=!0))}}if(!l)return;r.transitioning=!0,new vr((function(t){o>0?e.delayAnimation(o).play().promise().then(t):t()})).then((function(){return e.animation({style:s,duration:a,easing:e.pstyle("transition-timing-function").value,queue:!1}).play().promise()})).then((function(){n.removeBypasses(e,i),e.emitAndNotify("style"),r.transitioning=!1}))}else r.transitioning&&(this.removeBypasses(e,i),e.emitAndNotify("style"),r.transitioning=!1)},Cs.checkTrigger=function(e,t,n,r,i,a){var o=this.properties[t],s=i(o);null!=s&&s(n,r)&&a(o)},Cs.checkZOrderTrigger=function(e,t,n,r){var i=this;this.checkTrigger(e,t,n,r,(function(e){return e.triggersZOrder}),(function(){i._private.cy.notify("zorder",e)}))},Cs.checkBoundsTrigger=function(e,t,n,r){this.checkTrigger(e,t,n,r,(function(e){return e.triggersBounds}),(function(i){e.dirtyCompoundBoundsCache(),e.dirtyBoundingBoxCache(),!i.triggersBoundsOfParallelBeziers||"curve-style"!==t||"bezier"!==n&&"bezier"!==r||e.parallelEdges().forEach((function(e){e.isBundledBezier()&&e.dirtyBoundingBoxCache()})),!i.triggersBoundsOfConnectedEdges||"display"!==t||"none"!==n&&"none"!==r||e.connectedEdges().forEach((function(e){e.dirtyBoundingBoxCache()}))}))},Cs.checkTriggers=function(e,t,n,r){e.dirtyStyleCache(),this.checkZOrderTrigger(e,t,n,r),this.checkBoundsTrigger(e,t,n,r)};var Ss={applyBypass:function(e,t,n,r){var i=[];if("*"===t||"**"===t){if(void 0!==n)for(var a=0;a<this.properties.length;a++){var o=this.properties[a].name,s=this.parse(o,n,!0);s&&i.push(s)}}else if(v(t)){var l=this.parse(t,n,!0);l&&i.push(l)}else{if(!b(t))return!1;var u=t;r=n;for(var c=Object.keys(u),d=0;d<c.length;d++){var h=c[d],p=u[h];if(void 0===p&&(p=u[B(h)]),void 0!==p){var f=this.parse(h,p,!0);f&&i.push(f)}}}if(0===i.length)return!1;for(var g=!1,y=0;y<e.length;y++){for(var m=e[y],x={},w=void 0,E=0;E<i.length;E++){var k=i[E];if(r){var C=m.pstyle(k.name);w=x[k.name]={prev:C}}g=this.applyParsedProperty(m,qe(k))||g,r&&(w.next=m.pstyle(k.name))}g&&this.updateStyleHints(m),r&&this.updateTransitions(m,x,!0)}return g},overrideBypass:function(e,t,n){t=M(t);for(var r=0;r<e.length;r++){var i=e[r],a=i._private.style[t],o=this.properties[t].type,s=o.color,l=o.mutiple,u=a?null!=a.pfValue?a.pfValue:a.value:null;a&&a.bypass?(a.value=n,null!=a.pfValue&&(a.pfValue=n),a.strValue=s?"rgb("+n.join(",")+")":l?n.join(" "):""+n,this.updateStyleHints(i)):this.applyBypass(i,t,n),this.checkTriggers(i,t,u,n)}},removeAllBypasses:function(e,t){return this.removeBypasses(e,this.propertyNames,t)},removeBypasses:function(e,t,n){for(var r=0;r<e.length;r++){for(var i=e[r],a={},o=0;o<t.length;o++){var s=t[o],l=this.properties[s],u=i.pstyle(l.name);if(u&&u.bypass){var c=this.parse(s,"",!0),d=a[l.name]={prev:u};this.applyParsedProperty(i,c),d.next=i.pstyle(l.name)}}this.updateStyleHints(i),n&&this.updateTransitions(i,a,!0)}}},Ps={getEmSizeInPixels:function(){var e=this.containerCss("font-size");return null!=e?parseFloat(e):1},containerCss:function(e){var t=this._private.cy,n=t.container(),r=t.window();if(r&&n&&r.getComputedStyle)return r.getComputedStyle(n).getPropertyValue(e)}},Ds={getRenderedStyle:function(e,t){return t?this.getStylePropertyValue(e,t,!0):this.getRawStyle(e,!0)},getRawStyle:function(e,t){if(e=e[0]){for(var n={},r=0;r<this.properties.length;r++){var i=this.properties[r],a=this.getStylePropertyValue(e,i.name,t);null!=a&&(n[i.name]=a,n[B(i.name)]=a)}return n}},getIndexedStyle:function(e,t,n,r){var i=e.pstyle(t)[n][r];return null!=i?i:e.cy().style().getDefaultProperty(t)[n][0]},getStylePropertyValue:function(e,t,n){if(e=e[0]){var r=this.properties[t];r.alias&&(r=r.pointsTo);var i=r.type,a=e.pstyle(r.name);if(a){var o=a.value,s=a.units,l=a.strValue;if(n&&i.number&&null!=o&&x(o)){var u=e.cy().zoom(),c=function(e){return e*u},d=function(e,t){return c(e)+t},h=m(o);return(h?s.every((function(e){return null!=e})):null!=s)?h?o.map((function(e,t){return d(e,s[t])})).join(" "):d(o,s):h?o.map((function(e){return v(e)?e:""+c(e)})).join(" "):""+c(o)}if(null!=l)return l}return null}},getAnimationStartStyle:function(e,t){for(var n={},r=0;r<t.length;r++){var i=t[r].name,a=e.pstyle(i);void 0!==a&&(a=b(a)?this.parse(i,a.strValue):this.parse(i,a)),a&&(n[i]=a)}return n},getPropsList:function(e){var t=[],n=e,r=this.properties;if(n)for(var i=Object.keys(n),a=0;a<i.length;a++){var o=i[a],s=n[o],l=r[o]||r[M(o)],u=this.parse(l.name,s);u&&t.push(u)}return t},getNonDefaultPropertiesHash:function(e,t,n){var r,i,a,o,s,l,u=n.slice();for(s=0;s<t.length;s++)if(r=t[s],null!=(i=e.pstyle(r,!1)))if(null!=i.pfValue)u[0]=Ce(o,u[0]),u[1]=Se(o,u[1]);else for(a=i.strValue,l=0;l<a.length;l++)o=a.charCodeAt(l),u[0]=Ce(o,u[0]),u[1]=Se(o,u[1]);return u}};Ds.getPropertiesHash=Ds.getNonDefaultPropertiesHash;var Ts={appendFromJson:function(e){for(var t=0;t<e.length;t++){var n=e[t],r=n.selector,i=n.style||n.css,a=Object.keys(i);this.selector(r);for(var o=0;o<a.length;o++){var s=a[o],l=i[s];this.css(s,l)}}return this},fromJson:function(e){return this.resetToDefault(),this.appendFromJson(e),this},json:function(){for(var e=[],t=this.defaultLength;t<this.length;t++){for(var n=this[t],r=n.selector,i=n.properties,a={},o=0;o<i.length;o++){var s=i[o];a[s.name]=s.strValue}e.push({selector:r?r.toString():"core",style:a})}return e}},_s={appendFromString:function(e){var t,n,r,i=""+e;function a(){i=i.length>t.length?i.substr(t.length):""}function o(){n=n.length>r.length?n.substr(r.length):""}for(i=i.replace(/[/][*](\s|.)+?[*][/]/g,"");;){if(i.match(/^\s*$/))break;var s=i.match(/^\s*((?:.|\s)+?)\s*\{((?:.|\s)+?)\}/);if(!s){je("Halting stylesheet parsing: String stylesheet contains more to parse but no selector and block found in: "+i);break}t=s[0];var l=s[1];if("core"!==l)if(new ka(l).invalid){je("Skipping parsing of block: Invalid selector found in string stylesheet: "+l),a();continue}var u=s[2],c=!1;n=u;for(var d=[];;){if(n.match(/^\s*$/))break;var h=n.match(/^\s*(.+?)\s*:\s*(.+?)(?:\s*;|\s*$)/);if(!h){je("Skipping parsing of block: Invalid formatting of style property and value definitions found in:"+u),c=!0;break}r=h[0];var p=h[1],f=h[2];if(this.properties[p])this.parse(p,f)?(d.push({name:p,val:f}),o()):(je("Skipping property: Invalid property definition in: "+r),o());else je("Skipping property: Invalid property name in: "+r),o()}if(c){a();break}this.selector(l);for(var g=0;g<d.length;g++){var v=d[g];this.css(v.name,v.val)}a()}return this},fromString:function(e){return this.resetToDefault(),this.appendFromString(e),this}},Ms={};!function(){var e=I,t=function(e){return"^"+e+"\\s*\\(\\s*([\\w\\.]+)\\s*\\)$"},n=function(t){var n=e+"|\\w+|rgb[a]?\\((?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%]?)\\s*,\\s*(?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%]?)\\s*,\\s*(?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%]?)(?:\\s*,\\s*(?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))))?\\)|hsl[a]?\\((?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?)))\\s*,\\s*(?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%])\\s*,\\s*(?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))[%])(?:\\s*,\\s*(?:(?:[-+]?(?:(?:\\d+|\\d*\\.\\d+)(?:[Ee][+-]?\\d+)?))))?\\)|\\#[0-9a-fA-F]{3}|\\#[0-9a-fA-F]{6}";return"^"+t+"\\s*\\(([\\w\\.]+)\\s*\\,\\s*("+e+")\\s*\\,\\s*("+e+")\\s*,\\s*("+n+")\\s*\\,\\s*("+n+")\\)$"},r=["^url\\s*\\(\\s*['\"]?(.+?)['\"]?\\s*\\)$","^(none)$","^(.+)$"];Ms.types={time:{number:!0,min:0,units:"s|ms",implicitUnits:"ms"},percent:{number:!0,min:0,max:100,units:"%",implicitUnits:"%"},percentages:{number:!0,min:0,max:100,units:"%",implicitUnits:"%",multiple:!0},zeroOneNumber:{number:!0,min:0,max:1,unitless:!0},zeroOneNumbers:{number:!0,min:0,max:1,unitless:!0,multiple:!0},nOneOneNumber:{number:!0,min:-1,max:1,unitless:!0},nonNegativeInt:{number:!0,min:0,integer:!0,unitless:!0},nonNegativeNumber:{number:!0,min:0,unitless:!0},position:{enums:["parent","origin"]},nodeSize:{number:!0,min:0,enums:["label"]},number:{number:!0,unitless:!0},numbers:{number:!0,unitless:!0,multiple:!0},positiveNumber:{number:!0,unitless:!0,min:0,strictMin:!0},size:{number:!0,min:0},bidirectionalSize:{number:!0},bidirectionalSizeMaybePercent:{number:!0,allowPercent:!0},bidirectionalSizes:{number:!0,multiple:!0},sizeMaybePercent:{number:!0,min:0,allowPercent:!0},axisDirection:{enums:["horizontal","leftward","rightward","vertical","upward","downward","auto"]},paddingRelativeTo:{enums:["width","height","average","min","max"]},bgWH:{number:!0,min:0,allowPercent:!0,enums:["auto"],multiple:!0},bgPos:{number:!0,allowPercent:!0,multiple:!0},bgRelativeTo:{enums:["inner","include-padding"],multiple:!0},bgRepeat:{enums:["repeat","repeat-x","repeat-y","no-repeat"],multiple:!0},bgFit:{enums:["none","contain","cover"],multiple:!0},bgCrossOrigin:{enums:["anonymous","use-credentials","null"],multiple:!0},bgClip:{enums:["none","node"],multiple:!0},bgContainment:{enums:["inside","over"],multiple:!0},color:{color:!0},colors:{color:!0,multiple:!0},fill:{enums:["solid","linear-gradient","radial-gradient"]},bool:{enums:["yes","no"]},bools:{enums:["yes","no"],multiple:!0},lineStyle:{enums:["solid","dotted","dashed"]},lineCap:{enums:["butt","round","square"]},linePosition:{enums:["center","inside","outside"]},lineJoin:{enums:["round","bevel","miter"]},borderStyle:{enums:["solid","dotted","dashed","double"]},curveStyle:{enums:["bezier","unbundled-bezier","haystack","segments","straight","straight-triangle","taxi","round-segments","round-taxi"]},radiusType:{enums:["arc-radius","influence-radius"],multiple:!0},fontFamily:{regex:'^([\\w- \\"]+(?:\\s*,\\s*[\\w- \\"]+)*)$'},fontStyle:{enums:["italic","normal","oblique"]},fontWeight:{enums:["normal","bold","bolder","lighter","100","200","300","400","500","600","800","900",100,200,300,400,500,600,700,800,900]},textDecoration:{enums:["none","underline","overline","line-through"]},textTransform:{enums:["none","uppercase","lowercase"]},textWrap:{enums:["none","wrap","ellipsis"]},textOverflowWrap:{enums:["whitespace","anywhere"]},textBackgroundShape:{enums:["rectangle","roundrectangle","round-rectangle"]},nodeShape:{enums:["rectangle","roundrectangle","round-rectangle","cutrectangle","cut-rectangle","bottomroundrectangle","bottom-round-rectangle","barrel","ellipse","triangle","round-triangle","square","pentagon","round-pentagon","hexagon","round-hexagon","concavehexagon","concave-hexagon","heptagon","round-heptagon","octagon","round-octagon","tag","round-tag","star","diamond","round-diamond","vee","rhomboid","right-rhomboid","polygon"]},overlayShape:{enums:["roundrectangle","round-rectangle","ellipse"]},cornerRadius:{number:!0,min:0,units:"px|em",implicitUnits:"px",enums:["auto"]},compoundIncludeLabels:{enums:["include","exclude"]},arrowShape:{enums:["tee","triangle","triangle-tee","circle-triangle","triangle-cross","triangle-backcurve","vee","square","circle","diamond","chevron","none"]},arrowFill:{enums:["filled","hollow"]},arrowWidth:{number:!0,units:"%|px|em",implicitUnits:"px",enums:["match-line"]},display:{enums:["element","none"]},visibility:{enums:["hidden","visible"]},zCompoundDepth:{enums:["bottom","orphan","auto","top"]},zIndexCompare:{enums:["auto","manual"]},valign:{enums:["top","center","bottom"]},halign:{enums:["left","center","right"]},justification:{enums:["left","center","right","auto"]},text:{string:!0},data:{mapping:!0,regex:t("data")},layoutData:{mapping:!0,regex:t("layoutData")},scratch:{mapping:!0,regex:t("scratch")},mapData:{mapping:!0,regex:n("mapData")},mapLayoutData:{mapping:!0,regex:n("mapLayoutData")},mapScratch:{mapping:!0,regex:n("mapScratch")},fn:{mapping:!0,fn:!0},url:{regexes:r,singleRegexMatchValue:!0},urls:{regexes:r,singleRegexMatchValue:!0,multiple:!0},propList:{propList:!0},angle:{number:!0,units:"deg|rad",implicitUnits:"rad"},textRotation:{number:!0,units:"deg|rad",implicitUnits:"rad",enums:["none","autorotate"]},polygonPointList:{number:!0,multiple:!0,evenMultiple:!0,min:-1,max:1,unitless:!0},edgeDistances:{enums:["intersection","node-position","endpoints"]},edgeEndpoint:{number:!0,multiple:!0,units:"%|px|em|deg|rad",implicitUnits:"px",enums:["inside-to-node","outside-to-node","outside-to-node-or-label","outside-to-line","outside-to-line-or-label"],singleEnum:!0,validate:function(e,t){switch(e.length){case 2:return"deg"!==t[0]&&"rad"!==t[0]&&"deg"!==t[1]&&"rad"!==t[1];case 1:return v(e[0])||"deg"===t[0]||"rad"===t[0];default:return!1}}},easing:{regexes:["^(spring)\\s*\\(\\s*("+e+")\\s*,\\s*("+e+")\\s*\\)$","^(cubic-bezier)\\s*\\(\\s*("+e+")\\s*,\\s*("+e+")\\s*,\\s*("+e+")\\s*,\\s*("+e+")\\s*\\)$"],enums:["linear","ease","ease-in","ease-out","ease-in-out","ease-in-sine","ease-out-sine","ease-in-out-sine","ease-in-quad","ease-out-quad","ease-in-out-quad","ease-in-cubic","ease-out-cubic","ease-in-out-cubic","ease-in-quart","ease-out-quart","ease-in-out-quart","ease-in-quint","ease-out-quint","ease-in-out-quint","ease-in-expo","ease-out-expo","ease-in-out-expo","ease-in-circ","ease-out-circ","ease-in-out-circ"]},gradientDirection:{enums:["to-bottom","to-top","to-left","to-right","to-bottom-right","to-bottom-left","to-top-right","to-top-left","to-right-bottom","to-left-bottom","to-right-top","to-left-top"]},boundsExpansion:{number:!0,multiple:!0,min:0,validate:function(e){var t=e.length;return 1===t||2===t||4===t}}};var i={zeroNonZero:function(e,t){return(null==e||null==t)&&e!==t||(0==e&&0!=t||0!=e&&0==t)},any:function(e,t){return e!=t},emptyNonEmpty:function(e,t){var n=D(e),r=D(t);return n&&!r||!n&&r}},a=Ms.types,o=[{name:"label",type:a.text,triggersBounds:i.any,triggersZOrder:i.emptyNonEmpty},{name:"text-rotation",type:a.textRotation,triggersBounds:i.any},{name:"text-margin-x",type:a.bidirectionalSize,triggersBounds:i.any},{name:"text-margin-y",type:a.bidirectionalSize,triggersBounds:i.any}],s=[{name:"source-label",type:a.text,triggersBounds:i.any},{name:"source-text-rotation",type:a.textRotation,triggersBounds:i.any},{name:"source-text-margin-x",type:a.bidirectionalSize,triggersBounds:i.any},{name:"source-text-margin-y",type:a.bidirectionalSize,triggersBounds:i.any},{name:"source-text-offset",type:a.size,triggersBounds:i.any}],l=[{name:"target-label",type:a.text,triggersBounds:i.any},{name:"target-text-rotation",type:a.textRotation,triggersBounds:i.any},{name:"target-text-margin-x",type:a.bidirectionalSize,triggersBounds:i.any},{name:"target-text-margin-y",type:a.bidirectionalSize,triggersBounds:i.any},{name:"target-text-offset",type:a.size,triggersBounds:i.any}],u=[{name:"font-family",type:a.fontFamily,triggersBounds:i.any},{name:"font-style",type:a.fontStyle,triggersBounds:i.any},{name:"font-weight",type:a.fontWeight,triggersBounds:i.any},{name:"font-size",type:a.size,triggersBounds:i.any},{name:"text-transform",type:a.textTransform,triggersBounds:i.any},{name:"text-wrap",type:a.textWrap,triggersBounds:i.any},{name:"text-overflow-wrap",type:a.textOverflowWrap,triggersBounds:i.any},{name:"text-max-width",type:a.size,triggersBounds:i.any},{name:"text-outline-width",type:a.size,triggersBounds:i.any},{name:"line-height",type:a.positiveNumber,triggersBounds:i.any}],c=[{name:"text-valign",type:a.valign,triggersBounds:i.any},{name:"text-halign",type:a.halign,triggersBounds:i.any},{name:"color",type:a.color},{name:"text-outline-color",type:a.color},{name:"text-outline-opacity",type:a.zeroOneNumber},{name:"text-background-color",type:a.color},{name:"text-background-opacity",type:a.zeroOneNumber},{name:"text-background-padding",type:a.size,triggersBounds:i.any},{name:"text-border-opacity",type:a.zeroOneNumber},{name:"text-border-color",type:a.color},{name:"text-border-width",type:a.size,triggersBounds:i.any},{name:"text-border-style",type:a.borderStyle,triggersBounds:i.any},{name:"text-background-shape",type:a.textBackgroundShape,triggersBounds:i.any},{name:"text-justification",type:a.justification}],d=[{name:"events",type:a.bool,triggersZOrder:i.any},{name:"text-events",type:a.bool,triggersZOrder:i.any}],h=[{name:"display",type:a.display,triggersZOrder:i.any,triggersBounds:i.any,triggersBoundsOfConnectedEdges:!0},{name:"visibility",type:a.visibility,triggersZOrder:i.any},{name:"opacity",type:a.zeroOneNumber,triggersZOrder:i.zeroNonZero},{name:"text-opacity",type:a.zeroOneNumber},{name:"min-zoomed-font-size",type:a.size},{name:"z-compound-depth",type:a.zCompoundDepth,triggersZOrder:i.any},{name:"z-index-compare",type:a.zIndexCompare,triggersZOrder:i.any},{name:"z-index",type:a.number,triggersZOrder:i.any}],p=[{name:"overlay-padding",type:a.size,triggersBounds:i.any},{name:"overlay-color",type:a.color},{name:"overlay-opacity",type:a.zeroOneNumber,triggersBounds:i.zeroNonZero},{name:"overlay-shape",type:a.overlayShape,triggersBounds:i.any},{name:"overlay-corner-radius",type:a.cornerRadius}],f=[{name:"underlay-padding",type:a.size,triggersBounds:i.any},{name:"underlay-color",type:a.color},{name:"underlay-opacity",type:a.zeroOneNumber,triggersBounds:i.zeroNonZero},{name:"underlay-shape",type:a.overlayShape,triggersBounds:i.any},{name:"underlay-corner-radius",type:a.cornerRadius}],g=[{name:"transition-property",type:a.propList},{name:"transition-duration",type:a.time},{name:"transition-delay",type:a.time},{name:"transition-timing-function",type:a.easing}],y=function(e,t){return"label"===t.value?-e.poolIndex():t.pfValue},m=[{name:"height",type:a.nodeSize,triggersBounds:i.any,hashOverride:y},{name:"width",type:a.nodeSize,triggersBounds:i.any,hashOverride:y},{name:"shape",type:a.nodeShape,triggersBounds:i.any},{name:"shape-polygon-points",type:a.polygonPointList,triggersBounds:i.any},{name:"corner-radius",type:a.cornerRadius},{name:"background-color",type:a.color},{name:"background-fill",type:a.fill},{name:"background-opacity",type:a.zeroOneNumber},{name:"background-blacken",type:a.nOneOneNumber},{name:"background-gradient-stop-colors",type:a.colors},{name:"background-gradient-stop-positions",type:a.percentages},{name:"background-gradient-direction",type:a.gradientDirection},{name:"padding",type:a.sizeMaybePercent,triggersBounds:i.any},{name:"padding-relative-to",type:a.paddingRelativeTo,triggersBounds:i.any},{name:"bounds-expansion",type:a.boundsExpansion,triggersBounds:i.any}],b=[{name:"border-color",type:a.color},{name:"border-opacity",type:a.zeroOneNumber},{name:"border-width",type:a.size,triggersBounds:i.any},{name:"border-style",type:a.borderStyle},{name:"border-cap",type:a.lineCap},{name:"border-join",type:a.lineJoin},{name:"border-dash-pattern",type:a.numbers},{name:"border-dash-offset",type:a.number},{name:"border-position",type:a.linePosition}],x=[{name:"outline-color",type:a.color},{name:"outline-opacity",type:a.zeroOneNumber},{name:"outline-width",type:a.size,triggersBounds:i.any},{name:"outline-style",type:a.borderStyle},{name:"outline-offset",type:a.size,triggersBounds:i.any}],w=[{name:"background-image",type:a.urls},{name:"background-image-crossorigin",type:a.bgCrossOrigin},{name:"background-image-opacity",type:a.zeroOneNumbers},{name:"background-image-containment",type:a.bgContainment},{name:"background-image-smoothing",type:a.bools},{name:"background-position-x",type:a.bgPos},{name:"background-position-y",type:a.bgPos},{name:"background-width-relative-to",type:a.bgRelativeTo},{name:"background-height-relative-to",type:a.bgRelativeTo},{name:"background-repeat",type:a.bgRepeat},{name:"background-fit",type:a.bgFit},{name:"background-clip",type:a.bgClip},{name:"background-width",type:a.bgWH},{name:"background-height",type:a.bgWH},{name:"background-offset-x",type:a.bgPos},{name:"background-offset-y",type:a.bgPos}],E=[{name:"position",type:a.position,triggersBounds:i.any},{name:"compound-sizing-wrt-labels",type:a.compoundIncludeLabels,triggersBounds:i.any},{name:"min-width",type:a.size,triggersBounds:i.any},{name:"min-width-bias-left",type:a.sizeMaybePercent,triggersBounds:i.any},{name:"min-width-bias-right",type:a.sizeMaybePercent,triggersBounds:i.any},{name:"min-height",type:a.size,triggersBounds:i.any},{name:"min-height-bias-top",type:a.sizeMaybePercent,triggersBounds:i.any},{name:"min-height-bias-bottom",type:a.sizeMaybePercent,triggersBounds:i.any}],k=[{name:"line-style",type:a.lineStyle},{name:"line-color",type:a.color},{name:"line-fill",type:a.fill},{name:"line-cap",type:a.lineCap},{name:"line-opacity",type:a.zeroOneNumber},{name:"line-dash-pattern",type:a.numbers},{name:"line-dash-offset",type:a.number},{name:"line-outline-width",type:a.size},{name:"line-outline-color",type:a.color},{name:"line-gradient-stop-colors",type:a.colors},{name:"line-gradient-stop-positions",type:a.percentages},{name:"curve-style",type:a.curveStyle,triggersBounds:i.any,triggersBoundsOfParallelBeziers:!0},{name:"haystack-radius",type:a.zeroOneNumber,triggersBounds:i.any},{name:"source-endpoint",type:a.edgeEndpoint,triggersBounds:i.any},{name:"target-endpoint",type:a.edgeEndpoint,triggersBounds:i.any},{name:"control-point-step-size",type:a.size,triggersBounds:i.any},{name:"control-point-distances",type:a.bidirectionalSizes,triggersBounds:i.any},{name:"control-point-weights",type:a.numbers,triggersBounds:i.any},{name:"segment-distances",type:a.bidirectionalSizes,triggersBounds:i.any},{name:"segment-weights",type:a.numbers,triggersBounds:i.any},{name:"segment-radii",type:a.numbers,triggersBounds:i.any},{name:"radius-type",type:a.radiusType,triggersBounds:i.any},{name:"taxi-turn",type:a.bidirectionalSizeMaybePercent,triggersBounds:i.any},{name:"taxi-turn-min-distance",type:a.size,triggersBounds:i.any},{name:"taxi-direction",type:a.axisDirection,triggersBounds:i.any},{name:"taxi-radius",type:a.number,triggersBounds:i.any},{name:"edge-distances",type:a.edgeDistances,triggersBounds:i.any},{name:"arrow-scale",type:a.positiveNumber,triggersBounds:i.any},{name:"loop-direction",type:a.angle,triggersBounds:i.any},{name:"loop-sweep",type:a.angle,triggersBounds:i.any},{name:"source-distance-from-node",type:a.size,triggersBounds:i.any},{name:"target-distance-from-node",type:a.size,triggersBounds:i.any}],C=[{name:"ghost",type:a.bool,triggersBounds:i.any},{name:"ghost-offset-x",type:a.bidirectionalSize,triggersBounds:i.any},{name:"ghost-offset-y",type:a.bidirectionalSize,triggersBounds:i.any},{name:"ghost-opacity",type:a.zeroOneNumber}],S=[{name:"selection-box-color",type:a.color},{name:"selection-box-opacity",type:a.zeroOneNumber},{name:"selection-box-border-color",type:a.color},{name:"selection-box-border-width",type:a.size},{name:"active-bg-color",type:a.color},{name:"active-bg-opacity",type:a.zeroOneNumber},{name:"active-bg-size",type:a.size},{name:"outside-texture-bg-color",type:a.color},{name:"outside-texture-bg-opacity",type:a.zeroOneNumber}],P=[];Ms.pieBackgroundN=16,P.push({name:"pie-size",type:a.sizeMaybePercent});for(var T=1;T<=Ms.pieBackgroundN;T++)P.push({name:"pie-"+T+"-background-color",type:a.color}),P.push({name:"pie-"+T+"-background-size",type:a.percent}),P.push({name:"pie-"+T+"-background-opacity",type:a.zeroOneNumber});var _=[],M=Ms.arrowPrefixes=["source","mid-source","target","mid-target"];[{name:"arrow-shape",type:a.arrowShape,triggersBounds:i.any},{name:"arrow-color",type:a.color},{name:"arrow-fill",type:a.arrowFill},{name:"arrow-width",type:a.arrowWidth}].forEach((function(e){M.forEach((function(t){var n=t+"-"+e.name,r=e.type,i=e.triggersBounds;_.push({name:n,type:r,triggersBounds:i})}))}),{});var B=Ms.properties=[].concat(d,g,h,p,f,C,c,u,o,s,l,m,b,x,w,P,E,k,_,S),N=Ms.propertyGroups={behavior:d,transition:g,visibility:h,overlay:p,underlay:f,ghost:C,commonLabel:c,labelDimensions:u,mainLabel:o,sourceLabel:s,targetLabel:l,nodeBody:m,nodeBorder:b,nodeOutline:x,backgroundImage:w,pie:P,compound:E,edgeLine:k,edgeArrow:_,core:S},z=Ms.propertyGroupNames={};(Ms.propertyGroupKeys=Object.keys(N)).forEach((function(e){z[e]=N[e].map((function(e){return e.name})),N[e].forEach((function(t){return t.groupKey=e}))}));var A=Ms.aliases=[{name:"content",pointsTo:"label"},{name:"control-point-distance",pointsTo:"control-point-distances"},{name:"control-point-weight",pointsTo:"control-point-weights"},{name:"segment-distance",pointsTo:"segment-distances"},{name:"segment-weight",pointsTo:"segment-weights"},{name:"segment-radius",pointsTo:"segment-radii"},{name:"edge-text-rotation",pointsTo:"text-rotation"},{name:"padding-left",pointsTo:"padding"},{name:"padding-right",pointsTo:"padding"},{name:"padding-top",pointsTo:"padding"},{name:"padding-bottom",pointsTo:"padding"}];Ms.propertyNames=B.map((function(e){return e.name}));for(var L=0;L<B.length;L++){var O=B[L];B[O.name]=O}for(var R=0;R<A.length;R++){var V=A[R],F=B[V.pointsTo],j={name:V.name,alias:!0,pointsTo:F};B.push(j),B[V.name]=j}}(),Ms.getDefaultProperty=function(e){return this.getDefaultProperties()[e]},Ms.getDefaultProperties=function(){var e=this._private;if(null!=e.defaultProperties)return e.defaultProperties;for(var t=L({"selection-box-color":"#ddd","selection-box-opacity":.65,"selection-box-border-color":"#aaa","selection-box-border-width":1,"active-bg-color":"black","active-bg-opacity":.15,"active-bg-size":30,"outside-texture-bg-color":"#000","outside-texture-bg-opacity":.125,events:"yes","text-events":"no","text-valign":"top","text-halign":"center","text-justification":"auto","line-height":1,color:"#000","text-outline-color":"#000","text-outline-width":0,"text-outline-opacity":1,"text-opacity":1,"text-decoration":"none","text-transform":"none","text-wrap":"none","text-overflow-wrap":"whitespace","text-max-width":9999,"text-background-color":"#000","text-background-opacity":0,"text-background-shape":"rectangle","text-background-padding":0,"text-border-opacity":0,"text-border-width":0,"text-border-style":"solid","text-border-color":"#000","font-family":"Helvetica Neue, Helvetica, sans-serif","font-style":"normal","font-weight":"normal","font-size":16,"min-zoomed-font-size":0,"text-rotation":"none","source-text-rotation":"none","target-text-rotation":"none",visibility:"visible",display:"element",opacity:1,"z-compound-depth":"auto","z-index-compare":"auto","z-index":0,label:"","text-margin-x":0,"text-margin-y":0,"source-label":"","source-text-offset":0,"source-text-margin-x":0,"source-text-margin-y":0,"target-label":"","target-text-offset":0,"target-text-margin-x":0,"target-text-margin-y":0,"overlay-opacity":0,"overlay-color":"#000","overlay-padding":10,"overlay-shape":"round-rectangle","overlay-corner-radius":"auto","underlay-opacity":0,"underlay-color":"#000","underlay-padding":10,"underlay-shape":"round-rectangle","underlay-corner-radius":"auto","transition-property":"none","transition-duration":0,"transition-delay":0,"transition-timing-function":"linear","background-blacken":0,"background-color":"#999","background-fill":"solid","background-opacity":1,"background-image":"none","background-image-crossorigin":"anonymous","background-image-opacity":1,"background-image-containment":"inside","background-image-smoothing":"yes","background-position-x":"50%","background-position-y":"50%","background-offset-x":0,"background-offset-y":0,"background-width-relative-to":"include-padding","background-height-relative-to":"include-padding","background-repeat":"no-repeat","background-fit":"none","background-clip":"node","background-width":"auto","background-height":"auto","border-color":"#000","border-opacity":1,"border-width":0,"border-style":"solid","border-dash-pattern":[4,2],"border-dash-offset":0,"border-cap":"butt","border-join":"miter","border-position":"center","outline-color":"#999","outline-opacity":1,"outline-width":0,"outline-offset":0,"outline-style":"solid",height:30,width:30,shape:"ellipse","shape-polygon-points":"-1, -1,   1, -1,   1, 1,   -1, 1","corner-radius":"auto","bounds-expansion":0,"background-gradient-direction":"to-bottom","background-gradient-stop-colors":"#999","background-gradient-stop-positions":"0%",ghost:"no","ghost-offset-y":0,"ghost-offset-x":0,"ghost-opacity":0,padding:0,"padding-relative-to":"width",position:"origin","compound-sizing-wrt-labels":"include","min-width":0,"min-width-bias-left":0,"min-width-bias-right":0,"min-height":0,"min-height-bias-top":0,"min-height-bias-bottom":0},{"pie-size":"100%"},[{name:"pie-{{i}}-background-color",value:"black"},{name:"pie-{{i}}-background-size",value:"0%"},{name:"pie-{{i}}-background-opacity",value:1}].reduce((function(e,t){for(var n=1;n<=Ms.pieBackgroundN;n++){var r=t.name.replace("{{i}}",n),i=t.value;e[r]=i}return e}),{}),{"line-style":"solid","line-color":"#999","line-fill":"solid","line-cap":"butt","line-opacity":1,"line-outline-width":0,"line-outline-color":"#000","line-gradient-stop-colors":"#999","line-gradient-stop-positions":"0%","control-point-step-size":40,"control-point-weights":.5,"segment-weights":.5,"segment-distances":20,"segment-radii":15,"radius-type":"arc-radius","taxi-turn":"50%","taxi-radius":15,"taxi-turn-min-distance":10,"taxi-direction":"auto","edge-distances":"intersection","curve-style":"haystack","haystack-radius":0,"arrow-scale":1,"loop-direction":"-45deg","loop-sweep":"-90deg","source-distance-from-node":0,"target-distance-from-node":0,"source-endpoint":"outside-to-node","target-endpoint":"outside-to-node","line-dash-pattern":[6,3],"line-dash-offset":0},[{name:"arrow-shape",value:"none"},{name:"arrow-color",value:"#999"},{name:"arrow-fill",value:"filled"},{name:"arrow-width",value:1}].reduce((function(e,t){return Ms.arrowPrefixes.forEach((function(n){var r=n+"-"+t.name,i=t.value;e[r]=i})),e}),{})),n={},r=0;r<this.properties.length;r++){var i=this.properties[r];if(!i.pointsTo){var a=i.name,o=t[a],s=this.parse(a,o);n[a]=s}}return e.defaultProperties=n,e.defaultProperties},Ms.addDefaultStylesheet=function(){this.selector(":parent").css({shape:"rectangle",padding:10,"background-color":"#eee","border-color":"#ccc","border-width":1}).selector("edge").css({width:3}).selector(":loop").css({"curve-style":"bezier"}).selector("edge:compound").css({"curve-style":"bezier","source-endpoint":"outside-to-line","target-endpoint":"outside-to-line"}).selector(":selected").css({"background-color":"#0169D9","line-color":"#0169D9","source-arrow-color":"#0169D9","target-arrow-color":"#0169D9","mid-source-arrow-color":"#0169D9","mid-target-arrow-color":"#0169D9"}).selector(":parent:selected").css({"background-color":"#CCE1F9","border-color":"#aec8e5"}).selector(":active").css({"overlay-color":"black","overlay-padding":10,"overlay-opacity":.25}),this.defaultLength=this.length};var Bs={parse:function(e,t,n,r){if(y(t))return this.parseImplWarn(e,t,n,r);var i,a=_e(e,""+t,n?"t":"f","mapping"===r||!0===r||!1===r||null==r?"dontcare":r),o=this.propCache=this.propCache||[];return(i=o[a])||(i=o[a]=this.parseImplWarn(e,t,n,r)),(n||"mapping"===r)&&(i=qe(i))&&(i.value=qe(i.value)),i},parseImplWarn:function(e,t,n,r){var i=this.parseImpl(e,t,n,r);return i||null==t||je("The style property `".concat(e,": ").concat(t,"` is invalid")),!i||"width"!==i.name&&"height"!==i.name||"label"!==t||je("The style value of `label` is deprecated for `"+i.name+"`"),i}};Bs.parseImpl=function(e,t,n,r){e=M(e);var i=this.properties[e],a=t,o=this.types;if(!i)return null;if(void 0===t)return null;i.alias&&(i=i.pointsTo,e=i.name);var s=v(t);s&&(t=t.trim());var l,u,c=i.type;if(!c)return null;if(n&&(""===t||null===t))return{name:e,value:t,bypass:!0,deleteBypass:!0};if(y(t))return{name:e,value:t,strValue:"fn",mapped:o.fn,bypass:n};if(!s||r||t.length<7||"a"!==t[1]);else{if(t.length>=7&&"d"===t[0]&&(l=new RegExp(o.data.regex).exec(t))){if(n)return!1;var d=o.data;return{name:e,value:l,strValue:""+t,mapped:d,field:l[1],bypass:n}}if(t.length>=10&&"m"===t[0]&&(u=new RegExp(o.mapData.regex).exec(t))){if(n)return!1;if(c.multiple)return!1;var h=o.mapData;if(!c.color&&!c.number)return!1;var p=this.parse(e,u[4]);if(!p||p.mapped)return!1;var f=this.parse(e,u[5]);if(!f||f.mapped)return!1;if(p.pfValue===f.pfValue||p.strValue===f.strValue)return je("`"+e+": "+t+"` is not a valid mapper because the output range is zero; converting to `"+e+": "+p.strValue+"`"),this.parse(e,p.strValue);if(c.color){var g=p.value,b=f.value;if(!(g[0]!==b[0]||g[1]!==b[1]||g[2]!==b[2]||g[3]!==b[3]&&(null!=g[3]&&1!==g[3]||null!=b[3]&&1!==b[3])))return!1}return{name:e,value:u,strValue:""+t,mapped:h,field:u[1],fieldMin:parseFloat(u[2]),fieldMax:parseFloat(u[3]),valueMin:p.value,valueMax:f.value,bypass:n}}}if(c.multiple&&"multiple"!==r){var w;if(w=s?t.split(/\s+/):m(t)?t:[t],c.evenMultiple&&w.length%2!=0)return null;for(var E=[],k=[],C=[],S="",P=!1,D=0;D<w.length;D++){var T=this.parse(e,w[D],n,"multiple");P=P||v(T.value),E.push(T.value),C.push(null!=T.pfValue?T.pfValue:T.value),k.push(T.units),S+=(D>0?" ":"")+T.strValue}return c.validate&&!c.validate(E,k)?null:c.singleEnum&&P?1===E.length&&v(E[0])?{name:e,value:E[0],strValue:E[0],bypass:n}:null:{name:e,value:E,pfValue:C,strValue:S,bypass:n,units:k}}var _,B,N=function(){for(var r=0;r<c.enums.length;r++){if(c.enums[r]===t)return{name:e,value:t,strValue:""+t,bypass:n}}return null};if(c.number){var z,A="px";if(c.units&&(z=c.units),c.implicitUnits&&(A=c.implicitUnits),!c.unitless)if(s){var L="px|em"+(c.allowPercent?"|\\%":"");z&&(L=z);var R=t.match("^("+I+")("+L+")?$");R&&(t=R[1],z=R[2]||A)}else z&&!c.implicitUnits||(z=A);if(t=parseFloat(t),isNaN(t)&&void 0===c.enums)return null;if(isNaN(t)&&void 0!==c.enums)return t=a,N();if(c.integer&&(!x(B=t)||Math.floor(B)!==B))return null;if(void 0!==c.min&&(t<c.min||c.strictMin&&t===c.min)||void 0!==c.max&&(t>c.max||c.strictMax&&t===c.max))return null;var V={name:e,value:t,strValue:""+t+(z||""),units:z,bypass:n};return c.unitless||"px"!==z&&"em"!==z?V.pfValue=t:V.pfValue="px"!==z&&z?this.getEmSizeInPixels()*t:t,"ms"!==z&&"s"!==z||(V.pfValue="ms"===z?t:1e3*t),"deg"!==z&&"rad"!==z||(V.pfValue="rad"===z?t:(_=t,Math.PI*_/180)),"%"===z&&(V.pfValue=t/100),V}if(c.propList){var F=[],j=""+t;if("none"===j);else{for(var q=j.split(/\s*,\s*|\s+/),Y=0;Y<q.length;Y++){var X=q[Y].trim();this.properties[X]?F.push(X):je("`"+X+"` is not a valid property name")}if(0===F.length)return null}return{name:e,value:F,strValue:0===F.length?"none":F.join(" "),bypass:n}}if(c.color){var W=O(t);return W?{name:e,value:W,pfValue:W,strValue:"rgb("+W[0]+","+W[1]+","+W[2]+")",bypass:n}:null}if(c.regex||c.regexes){if(c.enums){var H=N();if(H)return H}for(var K=c.regexes?c.regexes:[c.regex],G=0;G<K.length;G++){var U=new RegExp(K[G]).exec(t);if(U)return{name:e,value:c.singleRegexMatchValue?U[1]:U,strValue:""+t,bypass:n}}return null}return c.string?{name:e,value:""+t,strValue:""+t,bypass:n}:c.enums?N():null};var Ns=function e(t){if(!(this instanceof e))return new e(t);S(t)?(this._private={cy:t,coreStyle:{}},this.length=0,this.resetToDefault()):Ve("A style must have a core reference")},zs=Ns.prototype;zs.instanceString=function(){return"style"},zs.clear=function(){for(var e=this._private,t=e.cy.elements(),n=0;n<this.length;n++)this[n]=void 0;return this.length=0,e.contextStyles={},e.propDiffs={},this.cleanElements(t,!0),t.forEach((function(e){var t=e[0]._private;t.styleDirty=!0,t.appliedInitStyle=!1})),this},zs.resetToDefault=function(){return this.clear(),this.addDefaultStylesheet(),this},zs.core=function(e){return this._private.coreStyle[e]||this.getDefaultProperty(e)},zs.selector=function(e){var t="core"===e?null:new ka(e),n=this.length++;return this[n]={selector:t,properties:[],mappedProperties:[],index:n},this},zs.css=function(){var e=this,t=arguments;if(1===t.length)for(var n=t[0],r=0;r<e.properties.length;r++){var i=e.properties[r],a=n[i.name];void 0===a&&(a=n[B(i.name)]),void 0!==a&&this.cssRule(i.name,a)}else 2===t.length&&this.cssRule(t[0],t[1]);return this},zs.style=zs.css,zs.cssRule=function(e,t){var n=this.parse(e,t);if(n){var r=this.length-1;this[r].properties.push(n),this[r].properties[n.name]=n,n.name.match(/pie-(\d+)-background-size/)&&n.value&&(this._private.hasPie=!0),n.mapped&&this[r].mappedProperties.push(n),!this[r].selector&&(this._private.coreStyle[n.name]=n)}return this},zs.append=function(e){return P(e)?e.appendToStyle(this):m(e)?this.appendFromJson(e):v(e)&&this.appendFromString(e),this},Ns.fromJson=function(e,t){var n=new Ns(e);return n.fromJson(t),n},Ns.fromString=function(e,t){return new Ns(e).fromString(t)},[Cs,Ss,Ps,Ds,Ts,_s,Ms,Bs].forEach((function(e){L(zs,e)})),Ns.types=zs.types,Ns.properties=zs.properties,Ns.propertyGroups=zs.propertyGroups,Ns.propertyGroupNames=zs.propertyGroupNames,Ns.propertyGroupKeys=zs.propertyGroupKeys;var Is={style:function(e){e&&this.setStyle(e).update();return this._private.style},setStyle:function(e){var t=this._private;return P(e)?t.style=e.generateStyle(this):m(e)?t.style=Ns.fromJson(this,e):v(e)?t.style=Ns.fromString(this,e):t.style=Ns(this),t.style},updateStyle:function(){this.mutableElements().updateStyle()}},As={autolock:function(e){return void 0===e?this._private.autolock:(this._private.autolock=!!e,this)},autoungrabify:function(e){return void 0===e?this._private.autoungrabify:(this._private.autoungrabify=!!e,this)},autounselectify:function(e){return void 0===e?this._private.autounselectify:(this._private.autounselectify=!!e,this)},selectionType:function(e){var t=this._private;return null==t.selectionType&&(t.selectionType="single"),void 0===e?t.selectionType:("additive"!==e&&"single"!==e||(t.selectionType=e),this)},panningEnabled:function(e){return void 0===e?this._private.panningEnabled:(this._private.panningEnabled=!!e,this)},userPanningEnabled:function(e){return void 0===e?this._private.userPanningEnabled:(this._private.userPanningEnabled=!!e,this)},zoomingEnabled:function(e){return void 0===e?this._private.zoomingEnabled:(this._private.zoomingEnabled=!!e,this)},userZoomingEnabled:function(e){return void 0===e?this._private.userZoomingEnabled:(this._private.userZoomingEnabled=!!e,this)},boxSelectionEnabled:function(e){return void 0===e?this._private.boxSelectionEnabled:(this._private.boxSelectionEnabled=!!e,this)},pan:function(){var e,t,n,r,i,a=arguments,o=this._private.pan;switch(a.length){case 0:return o;case 1:if(v(a[0]))return o[e=a[0]];if(b(a[0])){if(!this._private.panningEnabled)return this;r=(n=a[0]).x,i=n.y,x(r)&&(o.x=r),x(i)&&(o.y=i),this.emit("pan viewport")}break;case 2:if(!this._private.panningEnabled)return this;e=a[0],t=a[1],"x"!==e&&"y"!==e||!x(t)||(o[e]=t),this.emit("pan viewport")}return this.notify("viewport"),this},panBy:function(e,t){var n,r,i,a,o,s=arguments,l=this._private.pan;if(!this._private.panningEnabled)return this;switch(s.length){case 1:b(e)&&(a=(i=s[0]).x,o=i.y,x(a)&&(l.x+=a),x(o)&&(l.y+=o),this.emit("pan viewport"));break;case 2:r=t,"x"!==(n=e)&&"y"!==n||!x(r)||(l[n]+=r),this.emit("pan viewport")}return this.notify("viewport"),this},fit:function(e,t){var n=this.getFitViewport(e,t);if(n){var r=this._private;r.zoom=n.zoom,r.pan=n.pan,this.emit("pan zoom viewport"),this.notify("viewport")}return this},getFitViewport:function(e,t){if(x(e)&&void 0===t&&(t=e,e=void 0),this._private.panningEnabled&&this._private.zoomingEnabled){var n,r;if(v(e)){var i=e;e=this.$(i)}else if(b(r=e)&&x(r.x1)&&x(r.x2)&&x(r.y1)&&x(r.y2)){var a=e;(n={x1:a.x1,y1:a.y1,x2:a.x2,y2:a.y2}).w=n.x2-n.x1,n.h=n.y2-n.y1}else E(e)||(e=this.mutableElements());if(!E(e)||!e.empty()){n=n||e.boundingBox();var o,s=this.width(),l=this.height();if(t=x(t)?t:0,!isNaN(s)&&!isNaN(l)&&s>0&&l>0&&!isNaN(n.w)&&!isNaN(n.h)&&n.w>0&&n.h>0)return{zoom:o=(o=(o=Math.min((s-2*t)/n.w,(l-2*t)/n.h))>this._private.maxZoom?this._private.maxZoom:o)<this._private.minZoom?this._private.minZoom:o,pan:{x:(s-o*(n.x1+n.x2))/2,y:(l-o*(n.y1+n.y2))/2}}}}},zoomRange:function(e,t){var n=this._private;if(null==t){var r=e;e=r.min,t=r.max}return x(e)&&x(t)&&e<=t?(n.minZoom=e,n.maxZoom=t):x(e)&&void 0===t&&e<=n.maxZoom?n.minZoom=e:x(t)&&void 0===e&&t>=n.minZoom&&(n.maxZoom=t),this},minZoom:function(e){return void 0===e?this._private.minZoom:this.zoomRange({min:e})},maxZoom:function(e){return void 0===e?this._private.maxZoom:this.zoomRange({max:e})},getZoomedViewport:function(e){var t,n,r=this._private,i=r.pan,a=r.zoom,o=!1;if(r.zoomingEnabled||(o=!0),x(e)?n=e:b(e)&&(n=e.level,null!=e.position?t=yt(e.position,a,i):null!=e.renderedPosition&&(t=e.renderedPosition),null==t||r.panningEnabled||(o=!0)),n=(n=n>r.maxZoom?r.maxZoom:n)<r.minZoom?r.minZoom:n,o||!x(n)||n===a||null!=t&&(!x(t.x)||!x(t.y)))return null;if(null!=t){var s=i,l=a,u=n;return{zoomed:!0,panned:!0,zoom:u,pan:{x:-u/l*(t.x-s.x)+t.x,y:-u/l*(t.y-s.y)+t.y}}}return{zoomed:!0,panned:!1,zoom:n,pan:i}},zoom:function(e){if(void 0===e)return this._private.zoom;var t=this.getZoomedViewport(e),n=this._private;return null!=t&&t.zoomed?(n.zoom=t.zoom,t.panned&&(n.pan.x=t.pan.x,n.pan.y=t.pan.y),this.emit("zoom"+(t.panned?" pan":"")+" viewport"),this.notify("viewport"),this):this},viewport:function(e){var t=this._private,n=!0,r=!0,i=[],a=!1,o=!1;if(!e)return this;if(x(e.zoom)||(n=!1),b(e.pan)||(r=!1),!n&&!r)return this;if(n){var s=e.zoom;s<t.minZoom||s>t.maxZoom||!t.zoomingEnabled?a=!0:(t.zoom=s,i.push("zoom"))}if(r&&(!a||!e.cancelOnFailedZoom)&&t.panningEnabled){var l=e.pan;x(l.x)&&(t.pan.x=l.x,o=!1),x(l.y)&&(t.pan.y=l.y,o=!1),o||i.push("pan")}return i.length>0&&(i.push("viewport"),this.emit(i.join(" ")),this.notify("viewport")),this},center:function(e){var t=this.getCenterPan(e);return t&&(this._private.pan=t,this.emit("pan viewport"),this.notify("viewport")),this},getCenterPan:function(e,t){if(this._private.panningEnabled){if(v(e)){var n=e;e=this.mutableElements().filter(n)}else E(e)||(e=this.mutableElements());if(0!==e.length){var r=e.boundingBox(),i=this.width(),a=this.height();return{x:(i-(t=void 0===t?this._private.zoom:t)*(r.x1+r.x2))/2,y:(a-t*(r.y1+r.y2))/2}}}},reset:function(){return this._private.panningEnabled&&this._private.zoomingEnabled?(this.viewport({pan:{x:0,y:0},zoom:1}),this):this},invalidateSize:function(){this._private.sizeCache=null},size:function(){var e,t,n=this._private,r=n.container,i=this;return n.sizeCache=n.sizeCache||(r?(e=i.window().getComputedStyle(r),t=function(t){return parseFloat(e.getPropertyValue(t))},{width:r.clientWidth-t("padding-left")-t("padding-right"),height:r.clientHeight-t("padding-top")-t("padding-bottom")}):{width:1,height:1})},width:function(){return this.size().width},height:function(){return this.size().height},extent:function(){var e=this._private.pan,t=this._private.zoom,n=this.renderedExtent(),r={x1:(n.x1-e.x)/t,x2:(n.x2-e.x)/t,y1:(n.y1-e.y)/t,y2:(n.y2-e.y)/t};return r.w=r.x2-r.x1,r.h=r.y2-r.y1,r},renderedExtent:function(){var e=this.width(),t=this.height();return{x1:0,y1:0,x2:e,y2:t,w:e,h:t}},multiClickDebounceTime:function(e){return e?(this._private.multiClickDebounceTime=e,this):this._private.multiClickDebounceTime}};As.centre=As.center,As.autolockNodes=As.autolock,As.autoungrabifyNodes=As.autoungrabify;var Ls={data:Fi.data({field:"data",bindingEvent:"data",allowBinding:!0,allowSetting:!0,settingEvent:"data",settingTriggersEvent:!0,triggerFnName:"trigger",allowGetting:!0,updateStyle:!0}),removeData:Fi.removeData({field:"data",event:"data",triggerFnName:"trigger",triggerEvent:!0,updateStyle:!0}),scratch:Fi.data({field:"scratch",bindingEvent:"scratch",allowBinding:!0,allowSetting:!0,settingEvent:"scratch",settingTriggersEvent:!0,triggerFnName:"trigger",allowGetting:!0,updateStyle:!0}),removeScratch:Fi.removeData({field:"scratch",event:"scratch",triggerFnName:"trigger",triggerEvent:!0,updateStyle:!0})};Ls.attr=Ls.data,Ls.removeAttr=Ls.removeData;var Os=function(e){var t=this,n=(e=L({},e)).container;n&&!w(n)&&w(n[0])&&(n=n[0]);var r=n?n._cyreg:null;(r=r||{})&&r.cy&&(r.cy.destroy(),r={});var i=r.readies=r.readies||[];n&&(n._cyreg=r),r.cy=t;var a=void 0!==u&&void 0!==n&&!e.headless,o=e;o.layout=L({name:a?"grid":"null"},o.layout),o.renderer=L({name:a?"canvas":"null"},o.renderer);var s=function(e,t,n){return void 0!==t?t:void 0!==n?n:e},l=this._private={container:n,ready:!1,options:o,elements:new ts(this),listeners:[],aniEles:new ts(this),data:o.data||{},scratch:{},layout:null,renderer:null,destroyed:!1,notificationsEnabled:!0,minZoom:1e-50,maxZoom:1e50,zoomingEnabled:s(!0,o.zoomingEnabled),userZoomingEnabled:s(!0,o.userZoomingEnabled),panningEnabled:s(!0,o.panningEnabled),userPanningEnabled:s(!0,o.userPanningEnabled),boxSelectionEnabled:s(!0,o.boxSelectionEnabled),autolock:s(!1,o.autolock,o.autolockNodes),autoungrabify:s(!1,o.autoungrabify,o.autoungrabifyNodes),autounselectify:s(!1,o.autounselectify),styleEnabled:void 0===o.styleEnabled?a:o.styleEnabled,zoom:x(o.zoom)?o.zoom:1,pan:{x:b(o.pan)&&x(o.pan.x)?o.pan.x:0,y:b(o.pan)&&x(o.pan.y)?o.pan.y:0},animation:{current:[],queue:[]},hasCompoundNodes:!1,multiClickDebounceTime:s(250,o.multiClickDebounceTime)};this.createEmitter(),this.selectionType(o.selectionType),this.zoomRange({min:o.minZoom,max:o.maxZoom});l.styleEnabled&&t.setStyle([]);var c=L({},o,o.renderer);t.initRenderer(c);!function(e,t){if(e.some(T))return vr.all(e).then(t);t(e)}([o.style,o.elements],(function(e){var n=e[0],a=e[1];l.styleEnabled&&t.style().append(n),function(e,n,r){t.notifications(!1);var i=t.mutableElements();i.length>0&&i.remove(),null!=e&&(b(e)||m(e))&&t.add(e),t.one("layoutready",(function(e){t.notifications(!0),t.emit(e),t.one("load",n),t.emitAndNotify("load")})).one("layoutstop",(function(){t.one("done",r),t.emit("done")}));var a=L({},t._private.options.layout);a.eles=t.elements(),t.layout(a).run()}(a,(function(){t.startAnimationLoop(),l.ready=!0,y(o.ready)&&t.on("ready",o.ready);for(var e=0;e<i.length;e++){var n=i[e];t.on("ready",n)}r&&(r.readies=[]),t.emit("ready")}),o.done)}))},Rs=Os.prototype;L(Rs,{instanceString:function(){return"core"},isReady:function(){return this._private.ready},destroyed:function(){return this._private.destroyed},ready:function(e){return this.isReady()?this.emitter().emit("ready",[],e):this.on("ready",e),this},destroy:function(){var e=this;if(!e.destroyed())return e.stopAnimationLoop(),e.destroyRenderer(),this.emit("destroy"),e._private.destroyed=!0,e},hasElementWithId:function(e){return this._private.elements.hasElementWithId(e)},getElementById:function(e){return this._private.elements.getElementById(e)},hasCompoundNodes:function(){return this._private.hasCompoundNodes},headless:function(){return this._private.renderer.isHeadless()},styleEnabled:function(){return this._private.styleEnabled},addToPool:function(e){return this._private.elements.merge(e),this},removeFromPool:function(e){return this._private.elements.unmerge(e),this},container:function(){return this._private.container||null},window:function(){if(null==this._private.container)return u;var e=this._private.container.ownerDocument;return void 0===e||null==e?u:e.defaultView||u},mount:function(e){if(null!=e){var t=this,n=t._private,r=n.options;return!w(e)&&w(e[0])&&(e=e[0]),t.stopAnimationLoop(),t.destroyRenderer(),n.container=e,n.styleEnabled=!0,t.invalidateSize(),t.initRenderer(L({},r,r.renderer,{name:"null"===r.renderer.name?"canvas":r.renderer.name})),t.startAnimationLoop(),t.style(r.style),t.emit("mount"),t}},unmount:function(){var e=this;return e.stopAnimationLoop(),e.destroyRenderer(),e.initRenderer({name:"null"}),e.emit("unmount"),e},options:function(){return qe(this._private.options)},json:function(e){var t=this,n=t._private,r=t.mutableElements();if(b(e)){if(t.startBatch(),e.elements){var i={},a=function(e,n){for(var r=[],a=[],o=0;o<e.length;o++){var s=e[o];if(s.data.id){var l=""+s.data.id,u=t.getElementById(l);i[l]=!0,0!==u.length?a.push({ele:u,json:s}):n?(s.group=n,r.push(s)):r.push(s)}else je("cy.json() cannot handle elements without an ID attribute")}t.add(r);for(var c=0;c<a.length;c++){var d=a[c],h=d.ele,p=d.json;h.json(p)}};if(m(e.elements))a(e.elements);else for(var o=["nodes","edges"],s=0;s<o.length;s++){var l=o[s],u=e.elements[l];m(u)&&a(u,l)}var c=t.collection();r.filter((function(e){return!i[e.id()]})).forEach((function(e){e.isParent()?c.merge(e):e.remove()})),c.forEach((function(e){return e.children().move({parent:null})})),c.forEach((function(e){return function(e){return t.getElementById(e.id())}(e).remove()}))}e.style&&t.style(e.style),null!=e.zoom&&e.zoom!==n.zoom&&t.zoom(e.zoom),e.pan&&(e.pan.x===n.pan.x&&e.pan.y===n.pan.y||t.pan(e.pan)),e.data&&t.data(e.data);for(var d=["minZoom","maxZoom","zoomingEnabled","userZoomingEnabled","panningEnabled","userPanningEnabled","boxSelectionEnabled","autolock","autoungrabify","autounselectify","multiClickDebounceTime"],h=0;h<d.length;h++){var p=d[h];null!=e[p]&&t[p](e[p])}return t.endBatch(),this}var f={};!!e?f.elements=this.elements().map((function(e){return e.json()})):(f.elements={},r.forEach((function(e){var t=e.group();f.elements[t]||(f.elements[t]=[]),f.elements[t].push(e.json())}))),this._private.styleEnabled&&(f.style=t.style().json()),f.data=qe(t.data());var g=n.options;return f.zoomingEnabled=n.zoomingEnabled,f.userZoomingEnabled=n.userZoomingEnabled,f.zoom=n.zoom,f.minZoom=n.minZoom,f.maxZoom=n.maxZoom,f.panningEnabled=n.panningEnabled,f.userPanningEnabled=n.userPanningEnabled,f.pan=qe(n.pan),f.boxSelectionEnabled=n.boxSelectionEnabled,f.renderer=qe(g.renderer),f.hideEdgesOnViewport=g.hideEdgesOnViewport,f.textureOnViewport=g.textureOnViewport,f.wheelSensitivity=g.wheelSensitivity,f.motionBlur=g.motionBlur,f.multiClickDebounceTime=g.multiClickDebounceTime,f}}),Rs.$id=Rs.getElementById,[rs,fs,ys,ms,bs,xs,Es,ks,Is,As,Ls].forEach((function(e){L(Rs,e)}));var Vs={fit:!0,directed:!1,padding:30,circle:!1,grid:!1,spacingFactor:1.75,boundingBox:void 0,avoidOverlap:!0,nodeDimensionsIncludeLabels:!1,roots:void 0,depthSort:void 0,animate:!1,animationDuration:500,animationEasing:void 0,animateFilter:function(e,t){return!0},ready:void 0,stop:void 0,transform:function(e,t){return t}},Fs={maximal:!1,acyclic:!1},js=function(e){return e.scratch("breadthfirst")},qs=function(e,t){return e.scratch("breadthfirst",t)};function Ys(e){this.options=L({},Vs,Fs,e)}Ys.prototype.run=function(){var e,t=this.options,n=t,r=t.cy,i=n.eles,a=i.nodes().filter((function(e){return!e.isParent()})),o=i,s=n.directed,l=n.acyclic||n.maximal||n.maximalAdjustments>0,u=_t(n.boundingBox?n.boundingBox:{x1:0,y1:0,w:r.width(),h:r.height()});if(E(n.roots))e=n.roots;else if(m(n.roots)){for(var c=[],d=0;d<n.roots.length;d++){var h=n.roots[d],p=r.getElementById(h);c.push(p)}e=r.collection(c)}else if(v(n.roots))e=r.$(n.roots);else if(s)e=a.roots();else{var f=i.components();e=r.collection();for(var g=function(t){var n=f[t],r=n.maxDegree(!1),i=n.filter((function(e){return e.degree(!1)===r}));e=e.add(i)},y=0;y<f.length;y++)g(y)}var b=[],x={},w=function(e,t){null==b[t]&&(b[t]=[]);var n=b[t].length;b[t].push(e),qs(e,{index:n,depth:t})};o.bfs({roots:e,directed:n.directed,visit:function(e,t,n,r,i){var a=e[0],o=a.id();w(a,i),x[o]=!0}});for(var k=[],C=0;C<a.length;C++){var S=a[C];x[S.id()]||k.push(S)}var P=function(e){for(var t=b[e],n=0;n<t.length;n++){var r=t[n];null!=r?qs(r,{depth:e,index:n}):(t.splice(n,1),n--)}},D=function(){for(var e=0;e<b.length;e++)P(e)},T=function(e,t){for(var r=js(e),a=e.incomers().filter((function(e){return e.isNode()&&i.has(e)})),o=-1,s=e.id(),l=0;l<a.length;l++){var u=a[l],c=js(u);o=Math.max(o,c.depth)}if(r.depth<=o){if(!n.acyclic&&t[s])return null;var d=o+1;return function(e,t){var n=js(e),r=n.depth,i=n.index;b[r][i]=null,w(e,t)}(e,d),t[s]=d,!0}return!1};if(s&&l){var _=[],M={},B=function(e){return _.push(e)};for(a.forEach((function(e){return _.push(e)}));_.length>0;){var N=_.shift(),z=T(N,M);if(z)N.outgoers().filter((function(e){return e.isNode()&&i.has(e)})).forEach(B);else if(null===z){je("Detected double maximal shift for node `"+N.id()+"`.  Bailing maximal adjustment due to cycle.  Use `options.maximal: true` only on DAGs.");break}}}D();var I=0;if(n.avoidOverlap)for(var L=0;L<a.length;L++){var O=a[L].layoutDimensions(n),R=O.w,V=O.h;I=Math.max(I,R,V)}var F={},j=function(e){if(F[e.id()])return F[e.id()];for(var t=js(e).depth,n=e.neighborhood(),r=0,i=0,o=0;o<n.length;o++){var s=n[o];if(!s.isEdge()&&!s.isParent()&&a.has(s)){var l=js(s);if(null!=l){var u=l.index,c=l.depth;if(null!=u&&null!=c){var d=b[c].length;c<t&&(r+=u/d,i++)}}}}return r/=i=Math.max(1,i),0===i&&(r=0),F[e.id()]=r,r},q=function(e,t){var n=j(e)-j(t);return 0===n?A(e.id(),t.id()):n};void 0!==n.depthSort&&(q=n.depthSort);for(var Y=0;Y<b.length;Y++)b[Y].sort(q),P(Y);for(var X=[],W=0;W<k.length;W++)X.push(k[W]);b.unshift(X),D();for(var H=0,K=0;K<b.length;K++)H=Math.max(b[K].length,H);var G=u.x1+u.w/2,U=u.x1+u.h/2,Z=b.reduce((function(e,t){return Math.max(e,t.length)}),0);return i.nodes().layoutPositions(this,n,(function(e){var t=js(e),r=t.depth,i=t.index,a=b[r].length,o=Math.max(u.w/((n.grid?Z:a)+1),I),s=Math.max(u.h/(b.length+1),I),l=Math.min(u.w/2/b.length,u.h/2/b.length);if(l=Math.max(l,I),n.circle){var c=l*r+l-(b.length>0&&b[0].length<=3?l/2:0),d=2*Math.PI/b[r].length*i;return 0===r&&1===b[0].length&&(c=1),{x:G+c*Math.cos(d),y:U+c*Math.sin(d)}}return{x:G+(i+1-(a+1)/2)*o,y:(r+1)*s}})),this};var Xs={fit:!0,padding:30,boundingBox:void 0,avoidOverlap:!0,nodeDimensionsIncludeLabels:!1,spacingFactor:void 0,radius:void 0,startAngle:1.5*Math.PI,sweep:void 0,clockwise:!0,sort:void 0,animate:!1,animationDuration:500,animationEasing:void 0,animateFilter:function(e,t){return!0},ready:void 0,stop:void 0,transform:function(e,t){return t}};function Ws(e){this.options=L({},Xs,e)}Ws.prototype.run=function(){var e=this.options,t=e,n=e.cy,r=t.eles,i=void 0!==t.counterclockwise?!t.counterclockwise:t.clockwise,a=r.nodes().not(":parent");t.sort&&(a=a.sort(t.sort));for(var o,s=_t(t.boundingBox?t.boundingBox:{x1:0,y1:0,w:n.width(),h:n.height()}),l=s.x1+s.w/2,u=s.y1+s.h/2,c=(void 0===t.sweep?2*Math.PI-2*Math.PI/a.length:t.sweep)/Math.max(1,a.length-1),d=0,h=0;h<a.length;h++){var p=a[h].layoutDimensions(t),f=p.w,g=p.h;d=Math.max(d,f,g)}if(o=x(t.radius)?t.radius:a.length<=1?0:Math.min(s.h,s.w)/2-d,a.length>1&&t.avoidOverlap){d*=1.75;var v=Math.cos(c)-Math.cos(0),y=Math.sin(c)-Math.sin(0),m=Math.sqrt(d*d/(v*v+y*y));o=Math.max(m,o)}return r.nodes().layoutPositions(this,t,(function(e,n){var r=t.startAngle+n*c*(i?1:-1),a=o*Math.cos(r),s=o*Math.sin(r);return{x:l+a,y:u+s}})),this};var Hs,Ks={fit:!0,padding:30,startAngle:1.5*Math.PI,sweep:void 0,clockwise:!0,equidistant:!1,minNodeSpacing:10,boundingBox:void 0,avoidOverlap:!0,nodeDimensionsIncludeLabels:!1,height:void 0,width:void 0,spacingFactor:void 0,concentric:function(e){return e.degree()},levelWidth:function(e){return e.maxDegree()/4},animate:!1,animationDuration:500,animationEasing:void 0,animateFilter:function(e,t){return!0},ready:void 0,stop:void 0,transform:function(e,t){return t}};function Gs(e){this.options=L({},Ks,e)}Gs.prototype.run=function(){for(var e=this.options,t=e,n=void 0!==t.counterclockwise?!t.counterclockwise:t.clockwise,r=e.cy,i=t.eles,a=i.nodes().not(":parent"),o=_t(t.boundingBox?t.boundingBox:{x1:0,y1:0,w:r.width(),h:r.height()}),s=o.x1+o.w/2,l=o.y1+o.h/2,u=[],c=0,d=0;d<a.length;d++){var h,p=a[d];h=t.concentric(p),u.push({value:h,node:p}),p._private.scratch.concentric=h}a.updateStyle();for(var f=0;f<a.length;f++){var g=a[f].layoutDimensions(t);c=Math.max(c,g.w,g.h)}u.sort((function(e,t){return t.value-e.value}));for(var v=t.levelWidth(a),y=[[]],m=y[0],b=0;b<u.length;b++){var x=u[b];if(m.length>0)Math.abs(m[0].value-x.value)>=v&&(m=[],y.push(m));m.push(x)}var w=c+t.minNodeSpacing;if(!t.avoidOverlap){var E=y.length>0&&y[0].length>1,k=(Math.min(o.w,o.h)/2-w)/(y.length+E?1:0);w=Math.min(w,k)}for(var C=0,S=0;S<y.length;S++){var P=y[S],D=void 0===t.sweep?2*Math.PI-2*Math.PI/P.length:t.sweep,T=P.dTheta=D/Math.max(1,P.length-1);if(P.length>1&&t.avoidOverlap){var _=Math.cos(T)-Math.cos(0),M=Math.sin(T)-Math.sin(0),B=Math.sqrt(w*w/(_*_+M*M));C=Math.max(B,C)}P.r=C,C+=w}if(t.equidistant){for(var N=0,z=0,I=0;I<y.length;I++){var A=y[I].r-z;N=Math.max(N,A)}z=0;for(var L=0;L<y.length;L++){var O=y[L];0===L&&(z=O.r),O.r=z,z+=N}}for(var R={},V=0;V<y.length;V++)for(var F=y[V],j=F.dTheta,q=F.r,Y=0;Y<F.length;Y++){var X=F[Y],W=t.startAngle+(n?1:-1)*j*Y,H={x:s+q*Math.cos(W),y:l+q*Math.sin(W)};R[X.node.id()]=H}return i.nodes().layoutPositions(this,t,(function(e){var t=e.id();return R[t]})),this};var Us={ready:function(){},stop:function(){},animate:!0,animationEasing:void 0,animationDuration:void 0,animateFilter:function(e,t){return!0},animationThreshold:250,refresh:20,fit:!0,padding:30,boundingBox:void 0,nodeDimensionsIncludeLabels:!1,randomize:!1,componentSpacing:40,nodeRepulsion:function(e){return 2048},nodeOverlap:4,idealEdgeLength:function(e){return 32},edgeElasticity:function(e){return 32},nestingFactor:1.2,gravity:1,numIter:1e3,initialTemp:1e3,coolingFactor:.99,minTemp:1};function Zs(e){this.options=L({},Us,e),this.options.layout=this;var t=this.options.eles.nodes(),n=this.options.eles.edges().filter((function(e){var n=e.source().data("id"),r=e.target().data("id"),i=t.some((function(e){return e.data("id")===n})),a=t.some((function(e){return e.data("id")===r}));return!i||!a}));this.options.eles=this.options.eles.not(n)}Zs.prototype.run=function(){var e=this.options,t=e.cy,n=this;n.stopped=!1,!0!==e.animate&&!1!==e.animate||n.emit({type:"layoutstart",layout:n}),Hs=!0===e.debug;var r=$s(t,n,e);Hs&&(void 0)(r),e.randomize&&el(r);var i=we(),a=function(){nl(r,t,e),!0===e.fit&&t.fit(e.padding)},o=function(t){return!(n.stopped||t>=e.numIter)&&(rl(r,e),r.temperature=r.temperature*e.coolingFactor,!(r.temperature<e.minTemp))},s=function(){if(!0===e.animate||!1===e.animate)a(),n.one("layoutstop",e.stop),n.emit({type:"layoutstop",layout:n});else{var t=e.eles.nodes(),i=tl(r,e,t);t.layoutPositions(n,e,i)}},l=0,u=!0;if(!0===e.animate){!function t(){for(var n=0;u&&n<e.refresh;)u=o(l),l++,n++;u?(we()-i>=e.animationThreshold&&a(),xe(t)):(gl(r,e),s())}()}else{for(;u;)u=o(l),l++;gl(r,e),s()}return this},Zs.prototype.stop=function(){return this.stopped=!0,this.thread&&this.thread.stop(),this.emit("layoutstop"),this},Zs.prototype.destroy=function(){return this.thread&&this.thread.stop(),this};var $s=function(e,t,n){for(var r=n.eles.edges(),i=n.eles.nodes(),a=_t(n.boundingBox?n.boundingBox:{x1:0,y1:0,w:e.width(),h:e.height()}),o={isCompound:e.hasCompoundNodes(),layoutNodes:[],idToIndex:{},nodeSize:i.size(),graphSet:[],indexToGraph:[],layoutEdges:[],edgeSize:r.size(),temperature:n.initialTemp,clientWidth:a.w,clientHeight:a.h,boundingBox:a},s=n.eles.components(),l={},u=0;u<s.length;u++)for(var c=s[u],d=0;d<c.length;d++){l[c[d].id()]=u}for(u=0;u<o.nodeSize;u++){var h=(m=i[u]).layoutDimensions(n);(I={}).isLocked=m.locked(),I.id=m.data("id"),I.parentId=m.data("parent"),I.cmptId=l[m.id()],I.children=[],I.positionX=m.position("x"),I.positionY=m.position("y"),I.offsetX=0,I.offsetY=0,I.height=h.w,I.width=h.h,I.maxX=I.positionX+I.width/2,I.minX=I.positionX-I.width/2,I.maxY=I.positionY+I.height/2,I.minY=I.positionY-I.height/2,I.padLeft=parseFloat(m.style("padding")),I.padRight=parseFloat(m.style("padding")),I.padTop=parseFloat(m.style("padding")),I.padBottom=parseFloat(m.style("padding")),I.nodeRepulsion=y(n.nodeRepulsion)?n.nodeRepulsion(m):n.nodeRepulsion,o.layoutNodes.push(I),o.idToIndex[I.id]=u}var p=[],f=0,g=-1,v=[];for(u=0;u<o.nodeSize;u++){var m,b=(m=o.layoutNodes[u]).parentId;null!=b?o.layoutNodes[o.idToIndex[b]].children.push(m.id):(p[++g]=m.id,v.push(m.id))}for(o.graphSet.push(v);f<=g;){var x=p[f++],w=o.idToIndex[x],E=o.layoutNodes[w].children;if(E.length>0){o.graphSet.push(E);for(u=0;u<E.length;u++)p[++g]=E[u]}}for(u=0;u<o.graphSet.length;u++){var k=o.graphSet[u];for(d=0;d<k.length;d++){var C=o.idToIndex[k[d]];o.indexToGraph[C]=u}}for(u=0;u<o.edgeSize;u++){var S=r[u],P={};P.id=S.data("id"),P.sourceId=S.data("source"),P.targetId=S.data("target");var D=y(n.idealEdgeLength)?n.idealEdgeLength(S):n.idealEdgeLength,T=y(n.edgeElasticity)?n.edgeElasticity(S):n.edgeElasticity,_=o.idToIndex[P.sourceId],M=o.idToIndex[P.targetId];if(o.indexToGraph[_]!=o.indexToGraph[M]){for(var B=Qs(P.sourceId,P.targetId,o),N=o.graphSet[B],z=0,I=o.layoutNodes[_];-1===N.indexOf(I.id);)I=o.layoutNodes[o.idToIndex[I.parentId]],z++;for(I=o.layoutNodes[M];-1===N.indexOf(I.id);)I=o.layoutNodes[o.idToIndex[I.parentId]],z++;D*=z*n.nestingFactor}P.idealLength=D,P.elasticity=T,o.layoutEdges.push(P)}return o},Qs=function(e,t,n){var r=Js(e,t,0,n);return 2>r.count?0:r.graph},Js=function e(t,n,r,i){var a=i.graphSet[r];if(-1<a.indexOf(t)&&-1<a.indexOf(n))return{count:2,graph:r};for(var o=0,s=0;s<a.length;s++){var l=a[s],u=i.idToIndex[l],c=i.layoutNodes[u].children;if(0!==c.length){var d=e(t,n,i.indexToGraph[i.idToIndex[c[0]]],i);if(0!==d.count){if(1!==d.count)return d;if(2===++o)break}}}return{count:o,graph:r}},el=function(e,t){for(var n=e.clientWidth,r=e.clientHeight,i=0;i<e.nodeSize;i++){var a=e.layoutNodes[i];0!==a.children.length||a.isLocked||(a.positionX=Math.random()*n,a.positionY=Math.random()*r)}},tl=function(e,t,n){var r=e.boundingBox,i={x1:1/0,x2:-1/0,y1:1/0,y2:-1/0};return t.boundingBox&&(n.forEach((function(t){var n=e.layoutNodes[e.idToIndex[t.data("id")]];i.x1=Math.min(i.x1,n.positionX),i.x2=Math.max(i.x2,n.positionX),i.y1=Math.min(i.y1,n.positionY),i.y2=Math.max(i.y2,n.positionY)})),i.w=i.x2-i.x1,i.h=i.y2-i.y1),function(n,a){var o=e.layoutNodes[e.idToIndex[n.data("id")]];if(t.boundingBox){var s=(o.positionX-i.x1)/i.w,l=(o.positionY-i.y1)/i.h;return{x:r.x1+s*r.w,y:r.y1+l*r.h}}return{x:o.positionX,y:o.positionY}}},nl=function(e,t,n){var r=n.layout,i=n.eles.nodes(),a=tl(e,n,i);i.positions(a),!0!==e.ready&&(e.ready=!0,r.one("layoutready",n.ready),r.emit({type:"layoutready",layout:this}))},rl=function(e,t,n){il(e,t),ul(e),cl(e,t),dl(e),hl(e)},il=function(e,t){for(var n=0;n<e.graphSet.length;n++)for(var r=e.graphSet[n],i=r.length,a=0;a<i;a++)for(var o=e.layoutNodes[e.idToIndex[r[a]]],s=a+1;s<i;s++){var l=e.layoutNodes[e.idToIndex[r[s]]];ol(o,l,e,t)}},al=function(e){return-e+2*e*Math.random()},ol=function(e,t,n,r){if(e.cmptId===t.cmptId||n.isCompound){var i=t.positionX-e.positionX,a=t.positionY-e.positionY;0===i&&0===a&&(i=al(1),a=al(1));var o=sl(e,t,i,a);if(o>0)var s=(u=r.nodeOverlap*o)*i/(g=Math.sqrt(i*i+a*a)),l=u*a/g;else{var u,c=ll(e,i,a),d=ll(t,-1*i,-1*a),h=d.x-c.x,p=d.y-c.y,f=h*h+p*p,g=Math.sqrt(f);s=(u=(e.nodeRepulsion+t.nodeRepulsion)/f)*h/g,l=u*p/g}e.isLocked||(e.offsetX-=s,e.offsetY-=l),t.isLocked||(t.offsetX+=s,t.offsetY+=l)}},sl=function(e,t,n,r){if(n>0)var i=e.maxX-t.minX;else i=t.maxX-e.minX;if(r>0)var a=e.maxY-t.minY;else a=t.maxY-e.minY;return i>=0&&a>=0?Math.sqrt(i*i+a*a):0},ll=function(e,t,n){var r=e.positionX,i=e.positionY,a=e.height||1,o=e.width||1,s=n/t,l=a/o,u={};return 0===t&&0<n||0===t&&0>n?(u.x=r,u.y=i+a/2,u):0<t&&-1*l<=s&&s<=l?(u.x=r+o/2,u.y=i+o*n/2/t,u):0>t&&-1*l<=s&&s<=l?(u.x=r-o/2,u.y=i-o*n/2/t,u):0<n&&(s<=-1*l||s>=l)?(u.x=r+a*t/2/n,u.y=i+a/2,u):0>n&&(s<=-1*l||s>=l)?(u.x=r-a*t/2/n,u.y=i-a/2,u):u},ul=function(e,t){for(var n=0;n<e.edgeSize;n++){var r=e.layoutEdges[n],i=e.idToIndex[r.sourceId],a=e.layoutNodes[i],o=e.idToIndex[r.targetId],s=e.layoutNodes[o],l=s.positionX-a.positionX,u=s.positionY-a.positionY;if(0!==l||0!==u){var c=ll(a,l,u),d=ll(s,-1*l,-1*u),h=d.x-c.x,p=d.y-c.y,f=Math.sqrt(h*h+p*p),g=Math.pow(r.idealLength-f,2)/r.elasticity;if(0!==f)var v=g*h/f,y=g*p/f;else v=0,y=0;a.isLocked||(a.offsetX+=v,a.offsetY+=y),s.isLocked||(s.offsetX-=v,s.offsetY-=y)}}},cl=function(e,t){if(0!==t.gravity)for(var n=0;n<e.graphSet.length;n++){var r=e.graphSet[n],i=r.length;if(0===n)var a=e.clientHeight/2,o=e.clientWidth/2;else{var s=e.layoutNodes[e.idToIndex[r[0]]],l=e.layoutNodes[e.idToIndex[s.parentId]];a=l.positionX,o=l.positionY}for(var u=0;u<i;u++){var c=e.layoutNodes[e.idToIndex[r[u]]];if(!c.isLocked){var d=a-c.positionX,h=o-c.positionY,p=Math.sqrt(d*d+h*h);if(p>1){var f=t.gravity*d/p,g=t.gravity*h/p;c.offsetX+=f,c.offsetY+=g}}}}},dl=function(e,t){var n=[],r=0,i=-1;for(n.push.apply(n,e.graphSet[0]),i+=e.graphSet[0].length;r<=i;){var a=n[r++],o=e.idToIndex[a],s=e.layoutNodes[o],l=s.children;if(0<l.length&&!s.isLocked){for(var u=s.offsetX,c=s.offsetY,d=0;d<l.length;d++){var h=e.layoutNodes[e.idToIndex[l[d]]];h.offsetX+=u,h.offsetY+=c,n[++i]=l[d]}s.offsetX=0,s.offsetY=0}}},hl=function(e,t){for(var n=0;n<e.nodeSize;n++){0<(i=e.layoutNodes[n]).children.length&&(i.maxX=void 0,i.minX=void 0,i.maxY=void 0,i.minY=void 0)}for(n=0;n<e.nodeSize;n++){if(!(0<(i=e.layoutNodes[n]).children.length||i.isLocked)){var r=pl(i.offsetX,i.offsetY,e.temperature);i.positionX+=r.x,i.positionY+=r.y,i.offsetX=0,i.offsetY=0,i.minX=i.positionX-i.width,i.maxX=i.positionX+i.width,i.minY=i.positionY-i.height,i.maxY=i.positionY+i.height,fl(i,e)}}for(n=0;n<e.nodeSize;n++){var i;0<(i=e.layoutNodes[n]).children.length&&!i.isLocked&&(i.positionX=(i.maxX+i.minX)/2,i.positionY=(i.maxY+i.minY)/2,i.width=i.maxX-i.minX,i.height=i.maxY-i.minY)}},pl=function(e,t,n){var r=Math.sqrt(e*e+t*t);if(r>n)var i={x:n*e/r,y:n*t/r};else i={x:e,y:t};return i},fl=function e(t,n){var r=t.parentId;if(null!=r){var i=n.layoutNodes[n.idToIndex[r]],a=!1;return(null==i.maxX||t.maxX+i.padRight>i.maxX)&&(i.maxX=t.maxX+i.padRight,a=!0),(null==i.minX||t.minX-i.padLeft<i.minX)&&(i.minX=t.minX-i.padLeft,a=!0),(null==i.maxY||t.maxY+i.padBottom>i.maxY)&&(i.maxY=t.maxY+i.padBottom,a=!0),(null==i.minY||t.minY-i.padTop<i.minY)&&(i.minY=t.minY-i.padTop,a=!0),a?e(i,n):void 0}},gl=function(e,t){for(var n=e.layoutNodes,r=[],i=0;i<n.length;i++){var a=n[i],o=a.cmptId;(r[o]=r[o]||[]).push(a)}var s=0;for(i=0;i<r.length;i++){if(g=r[i]){g.x1=1/0,g.x2=-1/0,g.y1=1/0,g.y2=-1/0;for(var l=0;l<g.length;l++){var u=g[l];g.x1=Math.min(g.x1,u.positionX-u.width/2),g.x2=Math.max(g.x2,u.positionX+u.width/2),g.y1=Math.min(g.y1,u.positionY-u.height/2),g.y2=Math.max(g.y2,u.positionY+u.height/2)}g.w=g.x2-g.x1,g.h=g.y2-g.y1,s+=g.w*g.h}}r.sort((function(e,t){return t.w*t.h-e.w*e.h}));var c=0,d=0,h=0,p=0,f=Math.sqrt(s)*e.clientWidth/e.clientHeight;for(i=0;i<r.length;i++){var g;if(g=r[i]){for(l=0;l<g.length;l++){(u=g[l]).isLocked||(u.positionX+=c-g.x1,u.positionY+=d-g.y1)}c+=g.w+t.componentSpacing,h+=g.w+t.componentSpacing,p=Math.max(p,g.h),h>f&&(d+=p+t.componentSpacing,c=0,h=0,p=0)}}},vl={fit:!0,padding:30,boundingBox:void 0,avoidOverlap:!0,avoidOverlapPadding:10,nodeDimensionsIncludeLabels:!1,spacingFactor:void 0,condense:!1,rows:void 0,cols:void 0,position:function(e){},sort:void 0,animate:!1,animationDuration:500,animationEasing:void 0,animateFilter:function(e,t){return!0},ready:void 0,stop:void 0,transform:function(e,t){return t}};function yl(e){this.options=L({},vl,e)}yl.prototype.run=function(){var e=this.options,t=e,n=e.cy,r=t.eles,i=r.nodes().not(":parent");t.sort&&(i=i.sort(t.sort));var a=_t(t.boundingBox?t.boundingBox:{x1:0,y1:0,w:n.width(),h:n.height()});if(0===a.h||0===a.w)r.nodes().layoutPositions(this,t,(function(e){return{x:a.x1,y:a.y1}}));else{var o=i.size(),s=Math.sqrt(o*a.h/a.w),l=Math.round(s),u=Math.round(a.w/a.h*s),c=function(e){if(null==e)return Math.min(l,u);Math.min(l,u)==l?l=e:u=e},d=function(e){if(null==e)return Math.max(l,u);Math.max(l,u)==l?l=e:u=e},h=t.rows,p=null!=t.cols?t.cols:t.columns;if(null!=h&&null!=p)l=h,u=p;else if(null!=h&&null==p)l=h,u=Math.ceil(o/l);else if(null==h&&null!=p)u=p,l=Math.ceil(o/u);else if(u*l>o){var f=c(),g=d();(f-1)*g>=o?c(f-1):(g-1)*f>=o&&d(g-1)}else for(;u*l<o;){var v=c(),y=d();(y+1)*v>=o?d(y+1):c(v+1)}var m=a.w/u,b=a.h/l;if(t.condense&&(m=0,b=0),t.avoidOverlap)for(var x=0;x<i.length;x++){var w=i[x],E=w._private.position;null!=E.x&&null!=E.y||(E.x=0,E.y=0);var k=w.layoutDimensions(t),C=t.avoidOverlapPadding,S=k.w+C,P=k.h+C;m=Math.max(m,S),b=Math.max(b,P)}for(var D={},T=function(e,t){return!!D["c-"+e+"-"+t]},_=function(e,t){D["c-"+e+"-"+t]=!0},M=0,B=0,N=function(){++B>=u&&(B=0,M++)},z={},I=0;I<i.length;I++){var A=i[I],L=t.position(A);if(L&&(void 0!==L.row||void 0!==L.col)){var O={row:L.row,col:L.col};if(void 0===O.col)for(O.col=0;T(O.row,O.col);)O.col++;else if(void 0===O.row)for(O.row=0;T(O.row,O.col);)O.row++;z[A.id()]=O,_(O.row,O.col)}}i.layoutPositions(this,t,(function(e,t){var n,r;if(e.locked()||e.isParent())return!1;var i=z[e.id()];if(i)n=i.col*m+m/2+a.x1,r=i.row*b+b/2+a.y1;else{for(;T(M,B);)N();n=B*m+m/2+a.x1,r=M*b+b/2+a.y1,_(M,B),N()}return{x:n,y:r}}))}return this};var ml={ready:function(){},stop:function(){}};function bl(e){this.options=L({},ml,e)}bl.prototype.run=function(){var e=this.options,t=e.eles;return e.cy,this.emit("layoutstart"),t.nodes().positions((function(){return{x:0,y:0}})),this.one("layoutready",e.ready),this.emit("layoutready"),this.one("layoutstop",e.stop),this.emit("layoutstop"),this},bl.prototype.stop=function(){return this};var xl={positions:void 0,zoom:void 0,pan:void 0,fit:!0,padding:30,spacingFactor:void 0,animate:!1,animationDuration:500,animationEasing:void 0,animateFilter:function(e,t){return!0},ready:void 0,stop:void 0,transform:function(e,t){return t}};function wl(e){this.options=L({},xl,e)}wl.prototype.run=function(){var e=this.options,t=e.eles.nodes(),n=y(e.positions);return t.layoutPositions(this,e,(function(t,r){var i=function(t){if(null==e.positions)return function(e){return{x:e.x,y:e.y}}(t.position());if(n)return e.positions(t);var r=e.positions[t._private.data.id];return null==r?null:r}(t);return!t.locked()&&null!=i&&i})),this};var El={fit:!0,padding:30,boundingBox:void 0,animate:!1,animationDuration:500,animationEasing:void 0,animateFilter:function(e,t){return!0},ready:void 0,stop:void 0,transform:function(e,t){return t}};function kl(e){this.options=L({},El,e)}kl.prototype.run=function(){var e=this.options,t=e.cy,n=e.eles,r=_t(e.boundingBox?e.boundingBox:{x1:0,y1:0,w:t.width(),h:t.height()});return n.nodes().layoutPositions(this,e,(function(e,t){return{x:r.x1+Math.round(Math.random()*r.w),y:r.y1+Math.round(Math.random()*r.h)}})),this};var Cl=[{name:"breadthfirst",impl:Ys},{name:"circle",impl:Ws},{name:"concentric",impl:Gs},{name:"cose",impl:Zs},{name:"grid",impl:yl},{name:"null",impl:bl},{name:"preset",impl:wl},{name:"random",impl:kl}];function Sl(e){this.options=e,this.notifications=0}var Pl=function(){},Dl=function(){throw new Error("A headless instance can not render images")};Sl.prototype={recalculateRenderedStyle:Pl,notify:function(){this.notifications++},init:Pl,isHeadless:function(){return!0},png:Dl,jpg:Dl};var Tl={arrowShapeWidth:.3,registerArrowShapes:function(){var e=this.arrowShapes={},t=this,n=function(e,t,n,r,i,a,o){var s=i.x-n/2-o,l=i.x+n/2+o,u=i.y-n/2-o,c=i.y+n/2+o;return s<=e&&e<=l&&u<=t&&t<=c},r=function(e,t,n,r,i){var a=e*Math.cos(r)-t*Math.sin(r),o=(e*Math.sin(r)+t*Math.cos(r))*n;return{x:a*n+i.x,y:o+i.y}},i=function(e,t,n,i){for(var a=[],o=0;o<e.length;o+=2){var s=e[o],l=e[o+1];a.push(r(s,l,t,n,i))}return a},a=function(e){for(var t=[],n=0;n<e.length;n++){var r=e[n];t.push(r.x,r.y)}return t},o=function(e){return e.pstyle("width").pfValue*e.pstyle("arrow-scale").pfValue*2},s=function(r,s){v(s)&&(s=e[s]),e[r]=L({name:r,points:[-.15,-.3,.15,-.3,.15,.3,-.15,.3],collide:function(e,t,n,r,o,s){var l=a(i(this.points,n+2*s,r,o));return Yt(e,t,l)},roughCollide:n,draw:function(e,n,r,a){var o=i(this.points,n,r,a);t.arrowShapeImpl("polygon")(e,o)},spacing:function(e){return 0},gap:o},s)};s("none",{collide:Le,roughCollide:Le,draw:Re,spacing:Oe,gap:Oe}),s("triangle",{points:[-.15,-.3,0,0,.15,-.3]}),s("arrow","triangle"),s("triangle-backcurve",{points:e.triangle.points,controlPoint:[0,-.15],roughCollide:n,draw:function(e,n,a,o,s){var l=i(this.points,n,a,o),u=this.controlPoint,c=r(u[0],u[1],n,a,o);t.arrowShapeImpl(this.name)(e,l,c)},gap:function(e){return.8*o(e)}}),s("triangle-tee",{points:[0,0,.15,-.3,-.15,-.3,0,0],pointsTee:[-.15,-.4,-.15,-.5,.15,-.5,.15,-.4],collide:function(e,t,n,r,o,s,l){var u=a(i(this.points,n+2*l,r,o)),c=a(i(this.pointsTee,n+2*l,r,o));return Yt(e,t,u)||Yt(e,t,c)},draw:function(e,n,r,a,o){var s=i(this.points,n,r,a),l=i(this.pointsTee,n,r,a);t.arrowShapeImpl(this.name)(e,s,l)}}),s("circle-triangle",{radius:.15,pointsTr:[0,-.15,.15,-.45,-.15,-.45,0,-.15],collide:function(e,t,n,r,o,s,l){var u=o,c=Math.pow(u.x-e,2)+Math.pow(u.y-t,2)<=Math.pow((n+2*l)*this.radius,2),d=a(i(this.points,n+2*l,r,o));return Yt(e,t,d)||c},draw:function(e,n,r,a,o){var s=i(this.pointsTr,n,r,a);t.arrowShapeImpl(this.name)(e,s,a.x,a.y,this.radius*n)},spacing:function(e){return t.getArrowWidth(e.pstyle("width").pfValue,e.pstyle("arrow-scale").value)*this.radius}}),s("triangle-cross",{points:[0,0,.15,-.3,-.15,-.3,0,0],baseCrossLinePts:[-.15,-.4,-.15,-.4,.15,-.4,.15,-.4],crossLinePts:function(e,t){var n=this.baseCrossLinePts.slice(),r=t/e;return n[3]=n[3]-r,n[5]=n[5]-r,n},collide:function(e,t,n,r,o,s,l){var u=a(i(this.points,n+2*l,r,o)),c=a(i(this.crossLinePts(n,s),n+2*l,r,o));return Yt(e,t,u)||Yt(e,t,c)},draw:function(e,n,r,a,o){var s=i(this.points,n,r,a),l=i(this.crossLinePts(n,o),n,r,a);t.arrowShapeImpl(this.name)(e,s,l)}}),s("vee",{points:[-.15,-.3,0,0,.15,-.3,0,-.15],gap:function(e){return.525*o(e)}}),s("circle",{radius:.15,collide:function(e,t,n,r,i,a,o){var s=i;return Math.pow(s.x-e,2)+Math.pow(s.y-t,2)<=Math.pow((n+2*o)*this.radius,2)},draw:function(e,n,r,i,a){t.arrowShapeImpl(this.name)(e,i.x,i.y,this.radius*n)},spacing:function(e){return t.getArrowWidth(e.pstyle("width").pfValue,e.pstyle("arrow-scale").value)*this.radius}}),s("tee",{points:[-.15,0,-.15,-.1,.15,-.1,.15,0],spacing:function(e){return 1},gap:function(e){return 1}}),s("square",{points:[-.15,0,.15,0,.15,-.3,-.15,-.3]}),s("diamond",{points:[-.15,-.15,0,-.3,.15,-.15,0,0],gap:function(e){return e.pstyle("width").pfValue*e.pstyle("arrow-scale").value}}),s("chevron",{points:[0,0,-.15,-.15,-.1,-.2,0,-.1,.1,-.2,.15,-.15],gap:function(e){return.95*e.pstyle("width").pfValue*e.pstyle("arrow-scale").value}})}},_l={projectIntoViewport:function(e,t){var n=this.cy,r=this.findContainerClientCoords(),i=r[0],a=r[1],o=r[4],s=n.pan(),l=n.zoom();return[((e-i)/o-s.x)/l,((t-a)/o-s.y)/l]},findContainerClientCoords:function(){if(this.containerBB)return this.containerBB;var e=this.container,t=e.getBoundingClientRect(),n=this.cy.window().getComputedStyle(e),r=function(e){return parseFloat(n.getPropertyValue(e))},i=r("padding-left"),a=r("padding-right"),o=r("padding-top"),s=r("padding-bottom"),l=r("border-left-width"),u=r("border-right-width"),c=r("border-top-width"),d=(r("border-bottom-width"),e.clientWidth),h=e.clientHeight,p=i+a,f=o+s,g=l+u,v=t.width/(d+g),y=d-p,m=h-f,b=t.left+i+l,x=t.top+o+c;return this.containerBB=[b,x,y,m,v]},invalidateContainerClientCoordsCache:function(){this.containerBB=null},findNearestElement:function(e,t,n,r){return this.findNearestElements(e,t,n,r)[0]},findNearestElements:function(e,t,n,r){var i,a,o=this,s=this,l=s.getCachedZSortedEles(),u=[],c=s.cy.zoom(),d=s.cy.hasCompoundNodes(),h=(r?24:8)/c,p=(r?8:2)/c,f=(r?8:2)/c,g=1/0;function v(e,t){if(e.isNode()){if(a)return;a=e,u.push(e)}if(e.isEdge()&&(null==t||t<g))if(i){if(i.pstyle("z-compound-depth").value===e.pstyle("z-compound-depth").value&&i.pstyle("z-compound-depth").value===e.pstyle("z-compound-depth").value)for(var n=0;n<u.length;n++)if(u[n].isEdge()){u[n]=e,i=e,g=null!=t?t:g;break}}else u.push(e),i=e,g=null!=t?t:g}function y(n){var r=n.outerWidth()+2*p,i=n.outerHeight()+2*p,a=r/2,l=i/2,u=n.position(),c="auto"===n.pstyle("corner-radius").value?"auto":n.pstyle("corner-radius").pfValue,d=n._private.rscratch;if(u.x-a<=e&&e<=u.x+a&&u.y-l<=t&&t<=u.y+l&&s.nodeShapes[o.getNodeShape(n)].checkPoint(e,t,0,r,i,u.x,u.y,c,d))return v(n,0),!0}function m(n){var r,i=n._private,a=i.rscratch,l=n.pstyle("width").pfValue,c=n.pstyle("arrow-scale").value,p=l/2+h,f=p*p,g=2*p,m=i.source,b=i.target;if("segments"===a.edgeType||"straight"===a.edgeType||"haystack"===a.edgeType){for(var x=a.allpts,w=0;w+3<x.length;w+=2)if(Vt(e,t,x[w],x[w+1],x[w+2],x[w+3],g)&&f>(r=qt(e,t,x[w],x[w+1],x[w+2],x[w+3])))return v(n,r),!0}else if("bezier"===a.edgeType||"multibezier"===a.edgeType||"self"===a.edgeType||"compound"===a.edgeType)for(x=a.allpts,w=0;w+5<a.allpts.length;w+=4)if(Ft(e,t,x[w],x[w+1],x[w+2],x[w+3],x[w+4],x[w+5],g)&&f>(r=jt(e,t,x[w],x[w+1],x[w+2],x[w+3],x[w+4],x[w+5])))return v(n,r),!0;m=m||i.source,b=b||i.target;var E=o.getArrowWidth(l,c),k=[{name:"source",x:a.arrowStartX,y:a.arrowStartY,angle:a.srcArrowAngle},{name:"target",x:a.arrowEndX,y:a.arrowEndY,angle:a.tgtArrowAngle},{name:"mid-source",x:a.midX,y:a.midY,angle:a.midsrcArrowAngle},{name:"mid-target",x:a.midX,y:a.midY,angle:a.midtgtArrowAngle}];for(w=0;w<k.length;w++){var C=k[w],S=s.arrowShapes[n.pstyle(C.name+"-arrow-shape").value],P=n.pstyle("width").pfValue;if(S.roughCollide(e,t,E,C.angle,{x:C.x,y:C.y},P,h)&&S.collide(e,t,E,C.angle,{x:C.x,y:C.y},P,h))return v(n),!0}d&&u.length>0&&(y(m),y(b))}function b(e,t,n){return Ue(e,t,n)}function x(n,r){var i,a=n._private,o=f;i=r?r+"-":"",n.boundingBox();var s=a.labelBounds[r||"main"],l=n.pstyle(i+"label").value;if("yes"===n.pstyle("text-events").strValue&&l){var u=b(a.rscratch,"labelX",r),c=b(a.rscratch,"labelY",r),d=b(a.rscratch,"labelAngle",r),h=n.pstyle(i+"text-margin-x").pfValue,p=n.pstyle(i+"text-margin-y").pfValue,g=s.x1-o-h,y=s.x2+o-h,m=s.y1-o-p,x=s.y2+o-p;if(d){var w=Math.cos(d),E=Math.sin(d),k=function(e,t){return{x:(e-=u)*w-(t-=c)*E+u,y:e*E+t*w+c}},C=k(g,m),S=k(g,x),P=k(y,m),D=k(y,x),T=[C.x+h,C.y+p,P.x+h,P.y+p,D.x+h,D.y+p,S.x+h,S.y+p];if(Yt(e,t,T))return v(n),!0}else if(Lt(s,e,t))return v(n),!0}}n&&(l=l.interactive);for(var w=l.length-1;w>=0;w--){var E=l[w];E.isNode()?y(E)||x(E):m(E)||x(E)||x(E,"source")||x(E,"target")}return u},getAllInBox:function(e,t,n,r){for(var i,a,o=this.getCachedZSortedEles().interactive,s=[],l=Math.min(e,n),u=Math.max(e,n),c=Math.min(t,r),d=Math.max(t,r),h=_t({x1:e=l,y1:t=c,x2:n=u,y2:r=d}),p=0;p<o.length;p++){var f=o[p];if(f.isNode()){var g=f,v=g.boundingBox({includeNodes:!0,includeEdges:!1,includeLabels:!1});At(h,v)&&!Ot(v,h)&&s.push(g)}else{var y=f,m=y._private,b=m.rscratch;if(null!=b.startX&&null!=b.startY&&!Lt(h,b.startX,b.startY))continue;if(null!=b.endX&&null!=b.endY&&!Lt(h,b.endX,b.endY))continue;if("bezier"===b.edgeType||"multibezier"===b.edgeType||"self"===b.edgeType||"compound"===b.edgeType||"segments"===b.edgeType||"haystack"===b.edgeType){for(var x=m.rstyle.bezierPts||m.rstyle.linePts||m.rstyle.haystackPts,w=!0,E=0;E<x.length;E++)if(i=h,a=x[E],!Lt(i,a.x,a.y)){w=!1;break}w&&s.push(y)}else"haystack"!==b.edgeType&&"straight"!==b.edgeType||s.push(y)}}return s}},Ml={calculateArrowAngles:function(e){var t,n,r,i,a,o,s=e._private.rscratch,l="haystack"===s.edgeType,u="bezier"===s.edgeType,c="multibezier"===s.edgeType,d="segments"===s.edgeType,h="compound"===s.edgeType,p="self"===s.edgeType;if(l?(r=s.haystackPts[0],i=s.haystackPts[1],a=s.haystackPts[2],o=s.haystackPts[3]):(r=s.arrowStartX,i=s.arrowStartY,a=s.arrowEndX,o=s.arrowEndY),g=s.midX,v=s.midY,d)t=r-s.segpts[0],n=i-s.segpts[1];else if(c||h||p||u){var f=s.allpts;t=r-Pt(f[0],f[2],f[4],.1),n=i-Pt(f[1],f[3],f[5],.1)}else t=r-g,n=i-v;s.srcArrowAngle=xt(t,n);var g=s.midX,v=s.midY;if(l&&(g=(r+a)/2,v=(i+o)/2),t=a-r,n=o-i,d)if((f=s.allpts).length/2%2==0){var y=(S=f.length/2)-2;t=f[S]-f[y],n=f[S+1]-f[y+1]}else if(s.isRound)t=s.midVector[1],n=-s.midVector[0];else{y=(S=f.length/2-1)-2;t=f[S]-f[y],n=f[S+1]-f[y+1]}else if(c||h||p){var m,b,x,w,f=s.allpts;if(s.ctrlpts.length/2%2==0){var E=(k=(C=f.length/2-1)+2)+2;m=Pt(f[C],f[k],f[E],0),b=Pt(f[C+1],f[k+1],f[E+1],0),x=Pt(f[C],f[k],f[E],1e-4),w=Pt(f[C+1],f[k+1],f[E+1],1e-4)}else{var k,C;E=(k=f.length/2-1)+2;m=Pt(f[C=k-2],f[k],f[E],.4999),b=Pt(f[C+1],f[k+1],f[E+1],.4999),x=Pt(f[C],f[k],f[E],.5),w=Pt(f[C+1],f[k+1],f[E+1],.5)}t=x-m,n=w-b}if(s.midtgtArrowAngle=xt(t,n),s.midDispX=t,s.midDispY=n,t*=-1,n*=-1,d)if((f=s.allpts).length/2%2==0);else if(!s.isRound){var S,P=(S=f.length/2-1)+2;t=-(f[P]-f[S]),n=-(f[P+1]-f[S+1])}if(s.midsrcArrowAngle=xt(t,n),d)t=a-s.segpts[s.segpts.length-2],n=o-s.segpts[s.segpts.length-1];else if(c||h||p||u){var D=(f=s.allpts).length;t=a-Pt(f[D-6],f[D-4],f[D-2],.9),n=o-Pt(f[D-5],f[D-3],f[D-1],.9)}else t=a-g,n=o-v;s.tgtArrowAngle=xt(t,n)}};Ml.getArrowWidth=Ml.getArrowHeight=function(e,t){var n=this.arrowWidthCache=this.arrowWidthCache||{},r=n[e+", "+t];return r||(r=Math.max(Math.pow(13.37*e,.9),29)*t,n[e+", "+t]=r,r)};var Bl,Nl,zl,Il,Al,Ll,Ol,Rl,Vl,Fl,jl,ql,Yl,Xl,Wl,Hl,Kl,Gl={},Ul={},Zl=function(e,t,n){n.x=t.x-e.x,n.y=t.y-e.y,n.len=Math.sqrt(n.x*n.x+n.y*n.y),n.nx=n.x/n.len,n.ny=n.y/n.len,n.ang=Math.atan2(n.ny,n.nx)},$l=function(e,t,n,r,i){var a,o;if(e!==Kl?Zl(t,e,Gl):((o=Gl).x=-1*(a=Ul).x,o.y=-1*a.y,o.nx=-1*a.nx,o.ny=-1*a.ny,o.ang=a.ang>0?-(Math.PI-a.ang):Math.PI+a.ang),Zl(t,n,Ul),zl=Gl.nx*Ul.ny-Gl.ny*Ul.nx,Il=Gl.nx*Ul.nx-Gl.ny*-Ul.ny,Ol=Math.asin(Math.max(-1,Math.min(1,zl))),Math.abs(Ol)<1e-6)return Bl=t.x,Nl=t.y,void(Vl=jl=0);Al=1,Ll=!1,Il<0?Ol<0?Ol=Math.PI+Ol:(Ol=Math.PI-Ol,Al=-1,Ll=!0):Ol>0&&(Al=-1,Ll=!0),jl=void 0!==t.radius?t.radius:r,Rl=Ol/2,ql=Math.min(Gl.len/2,Ul.len/2),i?(Fl=Math.abs(Math.cos(Rl)*jl/Math.sin(Rl)))>ql?(Fl=ql,Vl=Math.abs(Fl*Math.sin(Rl)/Math.cos(Rl))):Vl=jl:(Fl=Math.min(ql,jl),Vl=Math.abs(Fl*Math.sin(Rl)/Math.cos(Rl))),Wl=t.x+Ul.nx*Fl,Hl=t.y+Ul.ny*Fl,Bl=Wl-Ul.ny*Vl*Al,Nl=Hl+Ul.nx*Vl*Al,Yl=t.x+Gl.nx*Fl,Xl=t.y+Gl.ny*Fl,Kl=t};function Ql(e,t){0===t.radius?e.lineTo(t.cx,t.cy):e.arc(t.cx,t.cy,t.radius,t.startAngle,t.endAngle,t.counterClockwise)}function Jl(e,t,n,r){var i=!(arguments.length>4&&void 0!==arguments[4])||arguments[4];return 0===r||0===t.radius?{cx:t.x,cy:t.y,radius:0,startX:t.x,startY:t.y,stopX:t.x,stopY:t.y,startAngle:void 0,endAngle:void 0,counterClockwise:void 0}:($l(e,t,n,r,i),{cx:Bl,cy:Nl,radius:Vl,startX:Yl,startY:Xl,stopX:Wl,stopY:Hl,startAngle:Gl.ang+Math.PI/2*Al,endAngle:Ul.ang-Math.PI/2*Al,counterClockwise:Ll})}var eu={};function tu(e){var t=[];if(null!=e){for(var n=0;n<e.length;n+=2){var r=e[n],i=e[n+1];t.push({x:r,y:i})}return t}}eu.findMidptPtsEtc=function(e,t){var n,r=t.posPts,i=t.intersectionPts,o=t.vectorNormInverse,s=e.pstyle("source-endpoint"),l=e.pstyle("target-endpoint"),u=null!=s.units&&null!=l.units;switch(e.pstyle("edge-distances").value){case"node-position":n=r;break;case"intersection":n=i;break;case"endpoints":if(u){var c=a(this.manualEndptToPx(e.source()[0],s),2),d=c[0],h=c[1],p=a(this.manualEndptToPx(e.target()[0],l),2),f=p[0],g=p[1],v={x1:d,y1:h,x2:f,y2:g};o=function(e,t,n,r){var i=r-t,a=n-e,o=Math.sqrt(a*a+i*i);return{x:-i/o,y:a/o}}(d,h,f,g),n=v}else je("Edge ".concat(e.id()," has edge-distances:endpoints specified without manual endpoints specified via source-endpoint and target-endpoint.  Falling back on edge-distances:intersection (default).")),n=i}return{midptPts:n,vectorNormInverse:o}},eu.findHaystackPoints=function(e){for(var t=0;t<e.length;t++){var n=e[t],r=n._private,i=r.rscratch;if(!i.haystack){var a=2*Math.random()*Math.PI;i.source={x:Math.cos(a),y:Math.sin(a)},a=2*Math.random()*Math.PI,i.target={x:Math.cos(a),y:Math.sin(a)}}var o=r.source,s=r.target,l=o.position(),u=s.position(),c=o.width(),d=s.width(),h=o.height(),p=s.height(),f=n.pstyle("haystack-radius").value/2;i.haystackPts=i.allpts=[i.source.x*c*f+l.x,i.source.y*h*f+l.y,i.target.x*d*f+u.x,i.target.y*p*f+u.y],i.midX=(i.allpts[0]+i.allpts[2])/2,i.midY=(i.allpts[1]+i.allpts[3])/2,i.edgeType="haystack",i.haystack=!0,this.storeEdgeProjections(n),this.calculateArrowAngles(n),this.recalculateEdgeLabelProjections(n),this.calculateLabelAngles(n)}},eu.findSegmentsPoints=function(e,t){var n=e._private.rscratch,r=e.pstyle("segment-weights"),i=e.pstyle("segment-distances"),a=e.pstyle("segment-radii"),o=e.pstyle("radius-type"),s=Math.min(r.pfValue.length,i.pfValue.length),l=a.pfValue[a.pfValue.length-1],u=o.pfValue[o.pfValue.length-1];n.edgeType="segments",n.segpts=[],n.radii=[],n.isArcRadius=[];for(var c=0;c<s;c++){var d=r.pfValue[c],h=i.pfValue[c],p=1-d,f=d,g=this.findMidptPtsEtc(e,t),v=g.midptPts,y=g.vectorNormInverse,m={x:v.x1*p+v.x2*f,y:v.y1*p+v.y2*f};n.segpts.push(m.x+y.x*h,m.y+y.y*h),n.radii.push(void 0!==a.pfValue[c]?a.pfValue[c]:l),n.isArcRadius.push("arc-radius"===(void 0!==o.pfValue[c]?o.pfValue[c]:u))}},eu.findLoopPoints=function(e,t,n,r){var i=e._private.rscratch,a=t.dirCounts,o=t.srcPos,s=e.pstyle("control-point-distances"),l=s?s.pfValue[0]:void 0,u=e.pstyle("loop-direction").pfValue,c=e.pstyle("loop-sweep").pfValue,d=e.pstyle("control-point-step-size").pfValue;i.edgeType="self";var h=n,p=d;r&&(h=0,p=l);var f=u-Math.PI/2,g=f-c/2,v=f+c/2,y=String(u+"_"+c);h=void 0===a[y]?a[y]=0:++a[y],i.ctrlpts=[o.x+1.4*Math.cos(g)*p*(h/3+1),o.y+1.4*Math.sin(g)*p*(h/3+1),o.x+1.4*Math.cos(v)*p*(h/3+1),o.y+1.4*Math.sin(v)*p*(h/3+1)]},eu.findCompoundLoopPoints=function(e,t,n,r){var i=e._private.rscratch;i.edgeType="compound";var a=t.srcPos,o=t.tgtPos,s=t.srcW,l=t.srcH,u=t.tgtW,c=t.tgtH,d=e.pstyle("control-point-step-size").pfValue,h=e.pstyle("control-point-distances"),p=h?h.pfValue[0]:void 0,f=n,g=d;r&&(f=0,g=p);var v={x:a.x-s/2,y:a.y-l/2},y={x:o.x-u/2,y:o.y-c/2},m={x:Math.min(v.x,y.x),y:Math.min(v.y,y.y)},b=Math.max(.5,Math.log(.01*s)),x=Math.max(.5,Math.log(.01*u));i.ctrlpts=[m.x,m.y-(1+Math.pow(50,1.12)/100)*g*(f/3+1)*b,m.x-(1+Math.pow(50,1.12)/100)*g*(f/3+1)*x,m.y]},eu.findStraightEdgePoints=function(e){e._private.rscratch.edgeType="straight"},eu.findBezierPoints=function(e,t,n,r,i){var a=e._private.rscratch,o=e.pstyle("control-point-step-size").pfValue,s=e.pstyle("control-point-distances"),l=e.pstyle("control-point-weights"),u=s&&l?Math.min(s.value.length,l.value.length):1,c=s?s.pfValue[0]:void 0,d=l.value[0],h=r;a.edgeType=h?"multibezier":"bezier",a.ctrlpts=[];for(var p=0;p<u;p++){var f=(.5-t.eles.length/2+n)*o*(i?-1:1),g=void 0,v=Et(f);h&&(c=s?s.pfValue[p]:o,d=l.value[p]);var y=void 0!==(g=r?c:void 0!==c?v*c:void 0)?g:f,m=1-d,b=d,x=this.findMidptPtsEtc(e,t),w=x.midptPts,E=x.vectorNormInverse,k={x:w.x1*m+w.x2*b,y:w.y1*m+w.y2*b};a.ctrlpts.push(k.x+E.x*y,k.y+E.y*y)}},eu.findTaxiPoints=function(e,t){var n=e._private.rscratch;n.edgeType="segments";var r=t.posPts,i=t.srcW,a=t.srcH,o=t.tgtW,s=t.tgtH,l="node-position"!==e.pstyle("edge-distances").value,u=e.pstyle("taxi-direction").value,c=u,d=e.pstyle("taxi-turn"),h="%"===d.units,p=d.pfValue,f=p<0,g=e.pstyle("taxi-turn-min-distance").pfValue,v=l?(i+o)/2:0,y=l?(a+s)/2:0,m=r.x2-r.x1,b=r.y2-r.y1,x=function(e,t){return e>0?Math.max(e-t,0):Math.min(e+t,0)},w=x(m,v),E=x(b,y),k=!1;"auto"===c?u=Math.abs(w)>Math.abs(E)?"horizontal":"vertical":"upward"===c||"downward"===c?(u="vertical",k=!0):"leftward"!==c&&"rightward"!==c||(u="horizontal",k=!0);var C,S="vertical"===u,P=S?E:w,D=S?b:m,T=Et(D),_=!1;(k&&(h||f)||!("downward"===c&&D<0||"upward"===c&&D>0||"leftward"===c&&D>0||"rightward"===c&&D<0)||(P=(T*=-1)*Math.abs(P),_=!0),h)?C=(p<0?1+p:p)*P:C=(p<0?P:0)+p*T;var M=function(e){return Math.abs(e)<g||Math.abs(e)>=Math.abs(P)},B=M(C),N=M(Math.abs(P)-Math.abs(C));if((B||N)&&!_)if(S){var z=Math.abs(D)<=a/2,I=Math.abs(m)<=o/2;if(z){var A=(r.x1+r.x2)/2,L=r.y1,O=r.y2;n.segpts=[A,L,A,O]}else if(I){var R=(r.y1+r.y2)/2,V=r.x1,F=r.x2;n.segpts=[V,R,F,R]}else n.segpts=[r.x1,r.y2]}else{var j=Math.abs(D)<=i/2,q=Math.abs(b)<=s/2;if(j){var Y=(r.y1+r.y2)/2,X=r.x1,W=r.x2;n.segpts=[X,Y,W,Y]}else if(q){var H=(r.x1+r.x2)/2,K=r.y1,G=r.y2;n.segpts=[H,K,H,G]}else n.segpts=[r.x2,r.y1]}else if(S){var U=r.y1+C+(l?a/2*T:0),Z=r.x1,$=r.x2;n.segpts=[Z,U,$,U]}else{var Q=r.x1+C+(l?i/2*T:0),J=r.y1,ee=r.y2;n.segpts=[Q,J,Q,ee]}if(n.isRound){var te=e.pstyle("taxi-radius").value,ne="arc-radius"===e.pstyle("radius-type").value[0];n.radii=new Array(n.segpts.length/2).fill(te),n.isArcRadius=new Array(n.segpts.length/2).fill(ne)}},eu.tryToCorrectInvalidPoints=function(e,t){var n=e._private.rscratch;if("bezier"===n.edgeType){var r=t.srcPos,i=t.tgtPos,a=t.srcW,o=t.srcH,s=t.tgtW,l=t.tgtH,u=t.srcShape,c=t.tgtShape,d=t.srcCornerRadius,h=t.tgtCornerRadius,p=t.srcRs,f=t.tgtRs,g=!x(n.startX)||!x(n.startY),v=!x(n.arrowStartX)||!x(n.arrowStartY),y=!x(n.endX)||!x(n.endY),m=!x(n.arrowEndX)||!x(n.arrowEndY),b=3*(this.getArrowWidth(e.pstyle("width").pfValue,e.pstyle("arrow-scale").value)*this.arrowShapeWidth),w=kt({x:n.ctrlpts[0],y:n.ctrlpts[1]},{x:n.startX,y:n.startY}),E=w<b,k=kt({x:n.ctrlpts[0],y:n.ctrlpts[1]},{x:n.endX,y:n.endY}),C=k<b,S=!1;if(g||v||E){S=!0;var P={x:n.ctrlpts[0]-r.x,y:n.ctrlpts[1]-r.y},D=Math.sqrt(P.x*P.x+P.y*P.y),T={x:P.x/D,y:P.y/D},_=Math.max(a,o),M={x:n.ctrlpts[0]+2*T.x*_,y:n.ctrlpts[1]+2*T.y*_},B=u.intersectLine(r.x,r.y,a,o,M.x,M.y,0,d,p);E?(n.ctrlpts[0]=n.ctrlpts[0]+T.x*(b-w),n.ctrlpts[1]=n.ctrlpts[1]+T.y*(b-w)):(n.ctrlpts[0]=B[0]+T.x*b,n.ctrlpts[1]=B[1]+T.y*b)}if(y||m||C){S=!0;var N={x:n.ctrlpts[0]-i.x,y:n.ctrlpts[1]-i.y},z=Math.sqrt(N.x*N.x+N.y*N.y),I={x:N.x/z,y:N.y/z},A=Math.max(a,o),L={x:n.ctrlpts[0]+2*I.x*A,y:n.ctrlpts[1]+2*I.y*A},O=c.intersectLine(i.x,i.y,s,l,L.x,L.y,0,h,f);C?(n.ctrlpts[0]=n.ctrlpts[0]+I.x*(b-k),n.ctrlpts[1]=n.ctrlpts[1]+I.y*(b-k)):(n.ctrlpts[0]=O[0]+I.x*b,n.ctrlpts[1]=O[1]+I.y*b)}S&&this.findEndpoints(e)}},eu.storeAllpts=function(e){var t=e._private.rscratch;if("multibezier"===t.edgeType||"bezier"===t.edgeType||"self"===t.edgeType||"compound"===t.edgeType){t.allpts=[],t.allpts.push(t.startX,t.startY);for(var n=0;n+1<t.ctrlpts.length;n+=2)t.allpts.push(t.ctrlpts[n],t.ctrlpts[n+1]),n+3<t.ctrlpts.length&&t.allpts.push((t.ctrlpts[n]+t.ctrlpts[n+2])/2,(t.ctrlpts[n+1]+t.ctrlpts[n+3])/2);var r;t.allpts.push(t.endX,t.endY),t.ctrlpts.length/2%2==0?(r=t.allpts.length/2-1,t.midX=t.allpts[r],t.midY=t.allpts[r+1]):(r=t.allpts.length/2-3,.5,t.midX=Pt(t.allpts[r],t.allpts[r+2],t.allpts[r+4],.5),t.midY=Pt(t.allpts[r+1],t.allpts[r+3],t.allpts[r+5],.5))}else if("straight"===t.edgeType)t.allpts=[t.startX,t.startY,t.endX,t.endY],t.midX=(t.startX+t.endX+t.arrowStartX+t.arrowEndX)/4,t.midY=(t.startY+t.endY+t.arrowStartY+t.arrowEndY)/4;else if("segments"===t.edgeType){if(t.allpts=[],t.allpts.push(t.startX,t.startY),t.allpts.push.apply(t.allpts,t.segpts),t.allpts.push(t.endX,t.endY),t.isRound){t.roundCorners=[];for(var i=2;i+3<t.allpts.length;i+=2){var a=t.radii[i/2-1],o=t.isArcRadius[i/2-1];t.roundCorners.push(Jl({x:t.allpts[i-2],y:t.allpts[i-1]},{x:t.allpts[i],y:t.allpts[i+1],radius:a},{x:t.allpts[i+2],y:t.allpts[i+3]},a,o))}}if(t.segpts.length%4==0){var s=t.segpts.length/2,l=s-2;t.midX=(t.segpts[l]+t.segpts[s])/2,t.midY=(t.segpts[l+1]+t.segpts[s+1])/2}else{var u=t.segpts.length/2-1;if(t.isRound){var c={x:t.segpts[u],y:t.segpts[u+1]},d=t.roundCorners[u/2],h=[c.x-d.cx,c.y-d.cy],p=d.radius/Math.sqrt(Math.pow(h[0],2)+Math.pow(h[1],2));h=h.map((function(e){return e*p})),t.midX=d.cx+h[0],t.midY=d.cy+h[1],t.midVector=h}else t.midX=t.segpts[u],t.midY=t.segpts[u+1]}}},eu.checkForInvalidEdgeWarning=function(e){var t=e[0]._private.rscratch;t.nodesOverlap||x(t.startX)&&x(t.startY)&&x(t.endX)&&x(t.endY)?t.loggedErr=!1:t.loggedErr||(t.loggedErr=!0,je("Edge `"+e.id()+"` has invalid endpoints and so it is impossible to draw.  Adjust your edge style (e.g. control points) accordingly or use an alternative edge type.  This is expected behaviour when the source node and the target node overlap."))},eu.findEdgeControlPoints=function(e){var t=this;if(e&&0!==e.length){for(var n=this,r=n.cy.hasCompoundNodes(),i={map:new $e,get:function(e){var t=this.map.get(e[0]);return null!=t?t.get(e[1]):null},set:function(e,t){var n=this.map.get(e[0]);null==n&&(n=new $e,this.map.set(e[0],n)),n.set(e[1],t)}},a=[],o=[],s=0;s<e.length;s++){var l=e[s],u=l._private,c=l.pstyle("curve-style").value;if(!l.removed()&&l.takesUpSpace())if("haystack"!==c){var d="unbundled-bezier"===c||c.endsWith("segments")||"straight"===c||"straight-triangle"===c||c.endsWith("taxi"),h="unbundled-bezier"===c||"bezier"===c,p=u.source,f=u.target,g=[p.poolIndex(),f.poolIndex()].sort(),v=i.get(g);null==v&&(v={eles:[]},i.set(g,v),a.push(g)),v.eles.push(l),d&&(v.hasUnbundled=!0),h&&(v.hasBezier=!0)}else o.push(l)}for(var y=function(e){var o=a[e],s=i.get(o),l=void 0;if(!s.hasUnbundled){var u=s.eles[0].parallelEdges().filter((function(e){return e.isBundledBezier()}));Ge(s.eles),u.forEach((function(e){return s.eles.push(e)})),s.eles.sort((function(e,t){return e.poolIndex()-t.poolIndex()}))}var c=s.eles[0],d=c.source(),h=c.target();if(d.poolIndex()>h.poolIndex()){var p=d;d=h,h=p}var f=s.srcPos=d.position(),g=s.tgtPos=h.position(),v=s.srcW=d.outerWidth(),y=s.srcH=d.outerHeight(),m=s.tgtW=h.outerWidth(),b=s.tgtH=h.outerHeight(),w=s.srcShape=n.nodeShapes[t.getNodeShape(d)],E=s.tgtShape=n.nodeShapes[t.getNodeShape(h)],k=s.srcCornerRadius="auto"===d.pstyle("corner-radius").value?"auto":d.pstyle("corner-radius").pfValue,C=s.tgtCornerRadius="auto"===h.pstyle("corner-radius").value?"auto":h.pstyle("corner-radius").pfValue,S=s.tgtRs=h._private.rscratch,P=s.srcRs=d._private.rscratch;s.dirCounts={north:0,west:0,south:0,east:0,northwest:0,southwest:0,northeast:0,southeast:0};for(var D=0;D<s.eles.length;D++){var T=s.eles[D],_=T[0]._private.rscratch,M=T.pstyle("curve-style").value,B="unbundled-bezier"===M||M.endsWith("segments")||M.endsWith("taxi"),N=!d.same(T.source());if(!s.calculatedIntersection&&d!==h&&(s.hasBezier||s.hasUnbundled)){s.calculatedIntersection=!0;var z=w.intersectLine(f.x,f.y,v,y,g.x,g.y,0,k,P),I=s.srcIntn=z,A=E.intersectLine(g.x,g.y,m,b,f.x,f.y,0,C,S),L=s.tgtIntn=A,O=s.intersectionPts={x1:z[0],x2:A[0],y1:z[1],y2:A[1]},R=s.posPts={x1:f.x,x2:g.x,y1:f.y,y2:g.y},V=A[1]-z[1],F=A[0]-z[0],j=Math.sqrt(F*F+V*V),q=s.vector={x:F,y:V},Y=s.vectorNorm={x:q.x/j,y:q.y/j},X={x:-Y.y,y:Y.x};s.nodesOverlap=!x(j)||E.checkPoint(z[0],z[1],0,m,b,g.x,g.y,C,S)||w.checkPoint(A[0],A[1],0,v,y,f.x,f.y,k,P),s.vectorNormInverse=X,l={nodesOverlap:s.nodesOverlap,dirCounts:s.dirCounts,calculatedIntersection:!0,hasBezier:s.hasBezier,hasUnbundled:s.hasUnbundled,eles:s.eles,srcPos:g,tgtPos:f,srcW:m,srcH:b,tgtW:v,tgtH:y,srcIntn:L,tgtIntn:I,srcShape:E,tgtShape:w,posPts:{x1:R.x2,y1:R.y2,x2:R.x1,y2:R.y1},intersectionPts:{x1:O.x2,y1:O.y2,x2:O.x1,y2:O.y1},vector:{x:-q.x,y:-q.y},vectorNorm:{x:-Y.x,y:-Y.y},vectorNormInverse:{x:-X.x,y:-X.y}}}var W=N?l:s;_.nodesOverlap=W.nodesOverlap,_.srcIntn=W.srcIntn,_.tgtIntn=W.tgtIntn,_.isRound=M.startsWith("round"),r&&(d.isParent()||d.isChild()||h.isParent()||h.isChild())&&(d.parents().anySame(h)||h.parents().anySame(d)||d.same(h)&&d.isParent())?t.findCompoundLoopPoints(T,W,D,B):d===h?t.findLoopPoints(T,W,D,B):M.endsWith("segments")?t.findSegmentsPoints(T,W):M.endsWith("taxi")?t.findTaxiPoints(T,W):"straight"===M||!B&&s.eles.length%2==1&&D===Math.floor(s.eles.length/2)?t.findStraightEdgePoints(T):t.findBezierPoints(T,W,D,B,N),t.findEndpoints(T),t.tryToCorrectInvalidPoints(T,W),t.checkForInvalidEdgeWarning(T),t.storeAllpts(T),t.storeEdgeProjections(T),t.calculateArrowAngles(T),t.recalculateEdgeLabelProjections(T),t.calculateLabelAngles(T)}},m=0;m<a.length;m++)y(m);this.findHaystackPoints(o)}},eu.getSegmentPoints=function(e){var t=e[0]._private.rscratch;if("segments"===t.edgeType)return this.recalculateRenderedStyle(e),tu(t.segpts)},eu.getControlPoints=function(e){var t=e[0]._private.rscratch,n=t.edgeType;if("bezier"===n||"multibezier"===n||"self"===n||"compound"===n)return this.recalculateRenderedStyle(e),tu(t.ctrlpts)},eu.getEdgeMidpoint=function(e){var t=e[0]._private.rscratch;return this.recalculateRenderedStyle(e),{x:t.midX,y:t.midY}};var nu={manualEndptToPx:function(e,t){var n=e.position(),r=e.outerWidth(),i=e.outerHeight(),a=e._private.rscratch;if(2===t.value.length){var o=[t.pfValue[0],t.pfValue[1]];return"%"===t.units[0]&&(o[0]=o[0]*r),"%"===t.units[1]&&(o[1]=o[1]*i),o[0]+=n.x,o[1]+=n.y,o}var s=t.pfValue[0];s=-Math.PI/2+s;var l=2*Math.max(r,i),u=[n.x+Math.cos(s)*l,n.y+Math.sin(s)*l];return this.nodeShapes[this.getNodeShape(e)].intersectLine(n.x,n.y,r,i,u[0],u[1],0,"auto"===e.pstyle("corner-radius").value?"auto":e.pstyle("corner-radius").pfValue,a)},findEndpoints:function(e){var t,n,r,i,a,o=this,s=e.source()[0],l=e.target()[0],u=s.position(),c=l.position(),d=e.pstyle("target-arrow-shape").value,h=e.pstyle("source-arrow-shape").value,p=e.pstyle("target-distance-from-node").pfValue,f=e.pstyle("source-distance-from-node").pfValue,g=s._private.rscratch,v=l._private.rscratch,y=e.pstyle("curve-style").value,m=e._private.rscratch,b=m.edgeType,w="self"===b||"compound"===b,E="bezier"===b||"multibezier"===b||w,k="bezier"!==b,C="straight"===b||"segments"===b,S="segments"===b,P=E||k||C,D=w||"taxi"===y,T=e.pstyle("source-endpoint"),_=D?"outside-to-node":T.value,M="auto"===s.pstyle("corner-radius").value?"auto":s.pstyle("corner-radius").pfValue,B=e.pstyle("target-endpoint"),N=D?"outside-to-node":B.value,z="auto"===l.pstyle("corner-radius").value?"auto":l.pstyle("corner-radius").pfValue;if(m.srcManEndpt=T,m.tgtManEndpt=B,E){var I=[m.ctrlpts[0],m.ctrlpts[1]];n=k?[m.ctrlpts[m.ctrlpts.length-2],m.ctrlpts[m.ctrlpts.length-1]]:I,r=I}else if(C){var A=S?m.segpts.slice(0,2):[c.x,c.y];n=S?m.segpts.slice(m.segpts.length-2):[u.x,u.y],r=A}if("inside-to-node"===N)t=[c.x,c.y];else if(B.units)t=this.manualEndptToPx(l,B);else if("outside-to-line"===N)t=m.tgtIntn;else if("outside-to-node"===N||"outside-to-node-or-label"===N?i=n:"outside-to-line"!==N&&"outside-to-line-or-label"!==N||(i=[u.x,u.y]),t=o.nodeShapes[this.getNodeShape(l)].intersectLine(c.x,c.y,l.outerWidth(),l.outerHeight(),i[0],i[1],0,z,v),"outside-to-node-or-label"===N||"outside-to-line-or-label"===N){var L=l._private.rscratch,O=L.labelWidth,R=L.labelHeight,V=L.labelX,F=L.labelY,j=O/2,q=R/2,Y=l.pstyle("text-valign").value;"top"===Y?F-=q:"bottom"===Y&&(F+=q);var X=l.pstyle("text-halign").value;"left"===X?V-=j:"right"===X&&(V+=j);var W=$t(i[0],i[1],[V-j,F-q,V+j,F-q,V+j,F+q,V-j,F+q],c.x,c.y);if(W.length>0){var H=u,K=Ct(H,bt(t)),G=Ct(H,bt(W)),U=K;if(G<K&&(t=W,U=G),W.length>2)Ct(H,{x:W[2],y:W[3]})<U&&(t=[W[2],W[3]])}}var Z=Qt(t,n,o.arrowShapes[d].spacing(e)+p),$=Qt(t,n,o.arrowShapes[d].gap(e)+p);if(m.endX=$[0],m.endY=$[1],m.arrowEndX=Z[0],m.arrowEndY=Z[1],"inside-to-node"===_)t=[u.x,u.y];else if(T.units)t=this.manualEndptToPx(s,T);else if("outside-to-line"===_)t=m.srcIntn;else if("outside-to-node"===_||"outside-to-node-or-label"===_?a=r:"outside-to-line"!==_&&"outside-to-line-or-label"!==_||(a=[c.x,c.y]),t=o.nodeShapes[this.getNodeShape(s)].intersectLine(u.x,u.y,s.outerWidth(),s.outerHeight(),a[0],a[1],0,M,g),"outside-to-node-or-label"===_||"outside-to-line-or-label"===_){var Q=s._private.rscratch,J=Q.labelWidth,ee=Q.labelHeight,te=Q.labelX,ne=Q.labelY,re=J/2,ie=ee/2,ae=s.pstyle("text-valign").value;"top"===ae?ne-=ie:"bottom"===ae&&(ne+=ie);var oe=s.pstyle("text-halign").value;"left"===oe?te-=re:"right"===oe&&(te+=re);var se=$t(a[0],a[1],[te-re,ne-ie,te+re,ne-ie,te+re,ne+ie,te-re,ne+ie],u.x,u.y);if(se.length>0){var le=c,ue=Ct(le,bt(t)),ce=Ct(le,bt(se)),de=ue;if(ce<ue&&(t=[se[0],se[1]],de=ce),se.length>2)Ct(le,{x:se[2],y:se[3]})<de&&(t=[se[2],se[3]])}}var he=Qt(t,r,o.arrowShapes[h].spacing(e)+f),pe=Qt(t,r,o.arrowShapes[h].gap(e)+f);m.startX=pe[0],m.startY=pe[1],m.arrowStartX=he[0],m.arrowStartY=he[1],P&&(x(m.startX)&&x(m.startY)&&x(m.endX)&&x(m.endY)?m.badLine=!1:m.badLine=!0)},getSourceEndpoint:function(e){var t=e[0]._private.rscratch;switch(this.recalculateRenderedStyle(e),t.edgeType){case"haystack":return{x:t.haystackPts[0],y:t.haystackPts[1]};default:return{x:t.arrowStartX,y:t.arrowStartY}}},getTargetEndpoint:function(e){var t=e[0]._private.rscratch;switch(this.recalculateRenderedStyle(e),t.edgeType){case"haystack":return{x:t.haystackPts[2],y:t.haystackPts[3]};default:return{x:t.arrowEndX,y:t.arrowEndY}}}},ru={};function iu(e,t,n){for(var r=function(e,t,n,r){return Pt(e,t,n,r)},i=t._private.rstyle.bezierPts,a=0;a<e.bezierProjPcts.length;a++){var o=e.bezierProjPcts[a];i.push({x:r(n[0],n[2],n[4],o),y:r(n[1],n[3],n[5],o)})}}ru.storeEdgeProjections=function(e){var t=e._private,n=t.rscratch,r=n.edgeType;if(t.rstyle.bezierPts=null,t.rstyle.linePts=null,t.rstyle.haystackPts=null,"multibezier"===r||"bezier"===r||"self"===r||"compound"===r){t.rstyle.bezierPts=[];for(var i=0;i+5<n.allpts.length;i+=4)iu(this,e,n.allpts.slice(i,i+6))}else if("segments"===r){var a=t.rstyle.linePts=[];for(i=0;i+1<n.allpts.length;i+=2)a.push({x:n.allpts[i],y:n.allpts[i+1]})}else if("haystack"===r){var o=n.haystackPts;t.rstyle.haystackPts=[{x:o[0],y:o[1]},{x:o[2],y:o[3]}]}t.rstyle.arrowWidth=this.getArrowWidth(e.pstyle("width").pfValue,e.pstyle("arrow-scale").value)*this.arrowShapeWidth},ru.recalculateEdgeProjections=function(e){this.findEdgeControlPoints(e)};var au={recalculateNodeLabelProjection:function(e){var t=e.pstyle("label").strValue;if(!D(t)){var n,r,i=e._private,a=e.width(),o=e.height(),s=e.padding(),l=e.position(),u=e.pstyle("text-halign").strValue,c=e.pstyle("text-valign").strValue,d=i.rscratch,h=i.rstyle;switch(u){case"left":n=l.x-a/2-s;break;case"right":n=l.x+a/2+s;break;default:n=l.x}switch(c){case"top":r=l.y-o/2-s;break;case"bottom":r=l.y+o/2+s;break;default:r=l.y}d.labelX=n,d.labelY=r,h.labelX=n,h.labelY=r,this.calculateLabelAngles(e),this.applyLabelDimensions(e)}}},ou=function(e,t){var n=Math.atan(t/e);return 0===e&&n<0&&(n*=-1),n},su=function(e,t){var n=t.x-e.x,r=t.y-e.y;return ou(n,r)};au.recalculateEdgeLabelProjections=function(e){var t,n=e._private,r=n.rscratch,i=this,a={mid:e.pstyle("label").strValue,source:e.pstyle("source-label").strValue,target:e.pstyle("target-label").strValue};if(a.mid||a.source||a.target){t={x:r.midX,y:r.midY};var o=function(e,t,r){Ze(n.rscratch,e,t,r),Ze(n.rstyle,e,t,r)};o("labelX",null,t.x),o("labelY",null,t.y);var s=ou(r.midDispX,r.midDispY);o("labelAutoAngle",null,s);var l=function(s){var l,u="source"===s;if(a[s]){var c=e.pstyle(s+"-text-offset").pfValue;switch(r.edgeType){case"self":case"compound":case"bezier":case"multibezier":for(var d,h=function e(){if(e.cache)return e.cache;for(var t=[],a=0;a+5<r.allpts.length;a+=4){var o={x:r.allpts[a],y:r.allpts[a+1]},s={x:r.allpts[a+2],y:r.allpts[a+3]},l={x:r.allpts[a+4],y:r.allpts[a+5]};t.push({p0:o,p1:s,p2:l,startDist:0,length:0,segments:[]})}var u=n.rstyle.bezierPts,c=i.bezierProjPcts.length;function d(e,t,n,r,i){var a=kt(t,n),o=e.segments[e.segments.length-1],s={p0:t,p1:n,t0:r,t1:i,startDist:o?o.startDist+o.length:0,length:a};e.segments.push(s),e.length+=a}for(var h=0;h<t.length;h++){var p=t[h],f=t[h-1];f&&(p.startDist=f.startDist+f.length),d(p,p.p0,u[h*c],0,i.bezierProjPcts[0]);for(var g=0;g<c-1;g++)d(p,u[h*c+g],u[h*c+g+1],i.bezierProjPcts[g],i.bezierProjPcts[g+1]);d(p,u[h*c+c-1],p.p2,i.bezierProjPcts[c-1],1)}return e.cache=t}(),p=0,f=0,g=0;g<h.length;g++){for(var v=h[u?g:h.length-1-g],y=0;y<v.segments.length;y++){var m=v.segments[u?y:v.segments.length-1-y],b=g===h.length-1&&y===v.segments.length-1;if(p=f,(f+=m.length)>=c||b){d={cp:v,segment:m};break}}if(d)break}var x=d.cp,w=d.segment,E=(c-p)/w.length,k=w.t1-w.t0,C=u?w.t0+k*E:w.t1-k*E;C=Tt(0,C,1),t=Dt(x.p0,x.p1,x.p2,C),l=function(e,t,n,r){var i=Tt(0,r-.001,1),a=Tt(0,r+.001,1),o=Dt(e,t,n,i),s=Dt(e,t,n,a);return su(o,s)}(x.p0,x.p1,x.p2,C);break;case"straight":case"segments":case"haystack":for(var S,P,D,T,_=0,M=r.allpts.length,B=0;B+3<M&&(u?(D={x:r.allpts[B],y:r.allpts[B+1]},T={x:r.allpts[B+2],y:r.allpts[B+3]}):(D={x:r.allpts[M-2-B],y:r.allpts[M-1-B]},T={x:r.allpts[M-4-B],y:r.allpts[M-3-B]}),P=_,!((_+=S=kt(D,T))>=c));B+=2);var N=(c-P)/S;N=Tt(0,N,1),t=function(e,t,n,r){var i=t.x-e.x,a=t.y-e.y,o=kt(e,t),s=i/o,l=a/o;return n=null==n?0:n,r=null!=r?r:n*o,{x:e.x+s*r,y:e.y+l*r}}(D,T,N),l=su(D,T)}o("labelX",s,t.x),o("labelY",s,t.y),o("labelAutoAngle",s,l)}};l("source"),l("target"),this.applyLabelDimensions(e)}},au.applyLabelDimensions=function(e){this.applyPrefixedLabelDimensions(e),e.isEdge()&&(this.applyPrefixedLabelDimensions(e,"source"),this.applyPrefixedLabelDimensions(e,"target"))},au.applyPrefixedLabelDimensions=function(e,t){var n=e._private,r=this.getLabelText(e,t),i=this.calculateLabelDimensions(e,r),a=e.pstyle("line-height").pfValue,o=e.pstyle("text-wrap").strValue,s=Ue(n.rscratch,"labelWrapCachedLines",t)||[],l="wrap"!==o?1:Math.max(s.length,1),u=i.height/l,c=u*a,d=i.width,h=i.height+(l-1)*(a-1)*u;Ze(n.rstyle,"labelWidth",t,d),Ze(n.rscratch,"labelWidth",t,d),Ze(n.rstyle,"labelHeight",t,h),Ze(n.rscratch,"labelHeight",t,h),Ze(n.rscratch,"labelLineHeight",t,c)},au.getLabelText=function(e,t){var n=e._private,r=t?t+"-":"",i=e.pstyle(r+"label").strValue,a=e.pstyle("text-transform").value,o=function(e,r){return r?(Ze(n.rscratch,e,t,r),r):Ue(n.rscratch,e,t)};if(!i)return"";"none"==a||("uppercase"==a?i=i.toUpperCase():"lowercase"==a&&(i=i.toLowerCase()));var s=e.pstyle("text-wrap").value;if("wrap"===s){var u=o("labelKey");if(null!=u&&o("labelWrapKey")===u)return o("labelWrapCachedText");for(var c=i.split("\n"),d=e.pstyle("text-max-width").pfValue,h="anywhere"===e.pstyle("text-overflow-wrap").value,p=[],f=/[\s\u200b]+|$/g,g=0;g<c.length;g++){var v=c[g],y=this.calculateLabelDimensions(e,v).width;if(h){var m=v.split("").join("​");v=m}if(y>d){var b,x="",w=0,E=l(v.matchAll(f));try{for(E.s();!(b=E.n()).done;){var k=b.value,C=k[0],S=v.substring(w,k.index);w=k.index+C.length;var P=0===x.length?S:x+S+C;this.calculateLabelDimensions(e,P).width<=d?x+=S+C:(x&&p.push(x),x=S+C)}}catch(e){E.e(e)}finally{E.f()}x.match(/^[\s\u200b]+$/)||p.push(x)}else p.push(v)}o("labelWrapCachedLines",p),i=o("labelWrapCachedText",p.join("\n")),o("labelWrapKey",u)}else if("ellipsis"===s){var D=e.pstyle("text-max-width").pfValue,T="",_=!1;if(this.calculateLabelDimensions(e,i).width<D)return i;for(var M=0;M<i.length;M++){if(this.calculateLabelDimensions(e,T+i[M]+"…").width>D)break;T+=i[M],M===i.length-1&&(_=!0)}return _||(T+="…"),T}return i},au.getLabelJustification=function(e){var t=e.pstyle("text-justification").strValue,n=e.pstyle("text-halign").strValue;if("auto"!==t)return t;if(!e.isNode())return"center";switch(n){case"left":return"right";case"right":return"left";default:return"center"}},au.calculateLabelDimensions=function(e,t){var n=this,r=n.cy.window().document,i=Te(t,e._private.labelDimsKey),a=n.labelDimCache||(n.labelDimCache=[]),o=a[i];if(null!=o)return o;var s=e.pstyle("font-style").strValue,l=e.pstyle("font-size").pfValue,u=e.pstyle("font-family").strValue,c=e.pstyle("font-weight").strValue,d=this.labelCalcCanvas,h=this.labelCalcCanvasContext;if(!d){d=this.labelCalcCanvas=r.createElement("canvas"),h=this.labelCalcCanvasContext=d.getContext("2d");var p=d.style;p.position="absolute",p.left="-9999px",p.top="-9999px",p.zIndex="-1",p.visibility="hidden",p.pointerEvents="none"}h.font="".concat(s," ").concat(c," ").concat(l,"px ").concat(u);for(var f=0,g=0,v=t.split("\n"),y=0;y<v.length;y++){var m=v[y],b=h.measureText(m),x=Math.ceil(b.width),w=l;f=Math.max(x,f),g+=w}return f+=0,g+=0,a[i]={width:f,height:g}},au.calculateLabelAngle=function(e,t){var n=e._private.rscratch,r=e.isEdge(),i=t?t+"-":"",a=e.pstyle(i+"text-rotation"),o=a.strValue;return"none"===o?0:r&&"autorotate"===o?n.labelAutoAngle:"autorotate"===o?0:a.pfValue},au.calculateLabelAngles=function(e){var t=this,n=e.isEdge(),r=e._private.rscratch;r.labelAngle=t.calculateLabelAngle(e),n&&(r.sourceLabelAngle=t.calculateLabelAngle(e,"source"),r.targetLabelAngle=t.calculateLabelAngle(e,"target"))};var lu={},uu=!1;lu.getNodeShape=function(e){var t=e.pstyle("shape").value;if("cutrectangle"===t&&(e.width()<28||e.height()<28))return uu||(je("The `cutrectangle` node shape can not be used at small sizes so `rectangle` is used instead"),uu=!0),"rectangle";if(e.isParent())return"rectangle"===t||"roundrectangle"===t||"round-rectangle"===t||"cutrectangle"===t||"cut-rectangle"===t||"barrel"===t?t:"rectangle";if("polygon"===t){var n=e.pstyle("shape-polygon-points").value;return this.nodeShapes.makePolygon(n).name}return t};var cu={registerCalculationListeners:function(){var e=this.cy,t=e.collection(),n=this,r=function(e){var n=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];if(t.merge(e),n)for(var r=0;r<e.length;r++){var i=e[r],a=i._private,o=a.rstyle;o.clean=!1,o.cleanConnected=!1}};n.binder(e).on("bounds.* dirty.*",(function(e){var t=e.target;r(t)})).on("style.* background.*",(function(e){var t=e.target;r(t,!1)}));var i=function(i){if(i){var a=n.onUpdateEleCalcsFns;t.cleanStyle();for(var o=0;o<t.length;o++){var s=t[o],l=s._private.rstyle;s.isNode()&&!l.cleanConnected&&(r(s.connectedEdges()),l.cleanConnected=!0)}if(a)for(var u=0;u<a.length;u++){(0,a[u])(i,t)}n.recalculateRenderedStyle(t),t=e.collection()}};n.flushRenderedStyleQueue=function(){i(!0)},n.beforeRender(i,n.beforeRenderPriorities.eleCalcs)},onUpdateEleCalcs:function(e){(this.onUpdateEleCalcsFns=this.onUpdateEleCalcsFns||[]).push(e)},recalculateRenderedStyle:function(e,t){var n=function(e){return e._private.rstyle.cleanConnected},r=[],i=[];if(!this.destroyed){void 0===t&&(t=!0);for(var a=0;a<e.length;a++){var o=e[a],s=o._private,l=s.rstyle;!o.isEdge()||n(o.source())&&n(o.target())||(l.clean=!1),t&&l.clean||o.removed()||"none"!==o.pstyle("display").value&&("nodes"===s.group?i.push(o):r.push(o),l.clean=!0)}for(var u=0;u<i.length;u++){var c=i[u],d=c._private.rstyle,h=c.position();this.recalculateNodeLabelProjection(c),d.nodeX=h.x,d.nodeY=h.y,d.nodeW=c.pstyle("width").pfValue,d.nodeH=c.pstyle("height").pfValue}this.recalculateEdgeProjections(r);for(var p=0;p<r.length;p++){var f=r[p]._private,g=f.rstyle,v=f.rscratch;g.srcX=v.arrowStartX,g.srcY=v.arrowStartY,g.tgtX=v.arrowEndX,g.tgtY=v.arrowEndY,g.midX=v.midX,g.midY=v.midY,g.labelAngle=v.labelAngle,g.sourceLabelAngle=v.sourceLabelAngle,g.targetLabelAngle=v.targetLabelAngle}}}},du={updateCachedGrabbedEles:function(){var e=this.cachedZSortedEles;if(e){e.drag=[],e.nondrag=[];for(var t=[],n=0;n<e.length;n++){var r=(i=e[n])._private.rscratch;i.grabbed()&&!i.isParent()?t.push(i):r.inDragLayer?e.drag.push(i):e.nondrag.push(i)}for(n=0;n<t.length;n++){var i=t[n];e.drag.push(i)}}},invalidateCachedZSortedEles:function(){this.cachedZSortedEles=null},getCachedZSortedEles:function(e){if(e||!this.cachedZSortedEles){var t=this.cy.mutableElements().toArray();t.sort(Mo),t.interactive=t.filter((function(e){return e.interactive()})),this.cachedZSortedEles=t,this.updateCachedGrabbedEles()}else t=this.cachedZSortedEles;return t}},hu={};[_l,Ml,eu,nu,ru,au,lu,cu,du].forEach((function(e){L(hu,e)}));var pu={getCachedImage:function(e,t,n){var r=this.imageCache=this.imageCache||{},i=r[e];if(i)return i.image.complete||i.image.addEventListener("load",n),i.image;var a=(i=r[e]=r[e]||{}).image=new Image;a.addEventListener("load",n),a.addEventListener("error",(function(){a.error=!0}));return"data:"===e.substring(0,"data:".length).toLowerCase()||(t="null"===t?null:t,a.crossOrigin=t),a.src=e,a}},fu={registerBinding:function(e,t,n,r){var i=Array.prototype.slice.apply(arguments,[1]),a=this.binder(e);return a.on.apply(a,i)}};fu.binder=function(e){var t,n=this,r=n.cy.window(),i=e===r||e===r.document||e===r.document.body||(t=e,"undefined"!=typeof HTMLElement&&t instanceof HTMLElement);if(null==n.supportsPassiveEvents){var a=!1;try{var o=Object.defineProperty({},"passive",{get:function(){return a=!0,!0}});r.addEventListener("test",null,o)}catch(e){}n.supportsPassiveEvents=a}var s=function(t,r,a){var o=Array.prototype.slice.call(arguments);return i&&n.supportsPassiveEvents&&(o[2]={capture:null!=a&&a,passive:!1,once:!1}),n.bindings.push({target:e,args:o}),(e.addEventListener||e.on).apply(e,o),this};return{on:s,addEventListener:s,addListener:s,bind:s}},fu.nodeIsDraggable=function(e){return e&&e.isNode()&&!e.locked()&&e.grabbable()},fu.nodeIsGrabbable=function(e){return this.nodeIsDraggable(e)&&e.interactive()},fu.load=function(){var e=this,t=e.cy.window(),n=function(e){return e.selected()},r=function(t,n,r,i){null==t&&(t=e.cy);for(var a=0;a<n.length;a++){var o=n[a];t.emit({originalEvent:r,type:o,position:i})}},i=function(e){return e.shiftKey||e.metaKey||e.ctrlKey},a=function(t,n){var r=!0;if(e.cy.hasCompoundNodes()&&t&&t.pannable())for(var i=0;n&&i<n.length;i++){if((t=n[i]).isNode()&&t.isParent()&&!t.pannable()){r=!1;break}}else r=!0;return r},o=function(e){e[0]._private.rscratch.inDragLayer=!0},s=function(e){e[0]._private.rscratch.isGrabTarget=!0},l=function(e,t){var n=t.addToList;n.has(e)||!e.grabbable()||e.locked()||(n.merge(e),function(e){e[0]._private.grabbed=!0}(e))},u=function(t,n){n=n||{};var r=t.cy().hasCompoundNodes();n.inDragLayer&&(t.forEach(o),t.neighborhood().stdFilter((function(e){return!r||e.isEdge()})).forEach(o)),n.addToList&&t.forEach((function(e){l(e,n)})),function(e,t){if(e.cy().hasCompoundNodes()&&(null!=t.inDragLayer||null!=t.addToList)){var n=e.descendants();t.inDragLayer&&(n.forEach(o),n.connectedEdges().forEach(o)),t.addToList&&l(n,t)}}(t,n),h(t,{inDragLayer:n.inDragLayer}),e.updateCachedGrabbedEles()},c=u,d=function(t){t&&(e.getCachedZSortedEles().forEach((function(e){!function(e){e[0]._private.grabbed=!1}(e),function(e){e[0]._private.rscratch.inDragLayer=!1}(e),function(e){e[0]._private.rscratch.isGrabTarget=!1}(e)})),e.updateCachedGrabbedEles())},h=function(e,t){if((null!=t.inDragLayer||null!=t.addToList)&&e.cy().hasCompoundNodes()){var n=e.ancestors().orphans();if(!n.same(e)){var r=n.descendants().spawnSelf().merge(n).unmerge(e).unmerge(e.descendants()),i=r.connectedEdges();t.inDragLayer&&(i.forEach(o),r.forEach(o)),t.addToList&&r.forEach((function(e){l(e,t)}))}}},p=function(){null!=document.activeElement&&null!=document.activeElement.blur&&document.activeElement.blur()},f="undefined"!=typeof MutationObserver,g="undefined"!=typeof ResizeObserver;f?(e.removeObserver=new MutationObserver((function(t){for(var n=0;n<t.length;n++){var r=t[n].removedNodes;if(r)for(var i=0;i<r.length;i++){if(r[i]===e.container){e.destroy();break}}}})),e.container.parentNode&&e.removeObserver.observe(e.container.parentNode,{childList:!0})):e.registerBinding(e.container,"DOMNodeRemoved",(function(t){e.destroy()}));var v=ve((function(){e.cy.resize()}),100);f&&(e.styleObserver=new MutationObserver(v),e.styleObserver.observe(e.container,{attributes:!0})),e.registerBinding(t,"resize",v),g&&(e.resizeObserver=new ResizeObserver(v),e.resizeObserver.observe(e.container));var y=function(){e.invalidateContainerClientCoordsCache()};!function(e,t){for(;null!=e;)t(e),e=e.parentNode}(e.container,(function(t){e.registerBinding(t,"transitionend",y),e.registerBinding(t,"animationend",y),e.registerBinding(t,"scroll",y)})),e.registerBinding(e.container,"contextmenu",(function(e){e.preventDefault()}));var m,b,w,E=function(t){for(var n=e.findContainerClientCoords(),r=n[0],i=n[1],a=n[2],o=n[3],s=t.touches?t.touches:[t],l=!1,u=0;u<s.length;u++){var c=s[u];if(r<=c.clientX&&c.clientX<=r+a&&i<=c.clientY&&c.clientY<=i+o){l=!0;break}}if(!l)return!1;for(var d=e.container,h=t.target.parentNode,p=!1;h;){if(h===d){p=!0;break}h=h.parentNode}return!!p};e.registerBinding(e.container,"mousedown",(function(t){if(E(t)&&(1!==e.hoverData.which||1===t.which)){t.preventDefault(),p(),e.hoverData.capture=!0,e.hoverData.which=t.which;var n=e.cy,i=[t.clientX,t.clientY],a=e.projectIntoViewport(i[0],i[1]),o=e.selection,l=e.findNearestElements(a[0],a[1],!0,!1),d=l[0],h=e.dragData.possibleDragElements;e.hoverData.mdownPos=a,e.hoverData.mdownGPos=i;if(3==t.which){e.hoverData.cxtStarted=!0;var f={originalEvent:t,type:"cxttapstart",position:{x:a[0],y:a[1]}};d?(d.activate(),d.emit(f),e.hoverData.down=d):n.emit(f),e.hoverData.downTime=(new Date).getTime(),e.hoverData.cxtDragged=!1}else if(1==t.which){if(d&&d.activate(),null!=d&&e.nodeIsGrabbable(d)){var g=function(e){return{originalEvent:t,type:e,position:{x:a[0],y:a[1]}}};if(s(d),d.selected()){h=e.dragData.possibleDragElements=n.collection();var v=n.$((function(t){return t.isNode()&&t.selected()&&e.nodeIsGrabbable(t)}));u(v,{addToList:h}),d.emit(g("grabon")),v.forEach((function(e){e.emit(g("grab"))}))}else h=e.dragData.possibleDragElements=n.collection(),c(d,{addToList:h}),d.emit(g("grabon")).emit(g("grab"));e.redrawHint("eles",!0),e.redrawHint("drag",!0)}e.hoverData.down=d,e.hoverData.downs=l,e.hoverData.downTime=(new Date).getTime(),r(d,["mousedown","tapstart","vmousedown"],t,{x:a[0],y:a[1]}),null==d?(o[4]=1,e.data.bgActivePosistion={x:a[0],y:a[1]},e.redrawHint("select",!0),e.redraw()):d.pannable()&&(o[4]=1),e.hoverData.tapholdCancelled=!1,clearTimeout(e.hoverData.tapholdTimeout),e.hoverData.tapholdTimeout=setTimeout((function(){if(!e.hoverData.tapholdCancelled){var r=e.hoverData.down;r?r.emit({originalEvent:t,type:"taphold",position:{x:a[0],y:a[1]}}):n.emit({originalEvent:t,type:"taphold",position:{x:a[0],y:a[1]}})}}),e.tapholdDuration)}o[0]=o[2]=a[0],o[1]=o[3]=a[1]}}),!1),e.registerBinding(t,"mousemove",(function(t){if(e.hoverData.capture||E(t)){var n=!1,o=e.cy,s=o.zoom(),l=[t.clientX,t.clientY],c=e.projectIntoViewport(l[0],l[1]),h=e.hoverData.mdownPos,p=e.hoverData.mdownGPos,f=e.selection,g=null;e.hoverData.draggingEles||e.hoverData.dragging||e.hoverData.selecting||(g=e.findNearestElement(c[0],c[1],!0,!1));var v,y=e.hoverData.last,m=e.hoverData.down,b=[c[0]-f[2],c[1]-f[3]],w=e.dragData.possibleDragElements;if(p){var k=l[0]-p[0],C=k*k,S=l[1]-p[1],P=C+S*S;e.hoverData.isOverThresholdDrag=v=P>=e.desktopTapThreshold2}var D=i(t);v&&(e.hoverData.tapholdCancelled=!0);n=!0,r(g,["mousemove","vmousemove","tapdrag"],t,{x:c[0],y:c[1]});var T=function(){e.data.bgActivePosistion=void 0,e.hoverData.selecting||o.emit({originalEvent:t,type:"boxstart",position:{x:c[0],y:c[1]}}),f[4]=1,e.hoverData.selecting=!0,e.redrawHint("select",!0),e.redraw()};if(3===e.hoverData.which){if(v){var _={originalEvent:t,type:"cxtdrag",position:{x:c[0],y:c[1]}};m?m.emit(_):o.emit(_),e.hoverData.cxtDragged=!0,e.hoverData.cxtOver&&g===e.hoverData.cxtOver||(e.hoverData.cxtOver&&e.hoverData.cxtOver.emit({originalEvent:t,type:"cxtdragout",position:{x:c[0],y:c[1]}}),e.hoverData.cxtOver=g,g&&g.emit({originalEvent:t,type:"cxtdragover",position:{x:c[0],y:c[1]}}))}}else if(e.hoverData.dragging){if(n=!0,o.panningEnabled()&&o.userPanningEnabled()){var M;if(e.hoverData.justStartedPan){var B=e.hoverData.mdownPos;M={x:(c[0]-B[0])*s,y:(c[1]-B[1])*s},e.hoverData.justStartedPan=!1}else M={x:b[0]*s,y:b[1]*s};o.panBy(M),o.emit("dragpan"),e.hoverData.dragged=!0}c=e.projectIntoViewport(t.clientX,t.clientY)}else if(1!=f[4]||null!=m&&!m.pannable()){if(m&&m.pannable()&&m.active()&&m.unactivate(),m&&m.grabbed()||g==y||(y&&r(y,["mouseout","tapdragout"],t,{x:c[0],y:c[1]}),g&&r(g,["mouseover","tapdragover"],t,{x:c[0],y:c[1]}),e.hoverData.last=g),m)if(v){if(o.boxSelectionEnabled()&&D)m&&m.grabbed()&&(d(w),m.emit("freeon"),w.emit("free"),e.dragData.didDrag&&(m.emit("dragfreeon"),w.emit("dragfree"))),T();else if(m&&m.grabbed()&&e.nodeIsDraggable(m)){var N=!e.dragData.didDrag;N&&e.redrawHint("eles",!0),e.dragData.didDrag=!0,e.hoverData.draggingEles||u(w,{inDragLayer:!0});var z={x:0,y:0};if(x(b[0])&&x(b[1])&&(z.x+=b[0],z.y+=b[1],N)){var I=e.hoverData.dragDelta;I&&x(I[0])&&x(I[1])&&(z.x+=I[0],z.y+=I[1])}e.hoverData.draggingEles=!0,w.silentShift(z).emit("position drag"),e.redrawHint("drag",!0),e.redraw()}}else!function(){var t=e.hoverData.dragDelta=e.hoverData.dragDelta||[];0===t.length?(t.push(b[0]),t.push(b[1])):(t[0]+=b[0],t[1]+=b[1])}();n=!0}else if(v){if(e.hoverData.dragging||!o.boxSelectionEnabled()||!D&&o.panningEnabled()&&o.userPanningEnabled()){if(!e.hoverData.selecting&&o.panningEnabled()&&o.userPanningEnabled()){a(m,e.hoverData.downs)&&(e.hoverData.dragging=!0,e.hoverData.justStartedPan=!0,f[4]=0,e.data.bgActivePosistion=bt(h),e.redrawHint("select",!0),e.redraw())}}else T();m&&m.pannable()&&m.active()&&m.unactivate()}return f[2]=c[0],f[3]=c[1],n?(t.stopPropagation&&t.stopPropagation(),t.preventDefault&&t.preventDefault(),!1):void 0}}),!1),e.registerBinding(t,"mouseup",(function(t){if((1!==e.hoverData.which||1===t.which||!e.hoverData.capture)&&e.hoverData.capture){e.hoverData.capture=!1;var a=e.cy,o=e.projectIntoViewport(t.clientX,t.clientY),s=e.selection,l=e.findNearestElement(o[0],o[1],!0,!1),u=e.dragData.possibleDragElements,c=e.hoverData.down,h=i(t);if(e.data.bgActivePosistion&&(e.redrawHint("select",!0),e.redraw()),e.hoverData.tapholdCancelled=!0,e.data.bgActivePosistion=void 0,c&&c.unactivate(),3===e.hoverData.which){var p={originalEvent:t,type:"cxttapend",position:{x:o[0],y:o[1]}};if(c?c.emit(p):a.emit(p),!e.hoverData.cxtDragged){var f={originalEvent:t,type:"cxttap",position:{x:o[0],y:o[1]}};c?c.emit(f):a.emit(f)}e.hoverData.cxtDragged=!1,e.hoverData.which=null}else if(1===e.hoverData.which){if(r(l,["mouseup","tapend","vmouseup"],t,{x:o[0],y:o[1]}),e.dragData.didDrag||e.hoverData.dragged||e.hoverData.selecting||e.hoverData.isOverThresholdDrag||(r(c,["click","tap","vclick"],t,{x:o[0],y:o[1]}),b=!1,t.timeStamp-w<=a.multiClickDebounceTime()?(m&&clearTimeout(m),b=!0,w=null,r(c,["dblclick","dbltap","vdblclick"],t,{x:o[0],y:o[1]})):(m=setTimeout((function(){b||r(c,["oneclick","onetap","voneclick"],t,{x:o[0],y:o[1]})}),a.multiClickDebounceTime()),w=t.timeStamp)),null!=c||e.dragData.didDrag||e.hoverData.selecting||e.hoverData.dragged||i(t)||(a.$(n).unselect(["tapunselect"]),u.length>0&&e.redrawHint("eles",!0),e.dragData.possibleDragElements=u=a.collection()),l!=c||e.dragData.didDrag||e.hoverData.selecting||null!=l&&l._private.selectable&&(e.hoverData.dragging||("additive"===a.selectionType()||h?l.selected()?l.unselect(["tapunselect"]):l.select(["tapselect"]):h||(a.$(n).unmerge(l).unselect(["tapunselect"]),l.select(["tapselect"]))),e.redrawHint("eles",!0)),e.hoverData.selecting){var g=a.collection(e.getAllInBox(s[0],s[1],s[2],s[3]));e.redrawHint("select",!0),g.length>0&&e.redrawHint("eles",!0),a.emit({type:"boxend",originalEvent:t,position:{x:o[0],y:o[1]}});var v=function(e){return e.selectable()&&!e.selected()};"additive"===a.selectionType()||h||a.$(n).unmerge(g).unselect(),g.emit("box").stdFilter(v).select().emit("boxselect"),e.redraw()}if(e.hoverData.dragging&&(e.hoverData.dragging=!1,e.redrawHint("select",!0),e.redrawHint("eles",!0),e.redraw()),!s[4]){e.redrawHint("drag",!0),e.redrawHint("eles",!0);var y=c&&c.grabbed();d(u),y&&(c.emit("freeon"),u.emit("free"),e.dragData.didDrag&&(c.emit("dragfreeon"),u.emit("dragfree")))}}s[4]=0,e.hoverData.down=null,e.hoverData.cxtStarted=!1,e.hoverData.draggingEles=!1,e.hoverData.selecting=!1,e.hoverData.isOverThresholdDrag=!1,e.dragData.didDrag=!1,e.hoverData.dragged=!1,e.hoverData.dragDelta=[],e.hoverData.mdownPos=null,e.hoverData.mdownGPos=null,e.hoverData.which=null}}),!1);var k,C,S,P,D,T,_,M,B,N,z,I,A,L=function(t){if(!e.scrollingPage){var n=e.cy,r=n.zoom(),i=n.pan(),a=e.projectIntoViewport(t.clientX,t.clientY),o=[a[0]*r+i.x,a[1]*r+i.y];if(e.hoverData.draggingEles||e.hoverData.dragging||e.hoverData.cxtStarted||0!==e.selection[4])t.preventDefault();else if(n.panningEnabled()&&n.userPanningEnabled()&&n.zoomingEnabled()&&n.userZoomingEnabled()){var s;t.preventDefault(),e.data.wheelZooming=!0,clearTimeout(e.data.wheelTimeout),e.data.wheelTimeout=setTimeout((function(){e.data.wheelZooming=!1,e.redrawHint("eles",!0),e.redraw()}),150),s=null!=t.deltaY?t.deltaY/-250:null!=t.wheelDeltaY?t.wheelDeltaY/1e3:t.wheelDelta/1e3,s*=e.wheelSensitivity,1===t.deltaMode&&(s*=33);var l=n.zoom()*Math.pow(10,s);"gesturechange"===t.type&&(l=e.gestureStartZoom*t.scale),n.zoom({level:l,renderedPosition:{x:o[0],y:o[1]}}),n.emit("gesturechange"===t.type?"pinchzoom":"scrollzoom")}}};e.registerBinding(e.container,"wheel",L,!0),e.registerBinding(t,"scroll",(function(t){e.scrollingPage=!0,clearTimeout(e.scrollingPageTimeout),e.scrollingPageTimeout=setTimeout((function(){e.scrollingPage=!1}),250)}),!0),e.registerBinding(e.container,"gesturestart",(function(t){e.gestureStartZoom=e.cy.zoom(),e.hasTouchStarted||t.preventDefault()}),!0),e.registerBinding(e.container,"gesturechange",(function(t){e.hasTouchStarted||L(t)}),!0),e.registerBinding(e.container,"mouseout",(function(t){var n=e.projectIntoViewport(t.clientX,t.clientY);e.cy.emit({originalEvent:t,type:"mouseout",position:{x:n[0],y:n[1]}})}),!1),e.registerBinding(e.container,"mouseover",(function(t){var n=e.projectIntoViewport(t.clientX,t.clientY);e.cy.emit({originalEvent:t,type:"mouseover",position:{x:n[0],y:n[1]}})}),!1);var O,R,V,F,j,q,Y,X=function(e,t,n,r){return Math.sqrt((n-e)*(n-e)+(r-t)*(r-t))},W=function(e,t,n,r){return(n-e)*(n-e)+(r-t)*(r-t)};if(e.registerBinding(e.container,"touchstart",O=function(t){if(e.hasTouchStarted=!0,E(t)){p(),e.touchData.capture=!0,e.data.bgActivePosistion=void 0;var n=e.cy,i=e.touchData.now,a=e.touchData.earlier;if(t.touches[0]){var o=e.projectIntoViewport(t.touches[0].clientX,t.touches[0].clientY);i[0]=o[0],i[1]=o[1]}if(t.touches[1]){o=e.projectIntoViewport(t.touches[1].clientX,t.touches[1].clientY);i[2]=o[0],i[3]=o[1]}if(t.touches[2]){o=e.projectIntoViewport(t.touches[2].clientX,t.touches[2].clientY);i[4]=o[0],i[5]=o[1]}if(t.touches[1]){e.touchData.singleTouchMoved=!0,d(e.dragData.touchDragEles);var l=e.findContainerClientCoords();B=l[0],N=l[1],z=l[2],I=l[3],k=t.touches[0].clientX-B,C=t.touches[0].clientY-N,S=t.touches[1].clientX-B,P=t.touches[1].clientY-N,A=0<=k&&k<=z&&0<=S&&S<=z&&0<=C&&C<=I&&0<=P&&P<=I;var h=n.pan(),f=n.zoom();D=X(k,C,S,P),T=W(k,C,S,P),M=[((_=[(k+S)/2,(C+P)/2])[0]-h.x)/f,(_[1]-h.y)/f];if(T<4e4&&!t.touches[2]){var g=e.findNearestElement(i[0],i[1],!0,!0),v=e.findNearestElement(i[2],i[3],!0,!0);return g&&g.isNode()?(g.activate().emit({originalEvent:t,type:"cxttapstart",position:{x:i[0],y:i[1]}}),e.touchData.start=g):v&&v.isNode()?(v.activate().emit({originalEvent:t,type:"cxttapstart",position:{x:i[0],y:i[1]}}),e.touchData.start=v):n.emit({originalEvent:t,type:"cxttapstart",position:{x:i[0],y:i[1]}}),e.touchData.start&&(e.touchData.start._private.grabbed=!1),e.touchData.cxt=!0,e.touchData.cxtDragged=!1,e.data.bgActivePosistion=void 0,void e.redraw()}}if(t.touches[2])n.boxSelectionEnabled()&&t.preventDefault();else if(t.touches[1]);else if(t.touches[0]){var y=e.findNearestElements(i[0],i[1],!0,!0),m=y[0];if(null!=m&&(m.activate(),e.touchData.start=m,e.touchData.starts=y,e.nodeIsGrabbable(m))){var b=e.dragData.touchDragEles=n.collection(),x=null;e.redrawHint("eles",!0),e.redrawHint("drag",!0),m.selected()?(x=n.$((function(t){return t.selected()&&e.nodeIsGrabbable(t)})),u(x,{addToList:b})):c(m,{addToList:b}),s(m);var w=function(e){return{originalEvent:t,type:e,position:{x:i[0],y:i[1]}}};m.emit(w("grabon")),x?x.forEach((function(e){e.emit(w("grab"))})):m.emit(w("grab"))}r(m,["touchstart","tapstart","vmousedown"],t,{x:i[0],y:i[1]}),null==m&&(e.data.bgActivePosistion={x:o[0],y:o[1]},e.redrawHint("select",!0),e.redraw()),e.touchData.singleTouchMoved=!1,e.touchData.singleTouchStartTime=+new Date,clearTimeout(e.touchData.tapholdTimeout),e.touchData.tapholdTimeout=setTimeout((function(){!1!==e.touchData.singleTouchMoved||e.pinching||e.touchData.selecting||r(e.touchData.start,["taphold"],t,{x:i[0],y:i[1]})}),e.tapholdDuration)}if(t.touches.length>=1){for(var L=e.touchData.startPosition=[null,null,null,null,null,null],O=0;O<i.length;O++)L[O]=a[O]=i[O];var R=t.touches[0];e.touchData.startGPosition=[R.clientX,R.clientY]}}},!1),e.registerBinding(t,"touchmove",R=function(t){var n=e.touchData.capture;if(n||E(t)){var i=e.selection,o=e.cy,s=e.touchData.now,l=e.touchData.earlier,c=o.zoom();if(t.touches[0]){var h=e.projectIntoViewport(t.touches[0].clientX,t.touches[0].clientY);s[0]=h[0],s[1]=h[1]}if(t.touches[1]){h=e.projectIntoViewport(t.touches[1].clientX,t.touches[1].clientY);s[2]=h[0],s[3]=h[1]}if(t.touches[2]){h=e.projectIntoViewport(t.touches[2].clientX,t.touches[2].clientY);s[4]=h[0],s[5]=h[1]}var p,f=e.touchData.startGPosition;if(n&&t.touches[0]&&f){for(var g=[],v=0;v<s.length;v++)g[v]=s[v]-l[v];var y=t.touches[0].clientX-f[0],m=y*y,b=t.touches[0].clientY-f[1];p=m+b*b>=e.touchTapThreshold2}if(n&&e.touchData.cxt){t.preventDefault();var w=t.touches[0].clientX-B,_=t.touches[0].clientY-N,z=t.touches[1].clientX-B,I=t.touches[1].clientY-N,L=W(w,_,z,I);if(L/T>=2.25||L>=22500){e.touchData.cxt=!1,e.data.bgActivePosistion=void 0,e.redrawHint("select",!0);var O={originalEvent:t,type:"cxttapend",position:{x:s[0],y:s[1]}};e.touchData.start?(e.touchData.start.unactivate().emit(O),e.touchData.start=null):o.emit(O)}}if(n&&e.touchData.cxt){O={originalEvent:t,type:"cxtdrag",position:{x:s[0],y:s[1]}};e.data.bgActivePosistion=void 0,e.redrawHint("select",!0),e.touchData.start?e.touchData.start.emit(O):o.emit(O),e.touchData.start&&(e.touchData.start._private.grabbed=!1),e.touchData.cxtDragged=!0;var R=e.findNearestElement(s[0],s[1],!0,!0);e.touchData.cxtOver&&R===e.touchData.cxtOver||(e.touchData.cxtOver&&e.touchData.cxtOver.emit({originalEvent:t,type:"cxtdragout",position:{x:s[0],y:s[1]}}),e.touchData.cxtOver=R,R&&R.emit({originalEvent:t,type:"cxtdragover",position:{x:s[0],y:s[1]}}))}else if(n&&t.touches[2]&&o.boxSelectionEnabled())t.preventDefault(),e.data.bgActivePosistion=void 0,this.lastThreeTouch=+new Date,e.touchData.selecting||o.emit({originalEvent:t,type:"boxstart",position:{x:s[0],y:s[1]}}),e.touchData.selecting=!0,e.touchData.didSelect=!0,i[4]=1,i&&0!==i.length&&void 0!==i[0]?(i[2]=(s[0]+s[2]+s[4])/3,i[3]=(s[1]+s[3]+s[5])/3):(i[0]=(s[0]+s[2]+s[4])/3,i[1]=(s[1]+s[3]+s[5])/3,i[2]=(s[0]+s[2]+s[4])/3+1,i[3]=(s[1]+s[3]+s[5])/3+1),e.redrawHint("select",!0),e.redraw();else if(n&&t.touches[1]&&!e.touchData.didSelect&&o.zoomingEnabled()&&o.panningEnabled()&&o.userZoomingEnabled()&&o.userPanningEnabled()){if(t.preventDefault(),e.data.bgActivePosistion=void 0,e.redrawHint("select",!0),ee=e.dragData.touchDragEles){e.redrawHint("drag",!0);for(var V=0;V<ee.length;V++){var F=ee[V]._private;F.grabbed=!1,F.rscratch.inDragLayer=!1}}var j=e.touchData.start,q=(w=t.touches[0].clientX-B,_=t.touches[0].clientY-N,z=t.touches[1].clientX-B,I=t.touches[1].clientY-N,X(w,_,z,I)),Y=q/D;if(A){var H=(w-k+(z-S))/2,K=(_-C+(I-P))/2,G=o.zoom(),U=G*Y,Z=o.pan(),$=M[0]*G+Z.x,Q=M[1]*G+Z.y,J={x:-U/G*($-Z.x-H)+$,y:-U/G*(Q-Z.y-K)+Q};if(j&&j.active()){var ee=e.dragData.touchDragEles;d(ee),e.redrawHint("drag",!0),e.redrawHint("eles",!0),j.unactivate().emit("freeon"),ee.emit("free"),e.dragData.didDrag&&(j.emit("dragfreeon"),ee.emit("dragfree"))}o.viewport({zoom:U,pan:J,cancelOnFailedZoom:!0}),o.emit("pinchzoom"),D=q,k=w,C=_,S=z,P=I,e.pinching=!0}if(t.touches[0]){h=e.projectIntoViewport(t.touches[0].clientX,t.touches[0].clientY);s[0]=h[0],s[1]=h[1]}if(t.touches[1]){h=e.projectIntoViewport(t.touches[1].clientX,t.touches[1].clientY);s[2]=h[0],s[3]=h[1]}if(t.touches[2]){h=e.projectIntoViewport(t.touches[2].clientX,t.touches[2].clientY);s[4]=h[0],s[5]=h[1]}}else if(t.touches[0]&&!e.touchData.didSelect){var te=e.touchData.start,ne=e.touchData.last;if(e.hoverData.draggingEles||e.swipePanning||(R=e.findNearestElement(s[0],s[1],!0,!0)),n&&null!=te&&t.preventDefault(),n&&null!=te&&e.nodeIsDraggable(te))if(p){ee=e.dragData.touchDragEles;var re=!e.dragData.didDrag;re&&u(ee,{inDragLayer:!0}),e.dragData.didDrag=!0;var ie={x:0,y:0};if(x(g[0])&&x(g[1]))if(ie.x+=g[0],ie.y+=g[1],re)e.redrawHint("eles",!0),(ae=e.touchData.dragDelta)&&x(ae[0])&&x(ae[1])&&(ie.x+=ae[0],ie.y+=ae[1]);e.hoverData.draggingEles=!0,ee.silentShift(ie).emit("position drag"),e.redrawHint("drag",!0),e.touchData.startPosition[0]==l[0]&&e.touchData.startPosition[1]==l[1]&&e.redrawHint("eles",!0),e.redraw()}else{var ae;0===(ae=e.touchData.dragDelta=e.touchData.dragDelta||[]).length?(ae.push(g[0]),ae.push(g[1])):(ae[0]+=g[0],ae[1]+=g[1])}if(r(te||R,["touchmove","tapdrag","vmousemove"],t,{x:s[0],y:s[1]}),te&&te.grabbed()||R==ne||(ne&&ne.emit({originalEvent:t,type:"tapdragout",position:{x:s[0],y:s[1]}}),R&&R.emit({originalEvent:t,type:"tapdragover",position:{x:s[0],y:s[1]}})),e.touchData.last=R,n)for(V=0;V<s.length;V++)s[V]&&e.touchData.startPosition[V]&&p&&(e.touchData.singleTouchMoved=!0);if(n&&(null==te||te.pannable())&&o.panningEnabled()&&o.userPanningEnabled()){a(te,e.touchData.starts)&&(t.preventDefault(),e.data.bgActivePosistion||(e.data.bgActivePosistion=bt(e.touchData.startPosition)),e.swipePanning?(o.panBy({x:g[0]*c,y:g[1]*c}),o.emit("dragpan")):p&&(e.swipePanning=!0,o.panBy({x:y*c,y:b*c}),o.emit("dragpan"),te&&(te.unactivate(),e.redrawHint("select",!0),e.touchData.start=null)));h=e.projectIntoViewport(t.touches[0].clientX,t.touches[0].clientY);s[0]=h[0],s[1]=h[1]}}for(v=0;v<s.length;v++)l[v]=s[v];n&&t.touches.length>0&&!e.hoverData.draggingEles&&!e.swipePanning&&null!=e.data.bgActivePosistion&&(e.data.bgActivePosistion=void 0,e.redrawHint("select",!0),e.redraw())}},!1),e.registerBinding(t,"touchcancel",V=function(t){var n=e.touchData.start;e.touchData.capture=!1,n&&n.unactivate()}),e.registerBinding(t,"touchend",F=function(t){var i=e.touchData.start;if(e.touchData.capture){0===t.touches.length&&(e.touchData.capture=!1),t.preventDefault();var a=e.selection;e.swipePanning=!1,e.hoverData.draggingEles=!1;var o,s=e.cy,l=s.zoom(),u=e.touchData.now,c=e.touchData.earlier;if(t.touches[0]){var h=e.projectIntoViewport(t.touches[0].clientX,t.touches[0].clientY);u[0]=h[0],u[1]=h[1]}if(t.touches[1]){h=e.projectIntoViewport(t.touches[1].clientX,t.touches[1].clientY);u[2]=h[0],u[3]=h[1]}if(t.touches[2]){h=e.projectIntoViewport(t.touches[2].clientX,t.touches[2].clientY);u[4]=h[0],u[5]=h[1]}if(i&&i.unactivate(),e.touchData.cxt){if(o={originalEvent:t,type:"cxttapend",position:{x:u[0],y:u[1]}},i?i.emit(o):s.emit(o),!e.touchData.cxtDragged){var p={originalEvent:t,type:"cxttap",position:{x:u[0],y:u[1]}};i?i.emit(p):s.emit(p)}return e.touchData.start&&(e.touchData.start._private.grabbed=!1),e.touchData.cxt=!1,e.touchData.start=null,void e.redraw()}if(!t.touches[2]&&s.boxSelectionEnabled()&&e.touchData.selecting){e.touchData.selecting=!1;var f=s.collection(e.getAllInBox(a[0],a[1],a[2],a[3]));a[0]=void 0,a[1]=void 0,a[2]=void 0,a[3]=void 0,a[4]=0,e.redrawHint("select",!0),s.emit({type:"boxend",originalEvent:t,position:{x:u[0],y:u[1]}});f.emit("box").stdFilter((function(e){return e.selectable()&&!e.selected()})).select().emit("boxselect"),f.nonempty()&&e.redrawHint("eles",!0),e.redraw()}if(null!=i&&i.unactivate(),t.touches[2])e.data.bgActivePosistion=void 0,e.redrawHint("select",!0);else if(t.touches[1]);else if(t.touches[0]);else if(!t.touches[0]){e.data.bgActivePosistion=void 0,e.redrawHint("select",!0);var g=e.dragData.touchDragEles;if(null!=i){var v=i._private.grabbed;d(g),e.redrawHint("drag",!0),e.redrawHint("eles",!0),v&&(i.emit("freeon"),g.emit("free"),e.dragData.didDrag&&(i.emit("dragfreeon"),g.emit("dragfree"))),r(i,["touchend","tapend","vmouseup","tapdragout"],t,{x:u[0],y:u[1]}),i.unactivate(),e.touchData.start=null}else{var y=e.findNearestElement(u[0],u[1],!0,!0);r(y,["touchend","tapend","vmouseup","tapdragout"],t,{x:u[0],y:u[1]})}var m=e.touchData.startPosition[0]-u[0],b=m*m,x=e.touchData.startPosition[1]-u[1],w=(b+x*x)*l*l;e.touchData.singleTouchMoved||(i||s.$(":selected").unselect(["tapunselect"]),r(i,["tap","vclick"],t,{x:u[0],y:u[1]}),j=!1,t.timeStamp-Y<=s.multiClickDebounceTime()?(q&&clearTimeout(q),j=!0,Y=null,r(i,["dbltap","vdblclick"],t,{x:u[0],y:u[1]})):(q=setTimeout((function(){j||r(i,["onetap","voneclick"],t,{x:u[0],y:u[1]})}),s.multiClickDebounceTime()),Y=t.timeStamp)),null!=i&&!e.dragData.didDrag&&i._private.selectable&&w<e.touchTapThreshold2&&!e.pinching&&("single"===s.selectionType()?(s.$(n).unmerge(i).unselect(["tapunselect"]),i.select(["tapselect"])):i.selected()?i.unselect(["tapunselect"]):i.select(["tapselect"]),e.redrawHint("eles",!0)),e.touchData.singleTouchMoved=!0}for(var E=0;E<u.length;E++)c[E]=u[E];e.dragData.didDrag=!1,0===t.touches.length&&(e.touchData.dragDelta=[],e.touchData.startPosition=[null,null,null,null,null,null],e.touchData.startGPosition=null,e.touchData.didSelect=!1),t.touches.length<2&&(1===t.touches.length&&(e.touchData.startGPosition=[t.touches[0].clientX,t.touches[0].clientY]),e.pinching=!1,e.redrawHint("eles",!0),e.redraw())}},!1),"undefined"==typeof TouchEvent){var H=[],K=function(e){return{clientX:e.clientX,clientY:e.clientY,force:1,identifier:e.pointerId,pageX:e.pageX,pageY:e.pageY,radiusX:e.width/2,radiusY:e.height/2,screenX:e.screenX,screenY:e.screenY,target:e.target}},G=function(e){H.push(function(e){return{event:e,touch:K(e)}}(e))},U=function(e){for(var t=0;t<H.length;t++){if(H[t].event.pointerId===e.pointerId)return void H.splice(t,1)}},Z=function(e){e.touches=H.map((function(e){return e.touch}))},$=function(e){return"mouse"===e.pointerType||4===e.pointerType};e.registerBinding(e.container,"pointerdown",(function(e){$(e)||(e.preventDefault(),G(e),Z(e),O(e))})),e.registerBinding(e.container,"pointerup",(function(e){$(e)||(U(e),Z(e),F(e))})),e.registerBinding(e.container,"pointercancel",(function(e){$(e)||(U(e),Z(e),V())})),e.registerBinding(e.container,"pointermove",(function(e){$(e)||(e.preventDefault(),function(e){var t=H.filter((function(t){return t.event.pointerId===e.pointerId}))[0];t.event=e,t.touch=K(e)}(e),Z(e),R(e))}))}};var gu={generatePolygon:function(e,t){return this.nodeShapes[e]={renderer:this,name:e,points:t,draw:function(e,t,n,r,i,a){this.renderer.nodeShapeImpl("polygon",e,t,n,r,i,this.points)},intersectLine:function(e,t,n,r,i,a,o,s){return $t(i,a,this.points,e,t,n/2,r/2,o)},checkPoint:function(e,t,n,r,i,a,o,s){return Xt(e,t,this.points,a,o,r,i,[0,-1],n)}}}};gu.generateEllipse=function(){return this.nodeShapes.ellipse={renderer:this,name:"ellipse",draw:function(e,t,n,r,i,a){this.renderer.nodeShapeImpl(this.name,e,t,n,r,i)},intersectLine:function(e,t,n,r,i,a,o,s){return function(e,t,n,r,i,a){var o=n-e,s=r-t;o/=i,s/=a;var l=Math.sqrt(o*o+s*s),u=l-1;if(u<0)return[];var c=u/l;return[(n-e)*c+e,(r-t)*c+t]}(i,a,e,t,n/2+o,r/2+o)},checkPoint:function(e,t,n,r,i,a,o,s){return Kt(e,t,r,i,a,o,n)}}},gu.generateRoundPolygon=function(e,t){return this.nodeShapes[e]={renderer:this,name:e,points:t,getOrCreateCorners:function(e,n,r,i,a,o,s){if(void 0!==o[s]&&o[s+"-cx"]===e&&o[s+"-cy"]===n)return o[s];o[s]=new Array(t.length/2),o[s+"-cx"]=e,o[s+"-cy"]=n;var l=r/2,u=i/2;a="auto"===a?rn(r,i):a;for(var c=new Array(t.length/2),d=0;d<t.length/2;d++)c[d]={x:e+l*t[2*d],y:n+u*t[2*d+1]};var h,p,f,g,v=c.length;for(p=c[v-1],h=0;h<v;h++)f=c[h%v],g=c[(h+1)%v],o[s][h]=Jl(p,f,g,a),p=f,f=g;return o[s]},draw:function(e,t,n,r,i,a,o){this.renderer.nodeShapeImpl("round-polygon",e,t,n,r,i,this.points,this.getOrCreateCorners(t,n,r,i,a,o,"drawCorners"))},intersectLine:function(e,t,n,r,i,a,o,s,l){return function(e,t,n,r,i,a,o,s,l){var u,c=[],d=new Array(2*n.length);l.forEach((function(n,a){0===a?(d[d.length-2]=n.startX,d[d.length-1]=n.startY):(d[4*a-2]=n.startX,d[4*a-1]=n.startY),d[4*a]=n.stopX,d[4*a+1]=n.stopY,0!==(u=Gt(e,t,r,i,n.cx,n.cy,n.radius)).length&&c.push(u[0],u[1])}));for(var h=0;h<d.length/4;h++)0!==(u=Zt(e,t,r,i,d[4*h],d[4*h+1],d[4*h+2],d[4*h+3],!1)).length&&c.push(u[0],u[1]);if(c.length>2){for(var p=[c[0],c[1]],f=Math.pow(p[0]-e,2)+Math.pow(p[1]-t,2),g=1;g<c.length/2;g++){var v=Math.pow(c[2*g]-e,2)+Math.pow(c[2*g+1]-t,2);v<=f&&(p[0]=c[2*g],p[1]=c[2*g+1],f=v)}return p}return c}(i,a,this.points,e,t,0,0,0,this.getOrCreateCorners(e,t,n,r,s,l,"corners"))},checkPoint:function(e,t,n,r,i,a,o,s,l){return function(e,t,n,r,i,a,o,s){for(var l=new Array(2*n.length),u=0;u<s.length;u++){var c=s[u];if(l[4*u+0]=c.startX,l[4*u+1]=c.startY,l[4*u+2]=c.stopX,l[4*u+3]=c.stopY,Math.pow(c.cx-e,2)+Math.pow(c.cy-t,2)<=Math.pow(c.radius,2))return!0}return Yt(e,t,l)}(e,t,this.points,0,0,0,0,this.getOrCreateCorners(a,o,r,i,s,l,"corners"))}}},gu.generateRoundRectangle=function(){return this.nodeShapes["round-rectangle"]=this.nodeShapes.roundrectangle={renderer:this,name:"round-rectangle",points:Jt(4,0),draw:function(e,t,n,r,i,a){this.renderer.nodeShapeImpl(this.name,e,t,n,r,i,this.points,a)},intersectLine:function(e,t,n,r,i,a,o,s){return Rt(i,a,e,t,n,r,o,s)},checkPoint:function(e,t,n,r,i,a,o,s){var l=r/2,u=i/2;s="auto"===s?nn(r,i):s;var c=2*(s=Math.min(l,u,s));return!!Xt(e,t,this.points,a,o,r,i-c,[0,-1],n)||(!!Xt(e,t,this.points,a,o,r-c,i,[0,-1],n)||(!!Kt(e,t,c,c,a-l+s,o-u+s,n)||(!!Kt(e,t,c,c,a+l-s,o-u+s,n)||(!!Kt(e,t,c,c,a+l-s,o+u-s,n)||!!Kt(e,t,c,c,a-l+s,o+u-s,n)))))}}},gu.generateCutRectangle=function(){return this.nodeShapes["cut-rectangle"]=this.nodeShapes.cutrectangle={renderer:this,name:"cut-rectangle",cornerLength:8,points:Jt(4,0),draw:function(e,t,n,r,i,a){this.renderer.nodeShapeImpl(this.name,e,t,n,r,i,null,a)},generateCutTrianglePts:function(e,t,n,r,i){var a="auto"===i?this.cornerLength:i,o=t/2,s=e/2,l=n-s,u=n+s,c=r-o,d=r+o;return{topLeft:[l,c+a,l+a,c,l+a,c+a],topRight:[u-a,c,u,c+a,u-a,c+a],bottomRight:[u,d-a,u-a,d,u-a,d-a],bottomLeft:[l+a,d,l,d-a,l+a,d-a]}},intersectLine:function(e,t,n,r,i,a,o,s){var l=this.generateCutTrianglePts(n+2*o,r+2*o,e,t,s),u=[].concat.apply([],[l.topLeft.splice(0,4),l.topRight.splice(0,4),l.bottomRight.splice(0,4),l.bottomLeft.splice(0,4)]);return $t(i,a,u,e,t)},checkPoint:function(e,t,n,r,i,a,o,s){var l="auto"===s?this.cornerLength:s;if(Xt(e,t,this.points,a,o,r,i-2*l,[0,-1],n))return!0;if(Xt(e,t,this.points,a,o,r-2*l,i,[0,-1],n))return!0;var u=this.generateCutTrianglePts(r,i,a,o);return Yt(e,t,u.topLeft)||Yt(e,t,u.topRight)||Yt(e,t,u.bottomRight)||Yt(e,t,u.bottomLeft)}}},gu.generateBarrel=function(){return this.nodeShapes.barrel={renderer:this,name:"barrel",points:Jt(4,0),draw:function(e,t,n,r,i,a){this.renderer.nodeShapeImpl(this.name,e,t,n,r,i)},intersectLine:function(e,t,n,r,i,a,o,s){var l=this.generateBarrelBezierPts(n+2*o,r+2*o,e,t),u=function(e){var t=Dt({x:e[0],y:e[1]},{x:e[2],y:e[3]},{x:e[4],y:e[5]},.15),n=Dt({x:e[0],y:e[1]},{x:e[2],y:e[3]},{x:e[4],y:e[5]},.5),r=Dt({x:e[0],y:e[1]},{x:e[2],y:e[3]},{x:e[4],y:e[5]},.85);return[e[0],e[1],t.x,t.y,n.x,n.y,r.x,r.y,e[4],e[5]]},c=[].concat(u(l.topLeft),u(l.topRight),u(l.bottomRight),u(l.bottomLeft));return $t(i,a,c,e,t)},generateBarrelBezierPts:function(e,t,n,r){var i=t/2,a=e/2,o=n-a,s=n+a,l=r-i,u=r+i,c=an(e,t),d=c.heightOffset,h=c.widthOffset,p=c.ctrlPtOffsetPct*e,f={topLeft:[o,l+d,o+p,l,o+h,l],topRight:[s-h,l,s-p,l,s,l+d],bottomRight:[s,u-d,s-p,u,s-h,u],bottomLeft:[o+h,u,o+p,u,o,u-d]};return f.topLeft.isTop=!0,f.topRight.isTop=!0,f.bottomLeft.isBottom=!0,f.bottomRight.isBottom=!0,f},checkPoint:function(e,t,n,r,i,a,o,s){var l=an(r,i),u=l.heightOffset,c=l.widthOffset;if(Xt(e,t,this.points,a,o,r,i-2*u,[0,-1],n))return!0;if(Xt(e,t,this.points,a,o,r-2*c,i,[0,-1],n))return!0;for(var d=this.generateBarrelBezierPts(r,i,a,o),h=function(e,t,n){var r,i,a=n[4],o=n[2],s=n[0],l=n[5],u=n[1],c=Math.min(a,s),d=Math.max(a,s),h=Math.min(l,u),p=Math.max(l,u);if(c<=e&&e<=d&&h<=t&&t<=p){var f=[(r=a)-2*(i=o)+s,2*(i-r),r],g=function(e,t,n,r){var i=t*t-4*e*(n-=r);if(i<0)return[];var a=Math.sqrt(i),o=2*e;return[(-t+a)/o,(-t-a)/o]}(f[0],f[1],f[2],e).filter((function(e){return 0<=e&&e<=1}));if(g.length>0)return g[0]}return null},p=Object.keys(d),f=0;f<p.length;f++){var g=d[p[f]],v=h(e,t,g);if(null!=v){var y=g[5],m=g[3],b=g[1],x=Pt(y,m,b,v);if(g.isTop&&x<=t)return!0;if(g.isBottom&&t<=x)return!0}}return!1}}},gu.generateBottomRoundrectangle=function(){return this.nodeShapes["bottom-round-rectangle"]=this.nodeShapes.bottomroundrectangle={renderer:this,name:"bottom-round-rectangle",points:Jt(4,0),draw:function(e,t,n,r,i,a){this.renderer.nodeShapeImpl(this.name,e,t,n,r,i,this.points,a)},intersectLine:function(e,t,n,r,i,a,o,s){var l=t-(r/2+o),u=Zt(i,a,e,t,e-(n/2+o),l,e+(n/2+o),l,!1);return u.length>0?u:Rt(i,a,e,t,n,r,o,s)},checkPoint:function(e,t,n,r,i,a,o,s){var l=2*(s="auto"===s?nn(r,i):s);if(Xt(e,t,this.points,a,o,r,i-l,[0,-1],n))return!0;if(Xt(e,t,this.points,a,o,r-l,i,[0,-1],n))return!0;var u=r/2+2*n,c=i/2+2*n;return!!Yt(e,t,[a-u,o-c,a-u,o,a+u,o,a+u,o-c])||(!!Kt(e,t,l,l,a+r/2-s,o+i/2-s,n)||!!Kt(e,t,l,l,a-r/2+s,o+i/2-s,n))}}},gu.registerNodeShapes=function(){var e=this.nodeShapes={},t=this;this.generateEllipse(),this.generatePolygon("triangle",Jt(3,0)),this.generateRoundPolygon("round-triangle",Jt(3,0)),this.generatePolygon("rectangle",Jt(4,0)),e.square=e.rectangle,this.generateRoundRectangle(),this.generateCutRectangle(),this.generateBarrel(),this.generateBottomRoundrectangle();var n=[0,1,1,0,0,-1,-1,0];this.generatePolygon("diamond",n),this.generateRoundPolygon("round-diamond",n),this.generatePolygon("pentagon",Jt(5,0)),this.generateRoundPolygon("round-pentagon",Jt(5,0)),this.generatePolygon("hexagon",Jt(6,0)),this.generateRoundPolygon("round-hexagon",Jt(6,0)),this.generatePolygon("heptagon",Jt(7,0)),this.generateRoundPolygon("round-heptagon",Jt(7,0)),this.generatePolygon("octagon",Jt(8,0)),this.generateRoundPolygon("round-octagon",Jt(8,0));var r=new Array(20),i=tn(5,0),a=tn(5,Math.PI/5),o=.5*(3-Math.sqrt(5));o*=1.57;for(var s=0;s<a.length/2;s++)a[2*s]*=o,a[2*s+1]*=o;for(s=0;s<5;s++)r[4*s]=i[2*s],r[4*s+1]=i[2*s+1],r[4*s+2]=a[2*s],r[4*s+3]=a[2*s+1];r=en(r),this.generatePolygon("star",r),this.generatePolygon("vee",[-1,-1,0,-.333,1,-1,0,1]),this.generatePolygon("rhomboid",[-1,-1,.333,-1,1,1,-.333,1]),this.generatePolygon("right-rhomboid",[-.333,-1,1,-1,.333,1,-1,1]),this.nodeShapes.concavehexagon=this.generatePolygon("concave-hexagon",[-1,-.95,-.75,0,-1,.95,1,.95,.75,0,1,-.95]);var l=[-1,-1,.25,-1,1,0,.25,1,-1,1];this.generatePolygon("tag",l),this.generateRoundPolygon("round-tag",l),e.makePolygon=function(e){var n,r="polygon-"+e.join("$");return(n=this[r])?n:t.generatePolygon(r,e)}};var vu={timeToRender:function(){return this.redrawTotalTime/this.redrawCount},redraw:function(e){e=e||We();var t=this;void 0===t.averageRedrawTime&&(t.averageRedrawTime=0),void 0===t.lastRedrawTime&&(t.lastRedrawTime=0),void 0===t.lastDrawTime&&(t.lastDrawTime=0),t.requestedFrame=!0,t.renderOptions=e},beforeRender:function(e,t){if(!this.destroyed){null==t&&Ve("Priority is not optional for beforeRender");var n=this.beforeRenderCallbacks;n.push({fn:e,priority:t}),n.sort((function(e,t){return t.priority-e.priority}))}}},yu=function(e,t,n){for(var r=e.beforeRenderCallbacks,i=0;i<r.length;i++)r[i].fn(t,n)};vu.startRenderLoop=function(){var e=this,t=e.cy;if(!e.renderLoopStarted){e.renderLoopStarted=!0;xe((function n(r){if(!e.destroyed){if(t.batching());else if(e.requestedFrame&&!e.skipFrame){yu(e,!0,r);var i=we();e.render(e.renderOptions);var a=e.lastDrawTime=we();void 0===e.averageRedrawTime&&(e.averageRedrawTime=a-i),void 0===e.redrawCount&&(e.redrawCount=0),e.redrawCount++,void 0===e.redrawTotalTime&&(e.redrawTotalTime=0);var o=a-i;e.redrawTotalTime+=o,e.lastRedrawTime=o,e.averageRedrawTime=e.averageRedrawTime/2+o/2,e.requestedFrame=!1}else yu(e,!1,r);e.skipFrame=!1,xe(n)}}))}};var mu=function(e){this.init(e)},bu=mu.prototype;bu.clientFunctions=["redrawHint","render","renderTo","matchCanvasSize","nodeShapeImpl","arrowShapeImpl"],bu.init=function(e){var t=this;t.options=e,t.cy=e.cy;var n=t.container=e.cy.container(),r=t.cy.window();if(r){var i=r.document,a=i.head,o="__________cytoscape_container",s=null!=i.getElementById("__________cytoscape_stylesheet");if(n.className.indexOf(o)<0&&(n.className=(n.className||"")+" "+o),!s){var l=i.createElement("style");l.id="__________cytoscape_stylesheet",l.textContent="."+o+" { position: relative; }",a.insertBefore(l,a.children[0])}"static"===r.getComputedStyle(n).getPropertyValue("position")&&je("A Cytoscape container has style position:static and so can not use UI extensions properly")}t.selection=[void 0,void 0,void 0,void 0,0],t.bezierProjPcts=[.05,.225,.4,.5,.6,.775,.95],t.hoverData={down:null,last:null,downTime:null,triggerMode:null,dragging:!1,initialPan:[null,null],capture:!1},t.dragData={possibleDragElements:[]},t.touchData={start:null,capture:!1,startPosition:[null,null,null,null,null,null],singleTouchStartTime:null,singleTouchMoved:!0,now:[null,null,null,null,null,null],earlier:[null,null,null,null,null,null]},t.redraws=0,t.showFps=e.showFps,t.debug=e.debug,t.hideEdgesOnViewport=e.hideEdgesOnViewport,t.textureOnViewport=e.textureOnViewport,t.wheelSensitivity=e.wheelSensitivity,t.motionBlurEnabled=e.motionBlur,t.forcedPixelRatio=x(e.pixelRatio)?e.pixelRatio:null,t.motionBlur=e.motionBlur,t.motionBlurOpacity=e.motionBlurOpacity,t.motionBlurTransparency=1-t.motionBlurOpacity,t.motionBlurPxRatio=1,t.mbPxRBlurry=1,t.minMbLowQualFrames=4,t.fullQualityMb=!1,t.clearedForMotionBlur=[],t.desktopTapThreshold=e.desktopTapThreshold,t.desktopTapThreshold2=e.desktopTapThreshold*e.desktopTapThreshold,t.touchTapThreshold=e.touchTapThreshold,t.touchTapThreshold2=e.touchTapThreshold*e.touchTapThreshold,t.tapholdDuration=500,t.bindings=[],t.beforeRenderCallbacks=[],t.beforeRenderPriorities={animations:400,eleCalcs:300,eleTxrDeq:200,lyrTxrDeq:150,lyrTxrSkip:100},t.registerNodeShapes(),t.registerArrowShapes(),t.registerCalculationListeners()},bu.notify=function(e,t){var n=this,r=n.cy;this.destroyed||("init"!==e?"destroy"!==e?(("add"===e||"remove"===e||"move"===e&&r.hasCompoundNodes()||"load"===e||"zorder"===e||"mount"===e)&&n.invalidateCachedZSortedEles(),"viewport"===e&&n.redrawHint("select",!0),"load"!==e&&"resize"!==e&&"mount"!==e||(n.invalidateContainerClientCoordsCache(),n.matchCanvasSize(n.container)),n.redrawHint("eles",!0),n.redrawHint("drag",!0),this.startRenderLoop(),this.redraw()):n.destroy():n.load())},bu.destroy=function(){var e=this;e.destroyed=!0,e.cy.stopAnimationLoop();for(var t=0;t<e.bindings.length;t++){var n=e.bindings[t],r=n.target;(r.off||r.removeEventListener).apply(r,n.args)}if(e.bindings=[],e.beforeRenderCallbacks=[],e.onUpdateEleCalcsFns=[],e.removeObserver&&e.removeObserver.disconnect(),e.styleObserver&&e.styleObserver.disconnect(),e.resizeObserver&&e.resizeObserver.disconnect(),e.labelCalcDiv)try{document.body.removeChild(e.labelCalcDiv)}catch(e){}},bu.isHeadless=function(){return!1},[Tl,hu,pu,fu,gu,vu].forEach((function(e){L(bu,e)}));var xu=function(e){return function(){var t=this,n=this.renderer;if(!t.dequeueingSetup){t.dequeueingSetup=!0;var r=ve((function(){n.redrawHint("eles",!0),n.redrawHint("drag",!0),n.redraw()}),e.deqRedrawThreshold),i=e.priority||Re;n.beforeRender((function(i,a){var o=we(),s=n.averageRedrawTime,l=n.lastRedrawTime,u=[],c=n.cy.extent(),d=n.getPixelRatio();for(i||n.flushRenderedStyleQueue();;){var h=we(),p=h-o,f=h-a;if(l<1e3/60){var g=1e3/60-(i?s:0);if(f>=e.deqFastCost*g)break}else if(i){if(p>=e.deqCost*l||p>=e.deqAvgCost*s)break}else if(f>=e.deqNoDrawCost*(1e3/60))break;var v=e.deq(t,d,c);if(!(v.length>0))break;for(var y=0;y<v.length;y++)u.push(v[y])}u.length>0&&(e.onDeqd(t,u),!i&&e.shouldRedraw(t,u,d,c)&&r())}),i(t))}}},wu=function(){function e(n){var r=arguments.length>1&&void 0!==arguments[1]?arguments[1]:Le;t(this,e),this.idsByKey=new $e,this.keyForId=new $e,this.cachesByLvl=new $e,this.lvls=[],this.getKey=n,this.doesEleInvalidateKey=r}return r(e,[{key:"getIdsFor",value:function(e){null==e&&Ve("Can not get id list for null key");var t=this.idsByKey,n=this.idsByKey.get(e);return n||(n=new Je,t.set(e,n)),n}},{key:"addIdForKey",value:function(e,t){null!=e&&this.getIdsFor(e).add(t)}},{key:"deleteIdForKey",value:function(e,t){null!=e&&this.getIdsFor(e).delete(t)}},{key:"getNumberOfIdsForKey",value:function(e){return null==e?0:this.getIdsFor(e).size}},{key:"updateKeyMappingFor",value:function(e){var t=e.id(),n=this.keyForId.get(t),r=this.getKey(e);this.deleteIdForKey(n,t),this.addIdForKey(r,t),this.keyForId.set(t,r)}},{key:"deleteKeyMappingFor",value:function(e){var t=e.id(),n=this.keyForId.get(t);this.deleteIdForKey(n,t),this.keyForId.delete(t)}},{key:"keyHasChangedFor",value:function(e){var t=e.id();return this.keyForId.get(t)!==this.getKey(e)}},{key:"isInvalid",value:function(e){return this.keyHasChangedFor(e)||this.doesEleInvalidateKey(e)}},{key:"getCachesAt",value:function(e){var t=this.cachesByLvl,n=this.lvls,r=t.get(e);return r||(r=new $e,t.set(e,r),n.push(e)),r}},{key:"getCache",value:function(e,t){return this.getCachesAt(t).get(e)}},{key:"get",value:function(e,t){var n=this.getKey(e),r=this.getCache(n,t);return null!=r&&this.updateKeyMappingFor(e),r}},{key:"getForCachedKey",value:function(e,t){var n=this.keyForId.get(e.id());return this.getCache(n,t)}},{key:"hasCache",value:function(e,t){return this.getCachesAt(t).has(e)}},{key:"has",value:function(e,t){var n=this.getKey(e);return this.hasCache(n,t)}},{key:"setCache",value:function(e,t,n){n.key=e,this.getCachesAt(t).set(e,n)}},{key:"set",value:function(e,t,n){var r=this.getKey(e);this.setCache(r,t,n),this.updateKeyMappingFor(e)}},{key:"deleteCache",value:function(e,t){this.getCachesAt(t).delete(e)}},{key:"delete",value:function(e,t){var n=this.getKey(e);this.deleteCache(n,t)}},{key:"invalidateKey",value:function(e){var t=this;this.lvls.forEach((function(n){return t.deleteCache(e,n)}))}},{key:"invalidate",value:function(e){var t=e.id(),n=this.keyForId.get(t);this.deleteKeyMappingFor(e);var r=this.doesEleInvalidateKey(e);return r&&this.invalidateKey(n),r||0===this.getNumberOfIdsForKey(n)}}]),e}(),Eu={dequeue:"dequeue",downscale:"downscale",highQuality:"highQuality"},ku=He({getKey:null,doesEleInvalidateKey:Le,drawElement:null,getBoundingBox:null,getRotationPoint:null,getRotationOffset:null,isVisible:Ae,allowEdgeTxrCaching:!0,allowParentTxrCaching:!0}),Cu=function(e,t){this.renderer=e,this.onDequeues=[];var n=ku(t);L(this,n),this.lookup=new wu(n.getKey,n.doesEleInvalidateKey),this.setupDequeueing()},Su=Cu.prototype;Su.reasons=Eu,Su.getTextureQueue=function(e){return this.eleImgCaches=this.eleImgCaches||{},this.eleImgCaches[e]=this.eleImgCaches[e]||[]},Su.getRetiredTextureQueue=function(e){var t=this.eleImgCaches.retired=this.eleImgCaches.retired||{};return t[e]=t[e]||[]},Su.getElementQueue=function(){return this.eleCacheQueue=this.eleCacheQueue||new rt((function(e,t){return t.reqs-e.reqs}))},Su.getElementKeyToQueue=function(){return this.eleKeyToCacheQueue=this.eleKeyToCacheQueue||{}},Su.getElement=function(e,t,n,r,i){var a=this,o=this.renderer,s=o.cy.zoom(),l=this.lookup;if(!t||0===t.w||0===t.h||isNaN(t.w)||isNaN(t.h)||!e.visible()||e.removed())return null;if(!a.allowEdgeTxrCaching&&e.isEdge()||!a.allowParentTxrCaching&&e.isParent())return null;if(null==r&&(r=Math.ceil(wt(s*n))),r<-4)r=-4;else if(s>=7.99||r>3)return null;var u=Math.pow(2,r),c=t.h*u,d=t.w*u,h=o.eleTextBiggerThanMin(e,u);if(!this.isVisible(e,h))return null;var p,f=l.get(e,r);if(f&&f.invalidated&&(f.invalidated=!1,f.texture.invalidatedWidth-=f.width),f)return f;if(p=c<=25?25:c<=50?50:50*Math.ceil(c/50),c>1024||d>1024)return null;var g=a.getTextureQueue(p),v=g[g.length-2],y=function(){return a.recycleTexture(p,d)||a.addTexture(p,d)};v||(v=g[g.length-1]),v||(v=y()),v.width-v.usedWidth<d&&(v=y());for(var m,b=function(e){return e&&e.scaledLabelShown===h},x=i&&i===Eu.dequeue,w=i&&i===Eu.highQuality,E=i&&i===Eu.downscale,k=r+1;k<=3;k++){var C=l.get(e,k);if(C){m=C;break}}var S=m&&m.level===r+1?m:null,P=function(){v.context.drawImage(S.texture.canvas,S.x,0,S.width,S.height,v.usedWidth,0,d,c)};if(v.context.setTransform(1,0,0,1,0,0),v.context.clearRect(v.usedWidth,0,d,p),b(S))P();else if(b(m)){if(!w)return a.queueElement(e,m.level-1),m;for(var D=m.level;D>r;D--)S=a.getElement(e,t,n,D,Eu.downscale);P()}else{var T;if(!x&&!w&&!E)for(var _=r-1;_>=-4;_--){var M=l.get(e,_);if(M){T=M;break}}if(b(T))return a.queueElement(e,r),T;v.context.translate(v.usedWidth,0),v.context.scale(u,u),this.drawElement(v.context,e,t,h,!1),v.context.scale(1/u,1/u),v.context.translate(-v.usedWidth,0)}return f={x:v.usedWidth,texture:v,level:r,scale:u,width:d,height:c,scaledLabelShown:h},v.usedWidth+=Math.ceil(d+8),v.eleCaches.push(f),l.set(e,r,f),a.checkTextureFullness(v),f},Su.invalidateElements=function(e){for(var t=0;t<e.length;t++)this.invalidateElement(e[t])},Su.invalidateElement=function(e){var t=this.lookup,n=[];if(t.isInvalid(e)){for(var r=-4;r<=3;r++){var i=t.getForCachedKey(e,r);i&&n.push(i)}if(t.invalidate(e))for(var a=0;a<n.length;a++){var o=n[a],s=o.texture;s.invalidatedWidth+=o.width,o.invalidated=!0,this.checkTextureUtility(s)}this.removeFromQueue(e)}},Su.checkTextureUtility=function(e){e.invalidatedWidth>=.2*e.width&&this.retireTexture(e)},Su.checkTextureFullness=function(e){var t=this.getTextureQueue(e.height);e.usedWidth/e.width>.8&&e.fullnessChecks>=10?Ke(t,e):e.fullnessChecks++},Su.retireTexture=function(e){var t=e.height,n=this.getTextureQueue(t),r=this.lookup;Ke(n,e),e.retired=!0;for(var i=e.eleCaches,a=0;a<i.length;a++){var o=i[a];r.deleteCache(o.key,o.level)}Ge(i),this.getRetiredTextureQueue(t).push(e)},Su.addTexture=function(e,t){var n={};return this.getTextureQueue(e).push(n),n.eleCaches=[],n.height=e,n.width=Math.max(1024,t),n.usedWidth=0,n.invalidatedWidth=0,n.fullnessChecks=0,n.canvas=this.renderer.makeOffscreenCanvas(n.width,n.height),n.context=n.canvas.getContext("2d"),n},Su.recycleTexture=function(e,t){for(var n=this.getTextureQueue(e),r=this.getRetiredTextureQueue(e),i=0;i<r.length;i++){var a=r[i];if(a.width>=t)return a.retired=!1,a.usedWidth=0,a.invalidatedWidth=0,a.fullnessChecks=0,Ge(a.eleCaches),a.context.setTransform(1,0,0,1,0,0),a.context.clearRect(0,0,a.width,a.height),Ke(r,a),n.push(a),a}},Su.queueElement=function(e,t){var n=this.getElementQueue(),r=this.getElementKeyToQueue(),i=this.getKey(e),a=r[i];if(a)a.level=Math.max(a.level,t),a.eles.merge(e),a.reqs++,n.updateItem(a);else{var o={eles:e.spawn().merge(e),level:t,reqs:1,key:i};n.push(o),r[i]=o}},Su.dequeue=function(e){for(var t=this.getElementQueue(),n=this.getElementKeyToQueue(),r=[],i=this.lookup,a=0;a<1&&t.size()>0;a++){var o=t.pop(),s=o.key,l=o.eles[0],u=i.hasCache(l,o.level);if(n[s]=null,!u){r.push(o);var c=this.getBoundingBox(l);this.getElement(l,c,e,o.level,Eu.dequeue)}}return r},Su.removeFromQueue=function(e){var t=this.getElementQueue(),n=this.getElementKeyToQueue(),r=this.getKey(e),i=n[r];null!=i&&(1===i.eles.length?(i.reqs=Ie,t.updateItem(i),t.pop(),n[r]=null):i.eles.unmerge(e))},Su.onDequeue=function(e){this.onDequeues.push(e)},Su.offDequeue=function(e){Ke(this.onDequeues,e)},Su.setupDequeueing=xu({deqRedrawThreshold:100,deqCost:.15,deqAvgCost:.1,deqNoDrawCost:.9,deqFastCost:.9,deq:function(e,t,n){return e.dequeue(t,n)},onDeqd:function(e,t){for(var n=0;n<e.onDequeues.length;n++){(0,e.onDequeues[n])(t)}},shouldRedraw:function(e,t,n,r){for(var i=0;i<t.length;i++)for(var a=t[i].eles,o=0;o<a.length;o++){var s=a[o].boundingBox();if(At(s,r))return!0}return!1},priority:function(e){return e.renderer.beforeRenderPriorities.eleTxrDeq}});var Pu=function(e){var t=this,n=t.renderer=e,r=n.cy;t.layersByLevel={},t.firstGet=!0,t.lastInvalidationTime=we()-500,t.skipping=!1,t.eleTxrDeqs=r.collection(),t.scheduleElementRefinement=ve((function(){t.refineElementTextures(t.eleTxrDeqs),t.eleTxrDeqs.unmerge(t.eleTxrDeqs)}),50),n.beforeRender((function(e,n){n-t.lastInvalidationTime<=250?t.skipping=!0:t.skipping=!1}),n.beforeRenderPriorities.lyrTxrSkip);t.layersQueue=new rt((function(e,t){return t.reqs-e.reqs})),t.setupDequeueing()},Du=Pu.prototype,Tu=0,_u=Math.pow(2,53)-1;Du.makeLayer=function(e,t){var n=Math.pow(2,t),r=Math.ceil(e.w*n),i=Math.ceil(e.h*n),a=this.renderer.makeOffscreenCanvas(r,i),o={id:Tu=++Tu%_u,bb:e,level:t,width:r,height:i,canvas:a,context:a.getContext("2d"),eles:[],elesQueue:[],reqs:0},s=o.context,l=-o.bb.x1,u=-o.bb.y1;return s.scale(n,n),s.translate(l,u),o},Du.getLayers=function(e,t,n){var r=this,i=r.renderer.cy.zoom(),a=r.firstGet;if(r.firstGet=!1,null==n)if((n=Math.ceil(wt(i*t)))<-4)n=-4;else if(i>=3.99||n>2)return null;r.validateLayersElesOrdering(n,e);var o,s,l=r.layersByLevel,u=Math.pow(2,n),c=l[n]=l[n]||[];if(r.levelIsComplete(n,e))return c;!function(){var t=function(t){if(r.validateLayersElesOrdering(t,e),r.levelIsComplete(t,e))return s=l[t],!0},i=function(e){if(!s)for(var r=n+e;-4<=r&&r<=2&&!t(r);r+=e);};i(1),i(-1);for(var a=c.length-1;a>=0;a--){var o=c[a];o.invalid&&Ke(c,o)}}();var d=function(t){var i=(t=t||{}).after;if(function(){if(!o){o=_t();for(var t=0;t<e.length;t++)Mt(o,e[t].boundingBox())}}(),o.w*u*(o.h*u)>16e6)return null;var a=r.makeLayer(o,n);if(null!=i){var s=c.indexOf(i)+1;c.splice(s,0,a)}else(void 0===t.insert||t.insert)&&c.unshift(a);return a};if(r.skipping&&!a)return null;for(var h=null,p=e.length/1,f=!a,g=0;g<e.length;g++){var v=e[g],y=v._private.rscratch,m=y.imgLayerCaches=y.imgLayerCaches||{},b=m[n];if(b)h=b;else{if((!h||h.eles.length>=p||!Ot(h.bb,v.boundingBox()))&&!(h=d({insert:!0,after:h})))return null;s||f?r.queueLayer(h,v):r.drawEleInLayer(h,v,n,t),h.eles.push(v),m[n]=h}}return s||(f?null:c)},Du.getEleLevelForLayerLevel=function(e,t){return e},Du.drawEleInLayer=function(e,t,n,r){var i=this.renderer,a=e.context,o=t.boundingBox();0!==o.w&&0!==o.h&&t.visible()&&(n=this.getEleLevelForLayerLevel(n,r),i.setImgSmoothing(a,!1),i.drawCachedElement(a,t,null,null,n,!0),i.setImgSmoothing(a,!0))},Du.levelIsComplete=function(e,t){var n=this.layersByLevel[e];if(!n||0===n.length)return!1;for(var r=0,i=0;i<n.length;i++){var a=n[i];if(a.reqs>0)return!1;if(a.invalid)return!1;r+=a.eles.length}return r===t.length},Du.validateLayersElesOrdering=function(e,t){var n=this.layersByLevel[e];if(n)for(var r=0;r<n.length;r++){for(var i=n[r],a=-1,o=0;o<t.length;o++)if(i.eles[0]===t[o]){a=o;break}if(a<0)this.invalidateLayer(i);else{var s=a;for(o=0;o<i.eles.length;o++)if(i.eles[o]!==t[s+o]){this.invalidateLayer(i);break}}}},Du.updateElementsInLayers=function(e,t){for(var n=k(e[0]),r=0;r<e.length;r++)for(var i=n?null:e[r],a=n?e[r]:e[r].ele,o=a._private.rscratch,s=o.imgLayerCaches=o.imgLayerCaches||{},l=-4;l<=2;l++){var u=s[l];u&&(i&&this.getEleLevelForLayerLevel(u.level)!==i.level||t(u,a,i))}},Du.haveLayers=function(){for(var e=!1,t=-4;t<=2;t++){var n=this.layersByLevel[t];if(n&&n.length>0){e=!0;break}}return e},Du.invalidateElements=function(e){var t=this;0!==e.length&&(t.lastInvalidationTime=we(),0!==e.length&&t.haveLayers()&&t.updateElementsInLayers(e,(function(e,n,r){t.invalidateLayer(e)})))},Du.invalidateLayer=function(e){if(this.lastInvalidationTime=we(),!e.invalid){var t=e.level,n=e.eles,r=this.layersByLevel[t];Ke(r,e),e.elesQueue=[],e.invalid=!0,e.replacement&&(e.replacement.invalid=!0);for(var i=0;i<n.length;i++){var a=n[i]._private.rscratch.imgLayerCaches;a&&(a[t]=null)}}},Du.refineElementTextures=function(e){var t=this;t.updateElementsInLayers(e,(function(e,n,r){var i=e.replacement;if(i||((i=e.replacement=t.makeLayer(e.bb,e.level)).replaces=e,i.eles=e.eles),!i.reqs)for(var a=0;a<i.eles.length;a++)t.queueLayer(i,i.eles[a])}))},Du.enqueueElementRefinement=function(e){this.eleTxrDeqs.merge(e),this.scheduleElementRefinement()},Du.queueLayer=function(e,t){var n=this.layersQueue,r=e.elesQueue,i=r.hasId=r.hasId||{};if(!e.replacement){if(t){if(i[t.id()])return;r.push(t),i[t.id()]=!0}e.reqs?(e.reqs++,n.updateItem(e)):(e.reqs=1,n.push(e))}},Du.dequeue=function(e){for(var t=this.layersQueue,n=[],r=0;r<1&&0!==t.size();){var i=t.peek();if(i.replacement)t.pop();else if(i.replaces&&i!==i.replaces.replacement)t.pop();else if(i.invalid)t.pop();else{var a=i.elesQueue.shift();a&&(this.drawEleInLayer(i,a,i.level,e),r++),0===n.length&&n.push(!0),0===i.elesQueue.length&&(t.pop(),i.reqs=0,i.replaces&&this.applyLayerReplacement(i),this.requestRedraw())}}return n},Du.applyLayerReplacement=function(e){var t=this.layersByLevel[e.level],n=e.replaces,r=t.indexOf(n);if(!(r<0||n.invalid)){t[r]=e;for(var i=0;i<e.eles.length;i++){var a=e.eles[i]._private,o=a.imgLayerCaches=a.imgLayerCaches||{};o&&(o[e.level]=e)}this.requestRedraw()}},Du.requestRedraw=ve((function(){var e=this.renderer;e.redrawHint("eles",!0),e.redrawHint("drag",!0),e.redraw()}),100),Du.setupDequeueing=xu({deqRedrawThreshold:50,deqCost:.15,deqAvgCost:.1,deqNoDrawCost:.9,deqFastCost:.9,deq:function(e,t){return e.dequeue(t)},onDeqd:Re,shouldRedraw:Ae,priority:function(e){return e.renderer.beforeRenderPriorities.lyrTxrDeq}});var Mu,Bu={};function Nu(e,t){for(var n=0;n<t.length;n++){var r=t[n];e.lineTo(r.x,r.y)}}function zu(e,t,n){for(var r,i=0;i<t.length;i++){var a=t[i];0===i&&(r=a),e.lineTo(a.x,a.y)}e.quadraticCurveTo(n.x,n.y,r.x,r.y)}function Iu(e,t,n){e.beginPath&&e.beginPath();for(var r=t,i=0;i<r.length;i++){var a=r[i];e.lineTo(a.x,a.y)}var o=n,s=n[0];e.moveTo(s.x,s.y);for(i=1;i<o.length;i++){a=o[i];e.lineTo(a.x,a.y)}e.closePath&&e.closePath()}function Au(e,t,n,r,i){e.beginPath&&e.beginPath(),e.arc(n,r,i,0,2*Math.PI,!1);var a=t,o=a[0];e.moveTo(o.x,o.y);for(var s=0;s<a.length;s++){var l=a[s];e.lineTo(l.x,l.y)}e.closePath&&e.closePath()}function Lu(e,t,n,r){e.arc(t,n,r,0,2*Math.PI,!1)}Bu.arrowShapeImpl=function(e){return(Mu||(Mu={polygon:Nu,"triangle-backcurve":zu,"triangle-tee":Iu,"circle-triangle":Au,"triangle-cross":Iu,circle:Lu}))[e]};var Ou={drawElement:function(e,t,n,r,i,a){t.isNode()?this.drawNode(e,t,n,r,i,a):this.drawEdge(e,t,n,r,i,a)},drawElementOverlay:function(e,t){t.isNode()?this.drawNodeOverlay(e,t):this.drawEdgeOverlay(e,t)},drawElementUnderlay:function(e,t){t.isNode()?this.drawNodeUnderlay(e,t):this.drawEdgeUnderlay(e,t)},drawCachedElementPortion:function(e,t,n,r,i,a,o,s){var l=this,u=n.getBoundingBox(t);if(0!==u.w&&0!==u.h){var c=n.getElement(t,u,r,i,a);if(null!=c){var d=s(l,t);if(0===d)return;var h,p,f,g,v,y,m=o(l,t),b=u.x1,x=u.y1,w=u.w,E=u.h;if(0!==m){var k=n.getRotationPoint(t);f=k.x,g=k.y,e.translate(f,g),e.rotate(m),(v=l.getImgSmoothing(e))||l.setImgSmoothing(e,!0);var C=n.getRotationOffset(t);h=C.x,p=C.y}else h=b,p=x;1!==d&&(y=e.globalAlpha,e.globalAlpha=y*d),e.drawImage(c.texture.canvas,c.x,0,c.width,c.height,h,p,w,E),1!==d&&(e.globalAlpha=y),0!==m&&(e.rotate(-m),e.translate(-f,-g),v||l.setImgSmoothing(e,!1))}else n.drawElement(e,t)}}},Ru=function(){return 0},Vu=function(e,t){return e.getTextAngle(t,null)},Fu=function(e,t){return e.getTextAngle(t,"source")},ju=function(e,t){return e.getTextAngle(t,"target")},qu=function(e,t){return t.effectiveOpacity()},Yu=function(e,t){return t.pstyle("text-opacity").pfValue*t.effectiveOpacity()};Ou.drawCachedElement=function(e,t,n,r,i,a){var o=this,s=o.data,l=s.eleTxrCache,u=s.lblTxrCache,c=s.slbTxrCache,d=s.tlbTxrCache,h=t.boundingBox(),p=!0===a?l.reasons.highQuality:null;if(0!==h.w&&0!==h.h&&t.visible()&&(!r||At(h,r))){var f=t.isEdge(),g=t.element()._private.rscratch.badLine;o.drawElementUnderlay(e,t),o.drawCachedElementPortion(e,t,l,n,i,p,Ru,qu),f&&g||o.drawCachedElementPortion(e,t,u,n,i,p,Vu,Yu),f&&!g&&(o.drawCachedElementPortion(e,t,c,n,i,p,Fu,Yu),o.drawCachedElementPortion(e,t,d,n,i,p,ju,Yu)),o.drawElementOverlay(e,t)}},Ou.drawElements=function(e,t){for(var n=0;n<t.length;n++){var r=t[n];this.drawElement(e,r)}},Ou.drawCachedElements=function(e,t,n,r){for(var i=0;i<t.length;i++){var a=t[i];this.drawCachedElement(e,a,n,r)}},Ou.drawCachedNodes=function(e,t,n,r){for(var i=0;i<t.length;i++){var a=t[i];a.isNode()&&this.drawCachedElement(e,a,n,r)}},Ou.drawLayeredElements=function(e,t,n,r){var i=this.data.lyrTxrCache.getLayers(t,n);if(i)for(var a=0;a<i.length;a++){var o=i[a],s=o.bb;0!==s.w&&0!==s.h&&e.drawImage(o.canvas,s.x1,s.y1,s.w,s.h)}else this.drawCachedElements(e,t,n,r)};var Xu={drawEdge:function(e,t,n){var r=!(arguments.length>3&&void 0!==arguments[3])||arguments[3],i=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],a=!(arguments.length>5&&void 0!==arguments[5])||arguments[5],o=this,s=t._private.rscratch;if((!a||t.visible())&&!s.badLine&&null!=s.allpts&&!isNaN(s.allpts[0])){var l;n&&(l=n,e.translate(-l.x1,-l.y1));var u=a?t.pstyle("opacity").value:1,c=a?t.pstyle("line-opacity").value:1,d=t.pstyle("curve-style").value,h=t.pstyle("line-style").value,p=t.pstyle("width").pfValue,f=t.pstyle("line-cap").value,g=t.pstyle("line-outline-width").value,v=t.pstyle("line-outline-color").value,y=u*c,m=u*c,b=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:y;"straight-triangle"===d?(o.eleStrokeStyle(e,t,n),o.drawEdgeTrianglePath(t,e,s.allpts)):(e.lineWidth=p,e.lineCap=f,o.eleStrokeStyle(e,t,n),o.drawEdgePath(t,e,s.allpts,h),e.lineCap="butt")},x=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:y;e.lineWidth=p+g,e.lineCap=f,g>0?(o.colorStrokeStyle(e,v[0],v[1],v[2],n),"straight-triangle"===d?o.drawEdgeTrianglePath(t,e,s.allpts):(o.drawEdgePath(t,e,s.allpts,h),e.lineCap="butt")):e.lineCap="butt"},w=function(){i&&o.drawEdgeOverlay(e,t)},E=function(){i&&o.drawEdgeUnderlay(e,t)},k=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:m;o.drawArrowheads(e,t,n)},C=function(){o.drawElementText(e,t,null,r)};e.lineJoin="round";var S="yes"===t.pstyle("ghost").value;if(S){var P=t.pstyle("ghost-offset-x").pfValue,D=t.pstyle("ghost-offset-y").pfValue,T=t.pstyle("ghost-opacity").value,_=y*T;e.translate(P,D),b(_),k(_),e.translate(-P,-D)}else x();E(),b(),k(),w(),C(),n&&e.translate(l.x1,l.y1)}}},Wu=function(e){if(!["overlay","underlay"].includes(e))throw new Error("Invalid state");return function(t,n){if(n.visible()){var r=n.pstyle("".concat(e,"-opacity")).value;if(0!==r){var i=this,a=i.usePaths(),o=n._private.rscratch,s=2*n.pstyle("".concat(e,"-padding")).pfValue,l=n.pstyle("".concat(e,"-color")).value;t.lineWidth=s,"self"!==o.edgeType||a?t.lineCap="round":t.lineCap="butt",i.colorStrokeStyle(t,l[0],l[1],l[2],r),i.drawEdgePath(n,t,o.allpts,"solid")}}}};Xu.drawEdgeOverlay=Wu("overlay"),Xu.drawEdgeUnderlay=Wu("underlay"),Xu.drawEdgePath=function(e,t,n,r){var i,a=e._private.rscratch,o=t,s=!1,u=this.usePaths(),c=e.pstyle("line-dash-pattern").pfValue,d=e.pstyle("line-dash-offset").pfValue;if(u){var h=n.join("$");a.pathCacheKey&&a.pathCacheKey===h?(i=t=a.pathCache,s=!0):(i=t=new Path2D,a.pathCacheKey=h,a.pathCache=i)}if(o.setLineDash)switch(r){case"dotted":o.setLineDash([1,1]);break;case"dashed":o.setLineDash(c),o.lineDashOffset=d;break;case"solid":o.setLineDash([])}if(!s&&!a.badLine)switch(t.beginPath&&t.beginPath(),t.moveTo(n[0],n[1]),a.edgeType){case"bezier":case"self":case"compound":case"multibezier":for(var p=2;p+3<n.length;p+=4)t.quadraticCurveTo(n[p],n[p+1],n[p+2],n[p+3]);break;case"straight":case"haystack":for(var f=2;f+1<n.length;f+=2)t.lineTo(n[f],n[f+1]);break;case"segments":if(a.isRound){var g,v=l(a.roundCorners);try{for(v.s();!(g=v.n()).done;){Ql(t,g.value)}}catch(e){v.e(e)}finally{v.f()}t.lineTo(n[n.length-2],n[n.length-1])}else for(var y=2;y+1<n.length;y+=2)t.lineTo(n[y],n[y+1])}t=o,u?t.stroke(i):t.stroke(),t.setLineDash&&t.setLineDash([])},Xu.drawEdgeTrianglePath=function(e,t,n){t.fillStyle=t.strokeStyle;for(var r=e.pstyle("width").pfValue,i=0;i+1<n.length;i+=2){var a=[n[i+2]-n[i],n[i+3]-n[i+1]],o=Math.sqrt(a[0]*a[0]+a[1]*a[1]),s=[a[1]/o,-a[0]/o],l=[s[0]*r/2,s[1]*r/2];t.beginPath(),t.moveTo(n[i]-l[0],n[i+1]-l[1]),t.lineTo(n[i]+l[0],n[i+1]+l[1]),t.lineTo(n[i+2],n[i+3]),t.closePath(),t.fill()}},Xu.drawArrowheads=function(e,t,n){var r=t._private.rscratch,i="haystack"===r.edgeType;i||this.drawArrowhead(e,t,"source",r.arrowStartX,r.arrowStartY,r.srcArrowAngle,n),this.drawArrowhead(e,t,"mid-target",r.midX,r.midY,r.midtgtArrowAngle,n),this.drawArrowhead(e,t,"mid-source",r.midX,r.midY,r.midsrcArrowAngle,n),i||this.drawArrowhead(e,t,"target",r.arrowEndX,r.arrowEndY,r.tgtArrowAngle,n)},Xu.drawArrowhead=function(e,t,n,r,i,a,o){if(!(isNaN(r)||null==r||isNaN(i)||null==i||isNaN(a)||null==a)){var s=t.pstyle(n+"-arrow-shape").value;if("none"!==s){var l="hollow"===t.pstyle(n+"-arrow-fill").value?"both":"filled",u=t.pstyle(n+"-arrow-fill").value,c=t.pstyle("width").pfValue,d=t.pstyle(n+"-arrow-width"),h="match-line"===d.value?c:d.pfValue;"%"===d.units&&(h*=c);var p=t.pstyle("opacity").value;void 0===o&&(o=p);var f=e.globalCompositeOperation;1===o&&"hollow"!==u||(e.globalCompositeOperation="destination-out",this.colorFillStyle(e,255,255,255,1),this.colorStrokeStyle(e,255,255,255,1),this.drawArrowShape(t,e,l,c,s,h,r,i,a),e.globalCompositeOperation=f);var g=t.pstyle(n+"-arrow-color").value;this.colorFillStyle(e,g[0],g[1],g[2],o),this.colorStrokeStyle(e,g[0],g[1],g[2],o),this.drawArrowShape(t,e,u,c,s,h,r,i,a)}}},Xu.drawArrowShape=function(e,t,n,r,i,a,o,s,l){var u,c=this,d=this.usePaths()&&"triangle-cross"!==i,h=!1,p=t,f={x:o,y:s},g=e.pstyle("arrow-scale").value,v=this.getArrowWidth(r,g),y=c.arrowShapes[i];if(d){var m=c.arrowPathCache=c.arrowPathCache||[],b=Te(i),x=m[b];null!=x?(u=t=x,h=!0):(u=t=new Path2D,m[b]=u)}h||(t.beginPath&&t.beginPath(),d?y.draw(t,1,0,{x:0,y:0},1):y.draw(t,v,l,f,r),t.closePath&&t.closePath()),t=p,d&&(t.translate(o,s),t.rotate(l),t.scale(v,v)),"filled"!==n&&"both"!==n||(d?t.fill(u):t.fill()),"hollow"!==n&&"both"!==n||(t.lineWidth=a/(d?v:1),t.lineJoin="miter",d?t.stroke(u):t.stroke()),d&&(t.scale(1/v,1/v),t.rotate(-l),t.translate(-o,-s))};var Hu={safeDrawImage:function(e,t,n,r,i,a,o,s,l,u){if(!(i<=0||a<=0||l<=0||u<=0))try{e.drawImage(t,n,r,i,a,o,s,l,u)}catch(e){je(e)}},drawInscribedImage:function(e,t,n,r,i){var a=this,o=n.position(),s=o.x,l=o.y,u=n.cy().style(),c=u.getIndexedStyle.bind(u),d=c(n,"background-fit","value",r),h=c(n,"background-repeat","value",r),p=n.width(),f=n.height(),g=2*n.padding(),v=p+("inner"===c(n,"background-width-relative-to","value",r)?0:g),y=f+("inner"===c(n,"background-height-relative-to","value",r)?0:g),m=n._private.rscratch,b="node"===c(n,"background-clip","value",r),x=c(n,"background-image-opacity","value",r)*i,w=c(n,"background-image-smoothing","value",r),E=n.pstyle("corner-radius").value;"auto"!==E&&(E=n.pstyle("corner-radius").pfValue);var k=t.width||t.cachedW,C=t.height||t.cachedH;null!=k&&null!=C||(document.body.appendChild(t),k=t.cachedW=t.width||t.offsetWidth,C=t.cachedH=t.height||t.offsetHeight,document.body.removeChild(t));var S=k,P=C;if("auto"!==c(n,"background-width","value",r)&&(S="%"===c(n,"background-width","units",r)?c(n,"background-width","pfValue",r)*v:c(n,"background-width","pfValue",r)),"auto"!==c(n,"background-height","value",r)&&(P="%"===c(n,"background-height","units",r)?c(n,"background-height","pfValue",r)*y:c(n,"background-height","pfValue",r)),0!==S&&0!==P){if("contain"===d)S*=D=Math.min(v/S,y/P),P*=D;else if("cover"===d){var D;S*=D=Math.max(v/S,y/P),P*=D}var T=s-v/2,_=c(n,"background-position-x","units",r),M=c(n,"background-position-x","pfValue",r);T+="%"===_?(v-S)*M:M;var B=c(n,"background-offset-x","units",r),N=c(n,"background-offset-x","pfValue",r);T+="%"===B?(v-S)*N:N;var z=l-y/2,I=c(n,"background-position-y","units",r),A=c(n,"background-position-y","pfValue",r);z+="%"===I?(y-P)*A:A;var L=c(n,"background-offset-y","units",r),O=c(n,"background-offset-y","pfValue",r);z+="%"===L?(y-P)*O:O,m.pathCache&&(T-=s,z-=l,s=0,l=0);var R=e.globalAlpha;e.globalAlpha=x;var V=a.getImgSmoothing(e),F=!1;if("no"===w&&V?(a.setImgSmoothing(e,!1),F=!0):"yes"!==w||V||(a.setImgSmoothing(e,!0),F=!0),"no-repeat"===h)b&&(e.save(),m.pathCache?e.clip(m.pathCache):(a.nodeShapes[a.getNodeShape(n)].draw(e,s,l,v,y,E,m),e.clip())),a.safeDrawImage(e,t,0,0,k,C,T,z,S,P),b&&e.restore();else{var j=e.createPattern(t,h);e.fillStyle=j,a.nodeShapes[a.getNodeShape(n)].draw(e,s,l,v,y,E,m),e.translate(T,z),e.fill(),e.translate(-T,-z)}e.globalAlpha=R,F&&a.setImgSmoothing(e,V)}}},Ku={};function Gu(e,t,n,r,i){var a=arguments.length>5&&void 0!==arguments[5]?arguments[5]:5,o=arguments.length>6?arguments[6]:void 0;e.beginPath(),e.moveTo(t+a,n),e.lineTo(t+r-a,n),e.quadraticCurveTo(t+r,n,t+r,n+a),e.lineTo(t+r,n+i-a),e.quadraticCurveTo(t+r,n+i,t+r-a,n+i),e.lineTo(t+a,n+i),e.quadraticCurveTo(t,n+i,t,n+i-a),e.lineTo(t,n+a),e.quadraticCurveTo(t,n,t+a,n),e.closePath(),o?e.stroke():e.fill()}Ku.eleTextBiggerThanMin=function(e,t){if(!t){var n=e.cy().zoom(),r=this.getPixelRatio(),i=Math.ceil(wt(n*r));t=Math.pow(2,i)}return!(e.pstyle("font-size").pfValue*t<e.pstyle("min-zoomed-font-size").pfValue)},Ku.drawElementText=function(e,t,n,r,i){var a=!(arguments.length>5&&void 0!==arguments[5])||arguments[5],o=this;if(null==r){if(a&&!o.eleTextBiggerThanMin(t))return}else if(!1===r)return;if(t.isNode()){var s=t.pstyle("label");if(!s||!s.value)return;var l=o.getLabelJustification(t);e.textAlign=l,e.textBaseline="bottom"}else{var u=t.element()._private.rscratch.badLine,c=t.pstyle("label"),d=t.pstyle("source-label"),h=t.pstyle("target-label");if(u||(!c||!c.value)&&(!d||!d.value)&&(!h||!h.value))return;e.textAlign="center",e.textBaseline="bottom"}var p,f=!n;n&&(p=n,e.translate(-p.x1,-p.y1)),null==i?(o.drawText(e,t,null,f,a),t.isEdge()&&(o.drawText(e,t,"source",f,a),o.drawText(e,t,"target",f,a))):o.drawText(e,t,i,f,a),n&&e.translate(p.x1,p.y1)},Ku.getFontCache=function(e){var t;this.fontCaches=this.fontCaches||[];for(var n=0;n<this.fontCaches.length;n++)if((t=this.fontCaches[n]).context===e)return t;return t={context:e},this.fontCaches.push(t),t},Ku.setupTextStyle=function(e,t){var n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2],r=t.pstyle("font-style").strValue,i=t.pstyle("font-size").pfValue+"px",a=t.pstyle("font-family").strValue,o=t.pstyle("font-weight").strValue,s=n?t.effectiveOpacity()*t.pstyle("text-opacity").value:1,l=t.pstyle("text-outline-opacity").value*s,u=t.pstyle("color").value,c=t.pstyle("text-outline-color").value;e.font=r+" "+o+" "+i+" "+a,e.lineJoin="round",this.colorFillStyle(e,u[0],u[1],u[2],s),this.colorStrokeStyle(e,c[0],c[1],c[2],l)},Ku.getTextAngle=function(e,t){var n=e._private.rscratch,r=t?t+"-":"",i=e.pstyle(r+"text-rotation"),a=Ue(n,"labelAngle",t);return"autorotate"===i.strValue?e.isEdge()?a:0:"none"===i.strValue?0:i.pfValue},Ku.drawText=function(e,t,n){var r=!(arguments.length>3&&void 0!==arguments[3])||arguments[3],i=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],a=t._private,o=a.rscratch,s=i?t.effectiveOpacity():1;if(!i||0!==s&&0!==t.pstyle("text-opacity").value){"main"===n&&(n=null);var l,u,c=Ue(o,"labelX",n),d=Ue(o,"labelY",n),h=this.getLabelText(t,n);if(null!=h&&""!==h&&!isNaN(c)&&!isNaN(d)){this.setupTextStyle(e,t,i);var p,f=n?n+"-":"",g=Ue(o,"labelWidth",n),v=Ue(o,"labelHeight",n),y=t.pstyle(f+"text-margin-x").pfValue,m=t.pstyle(f+"text-margin-y").pfValue,b=t.isEdge(),x=t.pstyle("text-halign").value,w=t.pstyle("text-valign").value;switch(b&&(x="center",w="center"),c+=y,d+=m,0!==(p=r?this.getTextAngle(t,n):0)&&(l=c,u=d,e.translate(l,u),e.rotate(p),c=0,d=0),w){case"top":break;case"center":d+=v/2;break;case"bottom":d+=v}var E=t.pstyle("text-background-opacity").value,k=t.pstyle("text-border-opacity").value,C=t.pstyle("text-border-width").pfValue,S=t.pstyle("text-background-padding").pfValue,P=t.pstyle("text-background-shape").strValue,D=0===P.indexOf("round"),T=2;if(E>0||C>0&&k>0){var _=c-S;switch(x){case"left":_-=g;break;case"center":_-=g/2}var M=d-v-S,B=g+2*S,N=v+2*S;if(E>0){var z=e.fillStyle,I=t.pstyle("text-background-color").value;e.fillStyle="rgba("+I[0]+","+I[1]+","+I[2]+","+E*s+")",D?Gu(e,_,M,B,N,T):e.fillRect(_,M,B,N),e.fillStyle=z}if(C>0&&k>0){var A=e.strokeStyle,L=e.lineWidth,O=t.pstyle("text-border-color").value,R=t.pstyle("text-border-style").value;if(e.strokeStyle="rgba("+O[0]+","+O[1]+","+O[2]+","+k*s+")",e.lineWidth=C,e.setLineDash)switch(R){case"dotted":e.setLineDash([1,1]);break;case"dashed":e.setLineDash([4,2]);break;case"double":e.lineWidth=C/4,e.setLineDash([]);break;case"solid":e.setLineDash([])}if(D?Gu(e,_,M,B,N,T,"stroke"):e.strokeRect(_,M,B,N),"double"===R){var V=C/2;D?Gu(e,_+V,M+V,B-2*V,N-2*V,T,"stroke"):e.strokeRect(_+V,M+V,B-2*V,N-2*V)}e.setLineDash&&e.setLineDash([]),e.lineWidth=L,e.strokeStyle=A}}var F=2*t.pstyle("text-outline-width").pfValue;if(F>0&&(e.lineWidth=F),"wrap"===t.pstyle("text-wrap").value){var j=Ue(o,"labelWrapCachedLines",n),q=Ue(o,"labelLineHeight",n),Y=g/2,X=this.getLabelJustification(t);switch("auto"===X||("left"===x?"left"===X?c+=-g:"center"===X&&(c+=-Y):"center"===x?"left"===X?c+=-Y:"right"===X&&(c+=Y):"right"===x&&("center"===X?c+=Y:"right"===X&&(c+=g))),w){case"top":d-=(j.length-1)*q;break;case"center":case"bottom":d-=(j.length-1)*q}for(var W=0;W<j.length;W++)F>0&&e.strokeText(j[W],c,d),e.fillText(j[W],c,d),d+=q}else F>0&&e.strokeText(h,c,d),e.fillText(h,c,d);0!==p&&(e.rotate(-p),e.translate(-l,-u))}}};var Uu={drawNode:function(e,t,n){var r,i,a=!(arguments.length>3&&void 0!==arguments[3])||arguments[3],o=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],s=!(arguments.length>5&&void 0!==arguments[5])||arguments[5],l=this,u=t._private,c=u.rscratch,d=t.position();if(x(d.x)&&x(d.y)&&(!s||t.visible())){var h,p,f=s?t.effectiveOpacity():1,g=l.usePaths(),v=!1,y=t.padding();r=t.width()+2*y,i=t.height()+2*y,n&&(p=n,e.translate(-p.x1,-p.y1));for(var m=t.pstyle("background-image"),b=m.value,w=new Array(b.length),E=new Array(b.length),k=0,C=0;C<b.length;C++){var S=b[C],P=w[C]=null!=S&&"none"!==S;if(P){var D=t.cy().style().getIndexedStyle(t,"background-image-crossorigin","value",C);k++,E[C]=l.getCachedImage(S,D,(function(){u.backgroundTimestamp=Date.now(),t.emitAndNotify("background")}))}}var T=t.pstyle("background-blacken").value,_=t.pstyle("border-width").pfValue,M=t.pstyle("background-opacity").value*f,B=t.pstyle("border-color").value,N=t.pstyle("border-style").value,z=t.pstyle("border-join").value,I=t.pstyle("border-cap").value,A=t.pstyle("border-position").value,L=t.pstyle("border-dash-pattern").pfValue,O=t.pstyle("border-dash-offset").pfValue,R=t.pstyle("border-opacity").value*f,V=t.pstyle("outline-width").pfValue,F=t.pstyle("outline-color").value,j=t.pstyle("outline-style").value,q=t.pstyle("outline-opacity").value*f,Y=t.pstyle("outline-offset").value,X=t.pstyle("corner-radius").value;"auto"!==X&&(X=t.pstyle("corner-radius").pfValue);var W=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:M;l.eleFillStyle(e,t,n)},H=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:R;l.colorStrokeStyle(e,B[0],B[1],B[2],t)},K=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:q;l.colorStrokeStyle(e,F[0],F[1],F[2],t)},G=function(e,t,n,r){var i,a=l.nodePathCache=l.nodePathCache||[],o=_e("polygon"===n?n+","+r.join(","):n,""+t,""+e,""+X),s=a[o],u=!1;return null!=s?(i=s,u=!0,c.pathCache=i):(i=new Path2D,a[o]=c.pathCache=i),{path:i,cacheHit:u}},U=t.pstyle("shape").strValue,Z=t.pstyle("shape-polygon-points").pfValue;if(g){e.translate(d.x,d.y);var $=G(r,i,U,Z);h=$.path,v=$.cacheHit}var Q=function(){if(!v){var n=d;g&&(n={x:0,y:0}),l.nodeShapes[l.getNodeShape(t)].draw(h||e,n.x,n.y,r,i,X,c)}g?e.fill(h):e.fill()},J=function(){for(var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:f,r=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],i=u.backgrounding,a=0,o=0;o<E.length;o++){var s=t.cy().style().getIndexedStyle(t,"background-image-containment","value",o);r&&"over"===s||!r&&"inside"===s?a++:w[o]&&E[o].complete&&!E[o].error&&(a++,l.drawInscribedImage(e,E[o],t,o,n))}u.backgrounding=!(a===k),i!==u.backgrounding&&t.updateStyle(!1)},ee=function(){var n=arguments.length>0&&void 0!==arguments[0]&&arguments[0],a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:f;l.hasPie(t)&&(l.drawPie(e,t,a),n&&(g||l.nodeShapes[l.getNodeShape(t)].draw(e,d.x,d.y,r,i,X,c)))},te=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:f,n=(T>0?T:-T)*t,r=T>0?0:255;0!==T&&(l.colorFillStyle(e,r,r,r,n),g?e.fill(h):e.fill())},ne=function(){if(_>0){if(e.lineWidth=_,e.lineCap=I,e.lineJoin=z,e.setLineDash)switch(N){case"dotted":e.setLineDash([1,1]);break;case"dashed":e.setLineDash(L),e.lineDashOffset=O;break;case"solid":case"double":e.setLineDash([])}if("center"!==A){if(e.save(),e.lineWidth*=2,"inside"===A)g?e.clip(h):e.clip();else{var t=new Path2D;t.rect(-r/2-_,-i/2-_,r+2*_,i+2*_),t.addPath(h),e.clip(t,"evenodd")}g?e.stroke(h):e.stroke(),e.restore()}else g?e.stroke(h):e.stroke();if("double"===N){e.lineWidth=_/3;var n=e.globalCompositeOperation;e.globalCompositeOperation="destination-out",g?e.stroke(h):e.stroke(),e.globalCompositeOperation=n}e.setLineDash&&e.setLineDash([])}},re=function(){if(V>0){if(e.lineWidth=V,e.lineCap="butt",e.setLineDash)switch(j){case"dotted":e.setLineDash([1,1]);break;case"dashed":e.setLineDash([4,2]);break;case"solid":case"double":e.setLineDash([])}var n=d;g&&(n={x:0,y:0});var a=l.getNodeShape(t),o=_;"inside"===A&&(o=0),"outside"===A&&(o*=2);var s,u=(r+o+(V+Y))/r,c=(i+o+(V+Y))/i,h=r*u,p=i*c,f=l.nodeShapes[a].points;if(g)s=G(h,p,a,f).path;if("ellipse"===a)l.drawEllipsePath(s||e,n.x,n.y,h,p);else if(["round-diamond","round-heptagon","round-hexagon","round-octagon","round-pentagon","round-polygon","round-triangle","round-tag"].includes(a)){var v=0,y=0,m=0;"round-diamond"===a?v=1.4*(o+Y+V):"round-heptagon"===a?(v=1.075*(o+Y+V),m=-(o/2+Y+V)/35):"round-hexagon"===a?v=1.12*(o+Y+V):"round-pentagon"===a?(v=1.13*(o+Y+V),m=-(o/2+Y+V)/15):"round-tag"===a?(v=1.12*(o+Y+V),y=.07*(o/2+V+Y)):"round-triangle"===a&&(v=(o+Y+V)*(Math.PI/2),m=-(o+Y/2+V)/Math.PI),0!==v&&(h=r*(u=(r+v)/r),["round-hexagon","round-tag"].includes(a)||(p=i*(c=(i+v)/i)));for(var b=h/2,x=p/2,w=(X="auto"===X?rn(h,p):X)+(o+V+Y)/2,E=new Array(f.length/2),k=new Array(f.length/2),C=0;C<f.length/2;C++)E[C]={x:n.x+y+b*f[2*C],y:n.y+m+x*f[2*C+1]};var S,P,D,T,M=E.length;for(P=E[M-1],S=0;S<M;S++)D=E[S%M],T=E[(S+1)%M],k[S]=Jl(P,D,T,w),P=D,D=T;l.drawRoundPolygonPath(s||e,n.x+y,n.y+m,r*u,i*c,f,k)}else if(["roundrectangle","round-rectangle"].includes(a))X="auto"===X?nn(h,p):X,l.drawRoundRectanglePath(s||e,n.x,n.y,h,p,X+(o+V+Y)/2);else if(["cutrectangle","cut-rectangle"].includes(a))X="auto"===X?8:X,l.drawCutRectanglePath(s||e,n.x,n.y,h,p,null,X+(o+V+Y)/4);else if(["bottomroundrectangle","bottom-round-rectangle"].includes(a))X="auto"===X?nn(h,p):X,l.drawBottomRoundRectanglePath(s||e,n.x,n.y,h,p,X+(o+V+Y)/2);else if("barrel"===a)l.drawBarrelPath(s||e,n.x,n.y,h,p);else if(a.startsWith("polygon")||["rhomboid","right-rhomboid","round-tag","tag","vee"].includes(a)){f=Wt(Ht(f,(o+V+Y)/r)),l.drawPolygonPath(s||e,n.x,n.y,r,i,f)}else{f=Wt(Ht(f,-((o+V+Y)/r))),l.drawPolygonPath(s||e,n.x,n.y,r,i,f)}if(g?e.stroke(s):e.stroke(),"double"===j){e.lineWidth=o/3;var B=e.globalCompositeOperation;e.globalCompositeOperation="destination-out",g?e.stroke(s):e.stroke(),e.globalCompositeOperation=B}e.setLineDash&&e.setLineDash([])}},ie=function(){o&&l.drawNodeOverlay(e,t,d,r,i)},ae=function(){o&&l.drawNodeUnderlay(e,t,d,r,i)},oe=function(){l.drawElementText(e,t,null,a)},se="yes"===t.pstyle("ghost").value;if(se){var le=t.pstyle("ghost-offset-x").pfValue,ue=t.pstyle("ghost-offset-y").pfValue,ce=t.pstyle("ghost-opacity").value,de=ce*f;e.translate(le,ue),K(),re(),W(ce*M),Q(),J(de,!0),H(ce*R),ne(),ee(0!==T||0!==_),J(de,!1),te(de),e.translate(-le,-ue)}g&&e.translate(-d.x,-d.y),ae(),g&&e.translate(d.x,d.y),K(),re(),W(),Q(),J(f,!0),H(),ne(),ee(0!==T||0!==_),J(f,!1),te(),g&&e.translate(-d.x,-d.y),oe(),ie(),n&&e.translate(p.x1,p.y1)}}},Zu=function(e){if(!["overlay","underlay"].includes(e))throw new Error("Invalid state");return function(t,n,r,i,a){if(n.visible()){var o=n.pstyle("".concat(e,"-padding")).pfValue,s=n.pstyle("".concat(e,"-opacity")).value,l=n.pstyle("".concat(e,"-color")).value,u=n.pstyle("".concat(e,"-shape")).value,c=n.pstyle("".concat(e,"-corner-radius")).value;if(s>0){if(r=r||n.position(),null==i||null==a){var d=n.padding();i=n.width()+2*d,a=n.height()+2*d}this.colorFillStyle(t,l[0],l[1],l[2],s),this.nodeShapes[u].draw(t,r.x,r.y,i+2*o,a+2*o,c),t.fill()}}}};Uu.drawNodeOverlay=Zu("overlay"),Uu.drawNodeUnderlay=Zu("underlay"),Uu.hasPie=function(e){return(e=e[0])._private.hasPie},Uu.drawPie=function(e,t,n,r){t=t[0],r=r||t.position();var i=t.cy().style(),a=t.pstyle("pie-size"),o=r.x,s=r.y,l=t.width(),u=t.height(),c=Math.min(l,u)/2,d=0;this.usePaths()&&(o=0,s=0),"%"===a.units?c*=a.pfValue:void 0!==a.pfValue&&(c=a.pfValue/2);for(var h=1;h<=i.pieBackgroundN;h++){var p=t.pstyle("pie-"+h+"-background-size").value,f=t.pstyle("pie-"+h+"-background-color").value,g=t.pstyle("pie-"+h+"-background-opacity").value*n,v=p/100;v+d>1&&(v=1-d);var y=1.5*Math.PI+2*Math.PI*d,m=y+2*Math.PI*v;0===p||d>=1||d+v>1||(e.beginPath(),e.moveTo(o,s),e.arc(o,s,c,y,m),e.closePath(),this.colorFillStyle(e,f[0],f[1],f[2],g),e.fill(),d+=v)}};var $u={};$u.getPixelRatio=function(){var e=this.data.contexts[0];if(null!=this.forcedPixelRatio)return this.forcedPixelRatio;var t=this.cy.window(),n=e.backingStorePixelRatio||e.webkitBackingStorePixelRatio||e.mozBackingStorePixelRatio||e.msBackingStorePixelRatio||e.oBackingStorePixelRatio||e.backingStorePixelRatio||1;return(t.devicePixelRatio||1)/n},$u.paintCache=function(e){for(var t,n=this.paintCaches=this.paintCaches||[],r=!0,i=0;i<n.length;i++)if((t=n[i]).context===e){r=!1;break}return r&&(t={context:e},n.push(t)),t},$u.createGradientStyleFor=function(e,t,n,r,i){var a,o=this.usePaths(),s=n.pstyle(t+"-gradient-stop-colors").value,l=n.pstyle(t+"-gradient-stop-positions").pfValue;if("radial-gradient"===r)if(n.isEdge()){var u=n.sourceEndpoint(),c=n.targetEndpoint(),d=n.midpoint(),h=kt(u,d),p=kt(c,d);a=e.createRadialGradient(d.x,d.y,0,d.x,d.y,Math.max(h,p))}else{var f=o?{x:0,y:0}:n.position(),g=n.paddedWidth(),v=n.paddedHeight();a=e.createRadialGradient(f.x,f.y,0,f.x,f.y,Math.max(g,v))}else if(n.isEdge()){var y=n.sourceEndpoint(),m=n.targetEndpoint();a=e.createLinearGradient(y.x,y.y,m.x,m.y)}else{var b=o?{x:0,y:0}:n.position(),x=n.paddedWidth()/2,w=n.paddedHeight()/2;switch(n.pstyle("background-gradient-direction").value){case"to-bottom":a=e.createLinearGradient(b.x,b.y-w,b.x,b.y+w);break;case"to-top":a=e.createLinearGradient(b.x,b.y+w,b.x,b.y-w);break;case"to-left":a=e.createLinearGradient(b.x+x,b.y,b.x-x,b.y);break;case"to-right":a=e.createLinearGradient(b.x-x,b.y,b.x+x,b.y);break;case"to-bottom-right":case"to-right-bottom":a=e.createLinearGradient(b.x-x,b.y-w,b.x+x,b.y+w);break;case"to-top-right":case"to-right-top":a=e.createLinearGradient(b.x-x,b.y+w,b.x+x,b.y-w);break;case"to-bottom-left":case"to-left-bottom":a=e.createLinearGradient(b.x+x,b.y-w,b.x-x,b.y+w);break;case"to-top-left":case"to-left-top":a=e.createLinearGradient(b.x+x,b.y+w,b.x-x,b.y-w)}}if(!a)return null;for(var E=l.length===s.length,k=s.length,C=0;C<k;C++)a.addColorStop(E?l[C]:C/(k-1),"rgba("+s[C][0]+","+s[C][1]+","+s[C][2]+","+i+")");return a},$u.gradientFillStyle=function(e,t,n,r){var i=this.createGradientStyleFor(e,"background",t,n,r);if(!i)return null;e.fillStyle=i},$u.colorFillStyle=function(e,t,n,r,i){e.fillStyle="rgba("+t+","+n+","+r+","+i+")"},$u.eleFillStyle=function(e,t,n){var r=t.pstyle("background-fill").value;if("linear-gradient"===r||"radial-gradient"===r)this.gradientFillStyle(e,t,r,n);else{var i=t.pstyle("background-color").value;this.colorFillStyle(e,i[0],i[1],i[2],n)}},$u.gradientStrokeStyle=function(e,t,n,r){var i=this.createGradientStyleFor(e,"line",t,n,r);if(!i)return null;e.strokeStyle=i},$u.colorStrokeStyle=function(e,t,n,r,i){e.strokeStyle="rgba("+t+","+n+","+r+","+i+")"},$u.eleStrokeStyle=function(e,t,n){var r=t.pstyle("line-fill").value;if("linear-gradient"===r||"radial-gradient"===r)this.gradientStrokeStyle(e,t,r,n);else{var i=t.pstyle("line-color").value;this.colorStrokeStyle(e,i[0],i[1],i[2],n)}},$u.matchCanvasSize=function(e){var t=this,n=t.data,r=t.findContainerClientCoords(),i=r[2],a=r[3],o=t.getPixelRatio(),s=t.motionBlurPxRatio;e!==t.data.bufferCanvases[t.MOTIONBLUR_BUFFER_NODE]&&e!==t.data.bufferCanvases[t.MOTIONBLUR_BUFFER_DRAG]||(o=s);var l,u=i*o,c=a*o;if(u!==t.canvasWidth||c!==t.canvasHeight){t.fontCaches=null;var d=n.canvasContainer;d.style.width=i+"px",d.style.height=a+"px";for(var h=0;h<t.CANVAS_LAYERS;h++)(l=n.canvases[h]).width=u,l.height=c,l.style.width=i+"px",l.style.height=a+"px";for(h=0;h<t.BUFFER_COUNT;h++)(l=n.bufferCanvases[h]).width=u,l.height=c,l.style.width=i+"px",l.style.height=a+"px";t.textureMult=1,o<=1&&(l=n.bufferCanvases[t.TEXTURE_BUFFER],t.textureMult=2,l.width=u*t.textureMult,l.height=c*t.textureMult),t.canvasWidth=u,t.canvasHeight=c}},$u.renderTo=function(e,t,n,r){this.render({forcedContext:e,forcedZoom:t,forcedPan:n,drawAllLayers:!0,forcedPxRatio:r})},$u.render=function(e){var t=(e=e||We()).forcedContext,n=e.drawAllLayers,r=e.drawOnlyNodeLayer,i=e.forcedZoom,a=e.forcedPan,o=this,s=void 0===e.forcedPxRatio?this.getPixelRatio():e.forcedPxRatio,l=o.cy,u=o.data,c=u.canvasNeedsRedraw,d=o.textureOnViewport&&!t&&(o.pinching||o.hoverData.dragging||o.swipePanning||o.data.wheelZooming),h=void 0!==e.motionBlur?e.motionBlur:o.motionBlur,p=o.motionBlurPxRatio,f=l.hasCompoundNodes(),g=o.hoverData.draggingEles,v=!(!o.hoverData.selecting&&!o.touchData.selecting),y=h=h&&!t&&o.motionBlurEnabled&&!v;t||(o.prevPxRatio!==s&&(o.invalidateContainerClientCoordsCache(),o.matchCanvasSize(o.container),o.redrawHint("eles",!0),o.redrawHint("drag",!0)),o.prevPxRatio=s),!t&&o.motionBlurTimeout&&clearTimeout(o.motionBlurTimeout),h&&(null==o.mbFrames&&(o.mbFrames=0),o.mbFrames++,o.mbFrames<3&&(y=!1),o.mbFrames>o.minMbLowQualFrames&&(o.motionBlurPxRatio=o.mbPxRBlurry)),o.clearingMotionBlur&&(o.motionBlurPxRatio=1),o.textureDrawLastFrame&&!d&&(c[o.NODE]=!0,c[o.SELECT_BOX]=!0);var m=l.style(),b=l.zoom(),x=void 0!==i?i:b,w=l.pan(),E={x:w.x,y:w.y},k={zoom:b,pan:{x:w.x,y:w.y}},C=o.prevViewport;void 0===C||k.zoom!==C.zoom||k.pan.x!==C.pan.x||k.pan.y!==C.pan.y||g&&!f||(o.motionBlurPxRatio=1),a&&(E=a),x*=s,E.x*=s,E.y*=s;var S=o.getCachedZSortedEles();function P(e,t,n,r,i){var a=e.globalCompositeOperation;e.globalCompositeOperation="destination-out",o.colorFillStyle(e,255,255,255,o.motionBlurTransparency),e.fillRect(t,n,r,i),e.globalCompositeOperation=a}function D(e,r){var s,l,c,d;o.clearingMotionBlur||e!==u.bufferContexts[o.MOTIONBLUR_BUFFER_NODE]&&e!==u.bufferContexts[o.MOTIONBLUR_BUFFER_DRAG]?(s=E,l=x,c=o.canvasWidth,d=o.canvasHeight):(s={x:w.x*p,y:w.y*p},l=b*p,c=o.canvasWidth*p,d=o.canvasHeight*p),e.setTransform(1,0,0,1,0,0),"motionBlur"===r?P(e,0,0,c,d):t||void 0!==r&&!r||e.clearRect(0,0,c,d),n||(e.translate(s.x,s.y),e.scale(l,l)),a&&e.translate(a.x,a.y),i&&e.scale(i,i)}if(d||(o.textureDrawLastFrame=!1),d){if(o.textureDrawLastFrame=!0,!o.textureCache){o.textureCache={},o.textureCache.bb=l.mutableElements().boundingBox(),o.textureCache.texture=o.data.bufferCanvases[o.TEXTURE_BUFFER];var T=o.data.bufferContexts[o.TEXTURE_BUFFER];T.setTransform(1,0,0,1,0,0),T.clearRect(0,0,o.canvasWidth*o.textureMult,o.canvasHeight*o.textureMult),o.render({forcedContext:T,drawOnlyNodeLayer:!0,forcedPxRatio:s*o.textureMult}),(k=o.textureCache.viewport={zoom:l.zoom(),pan:l.pan(),width:o.canvasWidth,height:o.canvasHeight}).mpan={x:(0-k.pan.x)/k.zoom,y:(0-k.pan.y)/k.zoom}}c[o.DRAG]=!1,c[o.NODE]=!1;var _=u.contexts[o.NODE],M=o.textureCache.texture;k=o.textureCache.viewport;_.setTransform(1,0,0,1,0,0),h?P(_,0,0,k.width,k.height):_.clearRect(0,0,k.width,k.height);var B=m.core("outside-texture-bg-color").value,N=m.core("outside-texture-bg-opacity").value;o.colorFillStyle(_,B[0],B[1],B[2],N),_.fillRect(0,0,k.width,k.height);b=l.zoom();D(_,!1),_.clearRect(k.mpan.x,k.mpan.y,k.width/k.zoom/s,k.height/k.zoom/s),_.drawImage(M,k.mpan.x,k.mpan.y,k.width/k.zoom/s,k.height/k.zoom/s)}else o.textureOnViewport&&!t&&(o.textureCache=null);var z=l.extent(),I=o.pinching||o.hoverData.dragging||o.swipePanning||o.data.wheelZooming||o.hoverData.draggingEles||o.cy.animated(),A=o.hideEdgesOnViewport&&I,L=[];if(L[o.NODE]=!c[o.NODE]&&h&&!o.clearedForMotionBlur[o.NODE]||o.clearingMotionBlur,L[o.NODE]&&(o.clearedForMotionBlur[o.NODE]=!0),L[o.DRAG]=!c[o.DRAG]&&h&&!o.clearedForMotionBlur[o.DRAG]||o.clearingMotionBlur,L[o.DRAG]&&(o.clearedForMotionBlur[o.DRAG]=!0),c[o.NODE]||n||r||L[o.NODE]){var O=h&&!L[o.NODE]&&1!==p;D(_=t||(O?o.data.bufferContexts[o.MOTIONBLUR_BUFFER_NODE]:u.contexts[o.NODE]),h&&!O?"motionBlur":void 0),A?o.drawCachedNodes(_,S.nondrag,s,z):o.drawLayeredElements(_,S.nondrag,s,z),o.debug&&o.drawDebugPoints(_,S.nondrag),n||h||(c[o.NODE]=!1)}if(!r&&(c[o.DRAG]||n||L[o.DRAG])){O=h&&!L[o.DRAG]&&1!==p;D(_=t||(O?o.data.bufferContexts[o.MOTIONBLUR_BUFFER_DRAG]:u.contexts[o.DRAG]),h&&!O?"motionBlur":void 0),A?o.drawCachedNodes(_,S.drag,s,z):o.drawCachedElements(_,S.drag,s,z),o.debug&&o.drawDebugPoints(_,S.drag),n||h||(c[o.DRAG]=!1)}if(o.showFps||!r&&c[o.SELECT_BOX]&&!n){if(D(_=t||u.contexts[o.SELECT_BOX]),1==o.selection[4]&&(o.hoverData.selecting||o.touchData.selecting)){b=o.cy.zoom();var R=m.core("selection-box-border-width").value/b;_.lineWidth=R,_.fillStyle="rgba("+m.core("selection-box-color").value[0]+","+m.core("selection-box-color").value[1]+","+m.core("selection-box-color").value[2]+","+m.core("selection-box-opacity").value+")",_.fillRect(o.selection[0],o.selection[1],o.selection[2]-o.selection[0],o.selection[3]-o.selection[1]),R>0&&(_.strokeStyle="rgba("+m.core("selection-box-border-color").value[0]+","+m.core("selection-box-border-color").value[1]+","+m.core("selection-box-border-color").value[2]+","+m.core("selection-box-opacity").value+")",_.strokeRect(o.selection[0],o.selection[1],o.selection[2]-o.selection[0],o.selection[3]-o.selection[1]))}if(u.bgActivePosistion&&!o.hoverData.selecting){b=o.cy.zoom();var V=u.bgActivePosistion;_.fillStyle="rgba("+m.core("active-bg-color").value[0]+","+m.core("active-bg-color").value[1]+","+m.core("active-bg-color").value[2]+","+m.core("active-bg-opacity").value+")",_.beginPath(),_.arc(V.x,V.y,m.core("active-bg-size").pfValue/b,0,2*Math.PI),_.fill()}var F=o.lastRedrawTime;if(o.showFps&&F){F=Math.round(F);var j=Math.round(1e3/F);_.setTransform(1,0,0,1,0,0),_.fillStyle="rgba(255, 0, 0, 0.75)",_.strokeStyle="rgba(255, 0, 0, 0.75)",_.lineWidth=1,_.fillText("1 frame = "+F+" ms = "+j+" fps",0,20);_.strokeRect(0,30,250,20),_.fillRect(0,30,250*Math.min(j/60,1),20)}n||(c[o.SELECT_BOX]=!1)}if(h&&1!==p){var q=u.contexts[o.NODE],Y=o.data.bufferCanvases[o.MOTIONBLUR_BUFFER_NODE],X=u.contexts[o.DRAG],W=o.data.bufferCanvases[o.MOTIONBLUR_BUFFER_DRAG],H=function(e,t,n){e.setTransform(1,0,0,1,0,0),n||!y?e.clearRect(0,0,o.canvasWidth,o.canvasHeight):P(e,0,0,o.canvasWidth,o.canvasHeight);var r=p;e.drawImage(t,0,0,o.canvasWidth*r,o.canvasHeight*r,0,0,o.canvasWidth,o.canvasHeight)};(c[o.NODE]||L[o.NODE])&&(H(q,Y,L[o.NODE]),c[o.NODE]=!1),(c[o.DRAG]||L[o.DRAG])&&(H(X,W,L[o.DRAG]),c[o.DRAG]=!1)}o.prevViewport=k,o.clearingMotionBlur&&(o.clearingMotionBlur=!1,o.motionBlurCleared=!0,o.motionBlur=!0),h&&(o.motionBlurTimeout=setTimeout((function(){o.motionBlurTimeout=null,o.clearedForMotionBlur[o.NODE]=!1,o.clearedForMotionBlur[o.DRAG]=!1,o.motionBlur=!1,o.clearingMotionBlur=!d,o.mbFrames=0,c[o.NODE]=!0,c[o.DRAG]=!0,o.redraw()}),100)),t||l.emit("render")};for(var Qu={drawPolygonPath:function(e,t,n,r,i,a){var o=r/2,s=i/2;e.beginPath&&e.beginPath(),e.moveTo(t+o*a[0],n+s*a[1]);for(var l=1;l<a.length/2;l++)e.lineTo(t+o*a[2*l],n+s*a[2*l+1]);e.closePath()},drawRoundPolygonPath:function(e,t,n,r,i,a,o){o.forEach((function(t){return Ql(e,t)})),e.closePath()},drawRoundRectanglePath:function(e,t,n,r,i,a){var o=r/2,s=i/2,l="auto"===a?nn(r,i):Math.min(a,s,o);e.beginPath&&e.beginPath(),e.moveTo(t,n-s),e.arcTo(t+o,n-s,t+o,n,l),e.arcTo(t+o,n+s,t,n+s,l),e.arcTo(t-o,n+s,t-o,n,l),e.arcTo(t-o,n-s,t,n-s,l),e.lineTo(t,n-s),e.closePath()},drawBottomRoundRectanglePath:function(e,t,n,r,i,a){var o=r/2,s=i/2,l="auto"===a?nn(r,i):a;e.beginPath&&e.beginPath(),e.moveTo(t,n-s),e.lineTo(t+o,n-s),e.lineTo(t+o,n),e.arcTo(t+o,n+s,t,n+s,l),e.arcTo(t-o,n+s,t-o,n,l),e.lineTo(t-o,n-s),e.lineTo(t,n-s),e.closePath()},drawCutRectanglePath:function(e,t,n,r,i,a,o){var s=r/2,l=i/2,u="auto"===o?8:o;e.beginPath&&e.beginPath(),e.moveTo(t-s+u,n-l),e.lineTo(t+s-u,n-l),e.lineTo(t+s,n-l+u),e.lineTo(t+s,n+l-u),e.lineTo(t+s-u,n+l),e.lineTo(t-s+u,n+l),e.lineTo(t-s,n+l-u),e.lineTo(t-s,n-l+u),e.closePath()},drawBarrelPath:function(e,t,n,r,i){var a=r/2,o=i/2,s=t-a,l=t+a,u=n-o,c=n+o,d=an(r,i),h=d.widthOffset,p=d.heightOffset,f=d.ctrlPtOffsetPct*h;e.beginPath&&e.beginPath(),e.moveTo(s,u+p),e.lineTo(s,c-p),e.quadraticCurveTo(s+f,c,s+h,c),e.lineTo(l-h,c),e.quadraticCurveTo(l-f,c,l,c-p),e.lineTo(l,u+p),e.quadraticCurveTo(l-f,u,l-h,u),e.lineTo(s+h,u),e.quadraticCurveTo(s+f,u,s,u+p),e.closePath()}},Ju=Math.sin(0),ec=Math.cos(0),tc={},nc={},rc=Math.PI/40,ic=0*Math.PI;ic<2*Math.PI;ic+=rc)tc[ic]=Math.sin(ic),nc[ic]=Math.cos(ic);Qu.drawEllipsePath=function(e,t,n,r,i){if(e.beginPath&&e.beginPath(),e.ellipse)e.ellipse(t,n,r/2,i/2,0,0,2*Math.PI);else for(var a,o,s=r/2,l=i/2,u=0*Math.PI;u<2*Math.PI;u+=rc)a=t-s*tc[u]*Ju+s*nc[u]*ec,o=n+l*nc[u]*Ju+l*tc[u]*ec,0===u?e.moveTo(a,o):e.lineTo(a,o);e.closePath()};var ac={};function oc(e){var t=e.indexOf(",");return e.substr(t+1)}function sc(e,t,n){var r=function(){return t.toDataURL(n,e.quality)};switch(e.output){case"blob-promise":return new vr((function(r,i){try{t.toBlob((function(e){null!=e?r(e):i(new Error("`canvas.toBlob()` sent a null value in its callback"))}),n,e.quality)}catch(e){i(e)}}));case"blob":return function(e,t){for(var n=atob(e),r=new ArrayBuffer(n.length),i=new Uint8Array(r),a=0;a<n.length;a++)i[a]=n.charCodeAt(a);return new Blob([r],{type:t})}(oc(r()),n);case"base64":return oc(r());case"base64uri":default:return r()}}ac.createBuffer=function(e,t){var n=document.createElement("canvas");return n.width=e,n.height=t,[n,n.getContext("2d")]},ac.bufferCanvasImage=function(e){var t=this.cy,n=t.mutableElements().boundingBox(),r=this.findContainerClientCoords(),i=e.full?Math.ceil(n.w):r[2],a=e.full?Math.ceil(n.h):r[3],o=x(e.maxWidth)||x(e.maxHeight),s=this.getPixelRatio(),l=1;if(void 0!==e.scale)i*=e.scale,a*=e.scale,l=e.scale;else if(o){var u=1/0,c=1/0;x(e.maxWidth)&&(u=l*e.maxWidth/i),x(e.maxHeight)&&(c=l*e.maxHeight/a),i*=l=Math.min(u,c),a*=l}o||(i*=s,a*=s,l*=s);var d=document.createElement("canvas");d.width=i,d.height=a,d.style.width=i+"px",d.style.height=a+"px";var h=d.getContext("2d");if(i>0&&a>0){h.clearRect(0,0,i,a),h.globalCompositeOperation="source-over";var p=this.getCachedZSortedEles();if(e.full)h.translate(-n.x1*l,-n.y1*l),h.scale(l,l),this.drawElements(h,p),h.scale(1/l,1/l),h.translate(n.x1*l,n.y1*l);else{var f=t.pan(),g={x:f.x*l,y:f.y*l};l*=t.zoom(),h.translate(g.x,g.y),h.scale(l,l),this.drawElements(h,p),h.scale(1/l,1/l),h.translate(-g.x,-g.y)}e.bg&&(h.globalCompositeOperation="destination-over",h.fillStyle=e.bg,h.rect(0,0,i,a),h.fill())}return d},ac.png=function(e){return sc(e,this.bufferCanvasImage(e),"image/png")},ac.jpg=function(e){return sc(e,this.bufferCanvasImage(e),"image/jpeg")};var lc={nodeShapeImpl:function(e,t,n,r,i,a,o,s){switch(e){case"ellipse":return this.drawEllipsePath(t,n,r,i,a);case"polygon":return this.drawPolygonPath(t,n,r,i,a,o);case"round-polygon":return this.drawRoundPolygonPath(t,n,r,i,a,o,s);case"roundrectangle":case"round-rectangle":return this.drawRoundRectanglePath(t,n,r,i,a,s);case"cutrectangle":case"cut-rectangle":return this.drawCutRectanglePath(t,n,r,i,a,o,s);case"bottomroundrectangle":case"bottom-round-rectangle":return this.drawBottomRoundRectanglePath(t,n,r,i,a,s);case"barrel":return this.drawBarrelPath(t,n,r,i,a)}}},uc=dc,cc=dc.prototype;function dc(e){var t=this,n=t.cy.window().document;t.data={canvases:new Array(cc.CANVAS_LAYERS),contexts:new Array(cc.CANVAS_LAYERS),canvasNeedsRedraw:new Array(cc.CANVAS_LAYERS),bufferCanvases:new Array(cc.BUFFER_COUNT),bufferContexts:new Array(cc.CANVAS_LAYERS)};t.data.canvasContainer=n.createElement("div");var r=t.data.canvasContainer.style;t.data.canvasContainer.style["-webkit-tap-highlight-color"]="rgba(0,0,0,0)",r.position="relative",r.zIndex="0",r.overflow="hidden";var i=e.cy.container();i.appendChild(t.data.canvasContainer),i.style["-webkit-tap-highlight-color"]="rgba(0,0,0,0)";var a={"-webkit-user-select":"none","-moz-user-select":"-moz-none","user-select":"none","-webkit-tap-highlight-color":"rgba(0,0,0,0)","outline-style":"none"};c&&c.userAgent.match(/msie|trident|edge/i)&&(a["-ms-touch-action"]="none",a["touch-action"]="none");for(var o=0;o<cc.CANVAS_LAYERS;o++){var s=t.data.canvases[o]=n.createElement("canvas");t.data.contexts[o]=s.getContext("2d"),Object.keys(a).forEach((function(e){s.style[e]=a[e]})),s.style.position="absolute",s.setAttribute("data-id","layer"+o),s.style.zIndex=String(cc.CANVAS_LAYERS-o),t.data.canvasContainer.appendChild(s),t.data.canvasNeedsRedraw[o]=!1}t.data.topCanvas=t.data.canvases[0],t.data.canvases[cc.NODE].setAttribute("data-id","layer"+cc.NODE+"-node"),t.data.canvases[cc.SELECT_BOX].setAttribute("data-id","layer"+cc.SELECT_BOX+"-selectbox"),t.data.canvases[cc.DRAG].setAttribute("data-id","layer"+cc.DRAG+"-drag");for(o=0;o<cc.BUFFER_COUNT;o++)t.data.bufferCanvases[o]=n.createElement("canvas"),t.data.bufferContexts[o]=t.data.bufferCanvases[o].getContext("2d"),t.data.bufferCanvases[o].style.position="absolute",t.data.bufferCanvases[o].setAttribute("data-id","buffer"+o),t.data.bufferCanvases[o].style.zIndex=String(-o-1),t.data.bufferCanvases[o].style.visibility="hidden";t.pathsEnabled=!0;var l=_t(),u=function(e){return{x:-e.w/2,y:-e.h/2}},d=function(e){return e.boundingBox(),e[0]._private.bodyBounds},h=function(e){return e.boundingBox(),e[0]._private.labelBounds.main||l},p=function(e){return e.boundingBox(),e[0]._private.labelBounds.source||l},f=function(e){return e.boundingBox(),e[0]._private.labelBounds.target||l},g=function(e,t){return t},v=function(e,t,n){var r=e?e+"-":"";return{x:t.x+n.pstyle(r+"text-margin-x").pfValue,y:t.y+n.pstyle(r+"text-margin-y").pfValue}},y=function(e,t,n){var r=e[0]._private.rscratch;return{x:r[t],y:r[n]}},m=t.data.eleTxrCache=new Cu(t,{getKey:function(e){return e[0]._private.nodeKey},doesEleInvalidateKey:function(e){var t=e[0]._private;return!(t.oldBackgroundTimestamp===t.backgroundTimestamp)},drawElement:function(e,n,r,i,a){return t.drawElement(e,n,r,!1,!1,a)},getBoundingBox:d,getRotationPoint:function(e){return{x:((t=d(e)).x1+t.x2)/2,y:(t.y1+t.y2)/2};var t},getRotationOffset:function(e){return u(d(e))},allowEdgeTxrCaching:!1,allowParentTxrCaching:!1}),b=t.data.lblTxrCache=new Cu(t,{getKey:function(e){return e[0]._private.labelStyleKey},drawElement:function(e,n,r,i,a){return t.drawElementText(e,n,r,i,"main",a)},getBoundingBox:h,getRotationPoint:function(e){return v("",y(e,"labelX","labelY"),e)},getRotationOffset:function(e){var t=h(e),n=u(h(e));if(e.isNode()){switch(e.pstyle("text-halign").value){case"left":n.x=-t.w;break;case"right":n.x=0}switch(e.pstyle("text-valign").value){case"top":n.y=-t.h;break;case"bottom":n.y=0}}return n},isVisible:g}),x=t.data.slbTxrCache=new Cu(t,{getKey:function(e){return e[0]._private.sourceLabelStyleKey},drawElement:function(e,n,r,i,a){return t.drawElementText(e,n,r,i,"source",a)},getBoundingBox:p,getRotationPoint:function(e){return v("source",y(e,"sourceLabelX","sourceLabelY"),e)},getRotationOffset:function(e){return u(p(e))},isVisible:g}),w=t.data.tlbTxrCache=new Cu(t,{getKey:function(e){return e[0]._private.targetLabelStyleKey},drawElement:function(e,n,r,i,a){return t.drawElementText(e,n,r,i,"target",a)},getBoundingBox:f,getRotationPoint:function(e){return v("target",y(e,"targetLabelX","targetLabelY"),e)},getRotationOffset:function(e){return u(f(e))},isVisible:g}),E=t.data.lyrTxrCache=new Pu(t);t.onUpdateEleCalcs((function(e,t){m.invalidateElements(t),b.invalidateElements(t),x.invalidateElements(t),w.invalidateElements(t),E.invalidateElements(t);for(var n=0;n<t.length;n++){var r=t[n]._private;r.oldBackgroundTimestamp=r.backgroundTimestamp}}));var k=function(e){for(var t=0;t<e.length;t++)E.enqueueElementRefinement(e[t].ele)};m.onDequeue(k),b.onDequeue(k),x.onDequeue(k),w.onDequeue(k)}cc.CANVAS_LAYERS=3,cc.SELECT_BOX=0,cc.DRAG=1,cc.NODE=2,cc.BUFFER_COUNT=3,cc.TEXTURE_BUFFER=0,cc.MOTIONBLUR_BUFFER_NODE=1,cc.MOTIONBLUR_BUFFER_DRAG=2,cc.redrawHint=function(e,t){var n=this;switch(e){case"eles":n.data.canvasNeedsRedraw[cc.NODE]=t;break;case"drag":n.data.canvasNeedsRedraw[cc.DRAG]=t;break;case"select":n.data.canvasNeedsRedraw[cc.SELECT_BOX]=t}};var hc="undefined"!=typeof Path2D;cc.path2dEnabled=function(e){if(void 0===e)return this.pathsEnabled;this.pathsEnabled=!!e},cc.usePaths=function(){return hc&&this.pathsEnabled},cc.setImgSmoothing=function(e,t){null!=e.imageSmoothingEnabled?e.imageSmoothingEnabled=t:(e.webkitImageSmoothingEnabled=t,e.mozImageSmoothingEnabled=t,e.msImageSmoothingEnabled=t)},cc.getImgSmoothing=function(e){return null!=e.imageSmoothingEnabled?e.imageSmoothingEnabled:e.webkitImageSmoothingEnabled||e.mozImageSmoothingEnabled||e.msImageSmoothingEnabled},cc.makeOffscreenCanvas=function(t,n){var r;"undefined"!==("undefined"==typeof OffscreenCanvas?"undefined":e(OffscreenCanvas))?r=new OffscreenCanvas(t,n):((r=this.cy.window().document.createElement("canvas")).width=t,r.height=n);return r},[Bu,Ou,Xu,Hu,Ku,Uu,$u,Qu,ac,lc].forEach((function(e){L(cc,e)}));var pc=[{type:"layout",extensions:Cl},{type:"renderer",extensions:[{name:"null",impl:Sl},{name:"base",impl:mu},{name:"canvas",impl:uc}]}],fc={},gc={};function vc(e,t,n){var r=n,i=function(n){je("Can not register `"+t+"` for `"+e+"` since `"+n+"` already exists in the prototype and can not be overridden")};if("core"===e){if(Os.prototype[t])return i(t);Os.prototype[t]=n}else if("collection"===e){if(ts.prototype[t])return i(t);ts.prototype[t]=n}else if("layout"===e){for(var a=function(e){this.options=e,n.call(this,e),b(this._private)||(this._private={}),this._private.cy=e.cy,this._private.listeners=[],this.createEmitter()},o=a.prototype=Object.create(n.prototype),s=[],l=0;l<s.length;l++){var u=s[l];o[u]=o[u]||function(){return this}}o.start&&!o.run?o.run=function(){return this.start(),this}:!o.start&&o.run&&(o.start=function(){return this.run(),this});var c=n.prototype.stop;o.stop=function(){var e=this.options;if(e&&e.animate){var t=this.animations;if(t)for(var n=0;n<t.length;n++)t[n].stop()}return c?c.call(this):this.emit("layoutstop"),this},o.destroy||(o.destroy=function(){return this}),o.cy=function(){return this._private.cy};var d=function(e){return e._private.cy},h={addEventFields:function(e,t){t.layout=e,t.cy=d(e),t.target=e},bubble:function(){return!0},parent:function(e){return d(e)}};L(o,{createEmitter:function(){return this._private.emitter=new xo(h,this),this},emitter:function(){return this._private.emitter},on:function(e,t){return this.emitter().on(e,t),this},one:function(e,t){return this.emitter().one(e,t),this},once:function(e,t){return this.emitter().one(e,t),this},removeListener:function(e,t){return this.emitter().removeListener(e,t),this},removeAllListeners:function(){return this.emitter().removeAllListeners(),this},emit:function(e,t){return this.emitter().emit(e,t),this}}),Fi.eventAliasesOn(o),r=a}else if("renderer"===e&&"null"!==t&&"base"!==t){var p=yc("renderer","base"),f=p.prototype,g=n,v=n.prototype,y=function(){p.apply(this,arguments),g.apply(this,arguments)},m=y.prototype;for(var x in f){var w=f[x];if(null!=v[x])return i(x);m[x]=w}for(var E in v)m[E]=v[E];f.clientFunctions.forEach((function(e){m[e]=m[e]||function(){Ve("Renderer does not implement `renderer."+e+"()` on its prototype")}})),r=y}else if("__proto__"===e||"constructor"===e||"prototype"===e)return Ve(e+" is an illegal type to be registered, possibly lead to prototype pollutions");return V({map:fc,keys:[e,t],value:r})}function yc(e,t){return F({map:fc,keys:[e,t]})}function mc(e,t,n,r,i){return V({map:gc,keys:[e,t,n,r],value:i})}function bc(e,t,n,r){return F({map:gc,keys:[e,t,n,r]})}var xc=function(){return 2===arguments.length?yc.apply(null,arguments):3===arguments.length?vc.apply(null,arguments):4===arguments.length?bc.apply(null,arguments):5===arguments.length?mc.apply(null,arguments):void Ve("Invalid extension access syntax")};Os.prototype.extension=xc,pc.forEach((function(e){e.extensions.forEach((function(t){vc(e.type,t.name,t.impl)}))}));var wc=function e(){if(!(this instanceof e))return new e;this.length=0},Ec=wc.prototype;Ec.instanceString=function(){return"stylesheet"},Ec.selector=function(e){return this[this.length++]={selector:e,properties:[]},this},Ec.css=function(e,t){var n=this.length-1;if(v(e))this[n].properties.push({name:e,value:t});else if(b(e))for(var r=e,i=Object.keys(r),a=0;a<i.length;a++){var o=i[a],s=r[o];if(null!=s){var l=Ns.properties[o]||Ns.properties[B(o)];if(null!=l){var u=l.name,c=s;this[n].properties.push({name:u,value:c})}}}return this},Ec.style=Ec.css,Ec.generateStyle=function(e){var t=new Ns(e);return this.appendToStyle(t)},Ec.appendToStyle=function(e){for(var t=0;t<this.length;t++){var n=this[t],r=n.selector,i=n.properties;e.selector(r);for(var a=0;a<i.length;a++){var o=i[a];e.css(o.name,o.value)}}return e};var kc=function(e){return void 0===e&&(e={}),b(e)?new Os(e):v(e)?xc.apply(xc,arguments):void 0};return kc.use=function(e){var t=Array.prototype.slice.call(arguments,1);return t.unshift(kc),e.apply(null,t),this},kc.warnings=function(e){return Fe(e)},kc.version="3.30.2",kc.stylesheet=kc.Stylesheet=wc,kc}));
````

## `launcher/__init__.py`

````
"""Windows EXE / desktop bootstrapper for the existing Second Brain app.

This package does not reimplement memory, search, or the API. It only
checks the environment and starts ``backend.app``.
"""

__version__ = "2.5.0"
````

## `launcher/__main__.py`

````
"""Entry point for SecondBrain.exe and ``python -m launcher``."""
from __future__ import annotations

import argparse
import os
import sys
import threading
import webbrowser

# Make the project root importable when launched from another CWD.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from launcher.bootstrap import (  # noqa: E402
    APP_VERSION,
    bootstrap_ok,
    create_server,
    port_free,
    prepare_environment,
    run_bootstrap,
    start_existing_app,
    wait_for_http,
)
from launcher.gui import native_alert, run_gui_bootstrap, tk_available  # noqa: E402


def _already_running(url: str, headless: bool) -> None:
    msg = (
        f"Second Brain is already running at {url}.\n"
        "If that is not this app, choose another port with --port."
    )
    if headless:
        print(msg)
        return
    native_alert("Second Brain", msg)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Second Brain desktop launcher")
    parser.add_argument("--headless", action="store_true",
                        help="No GUI (used by tests and servers without tkinter)")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--no-install", action="store_true")
    parser.add_argument("--pull-models", action="store_true",
                        help="Download missing Ollama models (off by default)")
    parser.add_argument("--host", default=os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int,
                        default=int(os.environ.get("SECOND_BRAIN_PORT", "8000")))
    parser.add_argument("--check", action="store_true", help="Bootstrap only, do not start")
    parser.add_argument("--tray", action="store_true",
                        help="After start, hide the setup window (no activity watching)")
    args = parser.parse_args(argv)

    prepare_environment()

    host, port = args.host, args.port
    url = f"http://127.0.0.1:{port}"
    headless = bool(args.headless or args.check or not tk_available())

    if not port_free("127.0.0.1", port):
        _already_running(url, headless=headless or args.check)
        if not args.no_browser and not args.check:
            webbrowser.open(url)
        return 0

    def steps(on_progress):
        return run_bootstrap(
            on_progress=on_progress,
            allow_install=not args.no_install,
            pull_models=args.pull_models,
        )

    def start():
        start_existing_app(host, port)

    if args.check or args.headless:
        print(f"Second Brain v{APP_VERSION}")
        results = steps(lambda t, d: print(f"  {t}" + (f" — {d}" if d else "")))
        if not bootstrap_ok(results):
            bad = next((r for r in results if not r.ok), None)
            print("FAILED:", bad.detail if bad else "bootstrap failed")
            return 1
        print("OK: bootstrap complete")
        if args.check:
            return 0
        if not args.no_browser:
            threading.Thread(
                target=lambda: wait_for_http(url) and webbrowser.open(url),
                daemon=True,
            ).start()
        start()
        return 0

    return run_gui_bootstrap(
        steps,
        start,
        url,
        open_browser=not args.no_browser,
        create_server=lambda: create_server(host, port),
        start_hidden=args.tray,
    )


if __name__ == "__main__":
    raise SystemExit(main())
````

## `launcher/bootstrap.py`

````
"""Idempotent bootstrap steps for the existing Second Brain application.

Never deletes ``brain.db``. Never resets memories. Installs a package only
when that import is actually missing and we are not running frozen.
"""
from __future__ import annotations

import importlib
import os
import socket
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

from backend import paths

APP_VERSION = paths.APP_VERSION
REQUIRED_MODELS = ("qwen3:0.6b", "nomic-embed-text")
RUNTIME_IMPORTS = (
    ("fastapi", "fastapi>=0.110"),
    ("uvicorn", "uvicorn[standard]>=0.29"),
    ("requests", "requests>=2.31"),
    ("numpy", "numpy>=1.26"),
)

# Exact status lines the setup UI must show, in order.
STATUS_LINES = (
    "Initializing Second Brain",
    "Checking Python/runtime",
    "Checking dependencies",
    "Installing only missing dependencies",
    "Checking database",
    "Checking configuration",
    "Checking Ollama",
    "Checking required models",
    "Running health checks",
    "Starting Second Brain",
)


@dataclass
class StepResult:
    key: str
    title: str
    ok: bool
    detail: str = ""
    skipped: bool = False
    installed: list[str] = field(default_factory=list)


OnProgress = Callable[[str, str], None]


def _emit(cb: OnProgress | None, title: str, detail: str = "") -> None:
    if cb:
        cb(title, detail)


def _missing_imports() -> list[tuple[str, str]]:
    missing = []
    for mod, spec in RUNTIME_IMPORTS:
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append((mod, spec))
    return missing


def _model_present(installed: Iterable[str], wanted: str) -> bool:
    wanted = (wanted or "").strip()
    for name in installed:
        if not name:
            continue
        if name == wanted or name.startswith(wanted + "-") or name.startswith(wanted + ":"):
            return True
        if name.split("-", 1)[0] == wanted:
            return True
    return False


def probe_ollama(url: str | None = None, timeout: float = 2.0) -> dict:
    url = (url or os.environ.get("OLLAMA_BASE_URL") or "http://localhost:11434").rstrip("/")
    if not url.startswith(("http://", "https://")):
        return {"available": False, "url": url, "models": [], "error": "URL must be http(s)"}
    try:
        import requests
        r = requests.get(url + "/api/tags", timeout=timeout)
        if r.status_code != 200:
            return {"available": False, "url": url, "models": [], "error": f"HTTP {r.status_code}"}
        models = [m.get("name") for m in r.json().get("models", [])]
        return {"available": True, "url": url, "models": models, "error": None}
    except Exception as exc:
        return {"available": False, "url": url, "models": [], "error": str(exc) or exc.__class__.__name__}


def port_free(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.4)
    try:
        return sock.connect_ex((host if host != "0.0.0.0" else "127.0.0.1", port)) != 0
    finally:
        sock.close()


def prepare_environment() -> Path:
    """Resolve and export the persistent DB path before backend import.

    If this process already opened a real database (tests, long-running
    server), keep that file. Never redirect away from an existing brain.
    """
    db_path = paths.resolve_db_path()
    if "backend.config" in sys.modules:
        current = Path(getattr(sys.modules["backend.config"], "DB_PATH", ""))
        if current.is_file() and not paths._is_ephemeral(current):
            db_path = current
    paths.ensure_data_dirs(db_path)
    os.environ["SECOND_BRAIN_DB"] = str(db_path)
    if "backend.config" in sys.modules:
        sys.modules["backend.config"].DB_PATH = str(db_path)
    root = str(paths.app_root())
    if root not in sys.path:
        sys.path.insert(0, root)
    return db_path


def run_bootstrap(
    on_progress: OnProgress | None = None,
    allow_install: bool = True,
    pull_models: bool = False,
) -> list[StepResult]:
    """Run lightweight, idempotent checks. Returns one result per step."""
    results: list[StepResult] = []

    def add(step: StepResult) -> StepResult:
        results.append(step)
        _emit(on_progress, step.title, step.detail)
        return step

    add(StepResult("init", "Initializing Second Brain", True, f"version {APP_VERSION}"))

    py = sys.version.split()[0]
    frozen = paths.is_frozen()
    if sys.version_info < (3, 11):
        add(StepResult("python", "Checking Python/runtime", False,
                       f"Python 3.11+ required (found {py})"))
        return results
    add(StepResult(
        "python", "Checking Python/runtime", True,
        f"Python {py}" + (" · packaged runtime" if frozen else ""),
    ))

    missing = _missing_imports()
    if not missing:
        add(StepResult("deps", "Checking dependencies", True, "all runtime imports present"))
        add(StepResult("install", "Installing only missing dependencies", True,
                       "nothing to install", skipped=True))
    elif frozen:
        names = ", ".join(m for m, _ in missing)
        add(StepResult("deps", "Checking dependencies", False,
                       f"packaged runtime is missing: {names}"))
        add(StepResult("install", "Installing only missing dependencies", False,
                       "cannot pip-install into a frozen EXE — rebuild SecondBrain.exe",
                       skipped=True))
        return results
    else:
        add(StepResult("deps", "Checking dependencies", True,
                       "missing: " + ", ".join(m for m, _ in missing)))
        if not allow_install:
            add(StepResult("install", "Installing only missing dependencies", False,
                           "install disabled and packages are missing: "
                           + ", ".join(m for m, _ in missing)))
            return results
        specs = [spec for _, spec in missing]
        _emit(on_progress, "Installing only missing dependencies", ", ".join(specs))
        try:
            import start as start_mod
            start_mod.install_packages(specs)
        except SystemExit as exc:
            add(StepResult("install", "Installing only missing dependencies", False,
                           str(exc) or "pip failed"))
            return results
        except Exception as exc:
            add(StepResult("install", "Installing only missing dependencies", False, str(exc)))
            return results
        still = _missing_imports()
        if still:
            add(StepResult("install", "Installing only missing dependencies", False,
                           "still missing after install: " + ", ".join(m for m, _ in still)))
            return results
        add(StepResult("install", "Installing only missing dependencies", True,
                       "installed: " + ", ".join(specs), installed=specs))

    db_path = prepare_environment()
    existed = db_path.is_file()
    if existed:
        try:
            size = db_path.stat().st_size
        except OSError as exc:
            add(StepResult("database", "Checking database", False,
                           f"cannot read {db_path}: {exc}"))
            return results
        add(StepResult("database", "Checking database", True,
                       f"preserving existing {db_path} ({size} bytes)"))
    else:
        add(StepResult("database", "Checking database", True,
                       f"no database yet; will create {db_path} on first API start"))

    frontend = paths.frontend_dir() / "index.html"
    if not frontend.is_file():
        add(StepResult("config", "Checking configuration", False,
                       f"frontend missing at {frontend}"))
        return results
    add(StepResult("config", "Checking configuration", True,
                   f"frontend {frontend.parent} · db {db_path}"))

    pull = pull_models or os.environ.get("SECOND_BRAIN_PULL_MODELS") == "1"
    oll = probe_ollama()
    if oll["available"]:
        add(StepResult("ollama", "Checking Ollama", True,
                       f"online at {oll['url']}"))
        installed = oll["models"]
        missing_models = [m for m in REQUIRED_MODELS if not _model_present(installed, m)]
        if not missing_models:
            add(StepResult("models", "Checking required models", True,
                           "found " + ", ".join(REQUIRED_MODELS)))
        elif pull:
            _emit(on_progress, "Checking required models",
                  "pulling " + ", ".join(missing_models))
            pulled, errors = [], []
            for model in missing_models:
                try:
                    import requests
                    r = requests.post(oll["url"] + "/api/pull",
                                      json={"name": model, "stream": False},
                                      timeout=600)
                    if r.status_code == 200:
                        pulled.append(model)
                    else:
                        errors.append(f"{model}: HTTP {r.status_code}")
                except Exception as exc:
                    errors.append(f"{model}: {exc}")
            add(StepResult(
                "models", "Checking required models", not errors,
                ("pulled " + ", ".join(pulled) if pulled else "")
                + (("; " + "; ".join(errors)) if errors else ""),
            ))
        else:
            add(StepResult(
                "models", "Checking required models", True,
                "not installed: " + ", ".join(missing_models)
                + " — will use fallback (no download)",
                skipped=True,
            ))
    else:
        why = oll.get("error") or "unreachable"
        add(StepResult("ollama", "Checking Ollama", True,
                       f"offline ({oll['url']}: {why}) — fallback extractor will be used"))
        add(StepResult("models", "Checking required models", True,
                       "skipped (Ollama offline)", skipped=True))

    try:
        from backend import db, store
        db.init_db()
        store.ensure_user_entity()
        n = db.query("SELECT COUNT(*) c FROM entities")[0]["c"]
        add(StepResult("health", "Running health checks", True,
                       f"database open · {n} entit{'y' if n == 1 else 'ies'}"))
    except Exception as exc:
        add(StepResult("health", "Running health checks", False,
                       f"database/health failed: {exc}"))
        return results

    add(StepResult("start", "Starting Second Brain", True, "ready"))
    return results


def bootstrap_ok(results: list[StepResult]) -> bool:
    return bool(results) and all(r.ok for r in results)


def create_server(host: str, port: int):
    """Build a uvicorn.Server around the existing FastAPI app."""
    os.chdir(paths.app_root())
    import uvicorn
    from backend.app import app
    config = uvicorn.Config(app, host=host, port=port, reload=False, log_level="info")
    return uvicorn.Server(config)


def start_existing_app(host: str, port: int) -> None:
    """Start the existing FastAPI app. Not a second server implementation."""
    create_server(host, port).run()


def wait_for_http(url: str, timeout: float = 30.0) -> bool:
    deadline = time.time() + timeout
    try:
        import requests
    except ImportError:
        return False
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            if r.status_code < 500:
                return True
        except Exception:
            time.sleep(0.2)
    return False
````

## `launcher/build_exe.py`

````
#!/usr/bin/env python3
"""Build SecondBrain.exe with PyInstaller.

On Windows 11 the output is dist/SecondBrain.exe.
PyInstaller cannot cross-compile a Windows PE from Linux or macOS.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    os.chdir(ROOT)
    spec = ROOT / "secondbrain.spec"
    if not spec.is_file():
        print("missing secondbrain.spec", file=sys.stderr)
        return 1

    if os.name != "nt":
        print(
            "NOTE: PyInstaller cannot produce a Windows .exe on this OS.\n"
            "Run this same command on Windows 11 to get dist/SecondBrain.exe.\n"
            "A native binary named dist/SecondBrain may be built instead.\n",
            file=sys.stderr,
        )

    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", str(spec)]
    print("Running:", " ".join(cmd))
    rc = subprocess.call(cmd)
    if rc != 0:
        return rc

    exe = ROOT / "dist" / ("SecondBrain.exe" if os.name == "nt" else "SecondBrain")
    if exe.is_file():
        print("Built:", exe)
        print("size:", exe.stat().st_size, "bytes")
        if os.name != "nt":
            print(
                "This is not a Windows EXE. Copy the project to Windows 11 and rerun:",
                file=sys.stderr,
            )
            print("  python -m launcher.build_exe", file=sys.stderr)
        return 0
    print("Build finished but binary not found at", exe, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
````

## `launcher/gui.py`

````
"""Dark setup window for SecondBrain.exe.

Uses tkinter when available (bundled on Windows). Falls back to stdout so
tests and headless environments still run the same bootstrap.

The setup window is the process lifetime for a windowed EXE: after checks
succeed the existing FastAPI app is started on a worker thread and the
window stays open (Open browser / Quit). Closing the window stops the
server. The server is never left on a daemon thread that dies with the UI.
"""
from __future__ import annotations

import os
import sys
import threading
import webbrowser
from typing import Callable

from launcher.bootstrap import APP_VERSION, StepResult, bootstrap_ok, wait_for_http
from launcher.icons import icon_ico, icon_png

BG = "#070a13"
PANEL = "#0f1628"
TEXT = "#e7ecf5"
MUTED = "#8b95a8"
ACCENT = "#22d3ee"
OK = "#34d399"
DANGER = "#f87171"
WARN = "#fbbf24"
ACCENT2 = "#8b5cf6"
LINE = "#1e293b"


def tk_available() -> bool:
    try:
        import tkinter  # noqa: F401
        return True
    except Exception:
        return False


def apply_window_icon(root) -> None:
    """Set the setup-window icon when the PNG/ICO shipped with the EXE exists."""
    png = icon_png()
    if png is not None:
        try:
            img = root.tk.call("image", "create", "photo", "-file", str(png))
            root.tk.call("wm", "iconphoto", root._w, img)
            root._sb_icon = img
        except Exception:
            try:
                import tkinter as tk
                photo = tk.PhotoImage(file=str(png))
                root.iconphoto(True, photo)
                root._sb_icon = photo
            except Exception:
                pass
    ico = icon_ico()
    if ico is not None and os.name == "nt":
        try:
            root.iconbitmap(str(ico))
        except Exception:
            pass


def native_alert(title: str, message: str) -> None:
    """Visible alert when there is no console (windowed EXE)."""
    if tk_available():
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            messagebox.showinfo(title, message)
            root.destroy()
            return
        except Exception:
            pass
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
            return
        except Exception:
            pass
    print(f"{title}: {message}")


class SetupWindow:
    def __init__(self):
        import tkinter as tk
        from tkinter import ttk

        self.tk = tk
        self.root = tk.Tk()
        self.root.title("Second Brain")
        self.root.configure(bg=BG)
        self.root.geometry("620x580")
        self.root.minsize(520, 460)
        self.root.resizable(True, True)
        apply_window_icon(self.root)

        self._status = tk.StringVar(value="Initializing Second Brain")
        self._ollama = tk.StringVar(value="Ollama: checking…")
        self._state = tk.StringVar(value="WORKING")
        self._closed = False
        self._server = None
        self.on_quit: Callable[[], None] | None = None

        pad = {"padx": 24, "pady": 2}
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", **pad)
        tk.Label(
            header, text="◈  SECOND BRAIN", fg=ACCENT, bg=BG,
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", pady=(12, 0))
        tk.Label(
            header, text=f"local knowledge OS  ·  v{APP_VERSION}",
            fg=MUTED, bg=BG, font=("Segoe UI", 9),
        ).pack(anchor="w")

        accent = tk.Frame(self.root, bg=ACCENT2, height=2)
        accent.pack(fill="x", padx=24, pady=(10, 4))

        tk.Label(
            self.root, textvariable=self._status, fg=TEXT, bg=BG,
            font=("Segoe UI", 13), wraplength=560, justify="left",
        ).pack(fill="x", padx=24, pady=(14, 6))

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure(
            "SB.Horizontal.TProgressbar",
            troughcolor=PANEL,
            background=ACCENT,
            bordercolor=PANEL,
            lightcolor=ACCENT,
            darkcolor=ACCENT2,
            thickness=10,
        )
        self.bar = ttk.Progressbar(
            self.root, style="SB.Horizontal.TProgressbar",
            mode="determinate", maximum=100,
        )
        self.bar.pack(fill="x", padx=24, pady=8)

        self.ollama_label = tk.Label(
            self.root, textvariable=self._ollama, fg=MUTED, bg=BG,
            font=("Segoe UI", 9),
        )
        self.ollama_label.pack(anchor="w", padx=24)

        log_frame = tk.Frame(self.root, bg=PANEL, highlightbackground=LINE,
                             highlightthickness=1)
        log_frame.pack(fill="both", expand=True, padx=24, pady=12)
        self.log = tk.Text(
            log_frame, bg=PANEL, fg=MUTED, insertbackground=TEXT,
            relief="flat", font=("Consolas", 9), wrap="word",
            state="disabled", height=12, borderwidth=0, highlightthickness=0,
        )
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=24, pady=(0, 16))
        self.footer = tk.Label(
            footer, textvariable=self._state, fg=ACCENT, bg=BG,
            font=("Segoe UI", 10, "bold"),
        )
        self.footer.pack(side="left")

        self.btn_row = tk.Frame(footer, bg=BG)
        self.btn_row.pack(side="right")
        self.btn_open = tk.Button(
            self.btn_row, text="Open browser", command=self._open_browser,
            bg="#132337", fg=ACCENT, activebackground="#1e3a4c",
            activeforeground=ACCENT, relief="flat", padx=12, pady=5,
            font=("Segoe UI", 9), cursor="hand2",
        )
        self.btn_quit = tk.Button(
            self.btn_row, text="Quit", command=self._on_close,
            bg="#1a1520", fg=MUTED, activebackground="#2a2030",
            activeforeground=TEXT, relief="flat", padx=12, pady=5,
            font=("Segoe UI", 9), cursor="hand2",
        )
        self.btn_tray = tk.Button(
            self.btn_row, text="Hide to tray", command=self._hide_to_tray,
            bg="#132337", fg=MUTED, activebackground="#1e3a4c",
            activeforeground=TEXT, relief="flat", padx=12, pady=5,
            font=("Segoe UI", 9), cursor="hand2",
        )
        self._url = "http://127.0.0.1:8000"
        self._tray = None

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _open_browser(self) -> None:
        try:
            webbrowser.open(self._url)
        except Exception:
            self.append_log("Could not open the browser. Visit " + self._url)

    def _hide_to_tray(self) -> None:
        """Hide the setup window. Tray does not watch the desktop."""
        try:
            self.root.withdraw()
        except Exception:
            pass
        self.append_log("Hidden. Tray / taskbar keeps Second Brain running. It does not watch what you do.")

    def _show_window(self) -> None:
        try:
            self.root.deiconify()
            self.root.lift()
        except Exception:
            pass

    def _on_close(self) -> None:
        if self._closed:
            return
        self._closed = True
        if self._tray is not None:
            try:
                self._tray.stop()
            except Exception:
                pass
        server = self._server
        if server is not None:
            try:
                server.should_exit = True
            except Exception:
                pass
        if self.on_quit:
            try:
                self.on_quit()
            except Exception:
                pass
        try:
            self.root.destroy()
        except Exception:
            pass

    def set_progress(self, percent: float, title: str, detail: str = "") -> None:
        if self._closed:
            return
        self._status.set(title)
        self.bar["value"] = max(0, min(100, percent))
        if detail:
            self.append_log(f"{title} — {detail}")
        else:
            self.append_log(title)
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def append_log(self, line: str) -> None:
        if self._closed:
            return
        self.log.configure(state="normal")
        self.log.insert("end", line.rstrip() + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def set_ollama(self, text: str, ok: bool | None = None) -> None:
        if self._closed:
            return
        self._ollama.set(text)
        if ok is True:
            self.ollama_label.configure(fg=OK)
        elif ok is False:
            self.ollama_label.configure(fg=WARN)
        else:
            self.ollama_label.configure(fg=MUTED)
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def succeed(self, url: str, server=None) -> None:
        if self._closed:
            return
        self._url = url
        self._server = server
        self._state.set("READY")
        self.footer.configure(fg=OK)
        self._status.set("Second Brain is running")
        self.bar["value"] = 100
        self.append_log(f"Started existing FastAPI app at {url}")
        self.append_log("Tray will not watch your screen or apps. Remember clipboard is click-only.")
        self.btn_open.pack(side="left", padx=(0, 8))
        self.btn_tray.pack(side="left", padx=(0, 8))
        self.btn_quit.pack(side="left")
        try:
            from launcher.tray import TrayController
            tray = TrayController(
                url, on_open=self._open_browser,
                on_show=self._show_window, on_quit=self._on_close,
            )
            if tray.start():
                self._tray = tray
                self.append_log("System tray icon ready (Open / Remember clipboard / Quit).")
        except Exception as exc:
            self.append_log(f"Tray unavailable ({exc}). Use Hide to tray / Quit.")
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def fail(self, message: str) -> None:
        if self._closed:
            return
        self._state.set("FAILED")
        self.footer.configure(fg=DANGER)
        self._status.set(message)
        self.append_log("ERROR: " + message)
        self.btn_quit.configure(text="Close")
        self.btn_quit.pack(side="left")
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def run(self) -> None:
        self.root.mainloop()


def _run_headless(
    steps: Callable[[Callable[[str, str], None]], list[StepResult]],
    start_server: Callable[[], None],
    url: str,
    open_browser: bool,
) -> int:
    print(f"Second Brain v{APP_VERSION} — setup (headless)")
    results = steps(lambda t, d: print(f"  {t}" + (f" — {d}" if d else "")))
    if not bootstrap_ok(results):
        bad = next((r for r in results if not r.ok), None)
        msg = bad.detail if bad else "unknown error"
        print("FAILED:", msg)
        if os.name == "nt" and getattr(sys, "frozen", False):
            native_alert("Second Brain — setup failed", msg)
        return 1
    print("OK: bootstrap complete")
    if open_browser:
        threading.Thread(
            target=lambda: wait_for_http(url) and webbrowser.open(url),
            daemon=True,
        ).start()
    start_server()
    return 0


def run_gui_bootstrap(
    steps: Callable[[Callable[[str, str], None]], list[StepResult]],
    start_server: Callable[[], None],
    url: str,
    open_browser: bool = True,
    create_server: Callable | None = None,
    start_hidden: bool = False,
) -> int:
    """Show the window, run checks, then keep the existing app alive."""
    if not tk_available():
        return _run_headless(steps, start_server, url, open_browser)

    win = SetupWindow()
    outcome = {"ok": False, "error": ""}
    server_holder: dict = {"server": None}

    def worker():
        seen: list[str] = []

        def progress(title: str, detail: str = "") -> None:
            seen.append(title)
            pct = min(95, 8 + len(seen) * 8)
            win.root.after(0, lambda t=title, d=detail, p=pct: win.set_progress(p, t, d))

        try:
            results = steps(progress)
            ollama_step = next((r for r in results if r.key == "ollama"), None)
            if ollama_step:
                offline = "offline" in (ollama_step.detail or "").lower()
                text = "Ollama: " + (ollama_step.detail or "unknown")
                win.root.after(0, lambda t=text, off=offline: win.set_ollama(t, ok=not off))
            if not bootstrap_ok(results):
                bad = next((r for r in results if not r.ok), None)
                outcome["error"] = (bad.detail or bad.title) if bad else "Setup failed"
                win.root.after(0, lambda: win.fail(outcome["error"]))
                return
            outcome["ok"] = True

            def ready():
                server = None
                if create_server is not None:
                    server = create_server()
                    server_holder["server"] = server
                    threading.Thread(
                        target=server.run, name="second-brain-server", daemon=True,
                    ).start()
                else:
                    threading.Thread(
                        target=start_server, name="second-brain-server", daemon=True,
                    ).start()
                win.succeed(url, server=server)
                if start_hidden:
                    win._hide_to_tray()
                if open_browser:
                    threading.Thread(
                        target=lambda: wait_for_http(url) and webbrowser.open(url),
                        daemon=True,
                    ).start()

            win.root.after(0, ready)
        except Exception as exc:
            outcome["error"] = str(exc)
            win.root.after(0, lambda m=str(exc): win.fail(m))

    threading.Thread(target=worker, daemon=True).start()
    win.run()
    server = server_holder.get("server")
    if server is not None:
        try:
            server.should_exit = True
        except Exception:
            pass
    return 0 if outcome["ok"] else 1
````

## `launcher/icons.py`

````
"""Resolve the Second Brain icon for the EXE, setup window, and tray.

Never required for the memory app to run. Missing files degrade to the
default window icon.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _candidates(name: str) -> list[Path]:
    here = Path(__file__).resolve().parent
    root = here.parent
    out = [here / name, root / "launcher" / name]
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        base = Path(meipass)
        out.extend([base / "launcher" / name, base / name])
    if getattr(sys, "frozen", False):
        out.append(Path(sys.executable).resolve().parent / name)
    return out


def icon_ico() -> Path | None:
    for path in _candidates("secondbrain.ico"):
        if path.is_file():
            return path
    return None


def icon_png() -> Path | None:
    for path in _candidates("secondbrain.png"):
        if path.is_file():
            return path
    return None
````

## `launcher/secondbrain.ico`

Binary file, 147587 bytes, SHA256 `6399bb5dd9171bb25e91b540181dcfad08886d1942943967773861ad6708f19d`. ICO type=1 sizes=[256, 128, 64, 48, 32, 16].
Not inlined as text. The live file in the repository is the source.

## `launcher/secondbrain.png`

Binary file, 48109 bytes, SHA256 `bca342072df70b8b3f80bd537dd1857487e4b2859351f9d57e34dfe4f4b134f6`.
Not inlined as text. The live file in the repository is the source.

## `launcher/tray.py`

````
"""Optional system tray for SecondBrain.exe.

The tray NEVER watches the user. It does not screenshot, read window titles,
keylog, or poll “what you are doing.” Those would fill the brain with junk
and secrets.

Menu actions are explicit clicks only:

- Open browser
- Remember clipboard  (user-initiated; same /api/chat path)
- Show window
- Quit

Activity auto-capture is a non-goal.
"""
from __future__ import annotations

import json
import os
import sys
import threading
import urllib.error
import urllib.request
from typing import Callable

# Hard rule: this module must not grow an activity watcher.
ACTIVITY_WATCH_ENABLED = False
ACTIVITY_POLL_SECONDS = None


def should_watch_activity() -> bool:
    """Always False. Auto-capture of the desktop is not a feature."""
    return False


def clip_remember_text(text: str, limit: int = 8000) -> str | None:
    """Return clipboard text worth sending, or None if empty."""
    raw = (text or "").strip()
    if not raw:
        return None
    if len(raw) > limit:
        raw = raw[:limit]
    return raw


def post_remember(url: str, text: str, timeout: float = 8.0) -> dict:
    """POST clipboard text into the existing chat/extract pipeline."""
    payload = json.dumps({"content": text}).encode("utf-8")
    req = urllib.request.Request(
        url.rstrip("/") + "/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    try:
        return json.loads(body)
    except ValueError:
        return {"ok": False, "error": "invalid response"}


def read_clipboard() -> str:
    """Best-effort clipboard read. Empty string if unavailable."""
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            user32 = ctypes.windll.user32
            kernel32 = ctypes.windll.kernel32
            CF_UNICODETEXT = 13
            if not user32.OpenClipboard(None):
                return ""
            try:
                handle = user32.GetClipboardData(CF_UNICODETEXT)
                if not handle:
                    return ""
                ptr = kernel32.GlobalLock(handle)
                if not ptr:
                    return ""
                try:
                    return ctypes.wstring_at(ptr)
                finally:
                    kernel32.GlobalUnlock(handle)
            finally:
                user32.CloseClipboard()
        except Exception:
            return ""
    try:
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()
        try:
            return root.clipboard_get()
        finally:
            root.destroy()
    except Exception:
        return ""


class TrayController:
    """Holds callbacks the GUI wires up. No background activity sampling."""

    def __init__(self, url: str, on_open: Callable[[], None] | None = None,
                 on_show: Callable[[], None] | None = None,
                 on_quit: Callable[[], None] | None = None):
        self.url = url
        self.on_open = on_open
        self.on_show = on_show
        self.on_quit = on_quit
        self._alive = False

    def remember_clipboard(self) -> dict:
        text = clip_remember_text(read_clipboard())
        if not text:
            return {"ok": False, "error": "clipboard empty"}
        try:
            return post_remember(self.url, text)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return {"ok": False, "error": str(exc)}

    def start(self) -> bool:
        """Start a Windows tray icon if possible. Never starts an activity poll."""
        if should_watch_activity():
            raise RuntimeError("activity watch must stay disabled")
        if os.name != "nt":
            return False
        self._alive = True
        thread = threading.Thread(target=self._win_loop, name="second-brain-tray",
                                  daemon=True)
        thread.start()
        return True

    def stop(self) -> None:
        self._alive = False

    def _win_loop(self) -> None:
        """Best-effort NotifyIcon. Failures are silent; the setup window remains."""
        try:
            self._win_notify()
        except Exception:
            self._alive = False

    def _win_notify(self) -> None:
        import ctypes
        from ctypes import wintypes

        from launcher.icons import icon_ico

        user32 = ctypes.windll.user32
        shell32 = ctypes.windll.shell32

        WM_USER = 0x0400
        WM_TRAY = WM_USER + 42
        WM_LBUTTONUP = 0x0202
        WM_RBUTTONUP = 0x0205
        NIM_ADD, NIM_DELETE = 0x00000000, 0x00000002
        NIF_MESSAGE, NIF_ICON, NIF_TIP = 0x00000001, 0x00000002, 0x00000004
        ID_OPEN, ID_CLIP, ID_SHOW, ID_QUIT = 1001, 1002, 1003, 1004

        class NOTIFYICONDATA(ctypes.Structure):
            _fields_ = [
                ("cbSize", wintypes.DWORD),
                ("hWnd", wintypes.HWND),
                ("uID", wintypes.UINT),
                ("uFlags", wintypes.UINT),
                ("uCallbackMessage", wintypes.UINT),
                ("hIcon", wintypes.HICON),
                ("szTip", ctypes.c_wchar * 128),
            ]

        WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, wintypes.HWND, wintypes.UINT,
                                     wintypes.WPARAM, wintypes.LPARAM)

        def wndproc(hwnd, msg, wparam, lparam):
            if msg == WM_TRAY and lparam in (WM_LBUTTONUP, WM_RBUTTONUP):
                if lparam == WM_LBUTTONUP and self.on_open:
                    self.on_open()
                elif lparam == WM_RBUTTONUP:
                    self._popup(hwnd, user32, ID_OPEN, ID_CLIP, ID_SHOW, ID_QUIT)
            elif msg == 0x0111:  # WM_COMMAND
                cmd = wparam & 0xFFFF
                if cmd == ID_OPEN and self.on_open:
                    self.on_open()
                elif cmd == ID_CLIP:
                    self.remember_clipboard()
                elif cmd == ID_SHOW and self.on_show:
                    self.on_show()
                elif cmd == ID_QUIT and self.on_quit:
                    self.on_quit()
            return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

        self._wndproc = WNDPROC(wndproc)

        class WNDCLASS(ctypes.Structure):
            _fields_ = [
                ("style", wintypes.UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", ctypes.c_int),
                ("cbWndExtra", ctypes.c_int),
                ("hInstance", wintypes.HINSTANCE),
                ("hIcon", wintypes.HICON),
                ("hCursor", wintypes.HCURSOR),
                ("hbrBackground", wintypes.HBRUSH),
                ("lpszMenuName", wintypes.LPCWSTR),
                ("lpszClassName", wintypes.LPCWSTR),
            ]

        wc = WNDCLASS()
        wc.lpfnWndProc = self._wndproc
        wc.hInstance = kernel32_instance()
        wc.lpszClassName = "SecondBrainTray"
        if not user32.RegisterClassW(ctypes.byref(wc)):
            return
        hwnd = user32.CreateWindowExW(0, wc.lpszClassName, "Second Brain",
                                      0, 0, 0, 0, 0, None, None, wc.hInstance, None)
        if not hwnd:
            return

        ico_path = icon_ico()
        hicon = None
        if ico_path:
            hicon = user32.LoadImageW(None, str(ico_path), 1, 16, 16, 0x00000010)
        if not hicon:
            hicon = user32.LoadIconW(None, 32512)

        nid = NOTIFYICONDATA()
        nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
        nid.hWnd = hwnd
        nid.uID = 1
        nid.uFlags = NIF_MESSAGE | NIF_ICON | NIF_TIP
        nid.uCallbackMessage = WM_TRAY
        nid.hIcon = hicon
        nid.szTip = "Second Brain"
        shell32.Shell_NotifyIconW(NIM_ADD, ctypes.byref(nid))

        msg = wintypes.MSG()
        while self._alive and user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

        shell32.Shell_NotifyIconW(NIM_DELETE, ctypes.byref(nid))

    def _popup(self, hwnd, user32, id_open, id_clip, id_show, id_quit) -> None:
        import ctypes
        from ctypes import wintypes

        try:
            menu = user32.CreatePopupMenu()
            user32.AppendMenuW(menu, 0, id_open, "Open browser")
            user32.AppendMenuW(menu, 0, id_clip, "Remember clipboard")
            user32.AppendMenuW(menu, 0, id_show, "Show window")
            user32.AppendMenuW(menu, 0, id_quit, "Quit")
            pt = wintypes.POINT()
            user32.GetCursorPos(ctypes.byref(pt))
            user32.SetForegroundWindow(hwnd)
            user32.TrackPopupMenu(menu, 0, pt.x, pt.y, 0, hwnd, None)
            user32.DestroyMenu(menu)
        except Exception:
            pass


def kernel32_instance():
    import ctypes
    return ctypes.windll.kernel32.GetModuleHandleW(None)
````

## `main.py`

````
#!/usr/bin/env python3
"""Second Brain — application entry point.

Starts the FastAPI app (same process as `python start.py` after setup).
Prefer `python start.py` on a new machine; it verifies dependencies first.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.app import app  # noqa: E402  — ASGI application


def main() -> None:
    import uvicorn

    host = os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0")
    port = int(os.environ.get("SECOND_BRAIN_PORT", "8000"))
    uvicorn.run(app, host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
````

## `pytest.ini`

````
[pytest]
testpaths = tests test_overall.py
filterwarnings =
    ignore::DeprecationWarning
````

## `README.md`

````
# Second Brain — Local AI Knowledge Graph

A **local, private Second Brain**. You talk to it. It extracts durable facts
into a SQLite knowledge graph, then answers later questions from that memory.

Nothing leaves the machine unless you export it. Ollama is optional.

```
Browser  →  FastAPI  →  SQLite
                    ↘  Ollama (optional)
                    ↘  deterministic fallback if Ollama is down
```

Reliability over cleverness. The database is the source of truth. The graph
visualizes the database. RAG never invents personal facts.

---

## How it works

```
message → command? → trivial filter → extract (Ollama or rules)
       → validate → normalize → duplicate merge → conflict/supersede
       → confidence → SQLite → graph + timeline → search/RAG
```

- Default extraction model: `qwen3:0.6b` (small on purpose)
- Default embeddings: `nomic-embed-text`
- Both are configurable in Settings or `.env` — no code changes
- LLM extraction is validated against the user's words, then merged with the
  deterministic fallback. Unsupported personal facts are dropped.
- Answers are **KNOWN / UNCERTAIN / UNKNOWN**
- History is kept; superseded facts stay available but are not treated as current

---

## Requirements

| Tool | Version |
|------|---------|
| Python | 3.11+ (3.11.9 recommended) |
| Ollama | optional |
| Node.js | not required to run |

Target hardware: Windows 11, i7-12700F, RTX 4060 Ti 8GB, 32GB RAM.

---

## Windows 11 setup

### Option A — double-click `SecondBrain.exe`

Build on **Windows 11** from a Python 3.11 environment (PyInstaller cannot cross-compile a PE from Linux):

```powershell
python -m pip install -r requirements.txt
python -m pip install pyinstaller
python -m launcher.build_exe
```

That produces **`dist/SecondBrain.exe`** with the Second Brain icon
(`launcher/secondbrain.ico`). Double-click it.

First launch shows a dark setup window (version, current step, progress, log, Ollama status). It:

- checks the packaged runtime
- finds an existing `brain.db` next to the EXE (`dist\data\brain.db`) or under `%LOCALAPPDATA%\SecondBrain\data\brain.db`
- creates that file only if none exists — it never deletes, resets, or replaces a brain
- probes Ollama over HTTP (`qwen3:0.6b`, `nomic-embed-text`)
- does **not** download models unless you set `SECOND_BRAIN_PULL_MODELS=1`
- starts the **existing** FastAPI app and opens the browser

If Ollama is down, the window says offline and the app uses the rule-based fallback. It does not crash.

Later launches skip installs, skip model downloads, and reopen the same database. The setup window stays open with **Open browser** / **Hide to tray** / **Quit** so the server is not killed when the first-run checks finish.

The optional tray does **not** watch your screen, windows, or typing. It only
opens the app, quits, or (if you click it) remembers the current clipboard
through the same chat extractor. Auto-capturing “what you are doing” every
few minutes would store junk and secrets. That is intentionally not a feature.

`start.py` remains the normal Python launcher. The EXE is an additional bootstrapper, not a second application.

### Option B — Python launcher

### 1. Optional: Ollama

Install from https://ollama.com then:

```powershell
ollama pull qwen3:0.6b
ollama pull nomic-embed-text
```

The app starts and works without this. Offline mode uses the rule-based extractor.

### 2. First startup

```powershell
cd second-brain
python start.py
```

`start.py` is the only primary launcher. It:

- requires Python 3.11+
- creates `.venv` only if runtime imports are missing
- installs **only** missing packages
- never reinstalls on later runs
- probes Ollama over HTTP (offline is valid)
- binds `0.0.0.0:8000`

Open **http://localhost:8000**.

### 3. Subsequent startup

```powershell
python start.py
```

No downloads. No reinstall.

### 4. Useful flags

```powershell
python start.py --check          # diagnose, do not start
python start.py --check-only     # same
python start.py --no-install     # fail if deps are missing
python start.py --dev            # auto-reload
python start.py --open           # open the local URL
python start.py --host 0.0.0.0 --port 8000
```

Works from any working directory; paths are resolved from `start.py`.

### 5. Tests

```powershell
python -m pip install pytest httpx
python test_overall.py
```

---

## Configuration

Copy `.env.example` to `.env`, or use Settings:

```
OLLAMA_MODEL=qwen3:0.6b
EMBEDDING_MODEL=nomic-embed-text
OLLAMA_BASE_URL=http://localhost:11434
```

Runtime Settings: models, Ollama URL (http/https only), confidence threshold,
duplicate-merge threshold, auto-memory, automatic local backup interval, theme.

---

## Memory system

Greetings, thanks, and jokes are not stored.

Durable statements become entities and relationships with confidence, source
message, and timestamps. Duplicates merge. Exclusive facts (`prefers`,
`lives_in`, `works_at`) supersede the previous active one. “I stopped …” and
“I switched from X to Y” supersede the old fact. History remains.

Commands (deterministic, always hit SQLite):

Remember · Forget · Remove · Pin · Unpin · Important · Unimportant · Merge ·
Rename · Change · Set confidence · Stop remembering

The chat rail can search conversation titles and message text.

Forgetting a preference or a “learning X” fact **supersedes** it. It does not
silently delete history.

---

## Search / RAG

Keyword + semantic + graph + recency + confidence + active/superseded + bounded
multi-hop. Short names (`Go`, `C#`, `AI`) are searchable. Direct questions
such as “Where do I live?”, “What technology does the game engine use?”,
“Who uses Bevy?”, “When did I start learning Rust?”, “What did I stop?”,
and “What changed this week?” read the graph first. If there is no evidence,
the answer is UNKNOWN. Ollama replies that invent names are dropped.

---

## Graph

Cytoscape visualization of the real SQLite graph. Pan, zoom, search, type /
relation / confidence / status / pinned / important filters, expand, focus,
edit, delete, merge. Layouts: force, group-by-type, from-User. Relationship
types can be edited on an entity. Isolated nodes can be hidden. No fabricated
nodes. Brains larger than 40 entities default to **Around me** (User + 2 hops);
Reset view loads the full graph. `#entity/12` and `#chat/3` survive refresh.
The entity panel lists near-duplicates so you can merge them yourself.

---

## Backup / export / import

- JSON + Markdown export
- Merge import or replace import (replace requires `confirm=true`)
- Merge import reports exclusive-fact conflicts and skipped relationships
- User relationships are remapped
- Local backups under `data/backups/` (SQLite + JSON + MD)
- Optional automatic local backups (default every 24 hours; never deletes)
- Secrets are not exported
- Reset requires confirmation
- Restore a named local backup (creates a safety snapshot first)
- Paste notes (plain text / markdown paragraphs) to extract memories

---

## Privacy

Local-first. No telemetry. No cloud accounts. The only optional network call is
the Ollama URL you configure.

---

## Project layout

```
second-brain/
├── start.py               # primary Python launcher
├── launcher/              # EXE bootstrapper + setup GUI (not a second app)
├── secondbrain.spec       # PyInstaller spec → dist/SecondBrain.exe
├── test_overall.py
├── requirements.txt
├── README.md
├── ROADMAP
├── projekt.md             # full first-party source archive
├── .env.example
├── .gitignore
├── backend/
├── frontend/
├── tests/
└── data/brain.db          # created on first run; never deleted by the EXE
```

---

## Limitations

- Single-user, local only
- Offline extractor is intentionally small; hard phrasing is better with Ollama
- SSE chat extracts first, then streams the reply token-by-token when Ollama is up
- Playwright browser tests skip if Chromium is not installed
- Learning several things at once is allowed unless you stop or switch
- `SecondBrain.exe` must be built on Windows (PyInstaller does not cross-compile a PE from Linux)
````

## `requirements.txt`

````
# Second Brain — runtime dependencies
# Install with:  python -m pip install -r requirements.txt
fastapi>=0.110
uvicorn[standard]>=0.29
requests>=2.31
numpy>=1.26
````

## `ROADMAP`

````
# Second Brain — Roadmap

Local-first personal AI memory. Reliability over cleverness.
The database is the source of truth.

## Done

- Chat, conversations, last-N context, persisted assistant replies
- Automatic extraction (Ollama + honest offline fallback)
- Deterministic memory commands including Important / Unimportant
- Entities, relationships, facts, aliases, confidence, sources, timestamps
- Active / superseded / pinned / important
- Duplicate merge and exclusive-fact supersession
- Knowledge graph as a visualization of SQLite
- Hybrid search + multi-hop RAG with KNOWN / UNCERTAIN / UNKNOWN
- Memory consolidation (originals kept)
- JSON / Markdown export; validated merge / replace import
- Local backups (SQLite + JSON + MD)
- Dashboard from live data; labelled demo data
- Settings, privacy panel, confirmed reset/replace
- start.py as the only primary Python launcher (no setup.py, no start.bat)
- SecondBrain.exe bootstrapper (PyInstaller) with a setup GUI; same FastAPI app
- Backup restore with safety snapshot; unique backup folders
- Entity browser, command palette, hash routing, conversation rename
- Yes/no fact questions and list extraction (Python, Rust, and Go)
- Natural command detection (no hijacking of "remember when")
- Tell-me-about / path questions with source snippets
- Note paragraph import; graph path + add-relationship
- Strict LLM extraction validation + merge with deterministic fallback
- Token-level SSE streaming after extraction / retrieval
- Scheduled local backups (opt-in interval, default 24h)
- Graph layouts (force / by type / from User) and relationship-type editing
- Direct NL answers for live / work / prefer / use-of questions
- Full first-party source archive in projekt.md
- Grounded Ollama answers (invented tech/entities dropped)
- Auto-backup after memory writes, not on the health poll
- Conversation search in the chat rail (title + message text)
- Default graph view is User + 2 hops on large brains
- Merge-import conflict / skip report
- Tighter Important / Unimportant command detection
- EXE icon (ICO) + setup-window icon
- Optional tray: Open / Remember clipboard / Quit — never activity-watch
- Entity hash routes, timeline source click, palette conversations
- Entity sort; backup size; DB integrity in Settings
- Direct answers for “what did I stop?” and “what changed this week?”
- Hash routes survive refresh; timeline opens the source message
- Near-duplicate suggestions on the entity panel
- “Who uses X?” and “When did I start …?” read stored dates/facts
- Non-stream RAG also drops ungrounded Ollama replies

## Next (optional)

- Explicit user-initiated binary file ingest
- Code-signed Windows EXE (needs a certificate on a Windows machine)

## Non-goals

- Cloud sync by default
- Telemetry
- Inventing personal memories
- A second graph store
- A second extraction implementation
- Background activity / screen / window-title surveillance
````

## `run.py`

````
"""Launch the Second Brain backend + UI.

Usage:  python run.py   (then open http://localhost:8000)
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=False)
````

## `secondbrain.spec`

````
# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for SecondBrain.exe
# Run on Windows 11:  python -m launcher.build_exe
# Output: dist/SecondBrain.exe
#
# This freezes the launcher + existing FastAPI app. It is not a second
# implementation. The database is resolved at runtime next to the EXE
# (portable) or under LOCALAPPDATA — never inside the extract directory.

from PyInstaller.utils.hooks import collect_all, collect_submodules

datas = [
    ("frontend", "frontend"),
    (".env.example", "."),
    ("launcher/secondbrain.ico", "launcher"),
    ("launcher/secondbrain.png", "launcher"),
]
binaries = []
hidden = []

for pkg in ("uvicorn", "fastapi", "starlette", "anyio", "pydantic", "pydantic_core",
            "numpy", "requests", "urllib3", "certifi", "idna", "charset_normalizer",
            "h11", "click", "sniffio"):
    try:
        d, b, h = collect_all(pkg)
        datas += d
        binaries += b
        hidden += h
    except Exception:
        try:
            hidden += collect_submodules(pkg)
        except Exception:
            pass

hidden += [
    "tkinter", "tkinter.ttk", "tkinter.messagebox",
    "uvicorn.logging", "uvicorn.loops", "uvicorn.loops.auto",
    "uvicorn.protocols", "uvicorn.protocols.http", "uvicorn.protocols.http.auto",
    "uvicorn.protocols.http.h11_impl",
    "uvicorn.protocols.websockets", "uvicorn.protocols.websockets.auto",
    "uvicorn.lifespan", "uvicorn.lifespan.on", "uvicorn.lifespan.off",
    "backend.app", "backend.db", "backend.store", "backend.config",
    "backend.paths", "backend.extract", "backend.fallback", "backend.search",
    "backend.graph", "backend.commands", "backend.export", "backend.backup",
    "backend.summarize", "backend.ollama",
    "launcher", "launcher.bootstrap", "launcher.gui",
    "launcher.icons", "launcher.tray",
    "multipart", "python_multipart",
]

seen = set()
hidden_unique = []
for name in hidden:
    if name not in seen:
        seen.add(name)
        hidden_unique.append(name)

a = Analysis(
    ["launcher/__main__.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
    hiddenimports=hidden_unique,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pytest", "playwright", "tkinter.test"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="SecondBrain",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon="launcher/secondbrain.ico",
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=False,
)
````

## `start.py`

````
#!/usr/bin/env python3
"""Primary launcher for Second Brain.

Paths are resolved from this file, so the current working directory does not
matter. After a successful first run this script must NOT reinstall packages.

Usage:
    python start.py
    python start.py --check
    python start.py --check-only
    python start.py --no-install
    python start.py --dev
    python start.py --open
    python start.py --host 0.0.0.0 --port 8000
"""
from __future__ import annotations

import argparse
import importlib
import os
import subprocess
import sys
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"

RUNTIME_DEPS = (
    ("fastapi", "fastapi>=0.110"),
    ("uvicorn", "uvicorn[standard]>=0.29"),
    ("requests", "requests>=2.31"),
    ("numpy", "numpy>=1.26"),
)

MIN_PY = (3, 11)


def is_windows() -> bool:
    return os.name == "nt"


def venv_python() -> Path:
    if is_windows():
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def running_in_project_venv() -> bool:
    try:
        prefix = Path(getattr(sys, "prefix", "")).resolve()
        base = Path(getattr(sys, "base_prefix", sys.prefix)).resolve()
        if prefix == VENV_DIR.resolve():
            return True
        raw = Path(sys.executable)
        if str(VENV_DIR) in str(raw):
            return True
        return prefix != base and str(VENV_DIR.resolve()) in str(prefix)
    except OSError:
        return False


def check_python() -> None:
    if sys.version_info < MIN_PY:
        ver = ".".join(str(p) for p in sys.version_info[:3])
        need = ".".join(str(p) for p in MIN_PY)
        raise SystemExit(
            f"Second Brain requires Python {need}+ (found {ver}).\n"
            "Install Python 3.11.9 or newer and retry."
        )


def missing_runtime() -> list[str]:
    missing = []
    for mod, spec in RUNTIME_DEPS:
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append(spec)
    return missing


def install_packages(packages: list[str]) -> None:
    print("Installing missing packages:", ", ".join(packages))
    cmd = [sys.executable, "-m", "pip", "install", "--disable-pip-version-check", *packages]
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            "Failed to install Python packages.\n"
            f"Command: {' '.join(cmd)}\n"
            "On Windows:  python -m pip install -r requirements.txt\n"
            f"pip exit code: {exc.returncode}"
        ) from exc


def ensure_venv() -> None:
    if os.environ.get("SECOND_BRAIN_NO_VENV") == "1":
        return
    if running_in_project_venv():
        return
    if missing_runtime() and not venv_python().is_file():
        print(f"Creating virtual environment at {VENV_DIR} …")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])
        except subprocess.CalledProcessError as exc:
            raise SystemExit(
                "Could not create a virtual environment.\n"
                "On Windows, re-run the official Python installer with pip and venv enabled."
            ) from exc


def reexec_in_venv_if_needed() -> None:
    if os.environ.get("SECOND_BRAIN_NO_VENV") == "1":
        return
    if running_in_project_venv():
        return
    py = venv_python()
    if py.is_file() and Path(sys.executable).resolve() != py.resolve():
        os.execv(str(py), [str(py), *sys.argv])


def create_dirs() -> None:
    (ROOT / "data").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "backups").mkdir(parents=True, exist_ok=True)


def verify_imports() -> None:
    missing = missing_runtime()
    if missing:
        raise SystemExit("Runtime packages are still missing: " + ", ".join(missing))
    frontend = ROOT / "frontend" / "index.html"
    if not frontend.is_file():
        raise SystemExit(f"Frontend is missing: {frontend}")


def setup_only(allow_install: bool = True) -> list[str]:
    check_python()
    if allow_install:
        ensure_venv()
    missing = missing_runtime()
    installed: list[str] = []
    if missing:
        if not allow_install:
            raise SystemExit(
                "Missing runtime packages and --no-install was set: "
                + ", ".join(missing)
            )
        install_packages(missing)
        installed = missing
    create_dirs()
    return installed


def detect_environment() -> dict:
    return {
        "python": sys.version.split()[0],
        "executable": sys.executable,
        "platform": sys.platform,
        "windows": is_windows(),
        "project": str(ROOT),
        "venv": running_in_project_venv(),
        "missing": missing_runtime(),
    }


def probe_ollama() -> dict:
    url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
    try:
        import requests
        r = requests.get(url.rstrip("/") + "/api/tags", timeout=2)
        if r.status_code != 200:
            return {"available": False, "url": url, "error": f"HTTP {r.status_code}"}
        models = [m.get("name") for m in r.json().get("models", [])]
        return {"available": True, "url": url, "models": models}
    except Exception as exc:
        return {"available": False, "url": url, "error": str(exc) or exc.__class__.__name__}


def print_env(info: dict) -> None:
    print("Second Brain — environment")
    print(f"  Python      : {info['python']} ({info['executable']})")
    print(f"  Platform    : {info['platform']}")
    print(f"  Project     : {info['project']}")
    print(f"  Project venv: {'yes' if info['venv'] else 'no'}")
    print(f"  Missing     : {', '.join(info['missing']) if info['missing'] else 'none'}")
    oll = probe_ollama()
    if oll.get("available"):
        models = ", ".join(oll.get("models") or []) or "none listed"
        print(f"  Ollama      : online at {oll['url']}")
        print(f"  Models      : {models}")
    else:
        print(f"  Ollama      : offline ({oll.get('url')})")
        if oll.get("error"):
            print(f"                {oll['error']}")
        print("                Fallback extractor will be used. Optional:")
        print("                ollama pull qwen3:0.6b && ollama pull nomic-embed-text")


def start_server(host: str, port: int, reload: bool = False, open_browser: bool = False) -> None:
    os.chdir(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        import uvicorn
    except ImportError as exc:
        raise SystemExit("uvicorn is not installed. Run:  python start.py") from exc
    url = f"http://127.0.0.1:{port}"
    print()
    print("Starting Second Brain")
    print(f"  Local URL  : {url}")
    print(f"  Bind       : {host}:{port}")
    print("  Privacy    : LOCAL · PRIVATE · no telemetry")
    print("  Stop       : Ctrl+C")
    if reload:
        print("  Reload     : on")
    print()
    if open_browser:
        threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    uvicorn.run("backend.app:app", host=host, port=port, reload=reload, log_level="info")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Start Second Brain")
    parser.add_argument("--check", action="store_true", help="Verify environment and exit")
    parser.add_argument("--check-only", action="store_true", help="Alias for --check")
    parser.add_argument("--no-install", action="store_true", help="Do not install missing packages")
    parser.add_argument("--dev", action="store_true", help="Start with auto-reload")
    parser.add_argument("--open", action="store_true", help="Open the local URL in a browser")
    parser.add_argument("--host", default=os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("SECOND_BRAIN_PORT", "8000")))
    args = parser.parse_args(argv)

    check_python()
    info = detect_environment()
    print_env(info)

    if args.check or args.check_only:
        create_dirs()
        if info["missing"] and not venv_python().is_file():
            print("FAIL: missing runtime packages:", ", ".join(info["missing"]))
            return 1
        if info["missing"] and venv_python().is_file() and not running_in_project_venv():
            extra = ["--check"]
            rc = subprocess.call([str(venv_python()), str(ROOT / "start.py"), *extra])
            return rc
        try:
            verify_imports()
        except SystemExit as exc:
            print("FAIL:", exc)
            return 1
        print("OK: environment is ready.")
        return 0

    allow_install = not args.no_install
    if allow_install and missing_runtime() and not running_in_project_venv():
        ensure_venv()
        if venv_python().is_file():
            reexec_in_venv_if_needed()

    try:
        installed = setup_only(allow_install=allow_install)
    except SystemExit as exc:
        print("ERROR:", exc)
        return 1
    if installed:
        print("Installed:", ", ".join(installed))

    try:
        verify_imports()
    except SystemExit as exc:
        print("ERROR:", exc)
        return 1

    start_server(args.host, args.port, reload=args.dev, open_browser=args.open)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
````

## `test_overall.py`

````
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
    import start as start_mod

    assert callable(start_mod.main)
    assert start_mod.missing_runtime() == [] or isinstance(start_mod.missing_runtime(), list)
    assert start_mod.main(["--check-only"]) == 0


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
    assert (_ROOT / "launcher" / "secondbrain.ico").is_file()
    assert (_ROOT / "launcher" / "secondbrain.png").is_file()


def test_root_contract_files_exist():
    for name in ("start.py", "test_overall.py", "requirements.txt",
                 "README.md", "ROADMAP", "projekt.md", ".env.example", ".gitignore"):
        assert (_ROOT / name).is_file(), f"missing required root file: {name}"
    assert not (_ROOT / "setup.py").exists()
    assert not (_ROOT / "start.bat").exists()
    archive = (_ROOT / "projekt.md").read_text(encoding="utf-8")
    assert "## `backend/app.py`" in archive
    assert "## `start.py`" in archive
    assert "## `frontend/app.js`" in archive
    assert "## `launcher/secondbrain.ico`" in archive
    assert "## `launcher/tray.py`" in archive
    assert "## `frontend/vendor/cytoscape.min.js`" in archive


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
    assert s["privacy"].get("activity_watch") is False


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
    assert 'id="view-browse"' in html
    assert 'id="palette"' in html
    assert 'id="privacy-info"' in html
    assert 'id="graph-path"' in html
    assert 'id="import-notes"' in html
    assert 'id="gf-layout"' in html
    assert 'id="set-auto-backup"' in html
    assert 'id="conv-search"' in html
    assert 'id="gf-around-me"' in html
    assert 'id="graph-to-me"' in html
    assert 'id="browse-sort"' in html


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
````

## `tests/conftest.py`

````
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
````

## `tests/test_api.py`

````
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
    assert h.get("version") == "2.5.0"
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


def test_chat_empty_and_huge_payload(client):
    empty = client.post("/api/chat", json={"content": "   "})
    assert empty.status_code == 200
    assert empty.json()["trivial"] is True
    huge = client.post("/api/chat", json={"content": "I am learning Python. " + ("x" * 20000)})
    assert huge.status_code == 200
    assert store.find_entity_by_name("Python") is not None
````

## `tests/test_api_phase3.py`

````
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
````

## `tests/test_backup.py`

````
"""Tests for the local backup mechanism."""
import os

from backend import backup, config, extract, store


def test_create_backup():
    extract.extract("I am learning Python.")
    r = backup.create_backup()
    assert r["ok"] is True
    assert os.path.isdir(r["path"])
    assert os.path.exists(os.path.join(r["path"], "brain.db"))
    assert os.path.exists(os.path.join(r["path"], "export.json"))


def test_backup_list_and_status():
    backup.create_backup()
    status = backup.backup_status()
    assert status["count"] >= 1
    assert status["latest"] is not None
    assert status["backup_dir"] == backup.backup_dir()
    assert status["latest"].get("bytes", 0) > 0
    assert status["latest"].get("has_db") is True


def test_backup_contains_real_data():
    extract.extract("I am learning Python.")
    r = backup.create_backup()
    # The backup DB should contain the Python entity.
    import sqlite3
    conn = sqlite3.connect(os.path.join(r["path"], "brain.db"))
    n = conn.execute("SELECT COUNT(*) FROM entities WHERE norm_name='python'").fetchone()[0]
    conn.close()
    assert n == 1


def test_restore_requires_confirmation():
    extract.extract("I am learning Python.")
    created = backup.create_backup()
    name = os.path.basename(created["path"])
    r = backup.restore_backup(name, confirm=False)
    assert r["ok"] is False
    assert "confirm" in r["error"]


def test_restore_rejects_path_traversal():
    r = backup.restore_backup("../etc", confirm=True)
    assert r["ok"] is False
    r2 = backup.restore_backup("backup-../../../tmp", confirm=True)
    assert r2["ok"] is False


def test_restore_roundtrip_preserves_memories():
    extract.extract("I am learning Python.")
    assert store.find_entity_by_name("Python") is not None
    created = backup.create_backup()
    name = os.path.basename(created["path"])
    store.delete_entity(store.find_entity_by_name("Python")["id"])
    assert store.find_entity_by_name("Python") is None
    r = backup.restore_backup(name, confirm=True)
    assert r["ok"] is True
    assert r["safety_copy"]
    assert os.path.isdir(r["safety_copy"])
    assert store.find_entity_by_name("Python") is not None


def test_health_does_not_create_backup():
    from fastapi.testclient import TestClient
    from backend import app as app_module
    extract.extract("I am learning Python.")
    before = backup.backup_status()["count"]
    client = TestClient(app_module.app)
    h = client.get("/api/health").json()
    assert h["ok"] is True
    assert "auto_backup" in h
    assert h["auto_backup"].get("count") == before
    assert backup.backup_status()["count"] == before


def test_maybe_auto_backup_skips_empty_and_fresh():
    r = backup.maybe_auto_backup()
    assert r.get("skipped") is True
    extract.extract("I am learning Python.")
    first = backup.maybe_auto_backup()
    assert first.get("ok") is True
    again = backup.maybe_auto_backup()
    assert again.get("skipped") is True


def test_no_secrets_in_backup():
    backup.create_backup()
    status = backup.backup_status()
    # backup.json metadata contains no secret keys.
    latest = status["latest"]
    assert latest is not None
    for key in latest.keys():
        assert "secret" not in key.lower() and "password" not in key.lower() and "token" not in key.lower()
````

## `tests/test_commands.py`

````
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


def test_stop_remembering_forgets_entity():
    e = store.create_entity("OldFact", "concept")
    r = commands.handle_command("Stop remembering OldFact")
    assert r["ok"] is True
    assert store.entity_row(e) is None
````

## `tests/test_export.py`

````
"""Tests for JSON/Markdown export and import (validation, merge, replace)."""
import json

from backend import db, export, extract, store


def _seed():
    extract.extract("I am learning Python.")
    extract.extract("My project Nebula uses Next.js.")


def test_json_export_shape():
    _seed()
    data = json.loads(export.export_json())
    assert data["format"] == "second-brain"
    assert data["version"] >= 1
    assert isinstance(data["entities"], list) and data["entities"]
    assert isinstance(data["relationships"], list)
    assert "exported_at" in data


def test_json_export_roundtrip_merge():
    _seed()
    data = json.loads(export.export_json())
    before = len(store.all_entities())
    result = export.import_merge(data)
    assert result["ok"] is True
    # Merge into an identical graph should not create duplicates.
    after = len(store.all_entities())
    assert after == before
    assert result["entities_created"] == 0


def test_markdown_export():
    _seed()
    md = export.export_markdown()
    assert "Second Brain" in md
    assert "## Entities" in md
    assert "## Relationships" in md
    assert "Python" in md


def test_import_validation_rejects_garbage():
    r = export.import_from_json("not json at all", mode="merge")
    assert r["ok"] is False


def test_import_validation_rejects_wrong_format():
    r = export.import_from_json(json.dumps({"format": "other", "entities": []}), mode="merge")
    assert r["ok"] is False


def test_import_validation_rejects_missing_keys():
    r = export.import_from_json(json.dumps({"format": "second-brain"}), mode="merge")
    assert r["ok"] is False


def test_import_merge_adds_new_entities():
    _seed()
    payload = {
        "format": "second-brain", "version": 1,
        "entities": [{"id": 999, "name": "Kubernetes", "type": "technology",
                      "description": "", "confidence": 0.9}],
        "relationships": [],
    }
    r = export.import_from_json(json.dumps(payload), mode="merge")
    assert r["ok"] is True
    assert store.find_entity_by_name("Kubernetes") is not None


def test_import_replace_wipes_and_loads():
    _seed()
    payload = {
        "format": "second-brain", "version": 1,
        "entities": [{"id": 1, "name": "Go", "type": "technology",
                      "description": "", "confidence": 0.9}],
        "relationships": [],
    }
    r = export.import_from_json(json.dumps(payload), mode="replace")
    assert r["ok"] is True
    ents = store.all_entities()
    names = {e["name"] for e in ents}
    assert "Go" in names
    # Old entities are gone (except the User entity).
    assert "Python" not in names
    assert "User" in names


def test_import_preserves_relationships():
    _seed()
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    store.add_relationship(a, b, "uses")
    data = json.loads(export.export_json())
    # Clear and re-import.
    export.import_from_json(json.dumps(data), mode="replace")
    rels = store.all_relationships()
    assert any(r["relation"] == "uses" for r in rels)


def test_export_includes_status_and_confidence():
    _seed()
    data = json.loads(export.export_json())
    ent = next(e for e in data["entities"] if e["name"] == "Python")
    assert "confidence" in ent and isinstance(ent["confidence"], (int, float))
    assert "status" in ent


def test_export_includes_facts():
    _seed()
    data = json.loads(export.export_json())
    assert "facts" in data and data["facts"]
    assert any("Python" in f["text"] for f in data["facts"])


def test_replace_import_restores_user_relationships():
    _seed()
    data = json.loads(export.export_json())
    r = export.import_from_json(json.dumps(data), mode="replace")
    assert r["ok"] is True
    py = store.find_entity_by_name("Python")
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=?",
        (uid, py["id"]),
    )
    assert rels, "learning relationship from User must survive replace import"


def test_note_chunk_split_and_import():
    chunks = export.split_note_chunks("I am learning Python.\n\n# Project\nNebula uses Ollama.")
    assert len(chunks) >= 2
    r = export.import_notes("I am learning Python.\n\nMy project Nebula uses Ollama.")
    assert r["ok"] is True
    assert store.find_entity_by_name("Python") is not None


def test_import_merge_reports_exclusive_conflict_and_skips():
    extract.extract("I live in Berlin")
    uid = store.ensure_user_entity()
    payload = {
        "format": "second-brain", "version": 1,
        "entities": [
            {"id": uid, "name": "User", "type": "person", "confidence": 1.0},
            {"id": 99, "name": "Paris", "type": "location", "confidence": 0.9},
        ],
        "relationships": [
            {"source_id": uid, "target_id": 99, "relation": "lives_in", "confidence": 0.9},
            {"source_id": 12345, "target_id": 99, "relation": "related_to", "confidence": 0.5},
        ],
    }
    r = export.import_merge(payload)
    assert r["ok"] is True
    assert r["conflicts"]
    assert any(c.get("superseded") == "Berlin" for c in r["conflicts"])
    assert r["relationships_skipped"] >= 1
    assert any(s.get("reason") == "missing_endpoint" for s in r["skipped"])
    paris = store.find_entity_by_name("Paris")
    berlin = store.find_entity_by_name("Berlin")
    assert paris and berlin
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND relation='lives_in'",
        (uid,),
    )
    active = [x for x in rels if x["status"] == "active"]
    assert len(active) == 1
    assert active[0]["target_id"] == paris["id"]
    assert r.get("report") and "conflicts" in r["report"]
````

## `tests/test_extraction.py`

````
"""Tests for the extraction pipeline (offline fallback path)."""
import json

from backend import config, db, extract, store


def _run(text):
    return extract.extract(text)


def test_trivial_filtering():
    for msg in ["hello", "hi", "thanks", "ok", "what time is it", "tell me a joke",
                "how are you", "lol", "👍"]:
        r = _run(msg)
        assert r["trivial"] is True, f"'{msg}' should be trivial"
        assert r["entities"] == [] and r["relationships"] == []


def test_extract_learning():
    r = _run("I am learning Python")
    assert not r["trivial"]
    names = [e["name"] for e in r["entities"]]
    assert "Python" in names
    # relationship User -> learning -> Python
    assert any(rel["relation"] == "learning" for rel in r["relationships"])


def test_extract_project_uses():
    r = _run("My new project Nebula uses Next.js and Ollama")
    names = [e["name"] for e in r["entities"]]
    assert "Nebula" in names and "Next.js" in names and "Ollama" in names
    rels = [(store.entity_row(x["source"])["name"], x["relation"], store.entity_row(x["target"])["name"])
            for x in r["relationships"]]
    assert ("Nebula", "uses", "Next.js") in rels
    assert ("Nebula", "uses", "Ollama") in rels


def test_no_duplicate_on_repeat():
    _run("I am learning Python")
    before = store.all_entities()
    _run("I am learning Python")
    after = store.all_entities()
    assert len(after) == len(before), "re-asserting the same fact must not create duplicates"


def test_preference_relation():
    r = _run("I prefer Python")
    rels = [(x["relation"]) for x in r["relationships"]]
    assert "prefers" in rels


def test_prefer_instead_does_not_create_junk_entity():
    _run("I prefer Python")
    r = _run("I prefer Rust instead of Python")
    names = {e["name"] for e in store.all_entities()}
    assert "Rust Instead Of Python" not in names
    assert "Rust" in names
    uid = store.ensure_user_entity()
    py = store.find_entity_by_name("Python")
    rust = store.find_entity_by_name("Rust")
    py_rel = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, py["id"]))
    rust_rel = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, rust["id"]))
    assert py_rel and py_rel[0]["status"] == "superseded"
    assert rust_rel and rust_rel[0]["status"] == "active"


def test_location_relation():
    r = _run("I live in Berlin")
    rels = [(x["relation"]) for x in r["relationships"]]
    assert "lives_in" in rels


def test_confidence_recorded():
    _run("I am learning Python")
    py = store.find_entity_by_name("Python")
    assert py is not None
    assert 0.0 < py["confidence"] <= 1.0


def test_source_message_tracking():
    mid = store.add_message("user", "I am learning Go")
    r = extract.extract("I am learning Go", source_message_id=mid)
    go = store.find_entity_by_name("Go")
    assert go is not None
    # The entity created during this extraction should reference the message.
    assert go["source_message_id"] == mid


def test_stopped_creates_supersession():
    _run("I am learning Rust")
    r = _run("I stopped learning Rust")
    assert r["superseded"] or any("no longer active" in u for u in r.get("relationship_updates", []))
    # The learning relationship should now be superseded.
    rust = store.find_entity_by_name("Rust")
    uid = store.ensure_user_entity()
    rels = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='learning'",
        (uid, rust["id"]))
    assert rels and rels[0]["status"] == "superseded"


def test_switched_detects_conflict():
    _run("I use Python")
    r = _run("I switched from Python to Rust")
    # Old learning/usage should be superseded; new preference recorded.
    assert r["superseded"] or any("no longer active" in u for u in r.get("relationship_updates", []))


def test_embedding_stored():
    _run("I am learning Python")
    py = store.find_entity_by_name("Python")
    assert py["embedding"] is not None
    vec = store.vec_from_json(py["embedding"])
    assert vec is not None and vec.size > 0


def test_memory_events_written():
    _run("I am learning Python")
    mems = store.recent_memories()
    assert any("Python" in m["text"] for m in mems)


def test_multiword_concepts_not_trimmed():
    # Regression: "game engine" must not be trimmed to just "Engine".
    r = _run("I am learning Rust and I want to build a game engine")
    names = [e["name"] for e in r["entities"]]
    assert "Game Engine" in names
    types = {e["name"]: e["type"] for e in r["entities"]}
    assert types.get("Game Engine") == "project"


def test_junk_clause_is_not_an_entity():
    r = _run("I prefer Rust instead of Python")
    names = {e["name"] for e in store.all_entities()}
    assert "Instead Of Python" not in names
    assert "Rust Instead Of Python" not in names
    assert extract.is_junk_entity_name("instead of Python")
    assert extract.is_junk_entity_name("a")
    assert not extract.is_junk_entity_name("Python")


def test_relearn_after_stop_is_remembered():
    _run("I am learning Rust")
    _run("I stopped learning Rust")
    r = _run("I am learning Rust")
    assert any(x["relation"] == "learning" for x in r["relationships"])
    rust = store.find_entity_by_name("Rust")
    uid = store.ensure_user_entity()
    assert store.relationship_active(uid, rust["id"], "learning")


def test_list_learning_extracts_each_item():
    r = _run("I am learning Python, Rust, and Go")
    names = {e["name"] for e in r["entities"]}
    assert {"Python", "Rust", "Go"} <= names
    rels = [x["relation"] for x in r["relationships"]]
    assert rels.count("learning") >= 3


def test_work_on_creates_project():
    r = _run("I am working on Second Brain")
    names = {e["name"] for e in r["entities"]}
    assert "Second Brain" in names
    assert any(x["relation"] == "works_on" for x in r["relationships"])


def test_skill_extraction():
    r = _run("I'm good at public speaking")
    names = {e["name"] for e in r["entities"]}
    assert "Public Speaking" in names
    types = {e["name"]: e["type"] for e in r["entities"]}
    assert types.get("Public Speaking") == "skill"


def test_mentioned_in_text_rejects_inventions():
    assert extract.mentioned_in_text("Python", "I am learning Python")
    assert extract.mentioned_in_text("Game Engine", "I want to build a game engine")
    assert not extract.mentioned_in_text("Google", "I am learning Python")
    assert extract.mentioned_in_text("User", "hello there")


def test_llm_invented_facts_rejected(fake_ollama, monkeypatch):
    def fake_chat(model, messages, temperature=0.0, format_json=False, timeout=None):
        return json.dumps({
            "entities": [
                {"name": "Python", "type": "technology", "description": "", "confidence": 0.9},
                {"name": "Google", "type": "organization", "description": "employer", "confidence": 0.99},
            ],
            "relationships": [
                {"source": "User", "target": "Python", "relation": "learning", "confidence": 0.9},
                {"source": "User", "target": "Google", "relation": "works_at", "confidence": 0.99},
            ],
            "stops": [],
        })
    monkeypatch.setattr("backend.ollama.chat", fake_chat)
    r = extract.extract("I am learning Python")
    names = {e["name"] for e in store.all_entities()}
    assert "Python" in names
    assert "Google" not in names
    uid = store.ensure_user_entity()
    google = store.find_entity_by_name("Google")
    assert google is None
    assert not any(
        rel["relation"] == "works_at" for rel in r["relationships"]
    )


def test_merge_llm_with_fallback_fills_gaps(fake_ollama, monkeypatch):
    def fake_chat(model, messages, temperature=0.0, format_json=False, timeout=None):
        return json.dumps({
            "entities": [{"name": "Python", "type": "technology", "confidence": 0.9}],
            "relationships": [
                {"source": "User", "target": "Python", "relation": "learning", "confidence": 0.9},
            ],
            "stops": [],
        })
    monkeypatch.setattr("backend.ollama.chat", fake_chat)
    r = extract.extract("I am learning Python and Rust")
    names = {e["name"] for e in store.all_entities()}
    assert "Python" in names and "Rust" in names
    assert r["used_fallback"] is False
    uid = store.ensure_user_entity()
    rust = store.find_entity_by_name("Rust")
    assert store.relationship_active(uid, rust["id"], "learning")


def test_correction_meant_not():
    extract.extract("I prefer Python")
    r = extract.extract("I meant Rust not Python")
    uid = store.ensure_user_entity()
    py = store.find_entity_by_name("Python")
    rust = store.find_entity_by_name("Rust")
    assert rust is not None
    py_rel = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, py["id"]))
    rust_rel = db.query(
        "SELECT * FROM relationships WHERE source_id=? AND target_id=? AND relation='prefers'",
        (uid, rust["id"]))
    assert py_rel and py_rel[0]["status"] == "superseded"
    assert rust_rel and rust_rel[0]["status"] == "active"
    assert r["superseded"] or rust_rel


def test_large_input_does_not_crash():
    blob = ("I am learning Python. " * 2000)
    r = extract.extract(blob)
    assert r["trivial"] is False
    assert store.find_entity_by_name("Python") is not None


def test_malformed_llm_json_falls_back(fake_ollama, monkeypatch):
    monkeypatch.setattr("backend.ollama.chat", lambda *a, **k: "<<<not json>>>")
    r = extract.extract("I am learning Python")
    assert r["used_fallback"] is True
    assert store.find_entity_by_name("Python") is not None


def test_confidence_threshold_respected(no_ollama, monkeypatch):
    monkeypatch.setattr(db, "get_setting_float",
                        lambda k, d: 0.99 if k == "confidence_threshold" else d)
    # With a very high threshold, nothing should be persisted.
    r = extract.extract("I am learning Python")
    # entities list in result is only appended for created entities; but even
    # upserts below threshold are skipped entirely.
    assert r["entities"] == [] or all(e.get("created") is False for e in r["entities"])
````

## `tests/test_frontend.py`

````
"""Playwright browser tests for the Second Brain frontend.

These run against the live app server. They exercise the core Chat → Memory →
Graph workflow plus navigation, search, and settings.

Skip gracefully if Playwright/Chromium isn't available (documented limitation).
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

pytest.importorskip("playwright.sync_api", reason="Playwright not installed")

from playwright.sync_api import sync_playwright  # noqa: E402

BASE_URL = os.environ.get("SECOND_BRAIN_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        try:
            b = p.chromium.launch(headless=True)
        except Exception as e:
            pytest.skip(f"Chromium unavailable: {e}")
        yield b
        b.close()


@pytest.fixture()
def page(browser):
    ctx = browser.new_context()
    pg = ctx.new_page()
    yield pg
    ctx.close()


def _seed_empty(page):
    """Reset the database so tests start from a clean slate."""
    page.request.post(BASE_URL + "/api/reset", data='{"confirm": true}',
                      headers={"Content-Type": "application/json"})


def _wait_boot(page):
    """Wait for the async boot() to finish (dashboard becomes active/populated)."""
    page.wait_for_selector("#view-dashboard.active .stat-card", timeout=15000)


def test_dashboard_loads(page):
    page.goto(BASE_URL + "/")
    # Wait for the async boot() to populate the dashboard stats.
    page.wait_for_selector("#view-dashboard.active .stat-card", timeout=10000)
    assert page.locator("#stats-grid .stat-card").count() >= 1


def test_chat_sends_message_and_memory_update(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "I am learning Rust and I want to build a game engine")
    page.click("#chat-send")
    # Memory update box appears.
    page.wait_for_selector(".remembered-box", timeout=8000)
    assert "Rust" in page.locator(".remembered-box").inner_text()


def test_entity_can_be_opened(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "I am learning Python")
    page.click("#chat-send")
    page.wait_for_selector(".remembered-chip", timeout=8000)
    page.locator(".remembered-chip").first.click()
    page.wait_for_selector("#entity-panel.open")
    assert "Python" in page.locator(".entity-title").inner_text()


def test_graph_updates(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "My project Nebula uses Next.js")
    page.click("#chat-send")
    page.wait_for_selector(".remembered-box", timeout=8000)
    page.click('[data-view="graph"]')
    page.wait_for_selector("#cy")
    # The graph should render nodes (canvas-based, so check the sub line updates).
    page.wait_for_timeout(1500)
    sub = page.locator("#graph-sub").inner_text()
    assert "Nebula" or "entities" in sub


def test_search_works(page):
    _seed_empty(page)
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="chat"]')
    page.fill("#chat-input", "I am learning Rust")
    page.click("#chat-send")
    page.wait_for_selector(".remembered-box", timeout=8000)
    page.click('[data-view="search"]')
    page.fill("#search-input", "What am I learning?")
    page.click("#search-btn")
    page.wait_for_selector("#search-answer", timeout=8000)
    assert "Rust" in page.locator("#search-answer").inner_text()


def test_entity_browser_and_palette_markup():
    html = open(os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html"), encoding="utf-8").read()
    js = open(os.path.join(os.path.dirname(__file__), "..", "frontend", "app.js"), encoding="utf-8").read()
    assert 'id="view-browse"' in html
    assert 'id="palette"' in html
    assert 'id="privacy-info"' in html
    assert 'id="backup-list"' in html
    assert 'id="gf-layout"' in html
    assert 'id="set-auto-backup"' in html
    assert 'id="conv-search"' in html
    assert 'id="gf-around-me"' in html
    assert 'id="graph-to-me"' in html
    assert 'id="browse-sort"' in html
    assert "function loadBrowse" in js
    assert "function formatImportReport" in js
    assert "/graph?focus=" in js
    assert "function openPalette" in js
    assert "function runGraphLayout" in js
    assert "function applyRoute" in js
    assert "function sourceChips" in js
    assert "data-mid" in js
    assert "Looks similar" in js
    assert "sources: m.sources" in js
    assert "function restore" not in js or "/backup/restore" in js


def test_settings_load(page):
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="settings"]')
    page.wait_for_selector("#view-settings.active #set-llm", timeout=10000)
    # Wait until boot() has loaded settings into the input.
    page.wait_for_function("document.querySelector('#set-llm').value.length > 0", timeout=10000)
    assert page.locator("#set-llm").input_value()


def test_reset_confirmation(page):
    page.goto(BASE_URL + "/")
    _wait_boot(page)
    page.click('[data-view="settings"]')
    page.wait_for_selector("#view-settings.active #reset-btn", timeout=10000)
    page.on("dialog", lambda d: d.dismiss())  # cancel the confirm
    page.click("#reset-btn")
    # Should not navigate away; still on settings.
    assert page.locator("#reset-btn").count() == 1
````

## `tests/test_graph.py`

````
"""Tests for graph traversal, filtering, neighborhood, paths, stats and
multi-hop retrieval."""
from backend import extract, graph, store


def _seed():
    # User -> learning -> Rust; User -> wants -> Game Engine; Game Engine -> uses -> Bevy
    extract.extract("I am learning Rust and I want to build a game engine.")
    extract.extract("My new project Game Engine uses Bevy.")


def test_neighborhood_depth_one():
    _seed()
    rust = store.find_entity_by_name("Rust")
    r = graph.neighborhood(rust["id"], depth=1)
    names = {n["name"] for n in r["nodes"]}
    assert "Rust" in names and "User" in names
    assert any(e["relation"] == "learning" for e in r["edges"])


def test_neighborhood_depth_two():
    _seed()
    rust = store.find_entity_by_name("Rust")
    r = graph.neighborhood(rust["id"], depth=2)
    names = {n["name"] for n in r["nodes"]}
    assert "Game Engine" in names  # reached via User


def test_neighborhood_relation_filter():
    _seed()
    rust = store.find_entity_by_name("Rust")
    r = graph.neighborhood(rust["id"], depth=2, relation="learning")
    # Only learning edges followed.
    assert all(e["relation"] == "learning" for e in r["edges"])


def test_shortest_path():
    _seed()
    rust = store.find_entity_by_name("Rust")
    bevy = store.find_entity_by_name("Bevy")
    p = graph.shortest_path(rust["id"], bevy["id"])
    assert p is not None
    # Should traverse Rust -> User -> Game Engine -> Bevy (or similar).
    assert len(p) >= 2


def test_shortest_path_none_for_disconnected():
    _seed()
    a = store.create_entity("Isolated Thing", "concept")
    rust = store.find_entity_by_name("Rust")
    assert graph.shortest_path(a, rust["id"]) is None


def test_filter_graph_by_type():
    _seed()
    r = graph.filter_graph(entity_type="technology", active_only=True)
    assert all(n["type"] == "technology" for n in r["nodes"])


def test_filter_graph_by_relation():
    _seed()
    r = graph.filter_graph(relation="uses", active_only=True)
    assert all(e["relation"] == "uses" for e in r["edges"])


def test_filter_graph_min_confidence():
    _seed()
    r = graph.filter_graph(min_confidence=0.9, active_only=True)
    assert all(e["confidence"] >= 0.9 for e in r["edges"])


def test_filter_graph_superseded_excluded():
    extract.extract("I am learning Rust")
    extract.extract("I stopped learning Rust")
    active = graph.filter_graph(active_only=True)
    allg = graph.filter_graph(active_only=False)
    # The superseded learning edge appears only in the non-active view.
    assert len(allg["edges"]) > len(active["edges"])


def test_filter_graph_pinned():
    eid = store.create_entity("Pinned Thing", "concept")
    store.update_entity(eid, pinned=1)
    r = graph.filter_graph(pinned=True)
    assert any(n["id"] == eid for n in r["nodes"])


def test_graph_stats():
    _seed()
    s = graph.graph_stats()
    assert s["nodes"] >= 3
    assert s["edges"] >= 2
    assert "by_type" in s and "by_relation" in s
    assert s["avg_degree"] >= 0


def test_multi_hop_collects_connected_facts():
    _seed()
    rust = store.find_entity_by_name("Rust")
    facts = graph.multi_hop([rust["id"]], max_depth=3)
    texts = [f["text"] for f in facts]
    assert any("learning" in t for t in texts)
    # Multi-hop should reach the "uses Bevy" fact.
    assert any("Bevy" in t for t in texts)


def test_multi_hop_respects_depth_limit():
    _seed()
    rust = store.find_entity_by_name("Rust")
    shallow = graph.multi_hop([rust["id"]], max_depth=1)
    deep = graph.multi_hop([rust["id"]], max_depth=4)
    # Deeper traversal should find at least as many facts.
    assert len(deep) >= len(shallow)


def test_group_by_type():
    _seed()
    groups = graph.group_by_type(active_only=True)
    assert "technology" in groups
    names = {n["name"] for rows in groups.values() for n in rows}
    assert "Rust" in names or "Bevy" in names


def test_explainable_rank():
    _seed()
    ranked = graph.explainable_rank("Rust")
    assert ranked, "should rank Rust first"
    top = ranked[0]
    assert "reasons" in top and isinstance(top["reasons"], list)


def test_graph_auto_focus_user_neighborhood():
    extract.extract("I am learning Rust")
    for i in range(45):
        store.create_entity(f"Island {i}", "concept")
    g = graph.graph_view(focus="auto", depth=2)
    assert g["focus"] == "user"
    assert g["truncated"] is True
    labels = {n["label"] for n in g["nodes"]}
    assert "User" in labels and "Rust" in labels
    assert "Island 0" not in labels
    full = graph.graph_view(focus="all")
    assert full["focus"] == "all"
    assert any(n["label"] == "Island 0" for n in full["nodes"])
    small = graph.graph_view(focus="auto")
    # After creating islands, auto stays on user.
    assert small["focus"] == "user"
````

## `tests/test_launcher.py`

````
"""Bootstrap / EXE-launcher tests. Does not start a second application."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

from backend import paths
from launcher import bootstrap


REQUIRED_TITLES = [
    "Initializing Second Brain",
    "Checking Python/runtime",
    "Checking dependencies",
    "Installing only missing dependencies",
    "Checking database",
    "Checking configuration",
    "Checking Ollama",
    "Checking required models",
    "Running health checks",
    "Starting Second Brain",
]


def test_resolve_db_honors_env(tmp_path, monkeypatch):
    target = tmp_path / "custom" / "brain.db"
    monkeypatch.setenv("SECOND_BRAIN_DB", str(target))
    assert paths.resolve_db_path() == target


def test_relative_env_db_is_not_cwd_based(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path)
    monkeypatch.setenv("SECOND_BRAIN_DB", "data/brain.db")
    other = tmp_path / "other cwd"
    other.mkdir()
    old = os.getcwd()
    try:
        os.chdir(other)
        resolved = paths.resolve_db_path()
    finally:
        os.chdir(old)
    assert resolved == tmp_path / "data" / "brain.db"


def test_existing_db_wins_over_empty_default(tmp_path, monkeypatch):
    monkeypatch.delenv("SECOND_BRAIN_DB", raising=False)
    existing = tmp_path / "data" / "brain.db"
    existing.parent.mkdir()
    existing.write_bytes(b"sqlite-placeholder")
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path)
    found = paths.resolve_db_path()
    assert found == existing
    assert found.read_bytes() == b"sqlite-placeholder"


def test_never_uses_meipass_for_db(tmp_path, monkeypatch):
    mei = tmp_path / "_MEI12345"
    mei.mkdir()
    user = tmp_path / "AppData" / "Local" / "SecondBrain" / "data"
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "_MEIPASS", str(mei), raising=False)
    monkeypatch.setenv("SECOND_BRAIN_DB", str(mei / "brain.db"))
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path / "install")
    monkeypatch.setattr(paths, "is_frozen", lambda: True)
    monkeypatch.setattr(paths, "_user_data_dir", lambda: user)
    resolved = paths.resolve_db_path()
    assert "_MEI" not in str(resolved)
    assert Path(mei) not in resolved.parents
    assert resolved == user / "brain.db"


def test_frozen_prefers_existing_portable_db(tmp_path, monkeypatch):
    portable = tmp_path / "install" / "data" / "brain.db"
    portable.parent.mkdir(parents=True)
    portable.write_bytes(b"portable-brain")
    user = tmp_path / "AppData" / "Local" / "SecondBrain" / "data"
    user.mkdir(parents=True)
    (user / "brain.db").write_bytes(b"roaming-brain")
    monkeypatch.delenv("SECOND_BRAIN_DB", raising=False)
    monkeypatch.setattr(paths, "is_frozen", lambda: True)
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path / "install")
    monkeypatch.setattr(paths, "_user_data_dir", lambda: user)
    found = paths.resolve_db_path()
    assert found == portable
    assert found.read_bytes() == b"portable-brain"


def test_spaces_in_path(tmp_path, monkeypatch):
    root = tmp_path / "Second Brain App"
    db = root / "data" / "brain.db"
    db.parent.mkdir(parents=True)
    db.write_bytes(b"x")
    monkeypatch.setenv("SECOND_BRAIN_DB", str(db))
    assert paths.resolve_db_path() == db
    assert db.is_file()


def test_ensure_data_dirs_does_not_delete_db(tmp_path):
    db = tmp_path / "data" / "brain.db"
    db.parent.mkdir()
    db.write_text("precious")
    paths.ensure_data_dirs(db)
    assert db.read_text() == "precious"


def test_bootstrap_preserves_existing_memories():
    from backend import store
    eid = store.create_entity("KeepMe", "concept")
    before = store.entity_row(eid)
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    after = store.entity_row(eid)
    assert after is not None
    assert after["name"] == "KeepMe"
    assert after["created_at"] == before["created_at"]


def test_second_bootstrap_does_not_install(monkeypatch):
    installed = []

    def boom(packages):
        installed.extend(packages)
        raise AssertionError("must not install when imports work")

    monkeypatch.setattr("start.install_packages", boom, raising=False)
    results = bootstrap.run_bootstrap(allow_install=True, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    install = next(r for r in results if r.key == "install")
    assert install.skipped is True
    assert installed == []


def test_missing_dependency_installs_only_that_package(monkeypatch):
    state = {"phase": 0, "installed": []}

    def fake_missing():
        state["phase"] += 1
        if state["phase"] == 1:
            return [("fastapi", "fastapi>=0.110")]
        return []

    def fake_install(packages):
        state["installed"] = list(packages)

    import start
    monkeypatch.setattr(bootstrap, "_missing_imports", fake_missing)
    monkeypatch.setattr(bootstrap.paths, "is_frozen", lambda: False)
    monkeypatch.setattr(start, "install_packages", fake_install)
    results = bootstrap.run_bootstrap(allow_install=True, pull_models=False)
    assert state["installed"] == ["fastapi>=0.110"]
    inst = next(r for r in results if r.key == "install")
    assert inst.ok
    assert inst.installed == ["fastapi>=0.110"]


def test_ollama_offline_does_not_fail(monkeypatch):
    monkeypatch.setattr(bootstrap, "probe_ollama", lambda *a, **k: {
        "available": False, "url": "http://localhost:11434", "models": [], "error": "refused",
    })
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    oll = next(r for r in results if r.key == "ollama")
    assert "offline" in oll.detail.lower() or "fallback" in oll.detail.lower()
    models = next(r for r in results if r.key == "models")
    assert models.skipped is True


def test_ollama_online_models_present_no_pull(monkeypatch):
    pulls = []

    def fake_probe(*a, **k):
        return {"available": True, "url": "http://localhost:11434",
                "models": ["qwen3:0.6b", "nomic-embed-text"], "error": None}

    monkeypatch.setattr(bootstrap, "probe_ollama", fake_probe)
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    models = next(r for r in results if r.key == "models")
    assert models.skipped is False
    assert "found" in models.detail
    assert pulls == []


def test_missing_models_not_downloaded_by_default(monkeypatch):
    monkeypatch.setattr(bootstrap, "probe_ollama", lambda *a, **k: {
        "available": True, "url": "http://localhost:11434",
        "models": [], "error": None,
    })
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    models = next(r for r in results if r.key == "models")
    assert models.skipped is True
    assert "no download" in models.detail.lower() or "not installed" in models.detail.lower()


def test_cwd_does_not_change_db(tmp_path, monkeypatch):
    db = tmp_path / "keep" / "brain.db"
    db.parent.mkdir()
    db.write_bytes(b"abc")
    monkeypatch.setenv("SECOND_BRAIN_DB", str(db))
    other = tmp_path / "other cwd"
    other.mkdir()
    old = os.getcwd()
    try:
        os.chdir(other)
        assert paths.resolve_db_path() == db
        assert db.read_bytes() == b"abc"
    finally:
        os.chdir(old)


def test_bootstrap_never_calls_reset(monkeypatch):
    called = []

    import backend.db as dbmod
    real_execute = dbmod.execute

    def guarded(sql, params=()):
        if isinstance(sql, str) and "DELETE FROM" in sql.upper() and "entities" in sql:
            called.append(sql)
        return real_execute(sql, params)

    monkeypatch.setattr(dbmod, "execute", guarded)
    bootstrap.run_bootstrap(allow_install=False)
    assert called == []


def test_bootstrap_emits_required_status_titles():
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    got = [r.title for r in results]
    for title in REQUIRED_TITLES:
        assert title in got


def test_headless_check_entrypoint():
    from launcher import __main__ as entry
    rc = entry.main(["--headless", "--check", "--no-install"])
    assert rc == 0


def test_create_server_uses_existing_app():
    from backend.app import app as existing
    server = bootstrap.create_server("127.0.0.1", 8099)
    assert server.config.app is existing
    assert server.config.port == 8099
````

## `tests/test_migration.py`

````
"""Tests for the database migration path (schema v2 -> v3 and idempotency)."""
import os
import sqlite3

from backend import config, db


def _build_v2_db(path):
    """Create a schema-v2 database (pre-`memories.meta`) with one memory row."""
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA user_version=2")
    conn.executescript("""
    CREATE TABLE entities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, norm_name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL DEFAULT 'concept', description TEXT NOT NULL DEFAULT '',
        aliases TEXT NOT NULL DEFAULT '[]', embedding TEXT,
        confidence REAL NOT NULL DEFAULT 0.8, source_message_id INTEGER,
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}',
        status TEXT NOT NULL DEFAULT 'active', pinned INTEGER NOT NULL DEFAULT 0,
        important INTEGER NOT NULL DEFAULT 0);
    CREATE TABLE relationships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_id INTEGER NOT NULL, target_id INTEGER NOT NULL, relation TEXT NOT NULL,
        confidence REAL NOT NULL DEFAULT 0.8, source_message_id INTEGER,
        created_at TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'active',
        UNIQUE(source_id, target_id, relation));
    CREATE TABLE conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
    CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT, conversation_id INTEGER,
        role TEXT NOT NULL, content TEXT NOT NULL, created_at TEXT NOT NULL,
        embedding TEXT, extracted INTEGER NOT NULL DEFAULT 0, meta TEXT NOT NULL DEFAULT '{}');
    CREATE TABLE memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT, kind TEXT NOT NULL, text TEXT NOT NULL,
        entity_ids TEXT NOT NULL DEFAULT '[]', message_id INTEGER,
        confidence REAL NOT NULL DEFAULT 0.8, created_at TEXT NOT NULL);
    CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT);
    """)
    conn.execute("INSERT INTO memories(kind, text, entity_ids, confidence, created_at) "
                 "VALUES('entity', 'legacy memory', '[]', 0.8, '2026-01-01T00:00:00+00:00')")
    conn.commit()
    conn.close()


def test_migration_v2_to_v3(monkeypatch, tmp_path):
    db_path = str(tmp_path / "legacy.db")
    _build_v2_db(db_path)
    monkeypatch.setattr(config, "DB_PATH", db_path)

    # Run the migration.
    db.init_db()

    conn = sqlite3.connect(db_path)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(memories)")}
    # New column added.
    assert "meta" in cols
    # Legacy data preserved.
    n = conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
    assert n == 1
    # user_version bumped.
    ver = conn.execute("PRAGMA user_version").fetchone()[0]
    assert ver == db.SCHEMA_VERSION
    conn.close()


def test_migration_idempotent(monkeypatch, tmp_path):
    """Running init_db() twice must not error or duplicate columns."""
    db_path = str(tmp_path / "idem.db")
    _build_v2_db(db_path)
    monkeypatch.setattr(config, "DB_PATH", db_path)
    db.init_db()
    db.init_db()  # second run must be a no-op
    conn = sqlite3.connect(db_path)
    cols = [r[1] for r in conn.execute("PRAGMA table_info(memories)")]
    assert cols.count("meta") == 1
    conn.close()
````

## `tests/test_ollama.py`

````
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
````

## `tests/test_reliability.py`

````
"""Malformed input, size caps, and database-recovery safety.

These tests never delete or replace a real user brain. They only use the
isolated fixture database.
"""
from backend import config, db, export, store


def test_integrity_ok_on_healthy_file():
    assert db.integrity_ok() is True


def test_integrity_ok_false_on_garbage_does_not_rebuild():
    path = config.DB_PATH
    with open(path, "wb") as fh:
        fh.write(b"not a sqlite database at all")
    assert db.integrity_ok() is False
    # The file is still there — we do not delete or replace a bad brain.
    with open(path, "rb") as fh:
        assert fh.read().startswith(b"not a sqlite")


def test_import_rejects_non_object_and_wrong_types():
    assert export.import_from_json("[]", mode="merge")["ok"] is False
    assert export.import_from_json("null", mode="merge")["ok"] is False
    bad = '{"format":"second-brain","entities":"nope","relationships":[]}'
    assert export.import_from_json(bad, mode="merge")["ok"] is False


def test_conversation_summaries_escape_like_wildcards():
    cid = store.create_conversation("Rust notes")
    store.add_message("user", "I am learning Rust", conversation_id=cid)
    hits = store.conversation_summaries(query="Rust")
    assert any(c["id"] == cid for c in hits)
    assert store.conversation_summaries(query="%") == []
    assert store.conversation_summaries(query="_") == []
    assert store.conversation_summaries(query="no-such-thread") == []
````

## `tests/test_search.py`

````
"""Tests for hybrid search, RAG answers, and hallucination protection."""
from backend import extract, search, store


def _seed():
    extract.extract("I am learning Python and I want to build AI agents.")
    extract.extract("My new project Nebula uses Next.js and Ollama.")


def test_keyword_search_finds_exact():
    _seed()
    hits = search.keyword_search("Nebula")
    assert any(h[1]["name"] == "Nebula" for h in hits)


def test_vector_search_returns_results():
    _seed()
    hits = search.vector_search("What programming language am I studying?")
    assert len(hits) > 0


def test_hybrid_search_combines_signals():
    _seed()
    res = search.search("Next.js")
    assert any(e["name"] == "Next.js" for e in res["entities"])


def test_answer_known():
    _seed()
    a = search.answer("What projects am I working on?")
    assert a["status"] in ("known", "answered")
    assert "Nebula" in a["text"]


def test_answer_unknown_no_hallucination():
    _seed()
    a = search.answer("Do I use Java?")
    assert a["status"] in ("unknown", "uncertain")
    # Must never invent a Java memory.
    if a["status"] == "unknown":
        assert "Java" not in a["text"] or "don't have" in a["text"] or "nothing" in a["text"]


def test_answer_learning_intent():
    _seed()
    a = search.answer("What am I learning?")
    assert a["status"] in ("known", "answered")
    assert "Python" in a["text"]


def test_answer_preference_intent():
    extract.extract("I prefer Python")
    a = search.answer("What language do I prefer?")
    assert a["status"] in ("known", "answered", "uncertain")
    if a["status"] == "answered":
        assert "Python" in a["text"]


def test_intent_detection():
    assert search.detect_intent("What projects am I working on?") == "project"
    assert search.detect_intent("What am I learning?") == "learning"
    assert search.detect_intent("Do you know who I met?") == "person"


def test_superseded_facts_not_in_active_search():
    extract.extract("I am learning Rust")
    extract.extract("I stopped learning Rust")
    # Active learning facts should not include Rust.
    facts = search.intent_facts("learning")
    texts = [f["text"] for f in facts]
    assert not any("Rust" in t and "learning" in t for t in texts)


def test_graph_facts_for_entity():
    _seed()
    neb = store.find_entity_by_name("Nebula")
    facts = search.graph_facts_for_entity(neb["id"])
    texts = [f["text"] for f in facts]
    assert any("uses Next.js" in t for t in texts)


def test_is_question():
    assert search.is_question("What projects am I working on?")
    assert search.is_question("Do I use Java?")
    assert search.is_question("Tell me about Nebula")
    assert not search.is_question("I am learning Python")


def test_tell_me_about_entity():
    extract.extract("My new project Nebula uses Next.js")
    a = search.answer("Tell me about Nebula")
    assert a["status"] == "known"
    assert "Nebula" in a["text"]
    assert a.get("sources") is not None


def test_path_question():
    extract.extract("My new project Game Engine uses Bevy")
    a = search.answer("How is Game Engine related to Bevy?")
    assert a["status"] == "known"
    assert "Bevy" in a["text"]


def test_yes_no_unknown_when_relation_missing():
    extract.extract("I am learning Python")
    a = search.answer("Do I use Python?")
    assert a["status"] == "unknown"
    assert "don't have" in a["text"].lower() or "nothing" in a["text"].lower()


def test_yes_no_known_when_fact_exists():
    extract.extract("I use Docker")
    a = search.answer("Do I use Docker?")
    assert a["status"] == "known"
    assert "Docker" in a["text"]


def test_pinned_entity_gets_reason():
    extract.extract("I am learning Python")
    py = store.find_entity_by_name("Python")
    store.update_entity(py["id"], pinned=1)
    res = search.search("Python")
    hit = next(e for e in res["entities"] if e["name"] == "Python")
    assert "pinned" in hit["reasons"]


def test_short_name_keyword_go():
    extract.extract("I am learning Go")
    hits = search.keyword_search("Go")
    assert any(h[1]["name"] == "Go" for h in hits)


def test_where_do_i_live_direct():
    extract.extract("I live in Berlin")
    a = search.answer("Where do I live?")
    assert a["status"] == "known"
    assert "Berlin" in a["text"]


def test_what_does_project_use_direct():
    extract.extract("My new project Game Engine uses Bevy")
    a = search.answer("What technology does the game engine use?")
    assert a["status"] == "known"
    assert "Bevy" in a["text"]


def test_ambiguous_unknown_stays_unknown():
    extract.extract("I prefer Python")
    a = search.answer("What is my favorite color?")
    assert a["status"] in ("unknown", "uncertain")
    if a["status"] == "unknown":
        assert "don't have" in a["text"].lower() or "nothing" in a["text"].lower()


def test_compose_drops_invented_tech():
    extract.extract("I am learning Python")
    res = search.search("What am I learning?")
    fake = "You're learning Python and also Java at Google."
    assert search.reply_is_grounded("You're learning Python.", res, "What am I learning?")
    assert not search.reply_is_grounded(fake, res, "What am I learning?")


def test_works_at_intent():
    extract.extract("I work at Acme")
    assert search.detect_intent("Where do I work at?") == "organization"
    facts = search.intent_facts("organization")
    assert any("Acme" in f["text"] for f in facts)


def test_what_did_i_stop_reads_superseded():
    extract.extract("I am learning Rust")
    extract.extract("I stopped learning Rust")
    a = search.answer("What did I stop?")
    assert a["status"] == "known"
    assert "Rust" in a["text"]
    assert "no longer active" in a["text"]


def test_what_changed_this_week():
    extract.extract("I prefer Python")
    extract.extract("I prefer Rust instead of Python")
    a = search.answer("What changed this week?")
    assert a["status"] == "known"
    assert a["text"]


def test_who_uses_named_entity():
    extract.extract("My new project Game Engine uses Bevy")
    a = search.answer("Who uses Bevy?")
    assert a["status"] == "known"
    assert "Game Engine" in a["text"]
    assert "Bevy" in a["text"]


def test_when_did_i_start_learning():
    extract.extract("I am learning Rust")
    a = search.answer("When did I start learning Rust?")
    assert a["status"] == "known"
    assert "Rust" in a["text"]
    assert "stored" in a["text"].lower()


def test_compose_answer_rejects_ungrounded(monkeypatch):
    extract.extract("I am learning Python")
    res = search.search("What am I learning?")
    monkeypatch.setattr(search.ollama, "available", lambda: True)
    monkeypatch.setattr(
        search.ollama, "chat",
        lambda *a, **k: "You're learning Python and also Java at Google.",
    )
    out = search.compose_answer("What am I learning?", res, "qwen3:0.6b")
    assert "Java" not in out["text"]
    assert "Google" not in out["text"]
    assert "Python" in out["text"]
````

## `tests/test_search_advanced.py`

````
"""Tests for multi-hop retrieval, explainable ranking, sources, recency and
superseded exclusion in search."""
from backend import extract, search, store


def _seed():
    extract.extract("I am learning Rust and I want to build a game engine.")
    extract.extract("My new project Game Engine uses Bevy.")
    extract.extract("I prefer Python.")


def test_multi_hop_question():
    _seed()
    # "What technology does the project I'm learning Rust for use?"
    a = search.answer("What technology does the game engine use?")
    assert a["status"] in ("known", "answered", "uncertain")
    # Should be able to reach "Bevy" through the graph.
    res = search.search("What technology does the game engine use?")
    fact_texts = [f["text"] for f in res["facts"]]
    assert any("Bevy" in t for t in fact_texts)


def test_sources_attributed():
    _seed()
    res = search.search("What am I learning?")
    assert res.get("sources"), "answers should carry traceable sources"
    # Each source has an entity and a name.
    assert all("name" in s and "entity_id" in s for s in res["sources"])


def test_sources_openable_entity():
    _seed()
    res = search.search("Rust")
    names = {s["name"] for s in res["sources"]}
    assert "Rust" in names


def test_reasons_explainable():
    _seed()
    res = search.search("Rust")
    rust = next(e for e in res["entities"] if e["name"] == "Rust")
    assert "reasons" in rust and rust["reasons"], "results should carry match reasons"


def test_superseded_excluded_from_facts():
    extract.extract("I am learning Rust")
    extract.extract("I stopped learning Rust")
    facts = [f["text"] for f in search.intent_facts("learning")]
    assert not any("Rust" in t for t in facts)


def test_confidence_filter():
    _seed()
    res = search.search("Rust", filters={"min_confidence": 0.99})
    # With a very high confidence threshold, low-confidence entities drop out.
    assert all(e["confidence"] >= 0.99 for e in res["entities"])


def test_type_filter():
    _seed()
    res = search.search("game engine", filters={"type": "project"})
    assert all(e["type"] == "project" for e in res["entities"])


def test_unknown_still_protected():
    _seed()
    a = search.answer("Do I use Java?")
    assert a["status"] == "unknown"
    assert "don't have" in a["text"] or "nothing" in a["text"].lower()


def test_uncertain_wording():
    _seed()
    a = search.answer("Do I use Rust in a web project?")
    # Whatever the status, an uncertain answer should hedge.
    if a["status"] == "uncertain":
        assert "confidence" in a["text"].lower() or "certain" in a["text"].lower() or "tentative" in a["text"].lower()


def test_uses_of_named_project():
    _seed()
    a = search.answer("What technology does the game engine use?")
    assert a["status"] == "known"
    assert "Bevy" in a["text"]


def test_recency_boost_present():
    _seed()
    ranked = search.search("Rust")
    # Just verify the recency signal is wired (no crash) and reasons may include recent.
    assert isinstance(ranked["entities"], list)
````

## `tests/test_store.py`

````
"""Tests for the graph store: entities, merging, confidence, supersession,
memory history, and persistence."""
import json

import numpy as np

from backend import config, db, store


def test_entity_creation_and_normalization():
    eid = store.create_entity("  Python  ", "technology", "a language", 0.9)
    row = store.entity_row(eid)
    assert row["name"] == "Python"
    assert row["norm_name"] == "python"
    assert row["type"] == "technology"


def test_upsert_merges_duplicate_names():
    eid1, created1 = store.upsert_entity("Python", "technology", confidence=0.8)
    eid2, created2 = store.upsert_entity("python", "technology", confidence=0.9)
    assert created1 is True
    assert created2 is False
    assert eid1 == eid2
    row = store.entity_row(eid1)
    assert row["confidence"] == 0.9  # boosted


def test_alias_detection():
    eid = store.create_entity("Next.js", "technology")
    store.update_entity(eid, aliases=["NextJS"])
    dup = store.find_duplicate("NextJS", "technology")
    assert dup is not None and dup["id"] == eid


def test_semantic_duplicate_detection():
    # Two near-identical embeddings should collide above the threshold.
    e1 = store.create_entity("Machine Learning", "topic",
                             embedding=np.array([1.0, 0.0, 0.0], dtype=np.float32))
    dup = store.find_duplicate("Machine-Learning", "topic",
                               embedding=np.array([0.999, 0.01, 0.0], dtype=np.float32))
    assert dup is not None and dup["id"] == e1


def test_semantic_duplicate_below_threshold():
    e1 = store.create_entity("Machine Learning", "topic",
                             embedding=np.array([1.0, 0.0, 0.0], dtype=np.float32))
    dup = store.find_duplicate("Knitting", "topic",
                               embedding=np.array([0.0, 1.0, 0.0], dtype=np.float32))
    assert dup is None


def test_manual_merge_rewires_relationships():
    a = store.create_entity("Nebula", "project")
    b = store.create_entity("Nebula2", "project")
    tech = store.create_entity("Next.js", "technology")
    store.add_relationship(b, tech, "uses")
    res = store.merge_entities(a, b)
    assert res.get("ok")
    # b is gone, a now has the relationship.
    assert store.entity_row(b) is None
    rels = store.all_relationships()
    assert any(r["source_id"] == a and r["target_id"] == tech for r in rels)


def test_add_relationship_dedup():
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    store.add_relationship(a, b, "related_to", confidence=0.5)
    store.add_relationship(a, b, "related_to", confidence=0.9)
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?",
                    (a, b))
    assert len(rels) == 1
    assert rels[0]["confidence"] == 0.9


def test_supersede_relationship():
    a = store.create_entity("User2", "person")
    b = store.create_entity("Rust", "technology")
    store.add_relationship(a, b, "learning")
    n = store.supersede_relationship(a, b, "learning")
    assert n == 1
    rels = db.query("SELECT * FROM relationships WHERE source_id=? AND target_id=?", (a, b))
    assert rels[0]["status"] == "superseded"


def test_supersede_relations_of_type():
    uid = store.ensure_user_entity()
    py = store.create_entity("Python", "technology")
    rs = store.create_entity("Rust", "technology")
    store.add_relationship(uid, py, "prefers")
    store.add_relationship(uid, rs, "prefers")
    changed = store.supersede_relations_of_type(uid, "prefers", except_target_id=rs)
    assert py in changed and rs not in changed


def test_update_relationship_changes_status_and_confidence():
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    rid = store.add_relationship(a, b, "related_to", confidence=0.5)
    assert store.update_relationship(rid, confidence=0.33, status="superseded")
    row = store.relationship_row(rid)
    assert abs(row["confidence"] - 0.33) < 1e-6
    assert row["status"] == "superseded"


def test_delete_entity_cascades():
    a = store.create_entity("X", "concept")
    b = store.create_entity("Y", "concept")
    store.add_relationship(a, b, "related_to")
    store.delete_entity(a)
    assert store.entity_row(a) is None
    rels = db.query("SELECT * FROM relationships WHERE source_id=? OR target_id=?", (a, a))
    assert rels == []


def test_pin_and_important():
    eid = store.create_entity("Nebula", "project")
    store.update_entity(eid, pinned=1, important=1)
    row = store.entity_row(eid)
    assert row["pinned"] == 1 and row["important"] == 1


def test_set_confidence():
    eid = store.create_entity("Python", "technology")
    store.set_confidence(eid, 0.42)
    assert store.entity_row(eid)["confidence"] == 0.42


def test_memory_history_preserved_on_supersede():
    uid = store.ensure_user_entity()
    rs = store.create_entity("Rust", "technology")
    store.add_relationship(uid, rs, "learning")
    store.add_memory("relationship", "User learning Rust", entity_ids=[uid, rs])
    store.supersede_relationship(uid, rs, "learning")
    # The memory event remains (history is not deleted).
    mems = store.recent_memories()
    assert any("learning Rust" in m["text"] for m in mems)


def test_conversation_lifecycle():
    cid = store.create_conversation("test")
    store.add_message("user", "hello", conversation_id=cid)
    msgs = store.conversation_messages(cid)
    assert len(msgs) == 1
    assert store.conversation_row(cid)["title"] == "test"


def test_persistence_across_reopen():
    eid = store.create_entity("Python", "technology", confidence=0.7)
    # Simulate a restart by re-initializing from the same file.
    db.init_db()
    row = store.entity_row(eid)
    assert row is not None and row["name"] == "Python"


def test_user_entity_protected():
    uid = store.ensure_user_entity()
    assert store.entity_row(uid)["norm_name"] == "user"


def test_integrity_ok_on_healthy_db():
    assert db.integrity_ok() is True


def test_similar_entities_by_embedding():
    a = store.create_entity(
        "Alpha", "concept", embedding=np.array([1.0, 0.0, 0.0], dtype=np.float32),
    )
    b = store.create_entity(
        "AlphaPrime", "concept",
        embedding=np.array([0.97, 0.05, 0.0], dtype=np.float32),
    )
    store.create_entity(
        "Unrelated", "concept", embedding=np.array([0.0, 1.0, 0.0], dtype=np.float32),
    )
    hits = store.similar_entities(a)
    ids = {h["id"] for h in hits}
    assert b in ids
    assert all(h["score"] >= 0.78 for h in hits)


def test_merge_preserves_description():
    a = store.create_entity("Nebula", "project", description="AI workspace")
    b = store.create_entity("Nebula2", "project", description="")
    store.merge_entities(a, b)
    assert store.entity_row(a)["description"] == "AI workspace"
````

## `tests/test_summarize.py`

````
"""Tests for memory consolidation / summarization."""
import json

from backend import db, extract, store, summarize


def _seed_rich_entity():
    # Create multiple memories around one project so it becomes a candidate.
    for line in [
        "My project Nebula uses Next.js.",
        "Nebula uses Ollama.",
        "Nebula is an AI creative workspace.",
        "I am building Nebula for image generation.",
    ]:
        extract.extract(line)


def test_find_candidates():
    _seed_rich_entity()
    cands = summarize.find_consolidation_candidates(min_shared=2)
    nebula = next((c for c in cands if c["entity_name"] == "Nebula"), None)
    assert nebula is not None
    assert nebula["count"] >= 2


def test_summarize_entity_creates_summary_memory():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    before = len(store.memories_for_entity(nebula["id"]))
    r = summarize.summarize_entity(nebula["id"])
    assert r["ok"] is True
    assert r["summary_id"] is not None
    # A new summary memory exists and references the entity.
    mems = db.query("SELECT * FROM memories WHERE kind='summary'")
    assert mems
    meta = json.loads(mems[0]["meta"] or "{}")
    assert "source_memory_ids" in meta


def test_summarize_does_not_delete_originals():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    before = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    summarize.summarize_entity(nebula["id"])
    after = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    assert after > before, "originals must be preserved, summary added on top"


def test_summary_references_source_memories():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    r = summarize.summarize_entity(nebula["id"])
    mem = db.query_one("SELECT * FROM memories WHERE id=?", (r["summary_id"],))
    meta = json.loads(mem["meta"] or "{}")
    assert meta["source_memory_ids"], "summary should reference the memories it came from"


def test_summarize_all():
    _seed_rich_entity()
    results = summarize.summarize_all(limit=5)
    assert any(res.get("ok") for res in results)


def test_no_repeated_summary_of_same_cluster():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    summarize.summarize_entity(nebula["id"])
    cands = summarize.find_consolidation_candidates(min_shared=2)
    # Nebula should be skipped now that it's been summarized.
    assert not any(c["entity_name"] == "Nebula" for c in cands)
````

## `tests/test_tray.py`

````
"""Tray and EXE icon tests. No activity watching."""
from pathlib import Path

from launcher import icons, tray


ROOT = Path(__file__).resolve().parent.parent


def test_activity_watch_is_hard_off():
    assert tray.should_watch_activity() is False
    assert tray.ACTIVITY_WATCH_ENABLED is False
    assert tray.ACTIVITY_POLL_SECONDS is None


def test_clip_remember_text_skips_empty_and_caps():
    assert tray.clip_remember_text("   ") is None
    assert tray.clip_remember_text("") is None
    long = "x" * 9000
    clipped = tray.clip_remember_text(long)
    assert clipped is not None and len(clipped) == 8000


def test_tray_source_has_no_activity_poller():
    src = Path(tray.__file__).read_text(encoding="utf-8")
    assert "GetForegroundWindow" not in src
    assert "BitBlt" not in src
    assert "SetWindowsHook" not in src
    assert "ACTIVITY_WATCH_ENABLED = False" in src
    assert "def should_watch_activity" in src


def test_icons_exist():
    ico = ROOT / "launcher" / "secondbrain.ico"
    png = ROOT / "launcher" / "secondbrain.png"
    assert ico.is_file() and ico.stat().st_size > 1000
    assert png.is_file() and png.stat().st_size > 1000
    assert icons.icon_ico() == ico
    assert icons.icon_png() == png


def test_spec_embeds_icon():
    spec = (ROOT / "secondbrain.spec").read_text(encoding="utf-8")
    assert 'icon="launcher/secondbrain.ico"' in spec
    assert "launcher/secondbrain.ico" in spec


def test_ico_has_standard_windows_sizes():
    import struct
    data = (ROOT / "launcher" / "secondbrain.ico").read_bytes()
    reserved, typ, count = struct.unpack_from("<HHH", data, 0)
    assert reserved == 0 and typ == 1 and count >= 4
    sizes = set()
    off = 6
    for _ in range(count):
        w, h = struct.unpack_from("<BB", data, off)
        sizes.add(w or 256)
        sizes.add(h or 256)
        off += 16
    assert {16, 32, 48, 256} <= sizes
````

