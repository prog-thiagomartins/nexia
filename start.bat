@echo off
echo Iniciando WAT Studio...
cd /d "%~dp0"
pip install -r requirements.txt -q
start http://localhost:8000
uvicorn frontend.server:app --port 8000 --reload
