#!/usr/bin/env python3
"""Primary launcher for Second Brain.

Detects the environment, installs only genuinely missing runtime
dependencies, then starts the local web app.

Usage:
    python start.py
    python start.py --check     # verify environment, do not start
    python start.py --setup     # install / verify only

After a successful setup this script must NOT reinstall packages.
"""
from __future__ import annotations

import argparse
import importlib
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"

# import-name -> pip extra specifier
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
        # Don't follow the python symlink (venv/bin/python -> system python).
        raw = Path(sys.executable)
        if VENV_DIR.resolve() in raw.resolve().parents or str(VENV_DIR) in str(raw):
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
            "On Windows, try:  python -m pip install -r requirements.txt\n"
            f"pip exit code: {exc.returncode}"
        ) from exc


def ensure_venv() -> None:
    """Create .venv once if the current interpreter cannot import runtime deps."""
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
                "Install the Python venv module (Windows: re-run the official installer "
                "with 'pip' and 'venv' enabled) and retry."
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
        raise SystemExit(
            "Runtime packages are still missing after install: "
            + ", ".join(missing)
        )
    frontend = ROOT / "frontend" / "index.html"
    if not frontend.is_file():
        raise SystemExit(f"Frontend is missing: {frontend}")


def setup_only() -> list[str]:
    """Install missing runtime deps and prepare data dirs. Returns installed specs."""
    check_python()
    ensure_venv()
    # If we just created a venv, the *current* interpreter may still lack
    # packages. Caller should re-exec; we still try to install into current.
    missing = missing_runtime()
    installed: list[str] = []
    if missing:
        install_packages(missing)
        installed = missing
    create_dirs()
    return installed


def detect_environment() -> dict:
    info = {
        "python": sys.version.split()[0],
        "executable": sys.executable,
        "platform": sys.platform,
        "windows": is_windows(),
        "project": str(ROOT),
        "venv": running_in_project_venv(),
        "missing": missing_runtime(),
    }
    return info


def print_env(info: dict) -> None:
    print("Second Brain — environment")
    print(f"  Python     : {info['python']} ({info['executable']})")
    print(f"  Platform   : {info['platform']}")
    print(f"  Project    : {info['project']}")
    print(f"  Project venv: {'yes' if info['venv'] else 'no'}")
    print(f"  Missing    : {', '.join(info['missing']) if info['missing'] else 'none'}")


def start_server(host: str, port: int) -> None:
    os.chdir(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        import uvicorn
    except ImportError as exc:
        raise SystemExit(
            "uvicorn is not installed. Run:  python setup.py"
        ) from exc
    print()
    print("Starting Second Brain")
    print(f"  Local URL  : http://127.0.0.1:{port}")
    print(f"  Bind       : {host}:{port}")
    print("  Privacy    : LOCAL · PRIVATE · no telemetry")
    print("  Stop       : Ctrl+C")
    print()
    uvicorn.run("backend.app:app", host=host, port=port, reload=False, log_level="info")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Start Second Brain")
    parser.add_argument("--check", action="store_true", help="Verify environment and exit")
    parser.add_argument("--setup", action="store_true", help="Install missing deps and exit")
    parser.add_argument("--host", default=os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("SECOND_BRAIN_PORT", "8000")))
    args = parser.parse_args(argv)

    check_python()
    info = detect_environment()
    print_env(info)

    if args.check:
        create_dirs()
        if info["missing"] and not venv_python().is_file():
            print("FAIL: missing runtime packages:", ", ".join(info["missing"]))
            return 1
        if info["missing"] and venv_python().is_file() and not running_in_project_venv():
            # Recheck inside the project venv without starting the server.
            rc = subprocess.call([str(venv_python()), str(ROOT / "start.py"), "--check"])
            return rc
        try:
            verify_imports()
        except SystemExit as exc:
            print("FAIL:", exc)
            return 1
        print("OK: environment is ready.")
        return 0

    # Prefer the project venv so we never pip-install into a managed system Python.
    if missing_runtime() and not running_in_project_venv():
        ensure_venv()
        if venv_python().is_file():
            reexec_in_venv_if_needed()

    installed = setup_only()
    if installed:
        print("Installed:", ", ".join(installed))

    try:
        verify_imports()
    except SystemExit as exc:
        print("ERROR:", exc)
        return 1

    if args.setup:
        print("Setup complete. Run:  python start.py")
        return 0

    start_server(args.host, args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
