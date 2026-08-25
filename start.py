#!/usr/bin/env python3
"""Primary launcher for Second Brain.

Paths are resolved from this file, so the current working directory does not
matter. After a successful first run this script must NOT reinstall packages.

Usage:
    python start.py
    python start.py --check
    python start.py --check-only
    python start.py --no-install
    python start.py --dev
    python start.py --open
    python start.py --host 0.0.0.0 --port 8000
"""
from __future__ import annotations

import argparse
import importlib
import os
import subprocess
import sys
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"

RUNTIME_DEPS = (
    ("fastapi", "fastapi>=0.110"),
    ("uvicorn", "uvicorn[standard]>=0.29"),
    ("requests", "requests>=2.31"),
    ("numpy", "numpy>=1.26"),
)

MIN_PY = (3, 11)


def is_windows() -> bool:
    return os.name == "nt"


def venv_python() -> Path:
    if is_windows():
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def running_in_project_venv() -> bool:
    try:
        prefix = Path(getattr(sys, "prefix", "")).resolve()
        base = Path(getattr(sys, "base_prefix", sys.prefix)).resolve()
        if prefix == VENV_DIR.resolve():
            return True
        raw = Path(sys.executable)
        if str(VENV_DIR) in str(raw):
            return True
        return prefix != base and str(VENV_DIR.resolve()) in str(prefix)
    except OSError:
        return False


def check_python() -> None:
    if sys.version_info < MIN_PY:
        ver = ".".join(str(p) for p in sys.version_info[:3])
        need = ".".join(str(p) for p in MIN_PY)
        raise SystemExit(
            f"Second Brain requires Python {need}+ (found {ver}).\n"
            "Install Python 3.11.9 or newer and retry."
        )


def missing_runtime() -> list[str]:
    missing = []
    for mod, spec in RUNTIME_DEPS:
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append(spec)
    return missing


def install_packages(packages: list[str]) -> None:
    print("Installing missing packages:", ", ".join(packages))
    cmd = [sys.executable, "-m", "pip", "install", "--disable-pip-version-check", *packages]
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            "Failed to install Python packages.\n"
            f"Command: {' '.join(cmd)}\n"
            "On Windows:  python -m pip install -r requirements.txt\n"
            f"pip exit code: {exc.returncode}"
        ) from exc


def ensure_venv() -> None:
    if os.environ.get("SECOND_BRAIN_NO_VENV") == "1":
        return
    if running_in_project_venv():
        return
    if missing_runtime() and not venv_python().is_file():
        print(f"Creating virtual environment at {VENV_DIR} …")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])
        except subprocess.CalledProcessError as exc:
            raise SystemExit(
                "Could not create a virtual environment.\n"
                "On Windows, re-run the official Python installer with pip and venv enabled."
            ) from exc


def reexec_in_venv_if_needed() -> None:
    if os.environ.get("SECOND_BRAIN_NO_VENV") == "1":
        return
    if running_in_project_venv():
        return
    py = venv_python()
    if py.is_file() and Path(sys.executable).resolve() != py.resolve():
        os.execv(str(py), [str(py), *sys.argv])


def create_dirs() -> None:
    (ROOT / "data").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "backups").mkdir(parents=True, exist_ok=True)


def verify_imports() -> None:
    missing = missing_runtime()
    if missing:
        raise SystemExit("Runtime packages are still missing: " + ", ".join(missing))
    frontend = ROOT / "frontend" / "index.html"
    if not frontend.is_file():
        raise SystemExit(f"Frontend is missing: {frontend}")


def setup_only(allow_install: bool = True) -> list[str]:
    check_python()
    if allow_install:
        ensure_venv()
    missing = missing_runtime()
    installed: list[str] = []
    if missing:
        if not allow_install:
            raise SystemExit(
                "Missing runtime packages and --no-install was set: "
                + ", ".join(missing)
            )
        install_packages(missing)
        installed = missing
    create_dirs()
    return installed


