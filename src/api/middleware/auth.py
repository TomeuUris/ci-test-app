from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from src.core.settings.authentication import get_authentication_settings

api_key_header = APIKeyHeader(name='access_token', auto_error=False)

async def check_api_key(api_key_header: str = Security(api_key_header)):
    settings = get_authentication_settings()
    if api_key_header == settings.apiKey:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail='Could not validate API KEY'
        )