# Second Brain — compact project overview

> This is the efficient orientation document for humans and AI agents.
> It describes the live files, symbols, routes, views, and test coverage without
> duplicating every source line. The live files remain the source of truth.

**Generated:** 2026-08-25 17:41 UTC
**Version:** 2.7.0
**Archived source:** `projekt.md` remains the full generated source archive for compatibility.

## Executive summary

Second Brain is one local FastAPI + SQLite application with an optional Ollama
integration. `start.py` is the normal launcher; the EXE bootstraps the same
`backend.app`. SQLite is the source of truth. The GUI is static files served by
the same FastAPI process. When Ollama is unavailable or malformed, deterministic
local extraction and hashed embeddings keep the app usable.

```text
Browser / EXE → FastAPI → SQLite → graph, memory timeline, search/RAG
                              ↘ optional Ollama (qwen3:0.6b / nomic-embed-text)
                              ↘ fallback extractor when offline
```

## Non-negotiable product rules

- Local-first; no cloud account, telemetry, activity capture, screen polling, or window-title polling.
- Never delete, reset, or overwrite a found `brain.db` file; destructive row operations require confirmation and now make a safety snapshot.
- Personal answers are grounded in stored entities, relationships, memories, and sources.
- Default models are `qwen3:0.6b` and `nomic-embed-text`.
- Preserve the existing architecture; no second app, second graph store, or second extractor.

## Runtime flow

1. User message enters `/api/chat` or `/api/chat/stream`.
2. Explicit deterministic command is handled first.
3. Questions use hybrid retrieval and grounded answers.
4. Non-trivial statements go through Ollama JSON extraction plus the rule fallback.
5. Validation removes invented/junk names; entities and relations are normalized.
6. SQLite stores source messages, entities, relationships, timeline memories, and settings.
7. GUI renders the real database: chat, dashboard, graph, browse, memory, search, settings.

## File map and code inventory

### `.env.example`
Documented runtime configuration: default Ollama and embedding models, endpoint, launcher overrides. **19 lines.**
- Configuration/content lines: `OLLAMA_MODEL=qwen3:0.6b`; `EMBEDDING_MODEL=nomic-embed-text`; `OLLAMA_BASE_URL=http://localhost:11434`

### `.gitignore`
Keeps personal databases, caches, virtual environments, and packaged artifacts out of Git. **27 lines.**
- Repository metadata/content file.

### `README.md`
User guide covering setup, privacy, memory behavior, graph, search, backups, and limitations. **278 lines.**
- User-facing operating guide; section headings are the behavior map.

### `ROADMAP`
Product scope: completed capabilities, optional next steps, and explicit non-goals. **80 lines.**
- Completed work, optional next work, and non-goals.

### `backend/.env.example`
Backend-side example configuration matching the root defaults. **12 lines.**
- Configuration/content lines: `OLLAMA_MODEL=qwen3:0.6b`; `EMBEDDING_MODEL=nomic-embed-text`; `OLLAMA_BASE_URL=http://localhost:11434`

### `backend/__init__.py`
Package marker; no runtime behavior. **0 lines.**
- Package/module marker or no top-level symbols.

### `backend/app.py`
FastAPI application, API models/routes, chat orchestration, SSE, static frontend serving. **1440 lines.**
- L46–50 `security_headers()` — app.middleware("http")
- L60–61 `effective_llm_model()`
- L64–65 `effective_embedding_model()`
- L68–69 `auto_memory_enabled()`
- L84–85 `smalltalk_reply()`
- L88–95 `_natural_reply_fallback()`
- L98–116 `_natural_reply_messages()`
- L119–131 `natural_reply()` — A short, grounded acknowledgment (never chain-of-thought).
- L134–149 `natural_reply_stream()`
- L152–154 `build_updates()` — Human-readable change list for the chat + timeline.
- L157–163 `_message_meta()` — Read message metadata defensively; old/corrupt rows must not break UI loads.
- L166–176 `_conversation_id_for_request()` — Resolve an optional chat conversation without creating orphan messages.
- L184–196 `health()` — app.get("/api/health")
- L199–204 `_safe_auto_backup()` — Create a backup only after a memory write. Never called from health.
- L207–217 `_required_safety_backup()` — Take a safety snapshot before a destructive user action.
- L221–226 `models()` — app.get("/api/models")
- L233–235 `ChatIn`
- L239–242 `chat()` — app.post("/api/chat")
- L245–347 `prepare_turn()` — Persist the user turn and run extraction / retrieval. No assistant text yet.
- L350–368 `render_reply()` — Yield reply text. Extraction / retrieval has already finished.
- L371–428 `finalize_turn()`
- L431–436 `_normalize_status()`
- L439–440 `_sse()`
- L448–458 `get_messages()` — app.get("/api/messages")
- L462–469 `get_message()` — app.get("/api/messages/{mid}")
- L473–480 `conversations()` — app.get("/api/conversations")
- L484–486 `conversations_new()` — app.post("/api/conversations/new")
- L489–492 `ConversationPatch`
- L496–513 `conversation_update()` — app.patch("/api/conversations/{cid}")
- L517–522 `conversation_summarize()` — app.post("/api/conversations/{cid}/summarize") — Recap one chat into a summary memory. Messages stay.
- L526–548 `conversation_export()` — app.get("/api/conversations/{cid}/export")
- L552–556 `conversation_delete()` — app.delete("/api/conversations/{cid}")
- L560–574 `conversation_messages()` — app.get("/api/conversations/{cid}/messages")
- L582–583 `graph()` — app.get("/api/graph")
- L587–594 `graph_filter()` — app.get("/api/graph/filter") — Filtered graph view (nodes + edges + stats).
- L598–602 `graph_neighborhood()` — app.get("/api/graph/neighborhood/{eid}")
- L606–608 `graph_path()` — app.get("/api/graph/path")
- L612–613 `graph_stats()` — app.get("/api/graph/stats")
- L617–618 `graph_groups()` — app.get("/api/graph/groups")
- L625–631 `_entity_degree_map()`
- L635–657 `entity_duplicates()` — app.get("/api/entities/duplicates") — Near-duplicate pairs by embedding. Never auto-merges.
- L661–692 `entities()` — app.get("/api/entities")
- L695–705 `_source_for()`
- L709–766 `entity_detail()` — app.get("/api/entities/{eid}")
- L769–784 `_readable_rels()` — Turn relationship rows into readable 'X relation Y' strings (canonical).
- L787–795 `EntityPatch`
- L799–834 `entity_update()` — app.patch("/api/entities/{eid}")
- L838–846 `entity_delete()` — app.delete("/api/entities/{eid}")
- L849–851 `MergeIn`
- L855–859 `entity_merge()` — app.post("/api/entities/merge")
- L862–865 `RelPatch`
- L869–887 `rel_update()` — app.patch("/api/relationships/{rid}")
- L891–895 `rel_delete()` — app.delete("/api/relationships/{rid}")
- L898–902 `RelCreate`
- L906–920 `rel_create()` — app.post("/api/relationships")
- L924–949 `list_facts()` — app.get("/api/facts") — Readable facts (relationships) from the real graph. Never fabricated.
- L957–992 `memories()` — app.get("/api/memories")
- L999–1008 `SearchIn`
- L1012–1026 `do_search()` — app.post("/api/search")
- L1034–1075 `dashboard()` — app.get("/api/dashboard")
- L1078–1079 `_has_demo_data()`
- L1087–1090 `export_json()` — app.get("/api/export/json")
- L1094–1097 `export_markdown()` — app.get("/api/export/markdown")
- L1100–1103 `ImportIn`
- L1107–1130 `do_import()` — app.post("/api/import")
- L1133–1134 `NotesIn`
- L1138–1145 `import_notes()` — app.post("/api/import/notes")
- L1148–1150 `FileIn`
- L1154–1166 `import_file()` — app.post("/api/import/file") — User-initiated text ingest. JSON uses merge import; anything else is notes.
- L1170–1172 `undo_last()` — app.post("/api/undo") — Supersede the last extract. Never deletes the database or history.
- L1180–1181 `do_backup()` — app.post("/api/backup")
- L1185–1186 `backup_status()` — app.get("/api/backup/status")
- L1190–1191 `backups_list()` — app.get("/api/backups")
- L1194–1196 `RestoreIn`
- L1200–1205 `backup_restore()` — app.post("/api/backup/restore")
- L1213–1214 `summarize_candidates()` — app.get("/api/summarize/candidates")
- L1217–1219 `SummarizeIn`
- L1223–1226 `do_summarize()` — app.post("/api/summarize")
- L1234–1257 `get_settings()` — app.get("/api/settings")
- L1260–1268 `SettingsIn`
- L1272–1293 `set_settings()` — app.post("/api/settings")
- L1296–1297 `ResetIn`
- L1301–1312 `reset()` — app.post("/api/reset") — Wipe all data. Requires explicit confirmation.
- L1330–1359 `demo()` — app.post("/api/demo")
- L1363–1376 `demo_clear()` — app.post("/api/demo/clear") — Remove only demo-marked entities and the demo conversation. Real data stays.
- L1380–1419 `chat_stream()` — app.post("/api/chat/stream") — SSE chat. Extraction/retrieval finish first; the reply then streams.
- L1428–1436 `favicon()` — app.get("/favicon.ico") | app.get("/favicon.png")

