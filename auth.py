from fastapi.security.api_key import APIKeyHeader, APIKeyQuery
from fastapi import Security, HTTPException, Depends, status
from functools import lru_cache
import config


@lru_cache()
def get_settings():
    return config.Settings()


api_key_header = APIKeyHeader(name="api-key", auto_error=False)

async def get_api_key(settings: config.Settings = Depends(get_settings), api_key_header: str = Security(api_key_header)):
    if api_key_header == settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key in Header"
        )
