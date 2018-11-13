"""
This test class avails tests for user views
"""
from flask import json

valid_user = {
    "name": "Test2",
    "email": "user@email.com",
    "password": "password",
    "role": "user"
}

invalid_user = {
    "name": "Test",
    "email": "email.com",
    "password": "password",
    "role": "user"
}

existing_user = {
    "name": "Test",
    "email": "test@email.com",
    "password": "password",
    "role": "user"
}

some_missing = {
    "name": "Test",
    "password": "password",
    "role": "user"
}

empty_data = {}

valid_email_login = {
    "email": "test@email.com",
    "password": "password"
}

invalid_email_login = {
    "email": "testemail.com",
    "password": "password"
}

wrong_login_password = {
    "email": "test@email.com",
    "password": "wrong"
}

user_doesnt_exist_login = {
    "email": "new@email.com",
    "password": "password"
}


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

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Created' in res_data['status']
        assert 'user@email.com' in str(res_data['data'])

    def test_user_exists(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(existing_user),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 409
        assert 'User already exists' in res_data['message']

    def test_empty_post_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(empty_data),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Missing data for required field.' in str(res_data['Message'])

    def test_some_missing_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(empty_data),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Missing data for required field.' in str(res_data['Message'])

    def test_invalid_email_login(self, client):
        """ This method tests for a invalid email address"""

        response = client.post(
            "/api/v1/login",
            data=json.dumps(invalid_email_login),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Not a valid email address.' in str(res_data['Message'])

    def test_wrong_login_password(self, client):
        """ This method tests for a invalid password"""

        response = client.post(
            "/api/v1/login",
            data=json.dumps(wrong_login_password),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Incorrect Password' in res_data['message']

    def test_user_doesnt_exist(self, client):
        """ This method tests for user not registered"""

        response = client.post(
            "/api/v1/login",
            data=json.dumps(user_doesnt_exist_login),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert "User doesn't exists" in res_data['message']
