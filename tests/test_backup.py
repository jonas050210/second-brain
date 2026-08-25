"""Tests for the local backup mechanism."""
import os

from backend import backup, config, extract, store


def test_create_backup():
    extract.extract("I am learning Python.")
    r = backup.create_backup()
    assert r["ok"] is True
    assert os.path.isdir(r["path"])
    assert os.path.exists(os.path.join(r["path"], "brain.db"))
    assert os.path.exists(os.path.join(r["path"], "export.json"))


def test_backup_list_and_status():
    backup.create_backup()
    status = backup.backup_status()
    assert status["count"] >= 1
    assert status["latest"] is not None
    assert status["backup_dir"] == backup.backup_dir()


def test_backup_contains_real_data():
    extract.extract("I am learning Python.")
    r = backup.create_backup()
    # The backup DB should contain the Python entity.
    import sqlite3
    conn = sqlite3.connect(os.path.join(r["path"], "brain.db"))
    n = conn.execute("SELECT COUNT(*) FROM entities WHERE norm_name='python'").fetchone()[0]
    conn.close()
    assert n == 1


def test_restore_requires_confirmation():
    extract.extract("I am learning Python.")
    created = backup.create_backup()
    name = os.path.basename(created["path"])
    r = backup.restore_backup(name, confirm=False)
    assert r["ok"] is False
    assert "confirm" in r["error"]


def test_restore_rejects_path_traversal():
    r = backup.restore_backup("../etc", confirm=True)
    assert r["ok"] is False
    r2 = backup.restore_backup("backup-../../../tmp", confirm=True)
    assert r2["ok"] is False


def test_restore_roundtrip_preserves_memories():
    extract.extract("I am learning Python.")
    assert store.find_entity_by_name("Python") is not None
    created = backup.create_backup()
    name = os.path.basename(created["path"])
    store.delete_entity(store.find_entity_by_name("Python")["id"])
    assert store.find_entity_by_name("Python") is None
    r = backup.restore_backup(name, confirm=True)
    assert r["ok"] is True
    assert r["safety_copy"]
    assert os.path.isdir(r["safety_copy"])
    assert store.find_entity_by_name("Python") is not None


def test_maybe_auto_backup_skips_empty_and_fresh():
    r = backup.maybe_auto_backup()
    assert r.get("skipped") is True
    extract.extract("I am learning Python.")
    first = backup.maybe_auto_backup()
    assert first.get("ok") is True
    again = backup.maybe_auto_backup()
    assert again.get("skipped") is True


def test_no_secrets_in_backup():
    backup.create_backup()
    status = backup.backup_status()
    # backup.json metadata contains no secret keys.
    latest = status["latest"]
    assert latest is not None
    for key in latest.keys():
        assert "secret" not in key.lower() and "password" not in key.lower() and "token" not in key.lower()
