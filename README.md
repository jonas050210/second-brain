# Second Brain — Local AI Knowledge Graph

A **local, private "Second Brain"** that builds a personal knowledge graph
automatically from normal conversation. You just talk to it — it extracts
people, projects, technologies, skills, interests, goals, facts and the
relationships between them, merges duplicates, remembers everything across
sessions, and answers questions from real memory (RAG) without hallucinating.

Everything runs on **your machine**. No cloud AI, no account, no data leaving
your PC.

```
Browser  →  Local Web App  →  Local Backend (FastAPI)  →  Ollama  →  Local SQLite
```

---

## How it works

Every chat message flows through an automatic pipeline:

```
message → memory-control command? → trivial-message filter → LLM extraction (or offline fallback)
       → JSON validation → normalization → duplicate detection → conflict/supersession
       → confidence check → SQLite → knowledge graph + timeline
```

Key ideas:

- **The LLM is replaceable.** Extraction uses `qwen3:0.6b` by default; flip to
  `qwen3:1.7b` (or anything else) in **Settings** — or via environment
  variables — without touching code.
- **Semantic memory** uses `nomic-embed-text` embeddings for vector search.
- **No Ollama? No problem.** The app auto-detects Ollama and otherwise falls
  back to a built-in offline extractor, so it always works.
- **Memory control** — you can steer memory in plain language:
  *"Remember that I prefer Python."*, *"Forget that I am learning Rust."*,
  *"Pin Nebula."*, *"Merge X with Y."*, *"Change my preferred language to Python."*
- **No hallucination** — answers are classified **KNOWN / UNKNOWN / UNCERTAIN**.
  If the brain doesn't know, it says so.
- **Traceability** — every memory links back to its source message and
  conversation, and shows a confidence score.

---

## Requirements

| Tool | Version |
|------|---------|
| Python | 3.11+ |
| Node.js | any recent (only needed if you hack on the frontend) |
| Ollama | optional but recommended |

Your hardware (RTX 4060 Ti 8GB / i7-12700F / 32GB) is more than enough. The app
uses the smallest viable model on purpose and won't consume your whole GPU.

---

## Quick start (Windows 11)

### 1. Install Ollama (recommended)

Download from <https://ollama.com>, then:

```powershell
ollama pull qwen3:0.6b
ollama pull nomic-embed-text
```

(For a more reliable extractor on harder text: `ollama pull qwen3:1.7b` and
switch to it in Settings.)

### 2. Run

```powershell
cd second-brain
python start.py
```

`start.py` is the **primary launcher**. It:

- checks Python 3.11+
- creates `.venv` only if runtime imports are missing
- installs **only** missing packages (never reinstalls on later runs)
- probes Ollama (offline is OK — fallback extractor is used)
- starts the app at **http://localhost:8000**

First-time setup only (same installer, no server):

```powershell
python setup.py
python start.py
```

Diagnostics without starting:

```powershell
python start.py --check
```

`main.py` / `run.py` start the server directly if dependencies are already installed.

### 3. Run the tests

```powershell
python -m pip install pytest httpx
python test_overall.py
```

---

## Configuration

Models and memory behavior are configured in **Settings** (persisted locally),
or via environment variables / a `.env` file (copy `backend/.env.example` to
`.env`):

```bash
OLLAMA_MODEL=qwen3:0.6b        # extraction LLM (try qwen3:1.7b if flaky)
EMBEDDING_MODEL=nomic-embed-text
OLLAMA_BASE_URL=http://localhost:11434
```

Configurable at runtime (Settings UI):

- LLM model, embedding model, Ollama URL
- Extraction confidence threshold
- Duplicate-merge similarity threshold
- Auto-memory on/off

No code changes required to swap models.

---

## Features

- **Chat** — multiple conversations, switcher, last-N context, SSE endpoint;
  assistant replies are always stored (they are never blanked by extraction).
  You see exactly what was remembered (with confidence) as clickable chips.
