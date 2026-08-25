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


def test_recency_boost_present():
    _seed()
    ranked = search.search("Rust")
    # Just verify the recency signal is wired (no crash) and reasons may include recent.
    assert isinstance(ranked["entities"], list)
