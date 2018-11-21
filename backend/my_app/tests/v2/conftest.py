"""
This is creates a pytest fixture.
"""
import pytest
from flask import json
from .data import CREATE_TEST_USER, CREATE_TEST_ADMIN
from ... import create_app
from ...db.db_config import destroy_tables


@pytest.fixture(scope='session')
def client():
    app = create_app('testing')
    test_client = app.test_client()

    create_user = test_client.post(
        "/api/v2/auth/signup",
        data=json.dumps(CREATE_TEST_USER),
        content_type='application/json;charset=utf-8'
    )

    create_admin = test_client.post(
        "/api/v2/auth/signup",
        data=json.dumps(CREATE_TEST_ADMIN),
        content_type='application/json;charset=utf-8'
    )
    yield test_client
    destroy_tables()


@pytest.fixture(scope='session')
def auth_token(client):

    login = {"email": "test@email.com", "password": "Passw0rd"}

    res = client.post(
        "/api/v2/auth/login",
        data=json.dumps(login),
        content_type='application/json;charset=utf-8')
    token = json.loads(res.data)["token"]
    return token


@pytest.fixture(scope='session')
def admin_token(client):

    login = {"email": "admin@email.com", "password": "Passw0rd"}

    res = client.post(
        "/api/v2/auth/login",
        data=json.dumps(login),
        content_type='application/json;charset=utf-8')
    token = json.loads(res.data)["token"]
    return token
