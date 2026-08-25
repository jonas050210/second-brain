"""Second Brain — local AI knowledge graph.

FastAPI backend + static frontend. Everything runs locally; the only external
dependency (optional) is a local Ollama instance.
"""
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import backup, commands, config, db, export, extract, ollama, search, store, summarize
from . import graph as graph_engine

app = FastAPI(title="Second Brain", version="2.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

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


def natural_reply(text, remembered, used_fallback):
    """A short, grounded acknowledgment (never chain-of-thought)."""
    if ollama.available():
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
        try:
            return ollama.chat(effective_llm_model(), [
                {"role": "system", "content": "You are a concise, friendly personal knowledge assistant."},
                {"role": "user", "content": prompt},
            ], temperature=0.3).strip()
        except Exception:
            pass
    if not remembered:
        return ("I heard you, but I didn't find anything durable to save yet. "
                "Try telling me about a project, a technology, or a goal.")
    n = len(remembered)
    head = "Got it — I've updated your brain." if n else "Understood."
    if used_fallback:
        head += " (offline mode)"
    return head


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
    }


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
    content = body.content.strip()
    if not content:
        return {"reply": "", "remembered": [], "trivial": True}

    cid = body.conversation_id or store.current_conversation_id()
    msg_id = store.add_message("user", content, conversation_id=cid,
                               embedding=store.embed_text(content))
    base = {"conversation_id": cid}

    # Title the conversation with its first user message.
    conv = store.conversation_row(cid)
    if conv and not conv["title"]:
        store.touch_conversation(cid, title=content[:60])

    # Build short-term conversation context (separate from long-term memory).
    context = [m for m in store.conversation_messages(cid, config.SHORT_TERM_CONTEXT_TURNS)]

    # 1. Explicit memory-control commands.
    cmd = commands.handle_command(content) if commands.is_command(content) else None
    if cmd and "action" not in cmd:
        reply = cmd.get("reply", "Done.")
        store.add_message("assistant", reply, conversation_id=cid,
                          meta={"kind": "command"})
        return {"reply": reply, "remembered": [], "updates": [],
                "is_command": True, "ok": cmd.get("ok", True), "trivial": False, **base}

    # "remember that X" -> force extraction of the payload.
    if cmd and cmd.get("action") == "remember":
        payload = cmd["payload"]
        return _extract_and_reply(payload, cid, msg_id, force=True, original=content)

    # 2. Questions -> grounded RAG over memory.
    if search.is_question(content) and not smalltalk_reply(content):
        # Recent conversation turns (short-term context) augment long-term memory.
        recent = [m["content"] for m in context if m["role"] == "user"][-4:]
        res = search.answer(content, model=effective_llm_model(),
                            context="\n".join(recent))
        reply = res["text"]
        store.add_message("assistant", reply, conversation_id=cid,
                          meta={"kind": "answer", "status": res["status"]})
        return {"reply": reply, "remembered": [], "updates": [],
                "is_answer": True, "status": res["status"], "trivial": False, **base}

    # 3. Small talk.
    if smalltalk_reply(content):
        reply = smalltalk_reply(content)
        store.add_message("assistant", reply, conversation_id=cid,
                          meta={"kind": "smalltalk"})
        return {"reply": reply, "remembered": [], "updates": [], "trivial": True, **base}

    # 4. Normal message: auto-memory (unless disabled).
    if not auto_memory_enabled():
        reply = "Auto-memory is off, so I won't save this. (Turn it back on in Settings.)"
        store.add_message("assistant", reply, conversation_id=cid, meta={"kind": "off"})
        return {"reply": reply, "remembered": [], "updates": [], "trivial": True, **base}

    return _extract_and_reply(content, cid, msg_id, force=False, original=content)


def _extract_and_reply(content, cid, msg_id, force=False, original=None):
    result = extract.extract(content, model=effective_llm_model(),
                             source_message_id=msg_id)
    if result["trivial"]:
        reply = "Noted. Tell me more about what you're building or learning."
        store.add_message("assistant", reply, conversation_id=cid, meta={"kind": "smalltalk"})
        return {"reply": reply, "remembered": [], "updates": [], "trivial": True,
                "conversation_id": cid}

    remembered = result["remembered"]
    updates = build_updates(result)
    reply = natural_reply(original or content, remembered, result["used_fallback"])

    if remembered or updates:
        store.add_message("assistant", "", conversation_id=cid, extracted=1,
                          meta={"updates": updates, "used_fallback": result["used_fallback"],
                                "remembered": remembered})
    else:
        store.add_message("assistant", reply, conversation_id=cid, meta={"kind": "empty"})

    return {
        "reply": reply,
        "remembered": remembered,
        "updates": updates,
        "superseded": result.get("superseded", []),
        "used_fallback": result["used_fallback"],
        "trivial": False,
        "conversation_id": cid,
    }


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


