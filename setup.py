#!/usr/bin/env python3
"""One-time environment setup for Second Brain.

Creates a virtual environment if needed, installs only missing runtime
dependencies, and prepares the local data directory.

Usage:
    python setup.py
"""
from __future__ import annotations

import sys


def main() -> int:
    # Reuse the launcher's setup path so there is a single installer.
    import start
    return start.main(["--setup"])


if __name__ == "__main__":
    raise SystemExit(main())
