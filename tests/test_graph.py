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


def test_explainable_rank():
    _seed()
    ranked = graph.explainable_rank("Rust")
    assert ranked, "should rank Rust first"
    top = ranked[0]
    assert "reasons" in top and isinstance(top["reasons"], list)
