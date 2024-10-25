from typing import Callable

from fastapi.testclient import TestClient
from faker import Faker
import pytest


@pytest.fixture
def user_creation_msg(faker: Faker):
    """ Auto-Generated User Creation Object """
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "username": faker.user_name(),
        "password": faker.password()
    }

@pytest.fixture
def create_user_msg(faker: Faker) -> Callable[[], dict[str, str]]:
    """ User Creation Msg Factory """
    def _create_user_msg():
        return {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "username": faker.user_name(),
            "password": faker.password()
        }
    return _create_user_msg


@pytest.fixture
def create_user(
    user_creation_msg: dict[str, str], client: TestClient
) -> Callable[[], None]:
    """ User Creation Factory """
    def _create_user():
        """ Creates User in DB """
        response = client.post('/users', json=user_creation_msg)
        return response.json()
    return _create_user


@pytest.fixture
def register_user(client: TestClient) -> Callable[[int], None]:
    """ Registraion Factory """
    def _register_user(user_id: int, registration_code: str) -> dict[str, str]:
        """ Completes Registration for User """
        # TODO: impliment
    # return _register_user
    raise NotImplementedError()


@pytest.fixture
def populate_users(
    create_user: Callable[[], None], 
    register_user: Callable[[int], None]
) -> Callable[[int], None]:
    """ Returns DB user populate function """
    def _populate_users(num_users: int):
        """ populates DB with provided num of users """
        for _ in range(num_users):
            user = create_user()
            register_user(user['id'])
    return _populate_users


@pytest.fixture
def created_user(create_user, register_user):
    """ User in DB """
    user = create_user()
    # TODO: impliment
    # return register_user(user['id'])
    raise NotImplementedError()


@pytest.fixture
def registered_user(create_user, register_user):
    """ User in DB """
    user = create_user()
    # TODO: impliment
    # return register_user(user['id'])
    raise NotImplementedError()