### `backend/backup.py`
Local SQLite/JSON/Markdown backups, listing, auto-backup status, restore with safety copy. **254 lines.**
- L30–33 `backup_dir()`
- L36–37 `_timestamp()`
- L40–55 `_unique_backup_dir()` — Never reuse or overwrite an existing backup folder.
- L58–100 `create_backup()` — Create a new backup. Returns a status dict.
- L103–115 `_dir_size()`
- L118–139 `list_backups()` — List all backups, newest first.
- L142–153 `backup_status()` — Status of the most recent backup (for the Settings UI).
- L156–166 `resolve_backup_dir()` — Return the absolute backup folder if `name` is a safe local backup.
- L169–170 `auto_backup_hours()`
- L173–181 `auto_backup_status()` — Read-only status. Never writes a backup.
- L184–208 `maybe_auto_backup()` — Create a local backup if the last one is older than the configured interval.
- L211–254 `restore_backup()` — Replace the live database with a named backup.

### `backend/commands.py`
Deterministic chat commands for remember, forget, pin, merge, rename, undo, and corrections. **364 lines.**
- L19–61 `is_command()` — True only for explicit memory-control utterances, not stories.
- L64–97 `_find_entity()` — Resolve an entity by (fuzzy) name: exact, alias, substring, then
- L100–102 `_title()` — Title-case a display name (consistent with entity canonicalization).
- L105–117 `_find_relationship()`
- L120–302 `handle_command()` — Dispatch a memory-control command. Returns a dict with a reply message
- L305–321 `_resolve_this()` — Resolve 'this/it/that' to the most recently touched non-user entity.
- L324–364 `forget_target()` — Forget an entity or a relationship, or supersede a stale fact.

### `backend/config.py`
Environment/database settings, model defaults, limits, entity types, relations, and privacy constants. **168 lines.**
- L16–37 `_load_dotenv()` — Load a local .env if present. Does not override already-set env vars.

### `backend/db.py`
SQLite connection, schema v4, additive migrations, typed settings, integrity check. **237 lines.**
- L119–120 `utcnow()`
- L123–131 `_connect()`
- L134–135 `_columns()`
- L138–155 `init_db()`
- L158–164 `query()`
- L167–169 `query_one()`
- L172–180 `execute()`
- L187–191 `get_setting()`
- L194–199 `set_setting()`
- L202–206 `get_setting_float()`
- L209–215 `get_setting_bool()`
- L218–226 `all_settings()`
- L229–237 `integrity_ok()` — True when SQLite reports a healthy file. Never deletes or rebuilds the DB.

### `backend/export.py`
Validated JSON/Markdown export and merge/replace import with ID/source remapping. **681 lines.**
- L20–23 `_json_default()`
- L26–75 `full_export()` — Serialize the entire knowledge base to a JSON-serializable dict.
- L78–79 `export_json()`
- L82–120 `export_markdown()` — Human-readable Markdown export of the knowledge graph.
- L127–133 `_valid_confidence()`
- L136–139 `_valid_id()`
- L142–150 `_valid_embedding()`
- L153–162 `_valid_json_list()`
- L165–254 `validate_payload()` — Validate an export completely before it touches the database.
- L257–283 `_apply_entity_flags()`
- L289–291 `_clip()`
- L294–296 `_entity_name()`
- L299–341 `_import_entities()`
- L344–405 `_import_relationships()`
- L408–435 `_import_conversations()` — Import conversations and return old-id -> local-id mapping.
- L438–471 `_import_messages()` — Import source messages and return old-id -> local-id mapping.
- L474–514 `_import_memories()`
- L517–544 `_import_summary()`
- L553–574 `_apply_import_settings()` — Restore user-facing settings without restoring session/backup metadata.
- L577–593 `import_merge()` — Merge-import without deleting local data, including source messages.
- L596–627 `import_replace()` — Replace-import: wipe and load while preserving traceable source data.
- L630–637 `import_from_json()`
- L640–656 `split_note_chunks()` — Split pasted notes into extractable paragraphs. Never invents content.
- L659–681 `import_notes()` — Run the existing extractor on each note paragraph. Does not wipe data.

### `backend/extract.py`
Ollama extraction plus deterministic fallback validation, confidence, duplicate and supersession handling. **605 lines.**
- L72–82 `_llm_extract()`
- L85–98 `_parse_json()`
- L101–102 `confidence_threshold()`
- L112–128 `is_junk_entity_name()` — True for empty, stopword, or clause-like names that should never persist.
- L131–154 `mentioned_in_text()` — True if the user's words support this entity name. Never true for inventions.
- L157–175 `calibrate_confidence()` — Bound model-reported confidence using how clearly the name appears.
- L178–181 `_as_dict_list()`
- L184–244 `validate_extraction()` — Drop invented, junk, or malformed extraction rows before persist.
- L247–304 `merge_extractions()` — Union of validated LLM + rule extractions. Rules fill gaps; LLM cannot invent.
- L307–469 `extract()` — Run the full extraction pipeline. Returns a dict summary of updates.
- L472–488 `_resolve_entity()`
- L491–492 `normalize_me()`
- L524–605 `_augment_from_text()` — Add stops (and missing entities) detected deterministically from the text.

### `backend/fallback.py`
Offline rule extractor, technology vocabulary, canonical names, trivial filter, hashed embeddings. **460 lines.**
- L21–34 `fallback_embed()`
- L83–92 `_title_word()`
- L95–105 `canonical_name()` — Turn a lowercased, possibly messy phrase into a clean display name.
- L108–116 `clean_phrase()` — Strip leading/trailing stopwords and trailing 'and'/conjunctions.
- L125–135 `looks_like_item()` — True if a phrase is a short concept name, not a clause.
- L138–146 `split_item_list()` — Split 'Python, Rust, and Go' into items. Ignores clause-like fragments.
- L153–448 `extract_with_rules()`
- L451–460 `is_trivial()` — Heuristic for small-talk that should never enter the brain.

