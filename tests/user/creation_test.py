""" Tests involving User Creation """
from datetime import datetime, timedelta, timezone
from typing import Callable

from fastapi.testclient import TestClient
from faker import Faker
import pytest

    
def test_create_user(user_creation_msg: dict[str, str], client: TestClient):
    """ verifies that user can be added to DB and pubilc data is returned """
    request_time = datetime.now(timezone.utc).replace(microsecond=0)
    response = client.post('/users', json=user_creation_msg)
    assert response.status_code == 201

    created_user: dict[str, str] = response.json()
    assert created_user.pop('status') == 'REGISTERED'

    creation_time = datetime.fromisoformat(
        created_user.pop('joined')).replace(tzinfo=timezone.utc)
    assert (
        request_time <= creation_time <= request_time + timedelta(seconds=15)
    )
    
    del created_user['id']
    del user_creation_msg['email']
    del user_creation_msg['password']
    assert user_creation_msg == created_user


def test_create_user_missing_data(user_creation_msg: dict, client: TestClient):
    """ verifies that all fields are required for user creation """
    users = client.get('/users').json()
    inital_user_count = len(users)

    for field in user_creation_msg:
        msg = user_creation_msg.copy()
        del msg[field]
        
        response = client.post('/users', json=msg)
        assert response.status_code == 422
        
        users = client.get('/users').json()
        assert len(users) == inital_user_count


def test_create_user_extra_data(
    faker: Faker, user_creation_msg: dict, client: TestClient
):
    """ verifies that adding extra fields results in failure """
    user_creation_msg[faker.word()] = faker.word()
    users = client.get('/users').json()
    inital_user_count = len(users)
    
    response = client.post('/users', json=user_creation_msg)
    assert response.status_code == 422

    users = client.get('/users').json()
    assert len(users) == inital_user_count


@pytest.mark.parametrize("unqiue_field", ["email", "username"])
def test_create_user_duplicate_field(
    unqiue_field, 
    create_user_msg: Callable[[], dict[str, str]], 
    client: TestClient
):
    """ verifies that duplicatating unqiue fields results in failure """
    creation_msg_a = create_user_msg()
    creation_msg_b = create_user_msg()
    creation_msg_b[unqiue_field] = creation_msg_a[unqiue_field]

    response = client.post('/users', json=creation_msg_a)
    assert response.status_code == 201

    users = client.get('/users').json()
    assert len(users) == 1

    response = client.post('/users', json=creation_msg_b)
    assert response.status_code == 409
    
    fields = response.json()['fields']
    assert len(fields) == 1
    assert fields[0]['name'] == unqiue_field
    assert fields[0]['input'] == creation_msg_b[unqiue_field]
    assert len(fields[0]['error'])

    users = client.get('/users').json()
    assert len(users) == 1


def test_create_user_duplicate_fields(
    create_user_msg: Callable[[], dict[str, str]], client: TestClient
):
    """ test that error lists all duplicatate unqiue fields """
    creation_msg_a = create_user_msg()
    creation_msg_b = create_user_msg()
    creation_msg_b["email"] = creation_msg_a["email"]
    creation_msg_b["username"] = creation_msg_a["username"]

    response = client.post('/users', json=creation_msg_a)
    assert response.status_code == 201

    users = client.get('/users').json()
    assert len(users) == 1

    response = client.post('/users', json=creation_msg_b)
    assert response.status_code == 409
    
    fields = response.json()['fields']
    assert len(fields) == 2

    assert fields[0]["name"] in ["email", "username"]
    assert fields[1]["name"] in ["email", "username"]

    for field in fields:
        assert field["input"] == creation_msg_b[field["name"]]
        assert len(field["error"])

    users = client.get('/users').json()
    assert len(users) == 1


@pytest.mark.skip
def test_register_user():
    """ verifies registration process """
    assert False


@pytest.mark.skip
def test_registration_timeout():
    """ verifies registration code expires """
    assert False


@pytest.mark.skip
def test_create_users():
    """ verifies user creation and registation works with multiple users """
    assert False
