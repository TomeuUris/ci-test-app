from pydantic_settings import BaseSettings


class AuthenticationSettings(BaseSettings):
    apiKey: str = '_MySecret4piKey!'
    model_config = {
        'env_prefix': 'authentication_'
    }


def get_authentication_settings():
    return AuthenticationSettings()