""" module for DB utilities and setup """
from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import StaticPool

from .config import config


class Base(DeclarativeBase): # pylint: disable=too-few-public-methods
    """ base class for all models """

default_engine = create_engine(
    config.SQLALCHEMY_URL, poolclass=StaticPool
)


class DatabaseManager:
    """ manages DB interactions """
    def __init__(self, engine: Engine = default_engine):
        self._engine = engine

    def get_session(self) -> Generator[Session, None, None]:
        """ returns open DB session to caller """
        try:
            session = Session(self._engine)
            yield session
        finally:
            session.close()


default_db_manager = DatabaseManager()
