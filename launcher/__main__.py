"""Entry point for SecondBrain.exe and ``python -m launcher``."""
from __future__ import annotations

import argparse
import os
import sys
import threading
import webbrowser

# Make the project root importable when launched from another CWD.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from launcher.bootstrap import (  # noqa: E402
    APP_VERSION,
    bootstrap_ok,
    create_server,
    port_free,
    prepare_environment,
    run_bootstrap,
    start_existing_app,
    wait_for_http,
)
from launcher.gui import native_alert, run_gui_bootstrap, tk_available  # noqa: E402


def _already_running(url: str, headless: bool) -> None:
    msg = (
        f"Second Brain is already running at {url}.\n"
        "If that is not this app, choose another port with --port."
    )
    if headless:
        print(msg)
        return
    native_alert("Second Brain", msg)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Second Brain desktop launcher")
    parser.add_argument("--headless", action="store_true",
                        help="No GUI (used by tests and servers without tkinter)")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--no-install", action="store_true")
    parser.add_argument("--pull-models", action="store_true",
                        help="Download missing Ollama models (off by default)")
    parser.add_argument("--host", default=os.environ.get("SECOND_BRAIN_HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int,
                        default=int(os.environ.get("SECOND_BRAIN_PORT", "8000")))
    parser.add_argument("--check", action="store_true", help="Bootstrap only, do not start")
    args = parser.parse_args(argv)

    prepare_environment()

    host, port = args.host, args.port
    url = f"http://127.0.0.1:{port}"
    headless = bool(args.headless or args.check or not tk_available())

    if not port_free("127.0.0.1", port):
        _already_running(url, headless=headless or args.check)
        if not args.no_browser and not args.check:
            webbrowser.open(url)
        return 0

    def steps(on_progress):
        return run_bootstrap(
            on_progress=on_progress,
            allow_install=not args.no_install,
            pull_models=args.pull_models,
        )

    def start():
        start_existing_app(host, port)

    if args.check or args.headless:
        print(f"Second Brain v{APP_VERSION}")
        results = steps(lambda t, d: print(f"  {t}" + (f" — {d}" if d else "")))
        if not bootstrap_ok(results):
            bad = next((r for r in results if not r.ok), None)
            print("FAILED:", bad.detail if bad else "bootstrap failed")
            return 1
        print("OK: bootstrap complete")
        if args.check:
            return 0
        if not args.no_browser:
            threading.Thread(
                target=lambda: wait_for_http(url) and webbrowser.open(url),
                daemon=True,
            ).start()
        start()
        return 0

    return run_gui_bootstrap(
        steps,
        start,
        url,
        open_browser=not args.no_browser,
        create_server=lambda: create_server(host, port),
    )


if __name__ == "__main__":
    raise SystemExit(main())