- **Memory control** — remember / forget / edit / delete / merge / pin / mark
  important / change confidence, all via natural-language commands or the UI.
- **Knowledge Graph** — interactive Cytoscape graph: pan, zoom, search, click,
  hover-highlight, filter by **type / relation / confidence / status / pinned /
  important**, neighborhood expansion (depth), shortest-path, and graph
  statistics. Pinned / important / superseded nodes are visually distinct.
- **Multi-hop retrieval** — RAG traverses relevant graph paths (bounded BFS), so
  *"What technology does the project I'm learning Rust for use?"* chains facts
  instead of only matching one hop.
- **Entity pages** — click any node for type, confidence, aliases, description,
  relationships (with status + confidence), **current vs. superseded history**,
  memory history, source conversation, embedding status, and timestamps.
- **Memory Timeline** — chronological record with sources, filterable by kind,
  entity, and date.
- **Smart Search** — unified keyword + vector (semantic) + graph search with
  grounded, source-attributed answers (KNOWN / UNKNOWN / UNCERTAIN). Results show
  *why* they matched (keyword / semantic / graph / recency) and a clickable
  "Sources used" list.
- **Memory consolidation** — detects clusters of related memories and produces
  entity summaries (deterministic; Ollama only to polish wording). Originals are
  never deleted — summaries reference their source memories.
- **Export / Import** — JSON and Markdown export; import with **merge** or
  **replace** modes and full validation.
- **Backup** — one-click local backups (SQLite copy + JSON + Markdown) with
  status/location shown.
- **Conversation memory** — short-term context is kept separate from long-term
  memory; only durable facts become permanent.
- **Memory decay / conflict detection** — "I stopped learning Rust" supersedes
  the old fact (kept in history, not shown as active); conflicting preferences
  are resolved, never silently duplicated.
- **Dashboard** — entity/relationship/memory/conversation counts, 14-day memory
  growth chart, memory-type breakdown, most-connected entities, recent changes.
- **Privacy** — 100% local by default, clearly labelled.

---

## Memory types

`person`, `project`, `technology`, `topic`, `skill`, `goal`, `interest`,
`preference`, `fact`, `location`, `organization`, `concept`, `task`, `event`.

When confidence is low, information is not forced into a specific category.

---

## Project layout

```
second-brain/
├── start.py               # primary launcher (detect + install missing + run)
├── setup.py               # one-time environment setup
├── main.py                # ASGI / uvicorn entry
├── test_overall.py        # full production test suite
├── requirements.txt
├── ROADMAP
├── run.py                 # thin server alias
├── backend/
│   ├── app.py             # FastAPI routes + serves the UI
│   ├── config.py          # env/config, entity & relation taxonomies
│   ├── db.py              # SQLite schema (versioned migrations) + access
│   ├── ollama.py          # Ollama client (LLM + embeddings)
│   ├── fallback.py        # offline rule-based extractor + hashed embeddings
│   ├── extract.py         # extraction pipeline (LLM prompt + normalization)
│   ├── commands.py        # natural-language memory control
│   ├── store.py           # entities / relationships / merging / supersession
│   ├── search.py          # hybrid search + grounded RAG answers
│   └── requirements.txt
├── frontend/
│   ├── index.html / style.css / app.js   # no build step
│   └── vendor/cytoscape.min.js           # bundled graph library
├── tests/                 # pytest suite (plus Playwright when Chromium is installed)
└── data/brain.db          # your knowledge (created at first run)
```

Backend modules:

- `graph.py` — bounded graph traversal, filtering, neighborhood, shortest path,
  statistics, and multi-hop retrieval.
- `export.py` — JSON/Markdown export + validated merge/replace import.
- `backup.py` — local backups (SQLite online-backup + JSON + Markdown).
- `summarize.py` — memory consolidation (deterministic, originals preserved).

The frontend is plain HTML/CSS/JS served directly by FastAPI — there is no
`npm install` or build step required to run it.
