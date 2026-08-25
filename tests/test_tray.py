"""Tray and EXE icon tests. No activity watching."""
from pathlib import Path

from launcher import icons, tray


ROOT = Path(__file__).resolve().parent.parent


def test_activity_watch_is_hard_off():
    assert tray.should_watch_activity() is False
    assert tray.ACTIVITY_WATCH_ENABLED is False
    assert tray.ACTIVITY_POLL_SECONDS is None


def test_clip_remember_text_skips_empty_and_caps():
    assert tray.clip_remember_text("   ") is None
    assert tray.clip_remember_text("") is None
    long = "x" * 9000
    clipped = tray.clip_remember_text(long)
    assert clipped is not None and len(clipped) == 8000


def test_tray_source_has_no_activity_poller():
    src = Path(tray.__file__).read_text(encoding="utf-8")
    assert "GetForegroundWindow" not in src
    assert "BitBlt" not in src
    assert "SetWindowsHook" not in src
    assert "ACTIVITY_WATCH_ENABLED = False" in src
    assert "def should_watch_activity" in src


def test_icons_exist():
    ico = ROOT / "launcher" / "secondbrain.ico"
    png = ROOT / "launcher" / "secondbrain.png"
    assert ico.is_file() and ico.stat().st_size > 1000
    assert png.is_file() and png.stat().st_size > 1000
    assert icons.icon_ico() == ico
    assert icons.icon_png() == png


def test_spec_embeds_icon():
    spec = (ROOT / "secondbrain.spec").read_text(encoding="utf-8")
    assert 'icon="launcher/secondbrain.ico"' in spec
    assert "launcher/secondbrain.ico" in spec


def test_ico_has_standard_windows_sizes():
    import struct
    data = (ROOT / "launcher" / "secondbrain.ico").read_bytes()
    reserved, typ, count = struct.unpack_from("<HHH", data, 0)
    assert reserved == 0 and typ == 1 and count >= 4
    sizes = set()
    off = 6
    for _ in range(count):
        w, h = struct.unpack_from("<BB", data, off)
        sizes.add(w or 256)
        sizes.add(h or 256)
        off += 16
    assert {16, 32, 48, 256} <= sizes
