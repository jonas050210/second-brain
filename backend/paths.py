"""Persistent, CWD-independent path resolution.

The database must NEVER live inside a PyInstaller extract directory
(``sys._MEIPASS``). That folder is temporary and would look like a "new
empty brain" on every launch.

Resolution order for the SQLite file:

1. ``SECOND_BRAIN_DB`` if it is a real, non-ephemeral path
   (relative values are resolved against the app root, not the CWD)
2. An existing ``brain.db`` next to the executable / project (portable)
3. An existing ``brain.db`` in the user data directory
4. Frozen default: ``%LOCALAPPDATA%/SecondBrain/data/brain.db``
   Source default: ``<app-root>/data/brain.db``

Existing files always win. Nothing here deletes or overwrites a database.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

APP_VERSION = "2.7.0"
DB_NAME = "brain.db"


def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def bundle_dir() -> Path:
    """Read-only files shipped with the app (frontend when frozen)."""
    if is_frozen():
        return Path(getattr(sys, "_MEIPASS", Path(sys.executable).resolve().parent))
    return Path(__file__).resolve().parent.parent


def app_root() -> Path:
    """Persistent application root (never _MEIPASS)."""
    if is_frozen():
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


def _user_data_dir() -> Path:
    override = os.environ.get("SECOND_BRAIN_DATA")
    if override:
        path = Path(override).expanduser()
        return path if path.is_absolute() else (app_root() / path)
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(base) / "SecondBrain" / "data"
    xdg = os.environ.get("XDG_DATA_HOME")
    if xdg:
        return Path(xdg) / "second-brain"
    return Path.home() / ".local" / "share" / "second-brain"


def _is_ephemeral(path: Path) -> bool:
    try:
        resolved = path.resolve()
    except OSError:
        resolved = path
    text = str(resolved)
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        try:
            if resolved == Path(meipass) or Path(meipass) in resolved.parents:
                return True
        except OSError:
            if str(meipass) in text:
                return True
    lowered = text.replace("\\", "/").lower()
    if "/_mei" in lowered and ("/temp" in lowered or "/tmp" in lowered):
        return True
    return False


def frontend_dir() -> Path:
    bundled = bundle_dir() / "frontend"
    if (bundled / "index.html").is_file():
        return bundled
    return app_root() / "frontend"


def _existing_db_candidates() -> list[Path]:
    return [
        app_root() / "data" / DB_NAME,
        _user_data_dir() / DB_NAME,
    ]


def _coerce_persistent(path: Path) -> Path:
    """Make a path absolute against the app root. Reject extract-dir targets."""
    candidate = path.expanduser()
    if not candidate.is_absolute():
        candidate = app_root() / candidate
    return candidate


def resolve_db_path() -> Path:
    """Return the database path. Never points at a temp extract dir."""
    env = os.environ.get("SECOND_BRAIN_DB")
    if env:
        candidate = _coerce_persistent(Path(env))
        if not _is_ephemeral(candidate):
            return candidate

    for path in _existing_db_candidates():
        try:
            if path.is_file() and not _is_ephemeral(path):
                return path
        except OSError:
            continue

    # Frozen builds persist under the user profile so moving the EXE
    # cannot orphan an existing brain or create a new empty one.
    if is_frozen():
        return _user_data_dir() / DB_NAME
    return app_root() / "data" / DB_NAME


def ensure_data_dirs(db_path: Path | None = None) -> Path:
    """Create parent folders only. Never deletes an existing database."""
    path = Path(db_path) if db_path is not None else resolve_db_path()
    parent = path.parent
    if str(parent):
        parent.mkdir(parents=True, exist_ok=True)
    (parent / "backups").mkdir(parents=True, exist_ok=True)
    return path
