# Second Brain — Architecture

This is the short technical orientation for contributors and AI agents. The
individual source files are the source of truth; this document intentionally
does not duplicate source code or generated line-number inventories.

## Product boundaries

- One local FastAPI application with a static frontend.
- SQLite is the system of record for entities, relationships, messages,
  conversations, memories, embeddings, and settings.
- Ollama is optional. If its URL points to another machine, user text may leave
  this machine; offline mode uses deterministic local extraction and embeddings.
- There is no telemetry, cloud account, activity capture, screen polling, or
  window-title polling.
- The EXE launcher starts the same `backend.app` used by the Python launcher.
  It is not a second application or a second server implementation.
- History is preserved where possible: superseded facts remain in SQLite.
  Database-level destructive operations—reset, replace, and restore—require
  confirmation and create a local safety backup first.

## Runtime flow

```text
Browser or EXE
  → FastAPI routes in backend/app.py
  → deterministic command handling or question retrieval
  → Ollama extraction plus rule-based fallback for statements
  → validation, normalization, duplicate merge, supersession
  → SQLite persistence
  → graph, timeline, search, grounded answer, and SSE response
```

The graph, dashboard, timeline, and search results are projections of SQLite;
they must not invent entities or relationships. Answers are classified as
known, uncertain, or unknown and are grounded in stored evidence.

## Repository map

### Runtime

- `start.py` — supported Python launcher; checks the environment, optionally
  creates the project virtual environment, probes Ollama, and starts Uvicorn.
- `backend/app.py` — FastAPI app, API models/routes, chat orchestration, SSE,
  and static frontend serving.
- `backend/db.py` — SQLite schema, additive migrations, settings, and integrity
  checks.
- `backend/store.py` — database operations for entities, relationships,
  conversations, messages, memories, merge, and undo.
- `backend/extract.py` — validated Ollama extraction and persistence pipeline.
- `backend/fallback.py` — offline rules, trivial-message filtering, and hashed
  embeddings.
- `backend/search.py` — keyword/vector/graph retrieval and grounded answers.
- `backend/graph.py` — graph traversal, filtering, paths, statistics, and
  explainable ranking.
- `backend/commands.py` — deterministic memory-control commands.
- `backend/export.py` — validated JSON/Markdown export and merge/replace import.
- `backend/backup.py` — local SQLite/JSON/Markdown backups and restore.
- `backend/summarize.py` — deterministic memory and conversation summaries.
- `backend/config.py`, `backend/paths.py`, `backend/ollama.py` — configuration,
  persistent paths, and the optional Ollama client.

### UI and desktop packaging

- `frontend/index.html` — static application shell and view markup.
- `frontend/app.js` — single-page GUI behavior and API calls.
- `frontend/style.css` — UI styling and responsive states.
- `frontend/vendor/cytoscape.min.js` — vendored graph renderer.
- `launcher/` — optional Windows setup GUI, tray actions, icon resolution, and
  PyInstaller bootstrap/build helpers. It launches the existing FastAPI app.
- `main.py` and `run.py` — compatibility wrappers; do not treat them as
  separate applications.
- `secondbrain.spec` — Windows PyInstaller specification.

### Tests and configuration

- `test_overall.py` — production contract and core-loop tests.
- `tests/` — focused tests for API, extraction, search, graph, storage,
  imports/exports, backups, launcher behavior, and the frontend.
- `requirements.txt` — runtime dependencies.
- `backend/requirements-dev.txt` — test, browser-test, and optional build
  dependencies.
- `.env.example` — root configuration template. Runtime settings can also be
  changed through the Settings UI.

## Data-safety rules

- Never delete, reset, or overwrite an existing database during startup.
- Never use a PyInstaller temporary extraction directory or the current working
  directory as an implicit persistent database location.
- Validate a complete import before writing anything.
- Replace, reset, and restore must take a safety snapshot before destructive
  work and must abort if that snapshot fails.
- Do not add automatic activity or screen capture. User-initiated clipboard
  remembering is intentionally the only tray capture action.
- Keep source-message links and timestamps when adding persistence features.

## Development workflow

From the repository root:

```powershell
python -m pip install -r requirements.txt
python -m pip install -r backend/requirements-dev.txt
pytest tests/ test_overall.py -q
```

Browser tests require Playwright and Chromium:

```powershell
python -m playwright install chromium
```

Run the application with:

```powershell
python start.py
```

On Windows, build the optional executable with `python -m launcher.build_exe`.
PyInstaller builds the Windows executable on Windows; the Linux checkout cannot
cross-compile a PE executable.

## Change guidance

1. Read the relevant live module and its focused tests before editing.
2. Preserve the single-app architecture and offline fallback.
3. Add or update tests for behavior changes.
4. Run `node --check frontend/app.js` after JavaScript changes and run the full
   test command above.
5. Update `README.md` when user-visible behavior changes. Keep this document
   focused on stable architecture rather than generated inventories.
