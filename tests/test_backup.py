"""Tests for the local backup mechanism."""
import os

from backend import backup, config, extract


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


def test_no_secrets_in_backup():
    backup.create_backup()
    status = backup.backup_status()
    # backup.json metadata contains no secret keys.
    latest = status["latest"]
    assert latest is not None
    for key in latest.keys():
        assert "secret" not in key.lower() and "password" not in key.lower() and "token" not in key.lower()
