#!/usr/bin/env python3
"""Second Brain — application entry point.

Starts the FastAPI app (same process as `python start.py` after setup).
Prefer `python start.py` on a new machine; it verifies dependencies first.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.app import app  # noqa: E402  — ASGI application


def main() -> None:
    import uvicorn

    host = os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0")
    port = int(os.environ.get("SECOND_BRAIN_PORT", "8000"))
    uvicorn.run(app, host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
