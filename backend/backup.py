"""Local backup mechanism.

Creates timestamped backups under data/backups/ containing:
  - a copy of the SQLite database (via SQLite's online backup API)
  - a JSON export of the knowledge graph
  - a Markdown export

Restore copies a named backup's brain.db over the live database after
taking a safety snapshot. Names are constrained so a path cannot escape
the backup directory. Two backups never share a folder.

No secrets are included (this application stores none). Backups are entirely
local. Provides listing + status of the latest backup.
"""
import json
import os
import re
import shutil
import sqlite3
import threading
from datetime import datetime, timedelta

from . import config, db, export

_auto_lock = threading.Lock()

_BACKUP_NAME = re.compile(r"^backup-\d{8}-\d{6}(?:-\d{1,6})?$")


def backup_dir():
    d = os.path.join(os.path.dirname(config.DB_PATH), "backups")
    os.makedirs(d, exist_ok=True)
    return d


def _timestamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def _unique_backup_dir():
    """Never reuse or overwrite an existing backup folder."""
    base = backup_dir()
    ts = _timestamp()
    candidate = os.path.join(base, f"backup-{ts}")
    if not os.path.exists(candidate):
        os.makedirs(candidate)
        return candidate
    ts = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    candidate = os.path.join(base, f"backup-{ts}")
    suffix = 1
    while os.path.exists(candidate):
        suffix += 1
        candidate = os.path.join(base, f"backup-{ts}-{suffix}")
    os.makedirs(candidate)
    return candidate


def create_backup():
    """Create a new backup. Returns a status dict."""
    target_dir = _unique_backup_dir()

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
    errors = []
    try:
        with open(os.path.join(target_dir, "export.json"), "w", encoding="utf-8") as f:
            f.write(export.export_json())
    except Exception as exc:
        errors.append(f"export.json: {exc}")
    try:
        with open(os.path.join(target_dir, "export.md"), "w", encoding="utf-8") as f:
            f.write(export.export_markdown())
    except Exception as exc:
        errors.append(f"export.md: {exc}")

    meta = {
        "created_at": datetime.now().isoformat(),
        "db": os.path.exists(db_copy),
        "export_json": os.path.exists(os.path.join(target_dir, "export.json")),
        "export_md": os.path.exists(os.path.join(target_dir, "export.md")),
    }
    if errors:
        meta["errors"] = errors
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
        "backups": backups[:20],
        "backup_dir": backup_dir(),
    }


def resolve_backup_dir(name):
    """Return the absolute backup folder if `name` is a safe local backup."""
    if not name or not _BACKUP_NAME.fullmatch(str(name)):
        return None
    base = os.path.realpath(backup_dir())
    target = os.path.realpath(os.path.join(base, name))
    if target == base or not target.startswith(base + os.sep):
        return None
    if not os.path.isdir(target):
        return None
    return target


def auto_backup_hours():
    return db.get_setting_float("auto_backup_hours", config.DEFAULT_AUTO_BACKUP_HOURS)


def maybe_auto_backup():
    """Create a local backup if the last one is older than the configured interval.

    Never deletes backups. Skips empty brains and disabled (0 hour) settings.
    """
    hours = auto_backup_hours()
    if hours is None or hours <= 0:
        return {"ok": False, "skipped": True, "reason": "disabled"}
    with _auto_lock:
        from . import store
        ents = store.all_entities()
        mems = store.recent_memories(1)
        if len(ents) <= 1 and not mems:
            return {"ok": False, "skipped": True, "reason": "empty"}
        last = db.get_setting("last_backup_at")
        if last:
            try:
                then = datetime.fromisoformat(str(last))
                if datetime.now() - then.replace(tzinfo=None) < timedelta(hours=float(hours)):
                    return {"ok": False, "skipped": True, "reason": "fresh"}
            except (TypeError, ValueError):
                pass
        result = create_backup()
        result["automatic"] = True
        return result


def restore_backup(name, confirm=False):
    """Replace the live database with a named backup.

    Always writes a safety snapshot of the current brain first. Never
    deletes the source backup. Requires confirm=True.
    """
    if not confirm:
        return {"ok": False, "error": "confirmation required"}
    target = resolve_backup_dir(name)
    if not target:
        return {"ok": False, "error": "backup not found"}
    src_db = os.path.join(target, "brain.db")
    if not os.path.isfile(src_db):
        return {"ok": False, "error": "backup is missing brain.db"}

    safety = create_backup()

    # Checkpoint then replace the live file. Leftover WAL/SHM from the
    # previous brain would otherwise be replayed onto the restored file
    # and hide the recovered memories.
    live = config.DB_PATH
    try:
        conn = sqlite3.connect(live)
        try:
            conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        finally:
            conn.close()
    except sqlite3.Error:
        pass

    shutil.copy2(src_db, live)
    for suffix in ("-wal", "-shm"):
        extra = live + suffix
        if os.path.isfile(extra):
            os.remove(extra)

    db.set_setting("last_restore_at", datetime.now().isoformat())
    db.set_setting("last_restore_from", name)
    return {
        "ok": True,
        "restored": name,
        "path": target,
        "safety_copy": safety.get("path"),
    }
