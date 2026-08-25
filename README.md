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
