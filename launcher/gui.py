"""Dark setup window for SecondBrain.exe.

Uses tkinter when available (bundled on Windows). Falls back to stdout so
tests and headless environments still run the same bootstrap.

The setup window is the process lifetime for a windowed EXE: after checks
succeed the existing FastAPI app is started on a worker thread and the
window stays open (Open browser / Quit). Closing the window stops the
server. The server is never left on a daemon thread that dies with the UI.
"""
from __future__ import annotations

import os
import sys
import threading
import webbrowser
from typing import Callable

from launcher.bootstrap import APP_VERSION, StepResult, bootstrap_ok, wait_for_http
from launcher.icons import icon_ico, icon_png

BG = "#070a13"
PANEL = "#0f1628"
TEXT = "#e7ecf5"
MUTED = "#8b95a8"
ACCENT = "#22d3ee"
OK = "#34d399"
DANGER = "#f87171"
WARN = "#fbbf24"
ACCENT2 = "#8b5cf6"
LINE = "#1e293b"


def tk_available() -> bool:
    try:
        import tkinter  # noqa: F401
        return True
    except Exception:
        return False


def apply_window_icon(root) -> None:
    """Set the setup-window icon when the PNG/ICO shipped with the EXE exists."""
    png = icon_png()
    if png is not None:
        try:
            img = root.tk.call("image", "create", "photo", "-file", str(png))
            root.tk.call("wm", "iconphoto", root._w, img)
            root._sb_icon = img
        except Exception:
            try:
                import tkinter as tk
                photo = tk.PhotoImage(file=str(png))
                root.iconphoto(True, photo)
                root._sb_icon = photo
            except Exception:
                pass
    ico = icon_ico()
    if ico is not None and os.name == "nt":
        try:
            root.iconbitmap(str(ico))
        except Exception:
            pass


def native_alert(title: str, message: str) -> None:
    """Visible alert when there is no console (windowed EXE)."""
    if tk_available():
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            messagebox.showinfo(title, message)
            root.destroy()
            return
        except Exception:
            pass
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
            return
        except Exception:
            pass
    print(f"{title}: {message}")


