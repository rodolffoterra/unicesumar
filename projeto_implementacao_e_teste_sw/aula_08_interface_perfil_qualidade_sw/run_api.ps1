Set-Location $PSScriptRoot
python -m uvicorn app.api.fastapi_app:app --reload
