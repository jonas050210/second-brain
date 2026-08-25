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
multi-hop. If there is no evidence, the answer is UNKNOWN.

---

## Graph

Cytoscape visualization of the real SQLite graph. Pan, zoom, search, type /
relation / confidence / status / pinned / important filters, expand, focus,
edit, delete, merge. No fabricated nodes.

---

## Backup / export / import

- JSON + Markdown export
- Merge import or replace import (replace requires `confirm=true`)
- User relationships are remapped
- Local backups under `data/backups/` (SQLite + JSON + MD)
- Secrets are not exported
- Reset requires confirmation

---

## Privacy

Local-first. No telemetry. No cloud accounts. The only optional network call is
the Ollama URL you configure.

---

## Project layout

```
second-brain/
├── start.py               # primary launcher
├── test_overall.py        # high-level system tests
├── requirements.txt
├── README.md
├── ROADMAP
├── .env.example
├── .gitignore
├── backend/               # FastAPI + SQLite + extract/search/graph
├── frontend/              # static HTML/CSS/JS (no build)
├── tests/
└── data/brain.db          # created on first run
```

---

## Limitations

- Single-user, local only
- Offline extractor is intentionally small; hard phrasing is better with Ollama
- SSE chat emits a completed reply (extraction must finish first)
- Playwright browser tests skip if Chromium is not installed
- Learning several things at once is allowed unless you stop or switch
