# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for SecondBrain.exe
# Run on Windows 11:  python -m launcher.build_exe
# Output: dist/SecondBrain.exe
#
# This freezes the launcher + existing FastAPI app. It is not a second
# implementation. The database is resolved at runtime next to the EXE
# (portable) or under LOCALAPPDATA — never inside the extract directory.

from PyInstaller.utils.hooks import collect_all, collect_submodules

datas = [
    ("frontend", "frontend"),
    (".env.example", "."),
]
binaries = []
hidden = []

for pkg in ("uvicorn", "fastapi", "starlette", "anyio", "pydantic", "pydantic_core",
            "numpy", "requests", "urllib3", "certifi", "idna", "charset_normalizer",
            "h11", "click", "sniffio"):
    try:
        d, b, h = collect_all(pkg)
        datas += d
        binaries += b
        hidden += h
    except Exception:
        try:
            hidden += collect_submodules(pkg)
        except Exception:
            pass

hidden += [
    "tkinter", "tkinter.ttk", "tkinter.messagebox",
    "uvicorn.logging", "uvicorn.loops", "uvicorn.loops.auto",
    "uvicorn.protocols", "uvicorn.protocols.http", "uvicorn.protocols.http.auto",
    "uvicorn.protocols.http.h11_impl",
    "uvicorn.protocols.websockets", "uvicorn.protocols.websockets.auto",
    "uvicorn.lifespan", "uvicorn.lifespan.on", "uvicorn.lifespan.off",
    "backend.app", "backend.db", "backend.store", "backend.config",
    "backend.paths", "backend.extract", "backend.fallback", "backend.search",
    "backend.graph", "backend.commands", "backend.export", "backend.backup",
    "backend.summarize", "backend.ollama",
    "launcher", "launcher.bootstrap", "launcher.gui",
    "multipart", "python_multipart",
]

seen = set()
hidden_unique = []
for name in hidden:
    if name not in seen:
        seen.add(name)
        hidden_unique.append(name)

a = Analysis(
    ["launcher/__main__.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
    hiddenimports=hidden_unique,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pytest", "playwright", "tkinter.test"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="SecondBrain",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=False,
)
