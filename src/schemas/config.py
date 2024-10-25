""" container for enviornment schema """
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    """ Container for required enviornment variables """
    model_config = SettingsConfigDict(env_file='.env', extra='forbid', env_ignore_empty=True)

    host: str = "localhost"
    port: str = "8000"

    log_level: Literal["critical", "error", "warning", "info", "debug" , "trace"] = "info"
    reload: bool = True

    keycloak_url: str = "http://localhost:8080"
    keycloak_realm: str = "creations"

    sqlalchemy_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432"