@app.get("/api/conversations/{cid}/messages")
def conversation_messages(cid: int):
    out = []
    for m in store.conversation_messages(cid):
        meta = json.loads(m.get("meta") or "{}")
        out.append({"id": m["id"], "role": m["role"], "content": m["content"],
                    "created_at": m["created_at"],
                    "updates": meta.get("updates", []),
                    "remembered": meta.get("remembered", []),
                    "kind": meta.get("kind", "")})
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
                            "direction": "out", "rid": r["rid"], "status": r["status"],
                            "confidence": r["confidence"],
                            "source": _source_for(r["source_message_id"])})
        else:
            inv = {v: k for k, v in config.RELATION_INVERSE.items()}.get(r["relation"], r["relation"])
            related.append({"other_id": r["sid"], "other_name": r["sname"],
                            "other_type": r["stype"], "relation": inv,
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


@app.delete("/api/relationships/{rid}")
def rel_delete(rid: int):
    store.delete_relationship(rid)
    return {"ok": True}


# --------------------------------------------------------------------------
# API: memories (timeline)
# --------------------------------------------------------------------------

@app.get("/api/memories")
def memories(limit: int = 200, entity_id: int = None, kind: str = None,
             type: str = None, conversation_id: int = None, date: str = None):
    rows = store.recent_memories(limit if limit <= 2000 else 2000)
    out = []
    for m in rows:
        if entity_id is not None and entity_id not in json.loads(m["entity_ids"] or "[]"):
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


@app.post("/api/search")
def do_search(body: SearchIn):
    filters = {k: v for k, v in {
        "type": body.type, "min_confidence": body.min_confidence,
        "status": body.status, "pinned": body.pinned, "important": body.important,
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


@app.post("/api/import")
def do_import(body: ImportIn):
    if body.mode not in ("merge", "replace"):
        raise HTTPException(400, "mode must be 'merge' or 'replace'")
    return export.import_from_json(body.data, mode=body.mode)


# --------------------------------------------------------------------------
# API: backup
# --------------------------------------------------------------------------

@app.post("/api/backup")
def do_backup():
    return backup.create_backup()


@app.get("/api/backup/status")
def backup_status():
    return backup.backup_status()


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
        "theme": db.get_setting("theme", "dark"),
        "ollama_available": ollama.available(),
        "models_installed": ollama.list_models(),
        "db_path": config.DB_PATH,
    }


class SettingsIn(BaseModel):
    llm_model: Optional[str] = None
    embedding_model: Optional[str] = None
    ollama_base_url: Optional[str] = None
    confidence_threshold: Optional[float] = None
    merge_similarity: Optional[float] = None
    auto_memory: Optional[bool] = None
    theme: Optional[str] = None


@app.post("/api/settings")
def set_settings(body: SettingsIn):
    if body.llm_model:
        db.set_setting("llm_model", body.llm_model.strip())
    if body.embedding_model:
        db.set_setting("embedding_model", body.embedding_model.strip())
    if body.ollama_base_url:
        db.set_setting("ollama_base_url", body.ollama_base_url.strip().rstrip("/"))
    if body.confidence_threshold is not None:
        db.set_setting("confidence_threshold", max(0.0, min(1.0, body.confidence_threshold)))
    if body.merge_similarity is not None:
        db.set_setting("merge_similarity", max(0.0, min(1.0, body.merge_similarity)))
    if body.auto_memory is not None:
        db.set_setting("auto_memory", bool(body.auto_memory))
    if body.theme:
        db.set_setting("theme", body.theme)
    return get_settings()


@app.post("/api/reset")
def reset():
    """Wipe all data (dangerous, for testing)."""
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
    # Clearly mark all messages and their extracted entities in this
    # conversation as demo data (distinct from real user data).
    db.execute("UPDATE messages SET meta=? WHERE conversation_id=?",
               (json.dumps({"demo": True}), cid))
    msg_ids = [m["id"] for m in store.conversation_messages(cid)]
    if msg_ids:
        placeholders = ",".join("?" for _ in msg_ids)
        db.execute(f"UPDATE entities SET meta=? WHERE source_message_id IN ({placeholders})",
                   (json.dumps({"demo": True}), *msg_ids))
    return {"ok": True, "replies": replies, "conversation_id": cid}


# --------------------------------------------------------------------------
# Static frontend (served by the same local server — no build step needed)
# --------------------------------------------------------------------------

if os.path.isdir(config.FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=config.FRONTEND_DIR, html=True), name="frontend")
