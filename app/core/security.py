from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from app.core.config import get_settings

_settings = get_settings()

API_KEY = _settings.VERIFY_API_TOKEN  # store in Azure Key Vault / env var
API_KEY_NAME = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )