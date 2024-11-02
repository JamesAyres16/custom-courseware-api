""" container for enviornment schema """
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    """ Container for required enviornment variables """
    model_config = SettingsConfigDict(env_prefix="APP", frozen=True)

    SQLALCHEMY_URL: str

    KEYCLOAK_URL: str
    KEYCLOAK_REALM: str
