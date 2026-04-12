@echo off
cd /d "%~dp0"
start "" http://localhost:8765
python -m uvicorn main:app --port 8765