### `backend/graph.py`
Bounded graph traversal, filtering, neighborhood/path queries, statistics, multi-hop facts, ranking. **404 lines.**
- L16–27 `_load_edges()` — Return adjacency lists + edge lookup. Loads relationships only (no
- L30–36 `_entity_map()` — Fetch entity rows for a set of ids.
- L43–74 `neighborhood()` — BFS from an entity up to `depth`. Returns nodes and edges.
- L77–81 `_serialize_nodes()`
- L84–87 `_serialize_edges()`
- L90–142 `graph_view()` — Full graph, or User + N hops when the brain is large enough to clutter.
- L149–183 `shortest_path()` — BFS shortest path between two entities. Returns list of hops or None.
- L190–238 `filter_graph()` — Filter the graph by type / relation / confidence / status / flags.
- L241–269 `graph_stats()` — Graph statistics: counts, distribution, degree.
- L276–323 `multi_hop()` — Bounded BFS from seed entities, collecting the facts encountered along
- L326–334 `group_by_type()` — Group live entities by type for larger-graph navigation.
- L337–404 `explainable_rank()` — Deterministic hybrid ranking with explainable reasons.

### `backend/ollama.py`
Small HTTP client for optional Ollama chat, streaming, model listing, availability, and embeddings. **174 lines.**
- L15–16 `OllamaError`
- L25–31 `get_base_url()` — Runtime-configurable base URL (persisted via Settings).
- L34–38 `_url()`
- L41–65 `available()` — True if Ollama is reachable at the configured base URL.
- L68–79 `list_models()` — Return installed model names, or an empty list when Ollama is offline.
- L82–90 `model_installed()`
- L93–110 `chat()` — Run a chat completion. Returns the assistant's text.
- L113–139 `chat_stream()` — Yield assistant text chunks from a streaming Ollama chat call.
- L142–174 `embed()` — Return an embedding vector (list of floats) for `text`.

### `backend/paths.py`
CWD-independent persistent paths; protects databases from PyInstaller temporary directories. **131 lines.**
- L28–29 `is_frozen()`
- L32–36 `bundle_dir()` — Read-only files shipped with the app (frontend when frozen).
- L39–43 `app_root()` — Persistent application root (never _MEIPASS).
- L46–57 `_user_data_dir()`
- L60–77 `_is_ephemeral()`
- L80–84 `frontend_dir()`
- L87–91 `_existing_db_candidates()`
- L94–99 `_coerce_persistent()` — Make a path absolute against the app root. Reject extract-dir targets.
- L102–121 `resolve_db_path()` — Return the database path. Never points at a temp extract dir.
- L124–131 `ensure_data_dirs()` — Create parent folders only. Never deletes an existing database.

### `backend/requirements-dev.txt`
Repository source file. **5 lines.**
- Configuration/content lines: `pytest>=8.0`; `httpx>=0.27`; `playwright>=1.40   # optional — browser tests (python -m playwright install chromium)`; `pyinstaller>=6.0   # optional — build SecondBrain.exe on Windows`

### `backend/requirements.txt`
Repository source file. **4 lines.**
- Configuration/content lines: `fastapi>=0.110`; `uvicorn[standard]>=0.29`; `requests>=2.31`; `numpy>=1.26`

### `backend/search.py`
Hybrid keyword/vector/graph retrieval, direct grounded answers, sources, filters, and RAG fallback. **1202 lines.**
- L39–44 `detect_intent()`
- L47–50 `_cosine()`
- L53–54 `re_tokenize()`
- L62–70 `query_terms()` — Content tokens for ranking. Keeps short tech names (Go, AI, C#).
- L73–78 `json_loads()`
- L85–96 `vector_search()`
- L103–121 `keyword_search()`
- L128–140 `graph_facts_for_entity()` — Relationships touching an entity, in canonical "s relation t" form.
- L143–208 `intent_facts()` — Graph facts directly matching a question intent (e.g. 'learning').
- L215–224 `_source_for_message()`
- L227–253 `sources_for_facts()` — Build a compact, deduplicated source list for a set of facts/entities.
- L260–343 `search()` — Combined ranking + multi-hop fact retrieval.
- L346–354 `_rank_facts()`
- L357–363 `_is_recent()`
- L366–367 `_recency_boost()`
- L370–401 `_passes_filters()`
- L426–460 `_entity_matches_filters()` — Apply search filters to an entity used by a direct answer.
- L463–496 `_filter_direct_facts()` — Keep facts that have at least one endpoint matching active filters.
- L499–539 `_direct_fact_answer()` — Yes/no questions about a specific stored fact. Never invents.
- L571–591 `_resolve_named_entity()`
- L594–623 `_about_answer()`
- L626–672 `_path_answer()`
- L675–684 `_unknown()`
- L687–702 `_list_intent_answer()` — Direct answers for where I live / who I know / what I prefer.
- L705–726 `_uses_of_answer()`
- L761–784 `_used_by_answer()` — Inverse of uses-of: which stored things use this entity.
- L787–833 `_when_answer()` — Date of the earliest stored fact about a named entity. Never invents.
- L836–860 `_stopped_answer()` — Active history: superseded facts. Never invents.
- L863–887 `_changed_answer()` — Recent superseded / conflict / command memories from the last 7 days.
- L891–911 `_overview_answer()` — Compact grounded recap of active facts. Never invents.
- L914–948 `_count_answer()` — Count stored things. Reads SQLite only.
- L951–992 `retrieve_answer()` — Deterministic retrieval. `final` answers skip the LLM composer.
- L995–1000 `answer()`
- L1003–1016 `_intent_relevant_facts()`
- L1019–1037 `_status_of()`
- L1040–1054 `_knowledge_names()` — Surface forms the composer is allowed to mention.
- L1057–1075 `reply_is_grounded()` — False if the reply names a stored entity or known tech absent from knowledge.
- L1078–1103 `_composer_messages()`
- L1106–1124 `compose_answer()`
- L1127–1147 `compose_answer_stream()` — Yield reply chunks after retrieval. Falls back to one complete chunk.
- L1150–1187 `_fallback_answer()`
- L1190–1202 `is_question()`

### `backend/store.py`
SQLite domain operations for entities, relations, conversations, messages, memories, merge, and undo. **809 lines.**
- L19–26 `normalize_name()` — Lowercase, collapse whitespace, strip surrounding punctuation.
- L29–30 `normalize_type()`
- L33–39 `normalize_relation()` — Return (canonical_relation, swap) for a raw relation label.
- L42–45 `vec_to_json()`
- L48–59 `vec_from_json()` — Decode a stored embedding without letting corrupt rows break the app.
- L66–86 `embed_text()` — Embed text using Ollama if available, else the fallback hasher.
- L89–90 `merge_similarity_threshold()`
- L97–110 `ensure_user_entity()` — Create the special 'User' entity if it does not exist yet.
- L113–114 `find_entity_by_name()`
- L117–131 `create_entity()`
- L134–167 `update_entity()`
- L170–178 `_cosine()`
- L181–213 `find_duplicate()` — Find an existing entity that this one should merge into.
- L216–245 `upsert_entity()` — Insert or merge an entity. Returns (entity_id, created_bool).
- L248–319 `merge_entities()` — Merge `drop_id` into `keep_id` without losing conflicting links.
- L322–323 `delete_entity()`
- L326–327 `set_entity_status()`
- L330–337 `toggle_entity_flag()`
- L340–342 `set_confidence()`
- L345–346 `entity_row()`
- L349–350 `all_entities()`
- L353–380 `similar_entities()` — Near-duplicates by embedding. Never auto-merges; the UI can suggest Merge.
- L387–410 `add_relationship()`
- L413–417 `relationship_exists()`
- L420–425 `relationship_active()`
- L428–436 `supersede_relationship()` — Mark a matching active relationship as superseded. Returns count changed.
- L439–452 `supersede_relations_of_type()` — Supersede all active `relation` links from `source_id` (optionally
- L455–478 `update_relationship()` — Update relation label, confidence, or status. Never deletes the row.
- L481–482 `delete_relationship()`
- L485–488 `all_relationships()`
- L491–492 `relationship_row()`
- L499–507 `create_conversation()`
- L510–518 `touch_conversation()`
- L521–522 `conversation_row()`
- L525–526 `all_conversations()`
- L529–534 `_like_pattern()`
- L537–591 `conversation_summaries()` — List conversations with counts/previews. Optional title+message search.
- L594–603 `current_conversation_id()`
- L606–609 `new_conversation()`
- L612–624 `conversation_messages()` — Return messages in chronological order. `limit` means the last N turns.
- L627–634 `delete_conversation()` — Delete a conversation and its messages. Long-term memories stay.
- L641–648 `add_memory()`
- L651–652 `recent_memories()`
- L655–667 `memories_for_entity()`
- L674–683 `add_message()`
- L686–687 `messages()`
- L690–691 `message_by_id()`
- L697–717 `_read_undo_stack()` — Newest first. Migrates the single last_extract setting if needed.
- L720–726 `_write_undo_stack()`
- L729–730 `undo_available()`
- L733–735 `clear_undo_stack()` — Discard undo metadata after a reset or database replacement.
- L738–770 `record_last_extract()` — Push this extract onto the undo stack. Never deletes rows.
- L773–808 `undo_last_extract()` — Supersede relationships from the newest extract. Entities stay in history.

### `backend/summarize.py`
Deterministic memory/conversation summaries with optional grounded Ollama wording polish. **205 lines.**
- L19–49 `find_consolidation_candidates()` — Find clusters of memories that share an entity and are ripe for
- L52–64 `_already_summarized()` — Avoid re-summarizing a cluster that a summary already references.
- L67–118 `summarize_entity()` — Generate a summary for an entity. Returns the created summary memory.
- L121–135 `store_relationships_readable()` — Readable active relationships for an entity (canonical direction).
- L138–149 `_summary_is_grounded()` — False if the polish invents a stored entity name not in this summary.
- L152–195 `summarize_conversation()` — Write a recap memory for one chat. Never deletes messages.
- L198–205 `summarize_all()` — Summarize the top consolidation candidates. Returns a list of results.

### `frontend/app.js`
Single-page GUI controller: navigation, chat/SSE, dashboard, graph, entities, memory, search, settings. **1861 lines.**
- L6 `$()` — GUI behavior/function.
- L7 `$$()` — GUI behavior/function.
- L17 `esc()` — GUI behavior/function.
- L22 `api()` — GUI behavior/function.
- L35 `toast()` — GUI behavior/function.
- L50 `badge()` — GUI behavior/function.
- L54 `fmtTime()` — GUI behavior/function.
- L58 `fmtDay()` — GUI behavior/function.
- L71 `parseHash()` — GUI behavior/function.
- L72 `raw()` — GUI behavior/function.
- L77 `setHash()` — GUI behavior/function.
- L84 `showView()` — GUI behavior/function.
- L104 `runViewLoad()` — GUI behavior/function.
- L111 `applyRoute()` — GUI behavior/function.
- L134 `refreshStatus()` — GUI behavior/function.
- L160 `loadDashboard()` — GUI behavior/function.
- L232 `scrollChat()` — GUI behavior/function.
- L237 `rememberChips()` — GUI behavior/function.
- L252 `sourceChips()` — GUI behavior/function.
- L258 `attachChips()` — GUI behavior/function.
- L264 `appendMessage()` — GUI behavior/function.
- L314 `parseSseBuffer()` — GUI behavior/function.
- L330 `sendChat()` — GUI behavior/function.
- L355 `finish()` — GUI behavior/function.
- L495 `loadConversations()` — GUI behavior/function.
- L499 `q()` — GUI behavior/function.
- L600 `renameConversation()` — GUI behavior/function.
- L609 `done()` — GUI behavior/function.
- L624 `openConversation()` — GUI behavior/function.
- L640 `loadChatHistory()` — GUI behavior/function.
- L653 `initGraph()` — GUI behavior/function.
- L733 `buildLegend()` — GUI behavior/function.
- L748 `applyTypeFilter()` — GUI behavior/function.
- L756 `buildGraph()` — GUI behavior/function.
- L785 `populateFilterDropdowns()` — GUI behavior/function.
- L786 `types()` — GUI behavior/function.
- L787 `rels()` — GUI behavior/function.
- L788 `fill()` — GUI behavior/function.
- L801 `loadBrowse()` — GUI behavior/function.
- L830 `applyGraphFilters()` — GUI behavior/function.
- L859 `runGraphLayout()` — GUI behavior/function.
- L861 `name()` — GUI behavior/function.
- L894 `applyConnectedFilter()` — GUI behavior/function.
- L932 `pathToUser()` — GUI behavior/function.
- L942 `showGraphPath()` — GUI behavior/function.
- L959 `expandSelectedNeighborhood()` — GUI behavior/function.
- L1010 `loadMemory()` — GUI behavior/function.
- L1072 `doSearch()` — GUI behavior/function.
- L1143 `openEntity()` — GUI behavior/function.
- L1149 `closeEntity()` — GUI behavior/function.
- L1157 `openSource()` — GUI behavior/function.
- L1173 `loadEntity()` — GUI behavior/function.
- L1201 `aliases()` — GUI behavior/function.
- L1346 `saveAliases()` — GUI behavior/function.
- L1358 `name()` — GUI behavior/function.
- L1360 `next()` — GUI behavior/function.
- L1396 `name()` — GUI behavior/function.
- L1424 `openMerge()` — GUI behavior/function.
- L1441 `render()` — GUI behavior/function.
- L1464 `loadSettings()` — GUI behavior/function.
- L1475 `hours()` — GUI behavior/function.
- L1547 `downloadBlob()` — GUI behavior/function.
- L1568 `formatImportReport()` — GUI behavior/function.
- L1627 `text()` — GUI behavior/function.
- L1647 `loadBackupStatus()` — GUI behavior/function.
- L1680 `loadSummarizeCandidates()` — GUI behavior/function.
- L1710 `closePalette()` — GUI behavior/function.
- L1717 `openPalette()` — GUI behavior/function.
- L1729 `renderPalette()` — GUI behavior/function.
- L1733 `query()` — GUI behavior/function.
- L1744 `convHits()` — GUI behavior/function.
- L1757 `choosePalette()` — GUI behavior/function.
- L1787 `showDuplicatePairs()` — GUI behavior/function.
- L1810 `tag()` — GUI behavior/function.
- L1833 `bootStep()` — GUI behavior/function.
- L1842 `boot()` — GUI behavior/function.

### `frontend/index.html`
Single static HTML shell containing all views, controls, overlays, and accessible navigation labels. **470 lines.**
- View: DASHBOARD
- View: CHAT
- View: GRAPH
- View: ENTITIES
- View: MEMORY
- View: SEARCH
- View: SETTINGS
- DOM contracts: `#status-indicator`, `#privacy-badge`, `#model-line`, `#view-dashboard`, `#demo-banner`, `#stats-grid`, `#growth-chart`, `#type-breakdown`, `#recent-memories`, `#top-entities`, `#view-chat`, `#chat-undo`, `#chat-new`, `#conv-search`, `#conv-archived`, `#conv-list`, `#chat-scroll`, `#chat-empty`, `#chat-messages`, `#chat-input`, `#chat-send`, `#view-graph`, `#graph-sub`, `#graph-search`, `#graph-reset`, `#gf-type`, `#gf-relation`, `#gf-superseded`, `#gf-pinned`, `#gf-important`, `#gf-conf-val`, `#gf-confidence`, `#gf-layout`, `#gf-connected`, `#gf-around-me`, `#graph-apply`, `#graph-legend`, `#graph-zoom-in`, `#graph-zoom-out`, `#graph-fit`, `#graph-expand`, `#graph-path`, `#graph-to-me`, `#cy`, `#view-browse`, `#browse-q`, `#browse-type`, `#browse-pinned`, `#browse-important`, `#browse-sort`, `#browse-orphans`, `#browse-dupes`, `#browse-list`, `#view-memory`, `#mem-kind`, `#mem-entity`, `#mem-q`, `#mem-date`, `#mem-clear`, `#timeline`, `#view-search`, `#search-input`, `#search-btn`, `#sf-type`, `#sf-confidence`, `#sf-status`, `#sf-pinned`, `#sf-important`, `#sf-from`, `#sf-to`, `#sf-source`, `#search-answer`, `#search-sources`, `#search-results`, `#view-settings`, `#set-llm`, `#set-emb`, `#set-ollama-url`, `#set-save`, `#set-hint`, `#conf-val`, `#set-confidence`, `#merge-val`, `#set-merge`, `#set-auto-memory`, `#set-auto-backup`, `#set-theme`, `#set-behavior-save`, `#privacy-info`, `#ollama-info`, `#db-path`, `#reset-btn`, `#demo-btn`, `#demo-clear-btn`, `#summarize-all`, `#summarize-status`, `#summarize-candidates`, `#export-json`, `#export-md`, `#import-data`, `#import-merge`, `#import-replace`, `#import-status`, `#import-notes`, `#import-notes-btn`, `#import-file`, `#backup-now`, `#backup-status`, `#backup-list`, `#entity-overlay`, `#entity-panel`, `#entity-inner`, `#palette-overlay`, `#palette`, `#palette-input`, `#palette-results`, `#toast`

### `frontend/style.css`
Dark/light responsive UI styling, graph/chat layouts, loading/error states, focus states, reduced motion. **621 lines.**
- L57 — animated background orbs
- L71 — sidebar
- L122 — main
- L132 — panels / cards
- L145 — dashboard
- L181 — type badges
- L192 — buttons / inputs
- L243 — chat
- L285 — graph
- L300 — timeline
- L317 — search
- L328 — settings form
- L333 — entity slide-over
- L359 — toast
- L369 — merge modal

### `frontend/vendor/cytoscape.min.js`
Vendored Cytoscape.js renderer used for the graph; not application logic. **32 lines.**
- Vendored JavaScript dependency; application does not modify its internals.

### `launcher/__init__.py`
Launcher package metadata/helpers. **7 lines.**
- Package/module marker or no top-level symbols.

### `launcher/__main__.py`
Desktop/EXE entry point that bootstraps and starts the existing FastAPI app. **107 lines.**
- L29–37 `_already_running()`
- L40–103 `main()`

### `launcher/bootstrap.py`
Idempotent launcher checks: dependencies, persistent DB, Ollama, models, health, server. **310 lines.**
- L44–50 `StepResult`
- L56–58 `_emit()`
- L61–68 `_missing_imports()`
- L71–80 `_model_present()`
- L83–95 `probe_ollama()`
- L98–104 `port_free()`
- L107–125 `prepare_environment()` — Resolve and export the persistent DB path before backend import.
- L128–276 `run_bootstrap()` — Run lightweight, idempotent checks. Returns one result per step.
- L279–280 `bootstrap_ok()`
- L283–289 `create_server()` — Build a uvicorn.Server around the existing FastAPI app.
- L292–294 `start_existing_app()` — Start the existing FastAPI app. Not a second server implementation.
- L297–310 `wait_for_http()`

### `launcher/build_exe.py`
Windows PyInstaller build command for the existing launcher. **54 lines.**
- L17–50 `main()`

### `launcher/gui.py`
Optional setup window for bootstrap progress, browser open, tray, and quit controls. **432 lines.**
- L34–39 `tk_available()`
- L42–63 `apply_window_icon()` — Set the setup-window icon when the PNG/ICO shipped with the EXE exists.
- L66–87 `native_alert()` — Visible alert when there is no console (windowed EXE).
- L90–332 `SetupWindow`
- L91–198 `SetupWindow.__init__()`
- L200–204 `SetupWindow._open_browser()`
- L206–212 `SetupWindow._hide_to_tray()` — Hide the setup window. Tray does not watch the desktop.
- L214–219 `SetupWindow._show_window()`
- L221–244 `SetupWindow._on_close()`
- L246–258 `SetupWindow.set_progress()`
- L260–270 `SetupWindow.append_log()`
- L272–285 `SetupWindow.set_ollama()`
- L287–315 `SetupWindow.succeed()`
- L317–329 `SetupWindow.fail()`
- L331–332 `SetupWindow.run()`
- L335–357 `_run_headless()`
- L360–432 `run_gui_bootstrap()` — Show the window, run checks, then keep the existing app alive.

### `launcher/icons.py`
Resolves packaged/source icon paths. **36 lines.**
- L12–22 `_candidates()`
- L25–29 `icon_ico()`
- L32–36 `icon_png()`

### `launcher/secondbrain.ico`
Windows application icon. Binary, 147587 bytes, SHA256 prefix `6399bb5dd9171bb2`.

### `launcher/secondbrain.png`
PNG application/setup icon. Binary, 48109 bytes, SHA256 prefix `bca342072df70b8b`.

### `launcher/tray.py`
Optional click-only tray actions; explicitly contains no activity/window/screen watcher. **267 lines.**
- L31–33 `should_watch_activity()` — Always False. Auto-capture of the desktop is not a feature.
- L36–43 `clip_remember_text()` — Return clipboard text worth sending, or None if empty.
- L46–60 `post_remember()` — POST clipboard text into the existing chat/extract pipeline.
- L63–100 `read_clipboard()` — Best-effort clipboard read. Empty string if unavailable.
- L103–262 `TrayController` — Holds callbacks the GUI wires up. No background activity sampling.
- L106–113 `TrayController.__init__()`
- L115–122 `TrayController.remember_clipboard()`
- L124–134 `TrayController.start()` — Start a Windows tray icon if possible. Never starts an activity poll.
- L136–137 `TrayController.stop()`
- L139–144 `TrayController._win_loop()` — Best-effort NotifyIcon. Failures are silent; the setup window remains.
- L146–244 `TrayController._win_notify()`
- L246–262 `TrayController._popup()`
- L265–267 `kernel32_instance()`

### `main.py`
Compatibility entry point delegating to the existing launcher. **29 lines.**
- L20–25 `main()`

### `pytest.ini`
Pytest discovery and warning configuration. **4 lines.**
- Repository metadata/content file.

### `requirements.txt`
Runtime dependencies: FastAPI, Uvicorn, requests, and NumPy. **6 lines.**
- Configuration/content lines: `fastapi>=0.110`; `uvicorn[standard]>=0.29`; `requests>=2.31`; `numpy>=1.26`

### `run.py`
Small compatibility runner for the existing app. **8 lines.**
- Package/module marker or no top-level symbols.

### `secondbrain.spec`
PyInstaller specification embedding the existing backend, frontend, launcher, and icon. **94 lines.**
- Repository metadata/content file.

### `start.py`
Primary Python launcher: checks Python, installs only missing runtime packages, probes Ollama, starts Uvicorn. **281 lines.**
- L40–41 `is_windows()`
- L44–47 `venv_python()`
- L50–61 `running_in_project_venv()`
- L64–71 `check_python()`
- L74–81 `missing_runtime()`
- L84–95 `install_packages()`
- L98–111 `ensure_venv()`
- L114–121 `reexec_in_venv_if_needed()`
- L124–126 `create_dirs()`
- L129–135 `verify_imports()`
- L138–153 `setup_only()`
- L156–165 `detect_environment()`
- L168–178 `probe_ollama()`
- L181–198 `print_env()`
- L201–221 `start_server()`
- L224–277 `main()`

### `test_overall.py`
End-to-end contract suite for startup, chat, memory, graph, search/RAG, API, frontend, and safety. **498 lines.**
- L54–61 `fresh_db()`
- L65–66 `client()`
- L73–78 `test_startup_modules_importable()`
- L81–86 `test_start_check_succeeds_in_ready_env()`
- L89–95 `test_frontend_assets_present()`
- L98–110 `test_root_contract_files_exist()`
- L117–125 `test_database_schema_and_user_entity()`
- L128–131 `test_persistence_survives_reinit()`
- L138–139 `test_ollama_availability_is_boolean()`
- L142–147 `test_fallback_embedding_and_extractor()`
- L150–153 `test_trivial_filter()`
- L160–167 `test_extract_creates_entities_relationships_and_memories()`
- L170–177 `test_source_message_id_on_memories_and_entities()`
- L180–184 `test_duplicate_detection_no_second_python()`
- L187–199 `test_switch_supersedes_old_learning()`
- L202–214 `test_exclusive_lives_in_supersedes()`
- L217–231 `test_remember_command_without_that()`
- L234–237 `test_important_command_modifies_db()`
- L240–264 `test_all_memory_commands_modify_db()`
- L271–276 `test_graph_is_real_data_not_fabricated()`
- L279–286 `test_graph_neighborhood_and_path()`
- L293–301 `test_hybrid_search_and_multihop_rag()`
- L304–308 `test_unknown_does_not_hallucinate()`
- L311–315 `test_superseded_excluded_from_active_learning()`
- L322–337 `test_consolidation_preserves_originals()`
- L340–356 `test_export_includes_facts_and_import_maps_user()`
- L359–361 `test_import_rejects_invalid_payload()`
- L364–370 `test_backup_is_local_and_real()`
- L373–380 `test_reset_keeps_only_user()`
- L387–394 `test_health_and_settings_and_privacy()`
- L397–403 `test_chat_persists_assistant_reply()`
- L406–412 `test_chat_stream_endpoint()`
- L415–418 `test_facts_endpoint()`
- L421–443 `test_frontend_served()`
- L446–474 `test_core_loop_chat_memory_graph_search_rag()` — The production contract: talk → remember → graph → retrieve.
- L477–482 `test_dashboard_uses_real_counts()`
- L489–494 `main()`

### `tests/conftest.py`
Isolated temporary SQLite fixture and deterministic Ollama/offline fixtures. **78 lines.**
- L22–36 `fresh_db()` — Recreate the schema and User entity before every test.
- L40–44 `no_ollama()` — Force the offline (rule-based) path for deterministic tests.
- L48–78 `fake_ollama()` — Simulate an available Ollama with a deterministic JSON extraction.

### `tests/test_api.py`
Repository source file. **464 lines.**
- L16–17 `client()`
- L20–23 `test_health()`
- L26–31 `test_chat_creates_memory()`
- L34–37 `test_chat_trivial_no_memory()`
- L40–42 `test_chat_command()`
- L45–48 `test_question_answer()`
- L51–56 `test_graph_endpoint()`
- L59–66 `test_entities_list_and_detail()`
- L69–78 `test_entity_patch_and_delete()`
- L81–86 `test_merge_endpoint()`
- L89–92 `test_memories_timeline()`
- L95–99 `test_search_endpoint()`
- L102–103 `test_search_rejects_empty_query()`
- L106–111 `test_dashboard()`
- L114–116 `test_settings_rejects_non_http_ollama_url()`
- L119–126 `test_settings_roundtrip()`
- L129–131 `test_reset_requires_confirmation()`
- L134–143 `test_reset()`
- L146–155 `test_reset_does_not_wipe_if_safety_backup_fails()`
- L158–161 `test_conversations()`
- L164–170 `test_chat_rejects_unknown_conversation_without_orphaning_message()`
- L173–177 `test_stream_rejects_unknown_conversation_before_opening_sse()`
- L180–187 `test_entity_rename_validation()`
- L190–191 `test_unknown_relationship_delete_is_404()`
- L194–198 `test_ollama_offline_fallback()`
- L201–205 `test_demo_endpoint()`
- L208–217 `test_relationship_patch()`
- L220–224 `test_security_headers_present()`
- L227–237 `test_create_relationship_endpoint()`
- L240–248 `test_import_notes_extracts_paragraphs()`
- L251–256 `test_health_reports_version()`
- L259–266 `test_graph_groups_endpoint()`
- L269–272 `test_auto_backup_setting_roundtrip()`
- L275–282 `test_chat_stream_emits_token_after_extract()`
- L285–288 `test_import_rejects_oversized_payload()`
- L291–300 `test_conversation_search_by_message_body()`
- L303–314 `test_graph_focus_user_hides_islands()`
- L317–320 `test_settings_reports_db_ok_and_no_activity_watch()`
- L323–331 `test_entities_sort_degree()`
- L334–339 `test_entity_detail_includes_similar()`
- L342–355 `test_undo_last_extract_supersedes()`
- L358–374 `test_undo_stack_two_extracts()`
- L377–390 `test_conversation_pin_and_archive()`
- L393–401 `test_import_file_notes()`
- L404–410 `test_entity_aliases_roundtrip()`
- L413–418 `test_memories_text_search()`
- L421–427 `test_entities_orphans_filter()`
- L430–440 `test_conversation_summarize_endpoint()`
- L443–449 `test_conversation_export_markdown()`
- L452–455 `test_favicon_served()`
- L458–464 `test_chat_empty_and_huge_payload()`

### `tests/test_api_phase3.py`
Repository source file. **182 lines.**
- L12–13 `client()`
- L16–18 `_seed()`
- L21–25 `test_graph_filter_endpoint()`
- L28–34 `test_graph_neighborhood_endpoint()`
- L37–43 `test_graph_path_endpoint()`
- L46–50 `test_graph_stats_endpoint()`
- L53–58 `test_export_json_endpoint()`
- L61–65 `test_export_markdown_endpoint()`
- L68–73 `test_import_merge_endpoint()`
- L76–84 `test_replace_import_creates_safety_backup()`
- L87–89 `test_import_invalid_rejected()`
- L92–100 `test_backup_endpoint()`
- L103–115 `test_backup_restore_endpoint()`
- L118–122 `test_summarize_candidates_endpoint()`
- L125–131 `test_search_with_filters_endpoint()`
- L134–139 `test_search_returns_sources_and_reasons()`
- L142–146 `test_facts_endpoint()`
- L149–158 `test_conversation_rename_and_delete()`
- L161–164 `test_privacy_in_settings()`
- L167–172 `test_chat_stream()`
- L175–182 `test_entity_history_endpoint()`

### `tests/test_backup.py`
Repository source file. **97 lines.**
- L7–13 `test_create_backup()`
- L16–23 `test_backup_list_and_status()`
- L26–34 `test_backup_contains_real_data()`
- L37–43 `test_restore_requires_confirmation()`
- L46–50 `test_restore_rejects_path_traversal()`
- L53–64 `test_restore_roundtrip_preserves_memories()`
- L67–77 `test_health_does_not_create_backup()`
- L80–87 `test_maybe_auto_backup_skips_empty_and_fresh()`
- L90–97 `test_no_secrets_in_backup()`

### `tests/test_commands.py`
Repository source file. **191 lines.**
- L5–26 `test_remember_command_recognized()`
- L29–38 `test_forget_supersedes_learning()`
- L41–47 `test_forget_removes_entity()`
- L50–54 `test_pin_command()`
- L57–61 `test_unpin_command()`
- L64–68 `test_mark_important()`
- L71–76 `test_merge_command()`
- L79–83 `test_rename_command()`
- L86–97 `test_preference_change_supersedes_old()`
- L100–104 `test_set_confidence_command()`
- L107–108 `test_unknown_command_returns_none()`
- L111–115 `test_remember_without_that_is_remember_action()`
- L118–122 `test_important_command()`
- L125–130 `test_unimportant_command()`
- L133–142 `test_forget_prefer_supersedes_not_deletes()`
- L145–156 `test_forget_live_in_supersedes()`
- L159–184 `test_undo_last_command()`
- L187–191 `test_stop_remembering_forgets_entity()`

### `tests/test_export.py`
Repository source file. **191 lines.**
- L7–9 `_seed()`
- L12–19 `test_json_export_shape()`
- L22–31 `test_json_export_roundtrip_merge()`
- L34–40 `test_markdown_export()`
- L43–45 `test_import_validation_rejects_garbage()`
- L48–50 `test_import_validation_rejects_wrong_format()`
- L53–55 `test_import_validation_rejects_missing_keys()`
- L58–68 `test_import_merge_adds_new_entities()`
- L71–86 `test_import_replace_wipes_and_loads()`
- L89–98 `test_import_preserves_relationships()`
- L101–106 `test_export_includes_status_and_confidence()`
- L109–113 `test_export_includes_facts()`
- L116–127 `test_replace_import_restores_user_relationships()`
- L130–135 `test_note_chunk_split_and_import()`
- L138–158 `test_replace_import_preserves_source_messages_and_conversation()`
- L161–191 `test_import_merge_reports_exclusive_conflict_and_skips()`

### `tests/test_extraction.py`
Repository source file. **270 lines.**
- L7–8 `_run()`
- L11–16 `test_trivial_filtering()`
- L19–25 `test_extract_learning()`
- L28–35 `test_extract_project_uses()`
- L38–43 `test_no_duplicate_on_repeat()`
- L46–49 `test_preference_relation()`
- L52–68 `test_prefer_instead_does_not_create_junk_entity()`
- L71–74 `test_location_relation()`
- L77–81 `test_confidence_recorded()`
- L84–90 `test_source_message_tracking()`
- L93–103 `test_stopped_creates_supersession()`
- L106–110 `test_switched_detects_conflict()`
- L113–118 `test_embedding_stored()`
- L121–124 `test_memory_events_written()`
- L127–133 `test_multiword_concepts_not_trimmed()`
- L136–143 `test_junk_clause_is_not_an_entity()`
- L146–153 `test_relearn_after_stop_is_remembered()`
- L156–161 `test_list_learning_extracts_each_item()`
- L164–168 `test_work_on_creates_project()`
- L171–176 `test_skill_extraction()`
- L179–183 `test_mentioned_in_text_rejects_inventions()`
- L186–209 `test_llm_invented_facts_rejected()`
- L212–228 `test_merge_llm_with_fallback_fills_gaps()`
- L231–246 `test_correction_meant_not()`
- L249–253 `test_large_input_does_not_crash()`
- L256–260 `test_malformed_llm_json_falls_back()`
- L263–270 `test_confidence_threshold_respected()`

### `tests/test_frontend.py`
Repository source file. **173 lines.**
- L23–30 `browser()`
- L34–38 `page()`
- L41–44 `_seed_empty()` — Reset the database so tests start from a clean slate.
- L47–49 `_wait_boot()` — Wait for the async boot() to finish (dashboard becomes active/populated).
- L52–56 `test_dashboard_loads()`
- L59–68 `test_chat_sends_message_and_memory_update()`
- L71–81 `test_entity_can_be_opened()`
- L84–97 `test_graph_updates()`
- L100–112 `test_search_works()`
- L115–152 `test_entity_browser_and_palette_markup()`
- L155–162 `test_settings_load()`
- L165–173 `test_reset_confirmation()`

### `tests/test_graph.py`
Repository source file. **147 lines.**
- L6–9 `_seed()`
- L12–18 `test_neighborhood_depth_one()`
- L21–26 `test_neighborhood_depth_two()`
- L29–34 `test_neighborhood_relation_filter()`
- L37–44 `test_shortest_path()`
- L47–51 `test_shortest_path_none_for_disconnected()`
- L54–57 `test_filter_graph_by_type()`
- L60–63 `test_filter_graph_by_relation()`
- L66–69 `test_filter_graph_min_confidence()`
- L72–78 `test_filter_graph_superseded_excluded()`
- L81–85 `test_filter_graph_pinned()`
- L88–94 `test_graph_stats()`
- L97–104 `test_multi_hop_collects_connected_facts()`
- L107–113 `test_multi_hop_respects_depth_limit()`
- L116–121 `test_group_by_type()`
- L124–129 `test_explainable_rank()`
- L132–147 `test_graph_auto_focus_user_neighborhood()`

### `tests/test_launcher.py`
Repository source file. **248 lines.**
- L28–31 `test_resolve_db_honors_env()`
- L34–45 `test_relative_env_db_is_not_cwd_based()`
- L48–56 `test_existing_db_wins_over_empty_default()`
- L59–72 `test_never_uses_meipass_for_db()`
- L75–88 `test_frozen_prefers_existing_portable_db()`
- L91–98 `test_spaces_in_path()`
- L101–106 `test_ensure_data_dirs_does_not_delete_db()`
- L109–118 `test_bootstrap_preserves_existing_memories()`
- L121–133 `test_second_bootstrap_does_not_install()`
- L136–156 `test_missing_dependency_installs_only_that_package()`
- L159–168 `test_ollama_offline_does_not_fail()`
- L171–184 `test_ollama_online_models_present_no_pull()`
- L187–196 `test_missing_models_not_downloaded_by_default()`
- L199–212 `test_cwd_does_not_change_db()`
- L215–228 `test_bootstrap_never_calls_reset()`
- L231–235 `test_bootstrap_emits_required_status_titles()`
- L238–241 `test_headless_check_entrypoint()`
- L244–248 `test_create_server_uses_existing_app()`

### `tests/test_migration.py`
Repository source file. **80 lines.**
- L8–44 `_build_v2_db()` — Create a schema-v2 database (pre-`memories.meta`) with one memory row.
- L47–67 `test_migration_v2_to_v3()`
- L70–80 `test_migration_idempotent()` — Running init_db() twice must not error or duplicate columns.

### `tests/test_ollama.py`
Repository source file. **97 lines.**
- L11–17 `test_llm_extraction_entities_and_relationships()`
- L20–36 `test_llm_extraction_stops()`
- L39–47 `test_model_switching_via_settings()`
- L50–58 `test_embedding_model_switching()`
- L61–63 `test_offline_fallback_used()`
- L66–73 `test_llm_failure_falls_back_to_rules()`
- L76–90 `test_malformed_ollama_responses_are_offline_safe()`
- L93–97 `test_malformed_ollama_url_is_offline_safe()`

### `tests/test_reliability.py`
Repository source file. **69 lines.**
- L9–10 `test_integrity_ok_on_healthy_file()`
- L13–20 `test_integrity_ok_false_on_garbage_does_not_rebuild()`
- L23–27 `test_import_rejects_non_object_and_wrong_types()`
- L30–37 `test_conversation_summaries_escape_like_wildcards()`
- L40–51 `test_invalid_import_is_rejected_before_any_write()`
- L54–61 `test_corrupt_embeddings_are_ignored_by_search()`
- L64–69 `test_shortest_path_honors_depth_limit()`

### `tests/test_search.py`
Repository source file. **240 lines.**
- L5–7 `_seed()`
- L10–13 `test_keyword_search_finds_exact()`
- L16–19 `test_vector_search_returns_results()`
- L22–25 `test_hybrid_search_combines_signals()`
- L28–32 `test_answer_known()`
- L35–41 `test_answer_unknown_no_hallucination()`
- L44–48 `test_answer_learning_intent()`
- L51–56 `test_answer_preference_intent()`
- L59–62 `test_intent_detection()`
- L65–71 `test_superseded_facts_not_in_active_search()`
- L74–79 `test_graph_facts_for_entity()`
- L82–86 `test_is_question()`
- L89–94 `test_tell_me_about_entity()`
- L97–101 `test_path_question()`
- L104–108 `test_yes_no_unknown_when_relation_missing()`
- L111–115 `test_yes_no_known_when_fact_exists()`
- L118–124 `test_pinned_entity_gets_reason()`
- L127–130 `test_short_name_keyword_go()`
- L133–137 `test_where_do_i_live_direct()`
- L140–144 `test_what_does_project_use_direct()`
- L147–152 `test_ambiguous_unknown_stays_unknown()`
- L155–160 `test_compose_drops_invented_tech()`
- L163–167 `test_works_at_intent()`
- L170–176 `test_what_did_i_stop_reads_superseded()`
- L179–184 `test_what_changed_this_week()`
- L187–192 `test_who_uses_named_entity()`
- L195–200 `test_when_did_i_start_learning()`
- L203–209 `test_what_do_i_know_overview()`
- L212–216 `test_how_many_projects()`
- L219–226 `test_search_filters_apply_to_facts_and_direct_answers()`
- L229–240 `test_compose_answer_rejects_ungrounded()`

### `tests/test_search_advanced.py`
Repository source file. **91 lines.**
- L6–9 `_seed()`
- L12–20 `test_multi_hop_question()`
- L23–28 `test_sources_attributed()`
- L31–35 `test_sources_openable_entity()`
- L38–42 `test_reasons_explainable()`
- L45–49 `test_superseded_excluded_from_facts()`
- L52–56 `test_confidence_filter()`
- L59–62 `test_type_filter()`
- L65–69 `test_unknown_still_protected()`
- L72–77 `test_uncertain_wording()`
- L80–84 `test_uses_of_named_project()`
- L87–91 `test_recency_boost_present()`

### `tests/test_store.py`
Repository source file. **211 lines.**
- L10–15 `test_entity_creation_and_normalization()`
- L18–25 `test_upsert_merges_duplicate_names()`
- L28–32 `test_alias_detection()`
- L35–41 `test_semantic_duplicate_detection()`
- L44–49 `test_semantic_duplicate_below_threshold()`
- L52–62 `test_manual_merge_rewires_relationships()`
- L65–73 `test_add_relationship_dedup()`
- L76–83 `test_supersede_relationship()`
- L86–93 `test_supersede_relations_of_type()`
- L96–103 `test_update_relationship_changes_status_and_confidence()`
- L106–113 `test_delete_entity_cascades()`
- L116–120 `test_pin_and_important()`
- L123–126 `test_set_confidence()`
- L129–137 `test_memory_history_preserved_on_supersede()`
- L140–145 `test_conversation_lifecycle()`
- L148–153 `test_persistence_across_reopen()`
- L156–158 `test_user_entity_protected()`
- L161–162 `test_integrity_ok_on_healthy_db()`
- L165–179 `test_similar_entities_by_embedding()`
- L182–196 `test_merge_preserves_conflicting_relationships()`
- L199–204 `test_merge_cannot_remove_user()`
- L207–211 `test_merge_preserves_description()`

### `tests/test_summarize.py`
Repository source file. **106 lines.**
- L7–15 `_seed_rich_entity()`
- L18–23 `test_find_candidates()`
- L26–37 `test_summarize_entity_creates_summary_memory()`
- L40–46 `test_summarize_does_not_delete_originals()`
- L49–55 `test_summary_references_source_memories()`
- L58–61 `test_summarize_all()`
- L64–70 `test_no_repeated_summary_of_same_cluster()`
- L73–85 `test_summarize_conversation_keeps_messages()`
- L88–91 `test_summarize_conversation_empty()`
- L94–106 `test_summary_polish_drops_inventions()`

### `tests/test_tray.py`
Repository source file. **60 lines.**
- L10–13 `test_activity_watch_is_hard_off()`
- L16–21 `test_clip_remember_text_skips_empty_and_caps()`
- L24–30 `test_tray_source_has_no_activity_poller()`
- L33–39 `test_icons_exist()`
- L42–45 `test_spec_embeds_icon()`
- L48–60 `test_ico_has_standard_windows_sizes()`

## API route index

All API routes live in `backend/app.py`; they call the modules above and never create a second service.

- Health/models: `GET /api/health`, `/api/models`
- Chat: `POST /api/chat`, `POST /api/chat/stream`
- Messages/conversations: `/api/messages`, `/api/conversations` and conversation actions
- Graph: `/api/graph`, `/api/graph/filter`, `/api/graph/neighborhood/{eid}`, `/api/graph/path`, `/api/graph/stats`, `/api/graph/groups`
- Entities/relationships/facts: `/api/entities`, `/api/entities/{eid}`, `/api/entities/merge`, `/api/relationships`, `/api/facts`
- Timeline/search: `/api/memories`, `POST /api/search`
- Data safety: `/api/export/*`, `/api/import`, `/api/import/notes`, `/api/import/file`, `/api/undo`, `/api/backup*`, `/api/reset`
- Summaries/settings/demo: `/api/summarize*`, `/api/settings`, `/api/demo*`

## GUI map

- Dashboard: counts, 14-day growth, memory types, recent source-linked memories, most-connected entities.
- Chat: SSE response streaming, remembered chips, sources, undo, conversation search/pin/archive/summarize/export.
- Knowledge Graph: Cytoscape nodes/edges, filters, layouts, focus/expand/path, entity inspector.
- Entities: searchable/sortable entity list, pinned/important/orphan filters, duplicate suggestions.
- Memory: timeline filters by kind/entity/text/date; source message modal.
- Search: grounded answer, status, sources, facts, explainable result reasons and filters.
- Settings: models, Ollama URL, thresholds, auto-memory/backups, theme, privacy, import/export/reset.
- GUI reliability: panel-local loading/error states, stale-response guards, accessible mobile labels, focus states, reduced-motion support.

## Test map

Run: `pytest tests/ test_overall.py`.

- `test_overall.py`: production contract and core loop.
- `tests/test_api.py`, `tests/test_api_phase3.py`: HTTP routes and API/UI contracts.
- `tests/test_frontend.py`: static GUI contracts; Playwright tests skip without Chromium.
- `tests/test_extraction.py`, `tests/test_ollama.py`: offline rules, validation, optional LLM path.
- `tests/test_search.py`, `tests/test_search_advanced.py`: hybrid retrieval, direct answers, grounding.
- `tests/test_graph.py`: traversal, filters, paths, stats, multi-hop.
- `tests/test_store.py`, `tests/test_migration.py`: persistence, merge, schema migration.
- `tests/test_commands.py`: deterministic memory controls.
- `tests/test_export.py`, `tests/test_backup.py`, `tests/test_reliability.py`: data portability and failure safety.
- `tests/test_launcher.py`, `tests/test_tray.py`: persistent paths, bootstrap, icon, and no-activity-watch guarantees.
- `tests/conftest.py`: all tests use isolated temporary databases.

## What an AI should read first

1. This file for orientation and the relevant test file for expected behavior.
2. `README.md` for user-visible behavior and constraints.
3. The specific live module named in the file map; do not read the whole repository by default.
4. `projekt.md` only when a complete historical/source archive is explicitly needed.

## Deliberately not included

The raw source archive is not duplicated here. The vendored Cytoscape build is
identified but not summarized line-by-line, and binary icons are represented by
metadata. This keeps AI context small while retaining a discoverable inventory
of every first-party file and code symbol.
