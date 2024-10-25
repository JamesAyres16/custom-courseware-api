""" Test for User Retrieval """
from fastapi.testclient import TestClient
from faker import Faker
import pytest


def test_no_users(client: TestClient):
    """ verifies the API returns an empty arrary when DB is empty """
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.skip
def test_get_user(user, client: TestClient):
    """ verifies that a specific user can be pulled """
    response = client.get(f'/users/{user['id']}')
    assert response.status_code == 200
    assert user == response.json()


def test_get_nonexistent_user(faker: Faker, client: TestClient):
    """ verifies that not found error is returned when a user doesn't exist """
    response = client.get(f'/users/{faker.random_int()}')
    assert response.status_code == 404


@pytest.mark.skip
def test_get_users():
    """ verifies retreival of multiple users """
    assert False


@pytest.mark.skip
def test_user_search():
    """ verifies user search """
    assert False


@pytest.mark.skip
def test_user_pagination():
    """ verifies user pagination """
    assert False


@pytest.mark.skip
def test_user_pagination_search():
    """ verifies user pagination with search """
    assert False
