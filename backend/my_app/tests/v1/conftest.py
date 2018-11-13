"""
This is creates a pytest fixture.
"""
import pytest
from flask import json
from my_app import create_app


@pytest.fixture
def client():
    """This function creates a test client"""
    app = create_app()
    test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()

@pytest.fixture
def auth_token(client):
    login = {
        "email": "test@email.com",
        "password": "password"
    }

    res = client.post(
        "/api/v1/login",
        data=json.dumps(login),
        content_type='application/json;charset=utf-8')

    token = json.loads(res.data)["token"]
    return token
