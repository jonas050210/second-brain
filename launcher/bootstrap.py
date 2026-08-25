"""Idempotent bootstrap steps for the existing Second Brain application.

Never deletes ``brain.db``. Never resets memories. Installs a package only
when that import is actually missing and we are not running frozen.
"""
from __future__ import annotations

import importlib
import os
import socket
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

from backend import paths

APP_VERSION = paths.APP_VERSION
REQUIRED_MODELS = ("qwen3:0.6b", "nomic-embed-text")
RUNTIME_IMPORTS = (
    ("fastapi", "fastapi>=0.110"),
    ("uvicorn", "uvicorn[standard]>=0.29"),
    ("requests", "requests>=2.31"),
    ("numpy", "numpy>=1.26"),
)

# Exact status lines the setup UI must show, in order.
STATUS_LINES = (
    "Initializing Second Brain",
    "Checking Python/runtime",
    "Checking dependencies",
    "Installing only missing dependencies",
    "Checking database",
    "Checking configuration",
    "Checking Ollama",
    "Checking required models",
    "Running health checks",
    "Starting Second Brain",
)


@dataclass
class StepResult:
    key: str
    title: str
    ok: bool
    detail: str = ""
    skipped: bool = False
    installed: list[str] = field(default_factory=list)


OnProgress = Callable[[str, str], None]


def _emit(cb: OnProgress | None, title: str, detail: str = "") -> None:
    if cb:
        cb(title, detail)


def _missing_imports() -> list[tuple[str, str]]:
    missing = []
    for mod, spec in RUNTIME_IMPORTS:
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append((mod, spec))
    return missing


def _model_present(installed: Iterable[str], wanted: str) -> bool:
    wanted = (wanted or "").strip()
    for name in installed:
        if not name:
            continue
        if name == wanted or name.startswith(wanted + "-") or name.startswith(wanted + ":"):
            return True
        if name.split("-", 1)[0] == wanted:
            return True
    return False


def probe_ollama(url: str | None = None, timeout: float = 2.0) -> dict:
    url = (url or os.environ.get("OLLAMA_BASE_URL") or "http://localhost:11434").rstrip("/")
    if not url.startswith(("http://", "https://")):
        return {"available": False, "url": url, "models": [], "error": "URL must be http(s)"}
    try:
        import requests
        r = requests.get(url + "/api/tags", timeout=timeout)
        if r.status_code != 200:
            return {"available": False, "url": url, "models": [], "error": f"HTTP {r.status_code}"}
        models = [m.get("name") for m in r.json().get("models", [])]
        return {"available": True, "url": url, "models": models, "error": None}
    except Exception as exc:
        return {"available": False, "url": url, "models": [], "error": str(exc) or exc.__class__.__name__}


def port_free(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.4)
    try:
        return sock.connect_ex((host if host != "0.0.0.0" else "127.0.0.1", port)) != 0
    finally:
        sock.close()


def prepare_environment() -> Path:
    """Resolve and export the persistent DB path before backend import.

    If this process already opened a real database (tests, long-running
    server), keep that file. Never redirect away from an existing brain.
    """
    db_path = paths.resolve_db_path()
    if "backend.config" in sys.modules:
        current = Path(getattr(sys.modules["backend.config"], "DB_PATH", ""))
        if current.is_file() and not paths._is_ephemeral(current):
            db_path = current
    paths.ensure_data_dirs(db_path)
    os.environ["SECOND_BRAIN_DB"] = str(db_path)
    if "backend.config" in sys.modules:
        sys.modules["backend.config"].DB_PATH = str(db_path)
    root = str(paths.app_root())
    if root not in sys.path:
        sys.path.insert(0, root)
    return db_path


