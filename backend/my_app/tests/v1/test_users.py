"""
This test class avails tests for user views
"""
from flask import json

valid_user = {
    "name": "Test2",
    "email": "user@email.com",
    "password": "password",
    "role": "2"
}

invalid_user = {
    "name": "Test",
    "email": "email.com",
    "password": "password",
    "role": "2"
}

existing_user = {
    "name": "Test",
    "email": "test@email.com",
    "password": "password",
    "role": "2"
}

some_missing = {
    "name": "Test",
    "password": "password",
    "role": "2"
}

empty_data = {}


class Testuser(object):
    """This class tests the views for user.
    These are the registration and login routes
    """

    def test_valid_registration(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(valid_user),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert 'Created' in res_data['status']

    def test_user_exists(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(existing_user),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 409
        assert 'User already exists' in res_data['message']

    def test_empty_post_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(empty_data),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Bad Request' in res_data['status']

    def test_some_missing_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(empty_data),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Bad Request' in res_data['status']
