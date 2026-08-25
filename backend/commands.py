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
import re

from . import config, db, store

# Leading phrases that mark an explicit memory-control command.
COMMAND_LEADS = [
    "remember that", "remember", "forget that", "forget", "delete the memory",
    "remove the memory", "remove", "delete", "unremember",
    "pin ", "unpin ", "mark ", "unmark ",
    "merge ", "change ", "update ", "rename ", "set confidence",
    "make this important", "stop remembering",
]


def is_command(text):
    t = text.strip().lower()
    return any(t.startswith(lead) for lead in COMMAND_LEADS) or \
        t.startswith(("remember ", "forget ", "remove ", "delete ", "pin ",
                      "unpin ", "mark ", "unmark ", "merge ", "change ",
                      "update ", "rename "))


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

    # ---- remember that X -------------------------------------------------
    m = re.match(r"remember that\s+(.+)$", tl, re.I)
    if m:
        return {"action": "remember", "payload": m.group(1).strip()}

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
        return {"reply": f'Pinned "{e["name"]}".', "ok": True, "entities": [e["id"]]}

    m = re.match(r"unpin\s+(.+)$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{m.group(1).strip()}\".", "ok": False}
        store.update_entity(e["id"], pinned=0)
        return {"reply": f'Unpinned "{e["name"]}".', "ok": True, "entities": [e["id"]]}

    # ---- mark as important / unmark --------------------------------------
    m = re.match(r"mark\s+(.+?)\s+as\s+important$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{m.group(1).strip()}\".", "ok": False}
        store.update_entity(e["id"], important=1)
        return {"reply": f'Marked "{e["name"]}" as important.', "ok": True, "entities": [e["id"]]}

    m = re.match(r"unmark\s+(.+)$", tl, re.I)
    if m:
        e = _find_entity(m.group(1).strip())
        if not e:
            return {"reply": f"I couldn't find an entity matching \"{m.group(1).strip()}\".", "ok": False}
        store.update_entity(e["id"], important=0)
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


def forget_target(target):
    """Forget an entity or a relationship, or supersede a stale fact."""
    tl = target.lower()

    # "that I am learning Rust" -> supersede the learning relationship.
    m = re.match(r"(?:that\s+)?(?:i\s+)?(?:am|was|is|were)?\s*(learning|using|working on|into|interested in)\s+(.+)$", tl)
    if m:
        rel, name = m.group(1).strip(), m.group(2).strip()
        e = _find_entity(name)
        if not e:
            return {"reply": f"I couldn't find \"{name}\".", "ok": False}
        # For learning/uses: supersede rather than delete (keep history).
        rel_map = {"learning": "learning", "using": "uses", "working on": "works_on",
                   "into": "interested_in", "interested in": "interested_in"}
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