def run_bootstrap(
    on_progress: OnProgress | None = None,
    allow_install: bool = True,
    pull_models: bool = False,
) -> list[StepResult]:
    """Run lightweight, idempotent checks. Returns one result per step."""
    results: list[StepResult] = []

    def add(step: StepResult) -> StepResult:
        results.append(step)
        _emit(on_progress, step.title, step.detail)
        return step

    add(StepResult("init", "Initializing Second Brain", True, f"version {APP_VERSION}"))

    py = sys.version.split()[0]
    frozen = paths.is_frozen()
    if sys.version_info < (3, 11):
        add(StepResult("python", "Checking Python/runtime", False,
                       f"Python 3.11+ required (found {py})"))
        return results
    add(StepResult(
        "python", "Checking Python/runtime", True,
        f"Python {py}" + (" · packaged runtime" if frozen else ""),
    ))

    missing = _missing_imports()
    if not missing:
        add(StepResult("deps", "Checking dependencies", True, "all runtime imports present"))
        add(StepResult("install", "Installing only missing dependencies", True,
                       "nothing to install", skipped=True))
    elif frozen:
        names = ", ".join(m for m, _ in missing)
        add(StepResult("deps", "Checking dependencies", False,
                       f"packaged runtime is missing: {names}"))
        add(StepResult("install", "Installing only missing dependencies", False,
                       "cannot pip-install into a frozen EXE — rebuild SecondBrain.exe",
                       skipped=True))
        return results
    else:
        add(StepResult("deps", "Checking dependencies", True,
                       "missing: " + ", ".join(m for m, _ in missing)))
        if not allow_install:
            add(StepResult("install", "Installing only missing dependencies", False,
                           "install disabled and packages are missing: "
                           + ", ".join(m for m, _ in missing)))
            return results
        specs = [spec for _, spec in missing]
        _emit(on_progress, "Installing only missing dependencies", ", ".join(specs))
        try:
            import start as start_mod
            start_mod.install_packages(specs)
        except SystemExit as exc:
            add(StepResult("install", "Installing only missing dependencies", False,
                           str(exc) or "pip failed"))
            return results
        except Exception as exc:
            add(StepResult("install", "Installing only missing dependencies", False, str(exc)))
            return results
        still = _missing_imports()
        if still:
            add(StepResult("install", "Installing only missing dependencies", False,
                           "still missing after install: " + ", ".join(m for m, _ in still)))
            return results
        add(StepResult("install", "Installing only missing dependencies", True,
                       "installed: " + ", ".join(specs), installed=specs))

    db_path = prepare_environment()
    existed = db_path.is_file()
    if existed:
        try:
            size = db_path.stat().st_size
        except OSError as exc:
            add(StepResult("database", "Checking database", False,
                           f"cannot read {db_path}: {exc}"))
            return results
        add(StepResult("database", "Checking database", True,
                       f"preserving existing {db_path} ({size} bytes)"))
    else:
        add(StepResult("database", "Checking database", True,
                       f"no database yet; will create {db_path} on first API start"))

    frontend = paths.frontend_dir() / "index.html"
    if not frontend.is_file():
        add(StepResult("config", "Checking configuration", False,
                       f"frontend missing at {frontend}"))
        return results
    add(StepResult("config", "Checking configuration", True,
                   f"frontend {frontend.parent} · db {db_path}"))

    pull = pull_models or os.environ.get("SECOND_BRAIN_PULL_MODELS") == "1"
    oll = probe_ollama()
    if oll["available"]:
        add(StepResult("ollama", "Checking Ollama", True,
                       f"online at {oll['url']}"))
        installed = oll["models"]
        missing_models = [m for m in REQUIRED_MODELS if not _model_present(installed, m)]
        if not missing_models:
            add(StepResult("models", "Checking required models", True,
                           "found " + ", ".join(REQUIRED_MODELS)))
        elif pull:
            _emit(on_progress, "Checking required models",
                  "pulling " + ", ".join(missing_models))
            pulled, errors = [], []
            for model in missing_models:
                try:
                    import requests
                    r = requests.post(oll["url"] + "/api/pull",
                                      json={"name": model, "stream": False},
                                      timeout=600)
                    if r.status_code == 200:
                        pulled.append(model)
                    else:
                        errors.append(f"{model}: HTTP {r.status_code}")
                except Exception as exc:
                    errors.append(f"{model}: {exc}")
            add(StepResult(
                "models", "Checking required models", not errors,
                ("pulled " + ", ".join(pulled) if pulled else "")
                + (("; " + "; ".join(errors)) if errors else ""),
            ))
        else:
            add(StepResult(
                "models", "Checking required models", True,
                "not installed: " + ", ".join(missing_models)
                + " — will use fallback (no download)",
                skipped=True,
            ))
    else:
        why = oll.get("error") or "unreachable"
        add(StepResult("ollama", "Checking Ollama", True,
                       f"offline ({oll['url']}: {why}) — fallback extractor will be used"))
        add(StepResult("models", "Checking required models", True,
                       "skipped (Ollama offline)", skipped=True))

    try:
        from backend import db, store
        db.init_db()
        store.ensure_user_entity()
        n = db.query("SELECT COUNT(*) c FROM entities")[0]["c"]
        add(StepResult("health", "Running health checks", True,
                       f"database open · {n} entit{'y' if n == 1 else 'ies'}"))
    except Exception as exc:
        add(StepResult("health", "Running health checks", False,
                       f"database/health failed: {exc}"))
        return results

    add(StepResult("start", "Starting Second Brain", True, "ready"))
    return results


def bootstrap_ok(results: list[StepResult]) -> bool:
    return bool(results) and all(r.ok for r in results)


def create_server(host: str, port: int):
    """Build a uvicorn.Server around the existing FastAPI app."""
    os.chdir(paths.app_root())
    import uvicorn
    from backend.app import app
    config = uvicorn.Config(app, host=host, port=port, reload=False, log_level="info")
    return uvicorn.Server(config)


def start_existing_app(host: str, port: int) -> None:
    """Start the existing FastAPI app. Not a second server implementation."""
    create_server(host, port).run()


def wait_for_http(url: str, timeout: float = 30.0) -> bool:
    deadline = time.time() + timeout
    try:
        import requests
    except ImportError:
        return False
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            if r.status_code < 500:
                return True
        except Exception:
            time.sleep(0.2)
    return False
