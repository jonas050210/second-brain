"""Local backup mechanism.

Creates timestamped backups under data/backups/ containing:
  - a copy of the SQLite database (via SQLite's online backup API)
  - a JSON export of the knowledge graph
  - a Markdown export

No secrets are included (this application stores none). Backups are entirely
local. Provides listing + status of the latest backup.
"""
import json
import os
import shutil
import sqlite3
from datetime import datetime

from . import config, db, export, store


def backup_dir():
    d = os.path.join(os.path.dirname(config.DB_PATH), "backups")
    os.makedirs(d, exist_ok=True)
    return d


def _timestamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def create_backup():
    """Create a new backup. Returns a status dict."""
    ts = _timestamp()
    target_dir = os.path.join(backup_dir(), f"backup-{ts}")
    os.makedirs(target_dir, exist_ok=True)

    # 1. SQLite online backup (safe even while the app is running).
    db_copy = os.path.join(target_dir, "brain.db")
    src = sqlite3.connect(config.DB_PATH)
    dst = sqlite3.connect(db_copy)
    try:
        with dst:
            src.backup(dst)
    finally:
        dst.close()
        src.close()

    # 2. JSON + Markdown exports.
    try:
        with open(os.path.join(target_dir, "export.json"), "w", encoding="utf-8") as f:
            f.write(export.export_json())
    except Exception:
        pass
    try:
        with open(os.path.join(target_dir, "export.md"), "w", encoding="utf-8") as f:
            f.write(export.export_markdown())
    except Exception:
        pass

    meta = {
        "created_at": datetime.now().isoformat(),
        "db": os.path.exists(db_copy),
        "export_json": os.path.exists(os.path.join(target_dir, "export.json")),
        "export_md": os.path.exists(os.path.join(target_dir, "export.md")),
    }
    with open(os.path.join(target_dir, "backup.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    db.set_setting("last_backup_at", datetime.now().isoformat())
    db.set_setting("last_backup_dir", target_dir)

    return {"ok": True, "path": target_dir, **meta}


def list_backups():
    """List all backups, newest first."""
    out = []
    base = backup_dir()
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base), reverse=True):
        p = os.path.join(base, name)
        if not os.path.isdir(p):
            continue
        meta = {}
        meta_path = os.path.join(p, "backup.json")
        if os.path.exists(meta_path):
            try:
                with open(meta_path) as f:
                    meta = json.load(f)
            except ValueError:
                meta = {}
        out.append({"name": name, "path": p, **meta})
    return out


def backup_status():
    """Status of the most recent backup (for the Settings UI)."""
    backups = list_backups()
    latest = backups[0] if backups else None
    return {
        "last_backup_at": db.get_setting("last_backup_at"),
        "last_backup_dir": db.get_setting("last_backup_dir"),
        "count": len(backups),
        "latest": latest,
        "backup_dir": backup_dir(),
    }