class SetupWindow:
    def __init__(self):
        import tkinter as tk
        from tkinter import ttk

        self.tk = tk
        self.root = tk.Tk()
        self.root.title("Second Brain")
        self.root.configure(bg=BG)
        self.root.geometry("620x580")
        self.root.minsize(520, 460)
        self.root.resizable(True, True)
        apply_window_icon(self.root)

        self._status = tk.StringVar(value="Initializing Second Brain")
        self._ollama = tk.StringVar(value="Ollama: checking…")
        self._state = tk.StringVar(value="WORKING")
        self._closed = False
        self._server = None
        self.on_quit: Callable[[], None] | None = None

        pad = {"padx": 24, "pady": 2}
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", **pad)
        tk.Label(
            header, text="◈  SECOND BRAIN", fg=ACCENT, bg=BG,
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", pady=(12, 0))
        tk.Label(
            header, text=f"local knowledge OS  ·  v{APP_VERSION}",
            fg=MUTED, bg=BG, font=("Segoe UI", 9),
        ).pack(anchor="w")

        accent = tk.Frame(self.root, bg=ACCENT2, height=2)
        accent.pack(fill="x", padx=24, pady=(10, 4))

        tk.Label(
            self.root, textvariable=self._status, fg=TEXT, bg=BG,
            font=("Segoe UI", 13), wraplength=560, justify="left",
        ).pack(fill="x", padx=24, pady=(14, 6))

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure(
            "SB.Horizontal.TProgressbar",
            troughcolor=PANEL,
            background=ACCENT,
            bordercolor=PANEL,
            lightcolor=ACCENT,
            darkcolor=ACCENT2,
            thickness=10,
        )
        self.bar = ttk.Progressbar(
            self.root, style="SB.Horizontal.TProgressbar",
            mode="determinate", maximum=100,
        )
        self.bar.pack(fill="x", padx=24, pady=8)

        self.ollama_label = tk.Label(
            self.root, textvariable=self._ollama, fg=MUTED, bg=BG,
            font=("Segoe UI", 9),
        )
        self.ollama_label.pack(anchor="w", padx=24)

        log_frame = tk.Frame(self.root, bg=PANEL, highlightbackground=LINE,
                             highlightthickness=1)
        log_frame.pack(fill="both", expand=True, padx=24, pady=12)
        self.log = tk.Text(
            log_frame, bg=PANEL, fg=MUTED, insertbackground=TEXT,
            relief="flat", font=("Consolas", 9), wrap="word",
            state="disabled", height=12, borderwidth=0, highlightthickness=0,
        )
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=24, pady=(0, 16))
        self.footer = tk.Label(
            footer, textvariable=self._state, fg=ACCENT, bg=BG,
            font=("Segoe UI", 10, "bold"),
        )
        self.footer.pack(side="left")

        self.btn_row = tk.Frame(footer, bg=BG)
        self.btn_row.pack(side="right")
        self.btn_open = tk.Button(
            self.btn_row, text="Open browser", command=self._open_browser,
            bg="#132337", fg=ACCENT, activebackground="#1e3a4c",
            activeforeground=ACCENT, relief="flat", padx=12, pady=5,
            font=("Segoe UI", 9), cursor="hand2",
        )
        self.btn_quit = tk.Button(
            self.btn_row, text="Quit", command=self._on_close,
            bg="#1a1520", fg=MUTED, activebackground="#2a2030",
            activeforeground=TEXT, relief="flat", padx=12, pady=5,
            font=("Segoe UI", 9), cursor="hand2",
        )
        self.btn_tray = tk.Button(
            self.btn_row, text="Hide to tray", command=self._hide_to_tray,
            bg="#132337", fg=MUTED, activebackground="#1e3a4c",
            activeforeground=TEXT, relief="flat", padx=12, pady=5,
            font=("Segoe UI", 9), cursor="hand2",
        )
        self._url = "http://127.0.0.1:8000"
        self._tray = None

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _open_browser(self) -> None:
        try:
            webbrowser.open(self._url)
        except Exception:
            self.append_log("Could not open the browser. Visit " + self._url)

    def _hide_to_tray(self) -> None:
        """Hide the setup window. Tray does not watch the desktop."""
        try:
            self.root.withdraw()
        except Exception:
            pass
        self.append_log("Hidden. Tray / taskbar keeps Second Brain running. It does not watch what you do.")

    def _show_window(self) -> None:
        try:
            self.root.deiconify()
            self.root.lift()
        except Exception:
            pass

    def _on_close(self) -> None:
        if self._closed:
            return
        self._closed = True
        if self._tray is not None:
            try:
                self._tray.stop()
            except Exception:
                pass
        server = self._server
        if server is not None:
            try:
                server.should_exit = True
            except Exception:
                pass
        if self.on_quit:
            try:
                self.on_quit()
            except Exception:
                pass
        try:
            self.root.destroy()
        except Exception:
            pass

    def set_progress(self, percent: float, title: str, detail: str = "") -> None:
        if self._closed:
            return
        self._status.set(title)
        self.bar["value"] = max(0, min(100, percent))
        if detail:
            self.append_log(f"{title} — {detail}")
        else:
            self.append_log(title)
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def append_log(self, line: str) -> None:
        if self._closed:
            return
        self.log.configure(state="normal")
        self.log.insert("end", line.rstrip() + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def set_ollama(self, text: str, ok: bool | None = None) -> None:
        if self._closed:
            return
        self._ollama.set(text)
        if ok is True:
            self.ollama_label.configure(fg=OK)
        elif ok is False:
            self.ollama_label.configure(fg=WARN)
        else:
            self.ollama_label.configure(fg=MUTED)
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def succeed(self, url: str, server=None) -> None:
        if self._closed:
            return
        self._url = url
        self._server = server
        self._state.set("READY")
        self.footer.configure(fg=OK)
        self._status.set("Second Brain is running")
        self.bar["value"] = 100
        self.append_log(f"Started existing FastAPI app at {url}")
        self.append_log("Tray will not watch your screen or apps. Remember clipboard is click-only.")
        self.btn_open.pack(side="left", padx=(0, 8))
        self.btn_tray.pack(side="left", padx=(0, 8))
        self.btn_quit.pack(side="left")
        try:
            from launcher.tray import TrayController
            tray = TrayController(
                url, on_open=self._open_browser,
                on_show=self._show_window, on_quit=self._on_close,
            )
            if tray.start():
                self._tray = tray
                self.append_log("System tray icon ready (Open / Remember clipboard / Quit).")
        except Exception as exc:
            self.append_log(f"Tray unavailable ({exc}). Use Hide to tray / Quit.")
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def fail(self, message: str) -> None:
        if self._closed:
            return
        self._state.set("FAILED")
        self.footer.configure(fg=DANGER)
        self._status.set(message)
        self.append_log("ERROR: " + message)
        self.btn_quit.configure(text="Close")
        self.btn_quit.pack(side="left")
        try:
            self.root.update_idletasks()
        except Exception:
            pass

    def run(self) -> None:
        self.root.mainloop()


def _run_headless(
    steps: Callable[[Callable[[str, str], None]], list[StepResult]],
    start_server: Callable[[], None],
    url: str,
    open_browser: bool,
) -> int:
    print(f"Second Brain v{APP_VERSION} — setup (headless)")
    results = steps(lambda t, d: print(f"  {t}" + (f" — {d}" if d else "")))
    if not bootstrap_ok(results):
        bad = next((r for r in results if not r.ok), None)
        msg = bad.detail if bad else "unknown error"
        print("FAILED:", msg)
        if os.name == "nt" and getattr(sys, "frozen", False):
            native_alert("Second Brain — setup failed", msg)
        return 1
    print("OK: bootstrap complete")
    if open_browser:
        threading.Thread(
            target=lambda: wait_for_http(url) and webbrowser.open(url),
            daemon=True,
        ).start()
    start_server()
    return 0


def run_gui_bootstrap(
    steps: Callable[[Callable[[str, str], None]], list[StepResult]],
    start_server: Callable[[], None],
    url: str,
    open_browser: bool = True,
    create_server: Callable | None = None,
    start_hidden: bool = False,
) -> int:
    """Show the window, run checks, then keep the existing app alive."""
    if not tk_available():
        return _run_headless(steps, start_server, url, open_browser)

    win = SetupWindow()
    outcome = {"ok": False, "error": ""}
    server_holder: dict = {"server": None}

    def worker():
        seen: list[str] = []

        def progress(title: str, detail: str = "") -> None:
            seen.append(title)
            pct = min(95, 8 + len(seen) * 8)
            win.root.after(0, lambda t=title, d=detail, p=pct: win.set_progress(p, t, d))

        try:
            results = steps(progress)
            ollama_step = next((r for r in results if r.key == "ollama"), None)
            if ollama_step:
                offline = "offline" in (ollama_step.detail or "").lower()
                text = "Ollama: " + (ollama_step.detail or "unknown")
                win.root.after(0, lambda t=text, off=offline: win.set_ollama(t, ok=not off))
            if not bootstrap_ok(results):
                bad = next((r for r in results if not r.ok), None)
                outcome["error"] = (bad.detail or bad.title) if bad else "Setup failed"
                win.root.after(0, lambda: win.fail(outcome["error"]))
                return
            outcome["ok"] = True

            def ready():
                server = None
                if create_server is not None:
                    server = create_server()
                    server_holder["server"] = server
                    threading.Thread(
                        target=server.run, name="second-brain-server", daemon=True,
                    ).start()
                else:
                    threading.Thread(
                        target=start_server, name="second-brain-server", daemon=True,
                    ).start()
                win.succeed(url, server=server)
                if start_hidden:
                    win._hide_to_tray()
                if open_browser:
                    threading.Thread(
                        target=lambda: wait_for_http(url) and webbrowser.open(url),
                        daemon=True,
                    ).start()

            win.root.after(0, ready)
        except Exception as exc:
            outcome["error"] = str(exc)
            win.root.after(0, lambda m=str(exc): win.fail(m))

    threading.Thread(target=worker, daemon=True).start()
    win.run()
    server = server_holder.get("server")
    if server is not None:
        try:
            server.should_exit = True
        except Exception:
            pass
    return 0 if outcome["ok"] else 1
