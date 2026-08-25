"""Tests for hybrid search, RAG answers, and hallucination protection."""
from backend import extract, search, store


def _seed():
    extract.extract("I am learning Python and I want to build AI agents.")
    extract.extract("My new project Nebula uses Next.js and Ollama.")


def test_keyword_search_finds_exact():
    _seed()
    hits = search.keyword_search("Nebula")
    assert any(h[1]["name"] == "Nebula" for h in hits)


def test_vector_search_returns_results():
    _seed()
    hits = search.vector_search("What programming language am I studying?")
    assert len(hits) > 0


def test_hybrid_search_combines_signals():
    _seed()
    res = search.search("Next.js")
    assert any(e["name"] == "Next.js" for e in res["entities"])


def test_answer_known():
    _seed()
    a = search.answer("What projects am I working on?")
    assert a["status"] in ("known", "answered")
    assert "Nebula" in a["text"]


def test_answer_unknown_no_hallucination():
    _seed()
    a = search.answer("Do I use Java?")
    assert a["status"] in ("unknown", "uncertain")
    # Must never invent a Java memory.
    if a["status"] == "unknown":
        assert "Java" not in a["text"] or "don't have" in a["text"] or "nothing" in a["text"]


def test_answer_learning_intent():
    _seed()
    a = search.answer("What am I learning?")
    assert a["status"] in ("known", "answered")
    assert "Python" in a["text"]


def test_answer_preference_intent():
    extract.extract("I prefer Python")
    a = search.answer("What language do I prefer?")
    assert a["status"] in ("known", "answered", "uncertain")
    if a["status"] == "answered":
        assert "Python" in a["text"]


def test_intent_detection():
    assert search.detect_intent("What projects am I working on?") == "project"
    assert search.detect_intent("What am I learning?") == "learning"
    assert search.detect_intent("Do you know who I met?") == "person"


def test_superseded_facts_not_in_active_search():
    extract.extract("I am learning Rust")
    extract.extract("I stopped learning Rust")
    # Active learning facts should not include Rust.
    facts = search.intent_facts("learning")
    texts = [f["text"] for f in facts]
    assert not any("Rust" in t and "learning" in t for t in texts)


def test_graph_facts_for_entity():
    _seed()
    neb = store.find_entity_by_name("Nebula")
    facts = search.graph_facts_for_entity(neb["id"])
    texts = [f["text"] for f in facts]
    assert any("uses Next.js" in t for t in texts)


def test_is_question():
    assert search.is_question("What projects am I working on?")
    assert search.is_question("Do I use Java?")
    assert not search.is_question("I am learning Python")


def test_yes_no_unknown_when_relation_missing():
    extract.extract("I am learning Python")
    a = search.answer("Do I use Python?")
    assert a["status"] == "unknown"
    assert "don't have" in a["text"].lower() or "nothing" in a["text"].lower()


def test_yes_no_known_when_fact_exists():
    extract.extract("I use Docker")
    a = search.answer("Do I use Docker?")
    assert a["status"] == "known"
    assert "Docker" in a["text"]


def test_pinned_entity_gets_reason():
    extract.extract("I am learning Python")
    py = store.find_entity_by_name("Python")
    store.update_entity(py["id"], pinned=1)
    res = search.search("Python")
    hit = next(e for e in res["entities"] if e["name"] == "Python")
    assert "pinned" in hit["reasons"]


def test_works_at_intent():
    extract.extract("I work at Acme")
    assert search.detect_intent("Where do I work at?") == "organization"
    facts = search.intent_facts("organization")
    assert any("Acme" in f["text"] for f in facts)
