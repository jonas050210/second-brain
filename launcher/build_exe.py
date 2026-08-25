#!/usr/bin/env python3
"""Build SecondBrain.exe with PyInstaller.

On Windows 11 the output is dist/SecondBrain.exe.
PyInstaller cannot cross-compile a Windows PE from Linux or macOS.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    os.chdir(ROOT)
    spec = ROOT / "secondbrain.spec"
    if not spec.is_file():
        print("missing secondbrain.spec", file=sys.stderr)
        return 1

    if os.name != "nt":
        print(
            "NOTE: PyInstaller cannot produce a Windows .exe on this OS.\n"
            "Run this same command on Windows 11 to get dist/SecondBrain.exe.\n"
            "A native binary named dist/SecondBrain may be built instead.\n",
            file=sys.stderr,
        )

    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", str(spec)]
    print("Running:", " ".join(cmd))
    rc = subprocess.call(cmd)
    if rc != 0:
        return rc

    exe = ROOT / "dist" / ("SecondBrain.exe" if os.name == "nt" else "SecondBrain")
    if exe.is_file():
        print("Built:", exe)
        print("size:", exe.stat().st_size, "bytes")
        if os.name != "nt":
            print(
                "This is not a Windows EXE. Copy the project to Windows 11 and rerun:",
                file=sys.stderr,
            )
            print("  python -m launcher.build_exe", file=sys.stderr)
        return 0
    print("Build finished but binary not found at", exe, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
