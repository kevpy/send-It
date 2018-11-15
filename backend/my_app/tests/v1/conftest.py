"""
This is creates a pytest fixture.
"""
import pytest
from flask import json
from my_app import create_app
from ...api.v1.models.parcel import ParcelModel
from ...api.v1.models.user_model import User
from .data import create_test_order, create_test_user


@pytest.fixture(scope='session')
def client():
    """This function creates a test client"""
    app = create_app()
    test_client = app.test_client()

    # create test user and order
    db = ParcelModel.parcels.append(create_test_order)
    user = User()
    add_user = user.add_user(create_test_user)

    ctx = app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()


@pytest.fixture(scope='session')
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
