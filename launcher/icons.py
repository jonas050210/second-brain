"""Resolve the Second Brain icon for the EXE, setup window, and tray.

Never required for the memory app to run. Missing files degrade to the
default window icon.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _candidates(name: str) -> list[Path]:
    here = Path(__file__).resolve().parent
    root = here.parent
    out = [here / name, root / "launcher" / name]
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        base = Path(meipass)
        out.extend([base / "launcher" / name, base / name])
    if getattr(sys, "frozen", False):
        out.append(Path(sys.executable).resolve().parent / name)
    return out


def icon_ico() -> Path | None:
    for path in _candidates("secondbrain.ico"):
        if path.is_file():
            return path
    return None


def icon_png() -> Path | None:
    for path in _candidates("secondbrain.png"):
        if path.is_file():
            return path
    return None
