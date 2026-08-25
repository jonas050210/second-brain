"""Bootstrap / EXE-launcher tests. Does not start a second application."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

from backend import paths
from launcher import bootstrap


REQUIRED_TITLES = [
    "Initializing Second Brain",
    "Checking Python/runtime",
    "Checking dependencies",
    "Installing only missing dependencies",
    "Checking database",
    "Checking configuration",
    "Checking Ollama",
    "Checking required models",
    "Running health checks",
    "Starting Second Brain",
]


def test_resolve_db_honors_env(tmp_path, monkeypatch):
    target = tmp_path / "custom" / "brain.db"
    monkeypatch.setenv("SECOND_BRAIN_DB", str(target))
    assert paths.resolve_db_path() == target


def test_relative_env_db_is_not_cwd_based(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path)
    monkeypatch.setenv("SECOND_BRAIN_DB", "data/brain.db")
    other = tmp_path / "other cwd"
    other.mkdir()
    old = os.getcwd()
    try:
        os.chdir(other)
        resolved = paths.resolve_db_path()
    finally:
        os.chdir(old)
    assert resolved == tmp_path / "data" / "brain.db"


def test_existing_db_wins_over_empty_default(tmp_path, monkeypatch):
    monkeypatch.delenv("SECOND_BRAIN_DB", raising=False)
    existing = tmp_path / "data" / "brain.db"
    existing.parent.mkdir()
    existing.write_bytes(b"sqlite-placeholder")
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path)
    found = paths.resolve_db_path()
    assert found == existing
    assert found.read_bytes() == b"sqlite-placeholder"


def test_never_uses_meipass_for_db(tmp_path, monkeypatch):
    mei = tmp_path / "_MEI12345"
    mei.mkdir()
    user = tmp_path / "AppData" / "Local" / "SecondBrain" / "data"
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "_MEIPASS", str(mei), raising=False)
    monkeypatch.setenv("SECOND_BRAIN_DB", str(mei / "brain.db"))
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path / "install")
    monkeypatch.setattr(paths, "is_frozen", lambda: True)
    monkeypatch.setattr(paths, "_user_data_dir", lambda: user)
    resolved = paths.resolve_db_path()
    assert "_MEI" not in str(resolved)
    assert Path(mei) not in resolved.parents
    assert resolved == user / "brain.db"


def test_frozen_prefers_existing_portable_db(tmp_path, monkeypatch):
    portable = tmp_path / "install" / "data" / "brain.db"
    portable.parent.mkdir(parents=True)
    portable.write_bytes(b"portable-brain")
    user = tmp_path / "AppData" / "Local" / "SecondBrain" / "data"
    user.mkdir(parents=True)
    (user / "brain.db").write_bytes(b"roaming-brain")
    monkeypatch.delenv("SECOND_BRAIN_DB", raising=False)
    monkeypatch.setattr(paths, "is_frozen", lambda: True)
    monkeypatch.setattr(paths, "app_root", lambda: tmp_path / "install")
    monkeypatch.setattr(paths, "_user_data_dir", lambda: user)
    found = paths.resolve_db_path()
    assert found == portable
    assert found.read_bytes() == b"portable-brain"


def test_spaces_in_path(tmp_path, monkeypatch):
    root = tmp_path / "Second Brain App"
    db = root / "data" / "brain.db"
    db.parent.mkdir(parents=True)
    db.write_bytes(b"x")
    monkeypatch.setenv("SECOND_BRAIN_DB", str(db))
    assert paths.resolve_db_path() == db
    assert db.is_file()


def test_ensure_data_dirs_does_not_delete_db(tmp_path):
    db = tmp_path / "data" / "brain.db"
    db.parent.mkdir()
    db.write_text("precious")
    paths.ensure_data_dirs(db)
    assert db.read_text() == "precious"


def test_bootstrap_preserves_existing_memories():
    from backend import store
    eid = store.create_entity("KeepMe", "concept")
    before = store.entity_row(eid)
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    after = store.entity_row(eid)
    assert after is not None
    assert after["name"] == "KeepMe"
    assert after["created_at"] == before["created_at"]


def test_second_bootstrap_does_not_install(monkeypatch):
    installed = []

    def boom(packages):
        installed.extend(packages)
        raise AssertionError("must not install when imports work")

    monkeypatch.setattr("start.install_packages", boom, raising=False)
    results = bootstrap.run_bootstrap(allow_install=True, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    install = next(r for r in results if r.key == "install")
    assert install.skipped is True
    assert installed == []


def test_missing_dependency_installs_only_that_package(monkeypatch):
    state = {"phase": 0, "installed": []}

    def fake_missing():
        state["phase"] += 1
        if state["phase"] == 1:
            return [("fastapi", "fastapi>=0.110")]
        return []

    def fake_install(packages):
        state["installed"] = list(packages)

    import start
    monkeypatch.setattr(bootstrap, "_missing_imports", fake_missing)
    monkeypatch.setattr(bootstrap.paths, "is_frozen", lambda: False)
    monkeypatch.setattr(start, "install_packages", fake_install)
    results = bootstrap.run_bootstrap(allow_install=True, pull_models=False)
    assert state["installed"] == ["fastapi>=0.110"]
    inst = next(r for r in results if r.key == "install")
    assert inst.ok
    assert inst.installed == ["fastapi>=0.110"]


def test_ollama_offline_does_not_fail(monkeypatch):
    monkeypatch.setattr(bootstrap, "probe_ollama", lambda *a, **k: {
        "available": False, "url": "http://localhost:11434", "models": [], "error": "refused",
    })
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    oll = next(r for r in results if r.key == "ollama")
    assert "offline" in oll.detail.lower() or "fallback" in oll.detail.lower()
    models = next(r for r in results if r.key == "models")
    assert models.skipped is True


def test_ollama_online_models_present_no_pull(monkeypatch):
    pulls = []

    def fake_probe(*a, **k):
        return {"available": True, "url": "http://localhost:11434",
                "models": ["qwen3:0.6b", "nomic-embed-text"], "error": None}

    monkeypatch.setattr(bootstrap, "probe_ollama", fake_probe)
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    models = next(r for r in results if r.key == "models")
    assert models.skipped is False
    assert "found" in models.detail
    assert pulls == []


def test_missing_models_not_downloaded_by_default(monkeypatch):
    monkeypatch.setattr(bootstrap, "probe_ollama", lambda *a, **k: {
        "available": True, "url": "http://localhost:11434",
        "models": [], "error": None,
    })
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    assert bootstrap.bootstrap_ok(results)
    models = next(r for r in results if r.key == "models")
    assert models.skipped is True
    assert "no download" in models.detail.lower() or "not installed" in models.detail.lower()


def test_cwd_does_not_change_db(tmp_path, monkeypatch):
    db = tmp_path / "keep" / "brain.db"
    db.parent.mkdir()
    db.write_bytes(b"abc")
    monkeypatch.setenv("SECOND_BRAIN_DB", str(db))
    other = tmp_path / "other cwd"
    other.mkdir()
    old = os.getcwd()
    try:
        os.chdir(other)
        assert paths.resolve_db_path() == db
        assert db.read_bytes() == b"abc"
    finally:
        os.chdir(old)


def test_bootstrap_never_calls_reset(monkeypatch):
    called = []

    import backend.db as dbmod
    real_execute = dbmod.execute

    def guarded(sql, params=()):
        if isinstance(sql, str) and "DELETE FROM" in sql.upper() and "entities" in sql:
            called.append(sql)
        return real_execute(sql, params)

    monkeypatch.setattr(dbmod, "execute", guarded)
    bootstrap.run_bootstrap(allow_install=False)
    assert called == []


def test_bootstrap_emits_required_status_titles():
    results = bootstrap.run_bootstrap(allow_install=False, pull_models=False)
    got = [r.title for r in results]
    for title in REQUIRED_TITLES:
        assert title in got


def test_headless_check_entrypoint():
    from launcher import __main__ as entry
    rc = entry.main(["--headless", "--check", "--no-install"])
    assert rc == 0


def test_create_server_uses_existing_app():
    from backend.app import app as existing
    server = bootstrap.create_server("127.0.0.1", 8099)
    assert server.config.app is existing
    assert server.config.port == 8099