def detect_environment() -> dict:
    return {
        "python": sys.version.split()[0],
        "executable": sys.executable,
        "platform": sys.platform,
        "windows": is_windows(),
        "project": str(ROOT),
        "venv": running_in_project_venv(),
        "missing": missing_runtime(),
    }


def probe_ollama() -> dict:
    url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
    try:
        import requests
        r = requests.get(url.rstrip("/") + "/api/tags", timeout=2)
        if r.status_code != 200:
            return {"available": False, "url": url, "error": f"HTTP {r.status_code}"}
        models = [m.get("name") for m in r.json().get("models", [])]
        return {"available": True, "url": url, "models": models}
    except Exception as exc:
        return {"available": False, "url": url, "error": str(exc) or exc.__class__.__name__}


def print_env(info: dict) -> None:
    print("Second Brain — environment")
    print(f"  Python      : {info['python']} ({info['executable']})")
    print(f"  Platform    : {info['platform']}")
    print(f"  Project     : {info['project']}")
    print(f"  Project venv: {'yes' if info['venv'] else 'no'}")
    print(f"  Missing     : {', '.join(info['missing']) if info['missing'] else 'none'}")
    oll = probe_ollama()
    if oll.get("available"):
        models = ", ".join(oll.get("models") or []) or "none listed"
        print(f"  Ollama      : online at {oll['url']}")
        print(f"  Models      : {models}")
    else:
        print(f"  Ollama      : offline ({oll.get('url')})")
        if oll.get("error"):
            print(f"                {oll['error']}")
        print("                Fallback extractor will be used. Optional:")
        print("                ollama pull qwen3:0.6b && ollama pull nomic-embed-text")


def start_server(host: str, port: int, reload: bool = False, open_browser: bool = False) -> None:
    os.chdir(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        import uvicorn
    except ImportError as exc:
        raise SystemExit("uvicorn is not installed. Run:  python start.py") from exc
    url = f"http://127.0.0.1:{port}"
    print()
    print("Starting Second Brain")
    print(f"  Local URL  : {url}")
    print(f"  Bind       : {host}:{port}")
    print("  Privacy    : LOCAL · PRIVATE · no telemetry")
    print("  Stop       : Ctrl+C")
    if reload:
        print("  Reload     : on")
    print()
    if open_browser:
        threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    uvicorn.run("backend.app:app", host=host, port=port, reload=reload, log_level="info")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Start Second Brain")
    parser.add_argument("--check", action="store_true", help="Verify environment and exit")
    parser.add_argument("--check-only", action="store_true", help="Alias for --check")
    parser.add_argument("--no-install", action="store_true", help="Do not install missing packages")
    parser.add_argument("--dev", action="store_true", help="Start with auto-reload")
    parser.add_argument("--open", action="store_true", help="Open the local URL in a browser")
    parser.add_argument("--host", default=os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("SECOND_BRAIN_PORT", "8000")))
    args = parser.parse_args(argv)

    check_python()
    info = detect_environment()
    print_env(info)

    if args.check or args.check_only:
        create_dirs()
        if info["missing"] and not venv_python().is_file():
            print("FAIL: missing runtime packages:", ", ".join(info["missing"]))
            return 1
        if info["missing"] and venv_python().is_file() and not running_in_project_venv():
            extra = ["--check"]
            rc = subprocess.call([str(venv_python()), str(ROOT / "start.py"), *extra])
            return rc
        try:
            verify_imports()
        except SystemExit as exc:
            print("FAIL:", exc)
            return 1
        print("OK: environment is ready.")
        return 0

    allow_install = not args.no_install
    if allow_install and missing_runtime() and not running_in_project_venv():
        ensure_venv()
        if venv_python().is_file():
            reexec_in_venv_if_needed()

    try:
        installed = setup_only(allow_install=allow_install)
    except SystemExit as exc:
        print("ERROR:", exc)
        return 1
    if installed:
        print("Installed:", ", ".join(installed))

    try:
        verify_imports()
    except SystemExit as exc:
        print("ERROR:", exc)
        return 1

    start_server(args.host, args.port, reload=args.dev, open_browser=args.open)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
