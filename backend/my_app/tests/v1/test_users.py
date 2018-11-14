"""
This test class avails tests for user views
"""
from flask import json
from .data import (valid_user, existing_user, invalid_user,
                   some_missing, invalid_email_login, empty_data,
                   wrong_login_password, user_doesnt_exist_login)


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

    def test_invalid_registration(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v1/register",
            data=json.dumps(invalid_user),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Not a valid email address' in str(res_data['Message'])

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
            data=json.dumps(some_missing),
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
