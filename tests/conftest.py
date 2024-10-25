import pytest

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine

from custom_courseware_api.database import DatabaseManager, default_db_manager
from custom_courseware_api.main import app


@pytest.fixture
def client():
        """ create a test client that overrides get_session """
        test_db_manager = DatabaseManager(create_engine(
            "sqlite://", connect_args={"check_same_thread": False}, 
            poolclass=StaticPool
        ))
        test_db_manager.create_tables()

        app.dependency_overrides[
            default_db_manager.get_session
        ] = test_db_manager.get_session
        with TestClient(app) as test_client:
                yield test_client


# TODO: mock for read email, write email
