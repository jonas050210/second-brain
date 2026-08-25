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
    try:
        max_depth = max(0, int(max_depth))
    except (TypeError, ValueError):
        max_depth = 6
    if source_id == target_id:
        return [{"node": source_id}]
    adj, edges = _load_edges(active_only)
    prev = {source_id: None}  # node -> (prev_node, rel_id, relation, direction)
    distances = {source_id: 0}
    q = deque([source_id])
    while q:
        cur = q.popleft()
        if cur == target_id:
            break
        if distances[cur] >= max_depth:
            continue
        for (other, rid, rel, conf, direction) in adj.get(cur, []):
            if other in prev:
                continue
            prev[other] = (cur, rid, rel, direction)
            distances[other] = distances[cur] + 1
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
