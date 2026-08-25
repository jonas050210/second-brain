@echo off
title Second Brain
echo ============================================
echo   Second Brain — local AI knowledge graph
echo ============================================
echo.
echo 1) Make sure Ollama is running with:
echo      ollama pull qwen3:0.6b
echo      ollama pull nomic-embed-text
echo.
echo 2) Starting the app at http://localhost:8000
echo.
python run.py
pause
