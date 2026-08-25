"""Tests for memory consolidation / summarization."""
import json

from backend import db, extract, store, summarize


def _seed_rich_entity():
    # Create multiple memories around one project so it becomes a candidate.
    for line in [
        "My project Nebula uses Next.js.",
        "Nebula uses Ollama.",
        "Nebula is an AI creative workspace.",
        "I am building Nebula for image generation.",
    ]:
        extract.extract(line)


def test_find_candidates():
    _seed_rich_entity()
    cands = summarize.find_consolidation_candidates(min_shared=2)
    nebula = next((c for c in cands if c["entity_name"] == "Nebula"), None)
    assert nebula is not None
    assert nebula["count"] >= 2


def test_summarize_entity_creates_summary_memory():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    before = len(store.memories_for_entity(nebula["id"]))
    r = summarize.summarize_entity(nebula["id"])
    assert r["ok"] is True
    assert r["summary_id"] is not None
    # A new summary memory exists and references the entity.
    mems = db.query("SELECT * FROM memories WHERE kind='summary'")
    assert mems
    meta = json.loads(mems[0]["meta"] or "{}")
    assert "source_memory_ids" in meta


def test_summarize_does_not_delete_originals():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    before = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    summarize.summarize_entity(nebula["id"])
    after = db.query("SELECT COUNT(*) c FROM memories")[0]["c"]
    assert after > before, "originals must be preserved, summary added on top"


def test_summary_references_source_memories():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    r = summarize.summarize_entity(nebula["id"])
    mem = db.query_one("SELECT * FROM memories WHERE id=?", (r["summary_id"],))
    meta = json.loads(mem["meta"] or "{}")
    assert meta["source_memory_ids"], "summary should reference the memories it came from"


def test_summarize_all():
    _seed_rich_entity()
    results = summarize.summarize_all(limit=5)
    assert any(res.get("ok") for res in results)


def test_no_repeated_summary_of_same_cluster():
    _seed_rich_entity()
    nebula = store.find_entity_by_name("Nebula")
    summarize.summarize_entity(nebula["id"])
    cands = summarize.find_consolidation_candidates(min_shared=2)
    # Nebula should be skipped now that it's been summarized.
    assert not any(c["entity_name"] == "Nebula" for c in cands)
