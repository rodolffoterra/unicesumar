@echo off
cd /d %~dp0
python -m uvicorn app.api.fastapi_app:app --reload
pause
