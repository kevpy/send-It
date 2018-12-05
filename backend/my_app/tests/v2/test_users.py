"""
This test class avails tests for user views
"""
from flask import json
from .data import (VALID_USER, INVALID_USER, EXISTING_USER,
                   SOME_MISSING, EMPTY_DATA, EMPTY_STRINGS)
from .data import (INVALID_EMAIL_LOGIN, WRONG_LOGIN_PASSWORD,
                   USER_NOT_EXIST_LOGIN)


class Testuser(object):
    """This class tests the views for user.
    These are the registration and login routes
    """

    def test_random_urls(self, client):
        """Test a random urls"""

        response = client.get(
            "/api/v2/auth/signup/jbhjjjjjj")
        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'The requested resource does not exist' in str(res_data[
                                                              'Message'])

    def test_valid_registration(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(VALID_USER),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'user@email.com' in str(res_data['data'])

    def test_invalid_registration(self, client):
        """ This method tests for a invalid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(INVALID_USER),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Not a valid email address' in str(res_data['email'])

    def test_user_exists(self, client):
        """ This method tests if a user is previously registered"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(EXISTING_USER),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 409
        assert 'User with given email address exist' in res_data['Message']

    def test_empty_post_data(self, client):
        """ This method tests empty registration post data"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(EMPTY_DATA),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Missing data for required field.' in str(res_data['email'])

    def test_some_missing_data(self, client):
        """ This method tests some missing post data"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(SOME_MISSING),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Missing data for required field.' in str(res_data['email'])

    def test_empty_strings_in_data(self, client):
        """ This method tests for empty strings in post data"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(EMPTY_STRINGS),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Value provided cannot be empty' in str(res_data['name'])

    def test_invalid_email_login(self, client):
        """ This method tests for a invalid email address"""

        response = client.post(
            "/api/v2/auth/login",
            data=json.dumps(INVALID_EMAIL_LOGIN),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Not a valid email address.' in str(res_data['email'])

    def test_wrong_login_password(self, client):
        """ This method tests for a wrong password"""

        response = client.post(
            "/api/v2/auth/login",
            data=json.dumps(WRONG_LOGIN_PASSWORD),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Incorrect Password' in res_data['Message']

    def test_user_doesnt_exist(self, client):
        """ This method tests for user not registered"""

        response = client.post(
            "/api/v2/auth/login",
            data=json.dumps(USER_NOT_EXIST_LOGIN),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert "User doesn't exists" in res_data['Message']

    def test_no_token(self, client):
        """Test a random urls"""

        response = client.get(
            "/api/v2/parcels")
        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Authorization token is needed' in str(res_data[
            'Message'])
