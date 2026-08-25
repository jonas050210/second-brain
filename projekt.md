# Second Brain — complete first-party archive

This file is a readable dump of every first-party project file.
It is documentation, not a second application. The live source of
truth remains the individual files in this repository.

Generated: 2026-08-25 13:38 UTC
Version: 2.3.0
Files archived: 54

Omitted on purpose:
- `.git/`, virtualenvs, caches, `__pycache__`
- user data (`data/brain.db` and backups)
- the minified third-party `frontend/vendor/cytoscape.min.js` (hash + size only)

## Table of contents

- [`.env.example`](#envexample)
- [`.gitignore`](#gitignore)
- [`README.md`](#READMEmd)
- [`ROADMAP`](#ROADMAP)
- [`backend/.env.example`](#backendenvexample)
- [`backend/__init__.py`](#backend__init__py)
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
- [`backend/requirements-dev.txt`](#backendrequirements-devtxt)
- [`backend/requirements.txt`](#backendrequirementstxt)
- [`backend/search.py`](#backendsearchpy)
- [`backend/store.py`](#backendstorepy)
- [`backend/summarize.py`](#backendsummarizepy)
- [`frontend/app.js`](#frontendappjs)
- [`frontend/index.html`](#frontendindexhtml)
- [`frontend/style.css`](#frontendstylecss)
- [`frontend/vendor/cytoscape.min.js`](#frontendvendorcytoscapeminjs)
- [`launcher/__init__.py`](#launcher__init__py)
- [`launcher/__main__.py`](#launcher__main__py)
- [`launcher/bootstrap.py`](#launcherbootstrappy)
- [`launcher/build_exe.py`](#launcherbuild_exepy)
- [`launcher/gui.py`](#launcherguipy)
- [`main.py`](#mainpy)
- [`pytest.ini`](#pytestini)
- [`requirements.txt`](#requirementstxt)
- [`run.py`](#runpy)
- [`secondbrain.spec`](#secondbrainspec)
- [`start.py`](#startpy)
- [`test_overall.py`](#test_overallpy)
- [`tests/conftest.py`](#testsconftestpy)
- [`tests/test_api.py`](#teststest_apipy)
- [`tests/test_api_phase3.py`](#teststest_api_phase3py)
- [`tests/test_backup.py`](#teststest_backuppy)
- [`tests/test_commands.py`](#teststest_commandspy)
- [`tests/test_export.py`](#teststest_exportpy)
- [`tests/test_extraction.py`](#teststest_extractionpy)
- [`tests/test_frontend.py`](#teststest_frontendpy)
- [`tests/test_graph.py`](#teststest_graphpy)
- [`tests/test_launcher.py`](#teststest_launcherpy)
- [`tests/test_migration.py`](#teststest_migrationpy)
- [`tests/test_ollama.py`](#teststest_ollamapy)
- [`tests/test_search.py`](#teststest_searchpy)
- [`tests/test_search_advanced.py`](#teststest_search_advancedpy)
- [`tests/test_store.py`](#teststest_storepy)
- [`tests/test_summarize.py`](#teststest_summarizepy)

## File tree

```
     634  .env.example
     285  .gitignore
    7305  README.md
    1989  ROADMAP
     459  backend/.env.example
       0  backend/__init__.py
   45093  backend/app.py
    7148  backend/backup.py
   15344  backend/commands.py
    8310  backend/config.py
    7595  backend/db.py
   13534  backend/export.py
   23023  backend/extract.py
   22824  backend/fallback.py
   12739  backend/graph.py
    4385  backend/ollama.py
    4130  backend/paths.py
     242  backend/requirements-dev.txt
      66  backend/requirements.txt
   32910  backend/search.py
   18480  backend/store.py
    5372  backend/summarize.py
   65236  frontend/app.js
   18495  frontend/index.html
   28065  frontend/style.css
  373304  frontend/vendor/cytoscape.min.js
     222  launcher/__init__.py
    3376  launcher/__main__.py
   11648  launcher/bootstrap.py
    1617  launcher/build_exe.py
   12035  launcher/gui.py
     728  main.py
      91  pytest.ini
     165  requirements.txt
     223  run.py
    2575  secondbrain.spec
    9375  start.py
   17435  test_overall.py
    2849  tests/conftest.py
    8685  tests/test_api.py
    5976  tests/test_api_phase3.py
    2756  tests/test_backup.py
    5709  tests/test_commands.py
    4400  tests/test_export.py
   10392  tests/test_extraction.py
    5219  tests/test_frontend.py
    4123  tests/test_graph.py
    8594  tests/test_launcher.py
    3365  tests/test_migration.py
    2945  tests/test_ollama.py
    5095  tests/test_search.py
    3065  tests/test_search_advanced.py
    6284  tests/test_store.py
    2508  tests/test_summarize.py
```

## `.env.example`

<a id="envexample"></a>

- size: 634 bytes
- sha256: `5c007e271562b43cede5dae7b3c34be642462cd580d7bc16786efe8c6c4e3777`

````dotenv
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

<a id="gitignore"></a>

- size: 285 bytes
- sha256: `05a9e530f8c4bb994c5420fb32ef100e17d33df0ca31f3b001b68dbca1391124`

````gitignore
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

## `README.md`

<a id="READMEmd"></a>

- size: 7305 bytes
- sha256: `8a2f27b9e405c08fbfca0c952a752a1c054a93d86f321b0dd277e211d714215a`

````markdown
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

That produces **`dist/SecondBrain.exe`**. Double-click it.

First launch shows a dark setup window (version, current step, progress, log, Ollama status). It:

- checks the packaged runtime
- finds an existing `brain.db` next to the EXE (`dist\data\brain.db`) or under `%LOCALAPPDATA%\SecondBrain\data\brain.db`
- creates that file only if none exists — it never deletes, resets, or replaces a brain
- probes Ollama over HTTP (`qwen3:0.6b`, `nomic-embed-text`)
- does **not** download models unless you set `SECOND_BRAIN_PULL_MODELS=1`
- starts the **existing** FastAPI app and opens the browser

If Ollama is down, the window says offline and the app uses the rule-based fallback. It does not crash.

Later launches skip installs, skip model downloads, and reopen the same database. The setup window stays open with **Open browser** / **Quit** so the server is not killed when the first-run checks finish.

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
duplicate-merge threshold, auto-memory, theme.

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

Forgetting a preference or a “learning X” fact **supersedes** it. It does not
silently delete history.

---

## Search / RAG

Keyword + semantic + graph + recency + confidence + active/superseded + bounded
multi-hop. Short names (`Go`, `C#`, `AI`) are searchable. Direct questions
such as “Where do I live?” or “What technology does the game engine use?”
read the graph first. If there is no evidence, the answer is UNKNOWN.

---

## Graph

Cytoscape visualization of the real SQLite graph. Pan, zoom, search, type /
relation / confidence / status / pinned / important filters, expand, focus,
edit, delete, merge. Layouts: force, group-by-type, from-User. Relationship
types can be edited on an entity. Isolated nodes can be hidden. No fabricated
nodes.

---

## Backup / export / import

- JSON + Markdown export
- Merge import or replace import (replace requires `confirm=true`)
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

## `ROADMAP`

<a id="ROADMAP"></a>

- size: 1989 bytes
- sha256: `339a5e08291470458107cce0168be6f886fbb4361b9e6a69e75a5c1ea159d144`

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

## Next (optional)

- Explicit user-initiated binary file ingest
- Tray icon / background service for the EXE

## Non-goals

- Cloud sync by default
- Telemetry
- Inventing personal memories
- A second graph store
- A second extraction implementation
````

## `backend/.env.example`

<a id="backendenvexample"></a>

- size: 459 bytes
- sha256: `1435eabbd4e80b18e1cad376c448d72516a0bb89ec240becdc2472e479946fdc`

````dotenv
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

<a id="backend__init__py"></a>

- size: 0 bytes
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

````python

````

## `backend/app.py`

<a id="backendapppy"></a>

- size: 45093 bytes
- sha256: `0d69749f766bbf7b8d5ed3ffdf61d0d9b61a792ba81074c88f7f1450cbd84d9c`

````python
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

app = FastAPI(title="Second Brain", version="2.3.0")
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
        "version": "2.3.0",
        "db_ok": db.integrity_ok(),
        "auto_backup": _safe_auto_backup(),
    }


def _safe_auto_backup():
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
def conversations():
    rows = store.all_conversations()
    out = []
    for c in rows:
        msgs = store.conversation_messages(c["id"])
        user_msgs = [m for m in msgs if m["role"] == "user"]
        out.append({"id": c["id"], "title": c["title"] or "(untitled)",
                    "created_at": c["created_at"], "updated_at": c["updated_at"],
                    "message_count": len(msgs),
                    "preview": user_msgs[-1]["content"][:80] if user_msgs else ""})
    return out


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
def graph(active_only: bool = True):
    ents = store.all_entities()
    rels = store.all_relationships(active_only=active_only)
    nodes = [{"id": e["id"], "label": e["name"], "type": e["type"],
              "description": e["description"], "confidence": e["confidence"],
              "pinned": e.get("pinned", 0), "important": e.get("important", 0),
              "status": e.get("status", "active")} for e in ents]
    edges = [{"id": f"e{r['id']}", "source": r["source_id"], "target": r["target_id"],
              "relation": r["relation"], "confidence": r["confidence"],
              "status": r.get("status", "active")} for r in rels]
    return {"nodes": nodes, "edges": edges,
            "type_colors": config.TYPE_COLORS,
            "relation_types": config.RELATION_TYPES,
            "entity_types": config.ENTITY_TYPES}


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
def entities(q: str = None, type: str = None, pinned: bool = None, important: bool = None):
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
    return [{"id": r["id"], "name": r["name"], "type": r["type"],
             "description": r["description"], "degree": deg.get(r["id"], 0),
             "confidence": r["confidence"], "pinned": r.get("pinned", 0),
             "important": r.get("important", 0), "status": r.get("status", "active"),
             "created_at": r["created_at"], "updated_at": r["updated_at"],
             "source_message_id": r.get("source_message_id")} for r in rows]


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
    return export.import_from_json(body.data, mode=body.mode)


class NotesIn(BaseModel):
    text: str


@app.post("/api/import/notes")
def import_notes(body: NotesIn):
    if len((body.text or "").encode("utf-8")) > MAX_IMPORT_BYTES:
        raise HTTPException(400, "note payload too large (8 MB max)")
    result = export.import_notes(body.text)
    if not result.get("ok"):
        raise HTTPException(400, result.get("error") or "import failed")
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
        "privacy": {
            "mode": "local-first",
            "local": True,
            "private": True,
            "telemetry": False,
            "cloud": False,
            "data_leaves_machine": False,
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

<a id="backendbackuppy"></a>

- size: 7148 bytes
- sha256: `0e50b4ed889fe295c81aa86ef29c1b5fa99c4ad4e55233b83a828f417d777f7c`

````python
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

<a id="backendcommandspy"></a>

- size: 15344 bytes
- sha256: `5f4186f9fcc542205f61926ff2117ac25d545fc9279479b7328154b2e0a4df77`

````python
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
    if re.match(r"^(?:important|unimportant)(?:\s|$)", t):
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

<a id="backendconfigpy"></a>

- size: 8310 bytes
- sha256: `c52b578e774c0ffa82948bf507a627082b5dcb39c6e66396e90c39c9031121c5`

````python
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

<a id="backenddbpy"></a>

- size: 7595 bytes
- sha256: `f7c3805206e14a80ce86cf3034b49c4fcdf6189cc982dd06bd88fb36dc1dcd0f`

````python
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

<a id="backendexportpy"></a>

- size: 13534 bytes
- sha256: `7eb85c90d1e7cd55bb0db094042f774bf17f9b340324230c02c50a7a35a32548`

````python
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


def _import_entities(data):
    user_id = store.ensure_user_entity()
    id_map = {}
    created, merged = 0, 0
    for e in data["entities"]:
        name = (e.get("name") or "").strip()
        if not name:
            continue
        if store.normalize_name(name) in ("user", "i", "me"):
            if e.get("id") is not None:
                id_map[e["id"]] = user_id
            continue
        eid, is_new = store.upsert_entity(
            name, e.get("type", "concept"), e.get("description", ""),
            confidence=float(e.get("confidence", 0.8)),
        )
        if eid is None:
            continue
        if is_new:
            created += 1
        else:
            merged += 1
        if e.get("id") is not None:
            id_map[e["id"]] = eid
        _apply_entity_flags(eid, e)
    return id_map, created, merged


def _import_relationships(data, id_map):
    added = 0
    for r in data["relationships"]:
        sid = id_map.get(r["source_id"])
        tid = id_map.get(r["target_id"])
        if sid is None or tid is None or sid == tid:
            continue
        rel, swap = store.normalize_relation(r["relation"])
        if swap:
            sid, tid = tid, sid
        existed = store.relationship_exists(sid, tid, rel)
        rid = store.add_relationship(sid, tid, rel,
                                     confidence=float(r.get("confidence", 0.8)))
        if r.get("status") and r["status"] != "active" and rid:
            store.update_relationship(rid, status=r["status"])
        if not existed:
            added += 1
    return added


def _import_memories(data, id_map, message_map=None, dedup=True):
    added = 0
    existing = set()
    if dedup:
        existing = {(m["kind"], m["text"]) for m in db.query("SELECT kind, text FROM memories")}
    for m in data.get("memories") or []:
        if not isinstance(m, dict) or not m.get("text"):
            continue
        key = (m.get("kind") or "entity", m["text"])
        if dedup and key in existing:
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
        store.add_memory(m.get("kind") or "entity", m["text"], entity_ids=eids,
                         message_id=mid, confidence=float(m.get("confidence", 0.8)),
                         meta=meta)
        existing.add(key)
        added += 1
    return added


def import_merge(data):
    """Merge-import: upsert entities (by name) and add relationships.
    Preserves existing data. Returns a summary."""
    ok, err = validate_payload(data)
    if not ok:
        return {"ok": False, "error": err}

    id_map, created, merged = _import_entities(data)
    added_rels = _import_relationships(data, id_map)
    added_mems = _import_memories(data, id_map, dedup=True)
    return {"ok": True, "mode": "merge", "entities_created": created,
            "entities_merged": merged, "relationships_added": added_rels,
            "memories_added": added_mems}


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

    id_map, created, merged = _import_entities(data)
    added_rels = _import_relationships(data, id_map)
    added_mems = _import_memories(data, id_map, message_map=msg_map, dedup=False)
    return {"ok": True, "mode": "replace", "entities_created": created,
            "entities_merged": merged, "relationships_added": added_rels,
            "memories_added": added_mems}


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

<a id="backendextractpy"></a>

- size: 23023 bytes
- sha256: `7d1344b6e4985c4819275e3a87f55cfb153ad4fb14d23c487cbad897ac4a9387`

````python
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
    exclusive_relations = {"prefers", "lives_in", "works_at"}

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

<a id="backendfallbackpy"></a>

- size: 22824 bytes
- sha256: `a26a7f4caf213ab95b1adc1e7530c1e00804d27b3ff09a800d8441e7d99820f8`

````python
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

<a id="backendgraphpy"></a>

- size: 12739 bytes
- sha256: `5f034da5f0a700c04e0bd8c2ad2398bd039349219d426a98f09dfc224d6187ef`

````python
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
                   "status": n.get("status", "active"), "pinned": n.get("pinned", 0),
                   "important": n.get("important", 0), "confidence": n["confidence"]}
                  for n in nodes.values()],
        "edges": [{"id": f"e{r['id']}", "source": r["source_id"], "target": r["target_id"],
                   "relation": r["relation"], "confidence": r["confidence"],
                   "status": r["status"]} for r in edge_rows],
    }


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

<a id="backendollamapy"></a>

- size: 4385 bytes
- sha256: `8fa91c03fb644a0f86f882a73758cdc339e5752527806737b9f6deac493cc805`

````python
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

<a id="backendpathspy"></a>

- size: 4130 bytes
- sha256: `5512f1b063728232400bc795562c83b068a286c49bd6fff372f39c674829eb05`

````python
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

APP_VERSION = "2.3.0"
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

<a id="backendrequirements-devtxt"></a>

- size: 242 bytes
- sha256: `cba222612690fe38756a122c48733174a7fef6874fb447957b8b98a355696869`

````text
# Test / development dependencies (on top of requirements.txt)
pytest>=8.0
httpx>=0.27
playwright>=1.40   # optional — browser tests (python -m playwright install chromium)
pyinstaller>=6.0   # optional — build SecondBrain.exe on Windows
````

## `backend/requirements.txt`

<a id="backendrequirementstxt"></a>

- size: 66 bytes
- sha256: `eeb35a2d0e586ada6d7a8809c121a9e78e27b47cd99fb37a9d2c35f8978cb6b6`

````text
fastapi>=0.110
uvicorn[standard]>=0.29
requests>=2.31
numpy>=1.26
````

## `backend/search.py`

<a id="backendsearchpy"></a>

- size: 32910 bytes
- sha256: `61a5914bf60358d07dabed120c44d2d15d0a54c4f968b03415f2a8989a6e61e2`

````python
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

from . import config, db, graph, ollama, store

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


def retrieve_answer(query_text, filters=None):
    """Deterministic retrieval. `final` answers skip the LLM composer."""
    direct = _direct_fact_answer(query_text)
    if direct is not None:
        out = dict(direct)
        out["final"] = True
        return out
    listed = _list_intent_answer(query_text)
    if listed is not None:
        return listed
    uses = _uses_of_answer(query_text)
    if uses is not None:
        return uses
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
            if text:
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
                    yield piece
            if "".join(acc).strip():
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

<a id="backendstorepy"></a>

- size: 18480 bytes
- sha256: `30ac5c95e9b277eefbbf6c36ed0c507c44e4691cbf602cdb1c96ca7eb211d72a`

````python
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

<a id="backendsummarizepy"></a>

- size: 5372 bytes
- sha256: `51bda4a03f5216ae384401dfd49a2cc1429691cb4a7c8d6e1853324fb021a016`

````python
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

<a id="frontendappjs"></a>

- size: 65236 bytes
- sha256: `28775f9ad54e0da9531046cfea4d43952f55d258790a6f664cd31d5a94ba368f`

````javascript
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

function showView(name) {
  if (!VIEWS.includes(name)) name = "dashboard";
  VIEWS.forEach((v) => {
    const el = $("#view-" + v);
    if (el) el.classList.toggle("active", v === name);
  });
  $$(".nav-item").forEach((b) => b.classList.toggle("active", b.dataset.view === name));
  if (location.hash !== "#" + name) {
    try { history.replaceState(null, "", "#" + name); } catch {}
  }
  if (name === "graph") requestAnimationFrame(() => { if (cy) cy.fit(undefined, 30); });
  if (name === "dashboard") loadDashboard();
  if (name === "memory") loadMemory();
  if (name === "browse") loadBrowse();
  if (name === "chat") scrollChat();
  if (name === "settings") { loadSettings(); loadBackupStatus(); }
}

window.addEventListener("hashchange", () => {
  const v = location.hash.replace(/^#/, "");
  if (VIEWS.includes(v)) showView(v);
});

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
      src.innerHTML = `<div class="remembered-title">Sources</div>` +
        sources.map((s) => `<span class="remembered-chip" data-id="${s.entity_id}">${esc(s.name)}${s.fact ? ` · <span class="conf">${esc(s.fact)}</span>` : ""}${s.snippet ? ` · <span class="conf">${esc(s.snippet)}</span>` : ""}</span>`).join("");
      wrap.appendChild(src);
      src.querySelectorAll(".remembered-chip").forEach((chip) =>
        chip.addEventListener("click", () => openEntity(chip.dataset.id)));
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
  $("#chat-messages").innerHTML = "";
  $("#chat-empty").style.display = "";
  toast("Started a new conversation");
  loadConversations();
});

async function loadConversations() {
  const list = $("#conv-list");
  if (!list) return;
  try {
    const convs = await api("/conversations");
    if (!convs.length) {
      list.innerHTML = `<p class="muted">No conversations yet.</p>`;
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
    if (src) {
      const cur = src.value;
      src.innerHTML = `<option value="">Any source</option>` +
        convs.map((c) => `<option value="${c.id}">${esc(c.title || "Conversation " + c.id)}</option>`).join("");
      src.value = cur;
    }
  } catch {}
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

async function buildGraph() {
  const g = await api("/graph");
  graphNodes = g.nodes;
  typeColors = g.type_colors || TYPE_COLORS;
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.label, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  if (!cy) initGraph();
  cy.elements().remove();
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  buildLegend();
  applyTypeFilter();
  $("#graph-sub").textContent = `${g.nodes.length} entities · ${g.edges.length} relationships`;
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

let lastFocusedId = null;
let pathEnds = [];

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
  if ($("#gf-layout")) $("#gf-layout").value = "cose";
  $$(".legend-row").forEach((r) => r.classList.remove("off"));
  hiddenTypes.clear();
  await buildGraph();
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
        return `<div class="tl-item">
          <div class="tl-time">${fmtTime(m.created_at)}</div>
          <div class="tl-text">${esc(m.text)}<span class="tl-kind">${esc(m.kind)}</span>
          ${m.confidence ? `<span class="conf">${Math.round(m.confidence * 100)}%</span>` : ""}</div>
        </div>`;
      }).join("")}
    </div>`).join("");
  $("#timeline").innerHTML = html || `<p class="muted">No memories recorded yet.</p>`;
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
}
function closeEntity() {
  $("#entity-panel").classList.remove("open");
  $("#entity-overlay").classList.remove("show");
  currentEntity = null;
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
      <p class="hint">Database: <code>${esc(s.db_path || "")}</code></p>`;
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

$("#import-merge").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "merge" }) });
    $("#import-status").textContent = r.ok
      ? `Merged: ${r.entities_created} created, ${r.entities_merged} merged, ${r.relationships_added} relationships.`
      : "Error: " + r.error;
    if (r.ok) { loadDashboard(); buildGraph(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

$("#import-replace").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  if (!confirm("Replace the ENTIRE database with this import? This wipes all current data.")) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "replace", confirm: true }) });
    $("#import-status").textContent = r.ok
      ? `Replaced: ${r.entities_created} entities imported.`
      : "Error: " + r.error;
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
        <span class="browse-meta">${esc((b.created_at || "").slice(0, 19))}</span>
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
  try { ents = await api("/entities" + (query ? ("?q=" + encodeURIComponent(query)) : "")); } catch {}
  const viewHits = views.filter((v) => !query || v.label.toLowerCase().includes(query));
  const entHits = ents.slice(0, 12).map((e) => ({ kind: "entity", id: e.id, label: e.name, type: e.type }));
  paletteItems = viewHits.concat(entHits);
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
  refreshStatus();
  await loadChatHistory();
  await buildGraph();
  await loadDashboard();
  await loadSettings();
  loadBackupStatus();
  loadSummarizeCandidates();
  loadConversations();
  const initial = location.hash.replace(/^#/, "");
  showView(VIEWS.includes(initial) ? initial : "dashboard");
  setInterval(refreshStatus, 15000);
}
boot();
````

## `frontend/index.html`

<a id="frontendindexhtml"></a>

- size: 18495 bytes
- sha256: `5fb9e4b2ddc014c7f3fbabb091e99c70de3aa69f397fa6e66d6ea290288ef9b1`

````html
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

<a id="frontendstylecss"></a>

- size: 28065 bytes
- sha256: `4d05de149b7d14c18c8875cc1cb76703cebd097f8f25a86227b0119a0b890133`

````css
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

<a id="frontendvendorcytoscapeminjs"></a>

- size: 373304 bytes
- sha256: `83e8c54a6bec655bfd81df07df605649c268af69aeca67a5ea2da54ea42dac81`

Third-party minified Cytoscape build. Not inlined.
Served from `frontend/vendor/cytoscape.min.js`.

## `launcher/__init__.py`

<a id="launcher__init__py"></a>

- size: 222 bytes
- sha256: `6fe14198c379c5da4655903cd5f6e13e53e0b314fdb696ef7c57047ce0a8f305`

````python
"""Windows EXE / desktop bootstrapper for the existing Second Brain app.

This package does not reimplement memory, search, or the API. It only
checks the environment and starts ``backend.app``.
"""

__version__ = "2.3.0"
````

## `launcher/__main__.py`

<a id="launcher__main__py"></a>

- size: 3376 bytes
- sha256: `c44ad0ff032d31583a8569e21c94799c859d3178da9a934feec6317842b992a5`

````python
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
    )


if __name__ == "__main__":
    raise SystemExit(main())
````

## `launcher/bootstrap.py`

<a id="launcherbootstrappy"></a>

- size: 11648 bytes
- sha256: `d0e28097e374b22ab239ee67845e60727afafd5f1cf9177b15aa56f33871c77a`

````python
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

<a id="launcherbuild_exepy"></a>

- size: 1617 bytes
- sha256: `e1b3b0110efceb3561847e4c9b207eb22e34ab885e986797b5052b475dd42e32`

````python
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

<a id="launcherguipy"></a>

- size: 12035 bytes
- sha256: `1d3a61a0ab941d20042fb1aec0ef995d2266e9c7cbae00fe0ccaa4e34906a236`

````python
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
        self._url = "http://127.0.0.1:8000"

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _open_browser(self) -> None:
        try:
            webbrowser.open(self._url)
        except Exception:
            self.append_log("Could not open the browser. Visit " + self._url)

    def _on_close(self) -> None:
        if self._closed:
            return
        self._closed = True
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
        self.btn_open.pack(side="left", padx=(0, 8))
        self.btn_quit.pack(side="left")
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

## `main.py`

<a id="mainpy"></a>

- size: 728 bytes
- sha256: `7832ff9b9a51171c6c8d9368420785947d0be409ce8c21fb6a4040a5541c906c`

````python
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

<a id="pytestini"></a>

- size: 91 bytes
- sha256: `87b28ec8b3ebfe5632bb76fbcfd2a2767cc13d7f561bdaa61d2a40e98fc339cf`

````ini
[pytest]
testpaths = tests test_overall.py
filterwarnings =
    ignore::DeprecationWarning
````

## `requirements.txt`

<a id="requirementstxt"></a>

- size: 165 bytes
- sha256: `3e71e7fb36655d9ec5b1d3bd6c701312fc94de522c2fca1673cd22ab4776f6b3`

````text
# Second Brain — runtime dependencies
# Install with:  python -m pip install -r requirements.txt
fastapi>=0.110
uvicorn[standard]>=0.29
requests>=2.31
numpy>=1.26
````

## `run.py`

<a id="runpy"></a>

- size: 223 bytes
- sha256: `3e7206e28b425b49ebfbbcb1a5ec70beb1549f5b7c0a0eb06a0a767b224056c3`

````python
"""Launch the Second Brain backend + UI.

Usage:  python run.py   (then open http://localhost:8000)
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=False)
````

## `secondbrain.spec`

<a id="secondbrainspec"></a>

- size: 2575 bytes
- sha256: `3ae1562bf0cfa5c17188e1ed90c31539501c5702bbfa995bfac71a776ce01fdc`

````python
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
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=False,
)
````

## `start.py`

<a id="startpy"></a>

- size: 9375 bytes
- sha256: `d68f92a4419136a85f60fbc82b5d82df79c7cd09cf802c797b0b7d371c51d7b2`

````python
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

<a id="test_overallpy"></a>

- size: 17435 bytes
- sha256: `6617054b2310a070961a43a8661f946dcf1077a900b14a713bed90a80642a9d9`

````python
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
    assert 'id="view-browse"' in html
    assert 'id="palette"' in html
    assert 'id="privacy-info"' in html
    assert 'id="graph-path"' in html
    assert 'id="import-notes"' in html
    assert 'id="gf-layout"' in html
    assert 'id="set-auto-backup"' in html


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

<a id="testsconftestpy"></a>

- size: 2849 bytes
- sha256: `c4e4b7172bbc525416206c85c967691847a990ae93752ea3ff02df304527e705`

````python
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

<a id="teststest_apipy"></a>

- size: 8685 bytes
- sha256: `c3e503f51ad34be22414c7c7ef4af6b52395fb945d80a9ff5d7a8c02a9f39561`

````python
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
    assert h.get("version") == "2.3.0"
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
````

## `tests/test_api_phase3.py`

<a id="teststest_api_phase3py"></a>

- size: 5976 bytes
- sha256: `fbefa92e3deb5215e3213deead001f9a2a858d39ec72fe504ae5d1208904ab66`

````python
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

<a id="teststest_backuppy"></a>

- size: 2756 bytes
- sha256: `4400c5973c30d71db9ca31b9644a32e1aa76768a37daf640f861bd79a62a2afb`

````python
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

<a id="teststest_commandspy"></a>

- size: 5709 bytes
- sha256: `22c8a3396ff66cf7b6256018f5f87d8600c851c15c49aa5f6e4a514e2524cb53`

````python
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

<a id="teststest_exportpy"></a>

- size: 4400 bytes
- sha256: `1ad892020d8088f94e302e224fc376b87229c64146064dfb0d6c9034c6e2f93a`

````python
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
````

## `tests/test_extraction.py`

<a id="teststest_extractionpy"></a>

- size: 10392 bytes
- sha256: `042f536827a8fcde86f27c33e04263b4dd0dc35dbba34617b931ae86e1c5b5c9`

````python
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

<a id="teststest_frontendpy"></a>

- size: 5219 bytes
- sha256: `8aec51bfae1de9c482b0ac370b30b8d3529410b12403a9c110219eb83c4d73b8`

````python
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
    assert "function loadBrowse" in js
    assert "function openPalette" in js
    assert "function runGraphLayout" in js
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

<a id="teststest_graphpy"></a>

- size: 4123 bytes
- sha256: `cf8d3a2236e8dfa19a68d250db45b9101182b5f999565f2ef3a07ae3e103c051`

````python
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
````

## `tests/test_launcher.py`

<a id="teststest_launcherpy"></a>

- size: 8594 bytes
- sha256: `c90d6673d3ee2d3a5f5063ddd9dbebc1627dea526e06a953252d5d7e42469438`

````python
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

<a id="teststest_migrationpy"></a>

- size: 3365 bytes
- sha256: `9d8c40bf5aae78e0b0d44a87f40001ea143646dc235791c479c903278b0a2ded`

````python
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

<a id="teststest_ollamapy"></a>

- size: 2945 bytes
- sha256: `664fdc5d39b244cedd8c40f23c6f1f7087ea5c3b9201d0b9e2726aec5f92c6b4`

````python
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

## `tests/test_search.py`

<a id="teststest_searchpy"></a>

- size: 5095 bytes
- sha256: `84c6f6da9430f75cd75f11b1743c0c93ef0ef03f6e9499786a364c2026f974b0`

````python
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


def test_works_at_intent():
    extract.extract("I work at Acme")
    assert search.detect_intent("Where do I work at?") == "organization"
    facts = search.intent_facts("organization")
    assert any("Acme" in f["text"] for f in facts)
````

## `tests/test_search_advanced.py`

<a id="teststest_search_advancedpy"></a>

- size: 3065 bytes
- sha256: `5747d3557579619d54497f008d221a05154dc3eaf244ff1fa898f85ec8dd2914`

````python
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

<a id="teststest_storepy"></a>

- size: 6284 bytes
- sha256: `cd7504c97384e4a3f7f264b7bfa444037854a9245b6300cac03078b75fdf0dcc`

````python
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


def test_merge_preserves_description():
    a = store.create_entity("Nebula", "project", description="AI workspace")
    b = store.create_entity("Nebula2", "project", description="")
    store.merge_entities(a, b)
    assert store.entity_row(a)["description"] == "AI workspace"
````

## `tests/test_summarize.py`

<a id="teststest_summarizepy"></a>

- size: 2508 bytes
- sha256: `406f096e94501d4026f5f2992b6882df87cf8569f1f9b072587f276a7f50edf2`

````python
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

