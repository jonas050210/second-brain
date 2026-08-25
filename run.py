"""Launch the Second Brain backend + UI.

Usage:  python run.py   (then open http://localhost:8000)
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=False)
