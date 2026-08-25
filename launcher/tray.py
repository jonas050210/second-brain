"""Optional system tray for SecondBrain.exe.

The tray NEVER watches the user. It does not screenshot, read window titles,
keylog, or poll “what you are doing.” Those would fill the brain with junk
and secrets.

Menu actions are explicit clicks only:

- Open browser
- Remember clipboard  (user-initiated; same /api/chat path)
- Show window
- Quit

Activity auto-capture is a non-goal.
"""
from __future__ import annotations

import json
import os
import sys
import threading
import urllib.error
import urllib.request
from typing import Callable

# Hard rule: this module must not grow an activity watcher.
ACTIVITY_WATCH_ENABLED = False
ACTIVITY_POLL_SECONDS = None


def should_watch_activity() -> bool:
    """Always False. Auto-capture of the desktop is not a feature."""
    return False


def clip_remember_text(text: str, limit: int = 8000) -> str | None:
    """Return clipboard text worth sending, or None if empty."""
    raw = (text or "").strip()
    if not raw:
        return None
    if len(raw) > limit:
        raw = raw[:limit]
    return raw


def post_remember(url: str, text: str, timeout: float = 8.0) -> dict:
    """POST clipboard text into the existing chat/extract pipeline."""
    payload = json.dumps({"content": text}).encode("utf-8")
    req = urllib.request.Request(
        url.rstrip("/") + "/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    try:
        return json.loads(body)
    except ValueError:
        return {"ok": False, "error": "invalid response"}


def read_clipboard() -> str:
    """Best-effort clipboard read. Empty string if unavailable."""
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            user32 = ctypes.windll.user32
            kernel32 = ctypes.windll.kernel32
            CF_UNICODETEXT = 13
            if not user32.OpenClipboard(None):
                return ""
            try:
                handle = user32.GetClipboardData(CF_UNICODETEXT)
                if not handle:
                    return ""
                ptr = kernel32.GlobalLock(handle)
                if not ptr:
                    return ""
                try:
                    return ctypes.wstring_at(ptr)
                finally:
                    kernel32.GlobalUnlock(handle)
            finally:
                user32.CloseClipboard()
        except Exception:
            return ""
    try:
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()
        try:
            return root.clipboard_get()
        finally:
            root.destroy()
    except Exception:
        return ""


class TrayController:
    """Holds callbacks the GUI wires up. No background activity sampling."""

    def __init__(self, url: str, on_open: Callable[[], None] | None = None,
                 on_show: Callable[[], None] | None = None,
                 on_quit: Callable[[], None] | None = None):
        self.url = url
        self.on_open = on_open
        self.on_show = on_show
        self.on_quit = on_quit
        self._alive = False

    def remember_clipboard(self) -> dict:
        text = clip_remember_text(read_clipboard())
        if not text:
            return {"ok": False, "error": "clipboard empty"}
        try:
            return post_remember(self.url, text)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return {"ok": False, "error": str(exc)}

    def start(self) -> bool:
        """Start a Windows tray icon if possible. Never starts an activity poll."""
        if should_watch_activity():
            raise RuntimeError("activity watch must stay disabled")
        if os.name != "nt":
            return False
        self._alive = True
        thread = threading.Thread(target=self._win_loop, name="second-brain-tray",
                                  daemon=True)
        thread.start()
        return True

    def stop(self) -> None:
        self._alive = False

    def _win_loop(self) -> None:
        """Best-effort NotifyIcon. Failures are silent; the setup window remains."""
        try:
            self._win_notify()
        except Exception:
            self._alive = False

    def _win_notify(self) -> None:
        import ctypes
        from ctypes import wintypes

        from launcher.icons import icon_ico

        user32 = ctypes.windll.user32
        shell32 = ctypes.windll.shell32

        WM_USER = 0x0400
        WM_TRAY = WM_USER + 42
        WM_LBUTTONUP = 0x0202
        WM_RBUTTONUP = 0x0205
        NIM_ADD, NIM_DELETE = 0x00000000, 0x00000002
        NIF_MESSAGE, NIF_ICON, NIF_TIP = 0x00000001, 0x00000002, 0x00000004
        ID_OPEN, ID_CLIP, ID_SHOW, ID_QUIT = 1001, 1002, 1003, 1004

        class NOTIFYICONDATA(ctypes.Structure):
            _fields_ = [
                ("cbSize", wintypes.DWORD),
                ("hWnd", wintypes.HWND),
                ("uID", wintypes.UINT),
                ("uFlags", wintypes.UINT),
                ("uCallbackMessage", wintypes.UINT),
                ("hIcon", wintypes.HICON),
                ("szTip", ctypes.c_wchar * 128),
            ]

        WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, wintypes.HWND, wintypes.UINT,
                                     wintypes.WPARAM, wintypes.LPARAM)

        def wndproc(hwnd, msg, wparam, lparam):
            if msg == WM_TRAY and lparam in (WM_LBUTTONUP, WM_RBUTTONUP):
                if lparam == WM_LBUTTONUP and self.on_open:
                    self.on_open()
                elif lparam == WM_RBUTTONUP:
                    self._popup(hwnd, user32, ID_OPEN, ID_CLIP, ID_SHOW, ID_QUIT)
            elif msg == 0x0111:  # WM_COMMAND
                cmd = wparam & 0xFFFF
                if cmd == ID_OPEN and self.on_open:
                    self.on_open()
                elif cmd == ID_CLIP:
                    self.remember_clipboard()
                elif cmd == ID_SHOW and self.on_show:
                    self.on_show()
                elif cmd == ID_QUIT and self.on_quit:
                    self.on_quit()
            return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

        self._wndproc = WNDPROC(wndproc)

        class WNDCLASS(ctypes.Structure):
            _fields_ = [
                ("style", wintypes.UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", ctypes.c_int),
                ("cbWndExtra", ctypes.c_int),
                ("hInstance", wintypes.HINSTANCE),
                ("hIcon", wintypes.HICON),
                ("hCursor", wintypes.HCURSOR),
                ("hbrBackground", wintypes.HBRUSH),
                ("lpszMenuName", wintypes.LPCWSTR),
                ("lpszClassName", wintypes.LPCWSTR),
            ]

        wc = WNDCLASS()
        wc.lpfnWndProc = self._wndproc
        wc.hInstance = kernel32_instance()
        wc.lpszClassName = "SecondBrainTray"
        if not user32.RegisterClassW(ctypes.byref(wc)):
            return
        hwnd = user32.CreateWindowExW(0, wc.lpszClassName, "Second Brain",
                                      0, 0, 0, 0, 0, None, None, wc.hInstance, None)
        if not hwnd:
            return

        ico_path = icon_ico()
        hicon = None
        if ico_path:
            hicon = user32.LoadImageW(None, str(ico_path), 1, 16, 16, 0x00000010)
        if not hicon:
            hicon = user32.LoadIconW(None, 32512)

        nid = NOTIFYICONDATA()
        nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
        nid.hWnd = hwnd
        nid.uID = 1
        nid.uFlags = NIF_MESSAGE | NIF_ICON | NIF_TIP
        nid.uCallbackMessage = WM_TRAY
        nid.hIcon = hicon
        nid.szTip = "Second Brain"
        shell32.Shell_NotifyIconW(NIM_ADD, ctypes.byref(nid))

        msg = wintypes.MSG()
        while self._alive and user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

        shell32.Shell_NotifyIconW(NIM_DELETE, ctypes.byref(nid))

    def _popup(self, hwnd, user32, id_open, id_clip, id_show, id_quit) -> None:
        import ctypes
        from ctypes import wintypes

        try:
            menu = user32.CreatePopupMenu()
            user32.AppendMenuW(menu, 0, id_open, "Open browser")
            user32.AppendMenuW(menu, 0, id_clip, "Remember clipboard")
            user32.AppendMenuW(menu, 0, id_show, "Show window")
            user32.AppendMenuW(menu, 0, id_quit, "Quit")
            pt = wintypes.POINT()
            user32.GetCursorPos(ctypes.byref(pt))
            user32.SetForegroundWindow(hwnd)
            user32.TrackPopupMenu(menu, 0, pt.x, pt.y, 0, hwnd, None)
            user32.DestroyMenu(menu)
        except Exception:
            pass


def kernel32_instance():
    import ctypes
    return ctypes.windll.kernel32.GetModuleHandleW(None)
