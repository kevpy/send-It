"""
This test class avails tests for user views
"""
from flask import json
from .data import (VALID_USER, INVALID_USER, EXISTING_USER,
                   SOME_MISSING, EMPTY_DATA, EMPTY_STRINGS)


class Testuser(object):
    """This class tests the views for user.
    These are the registration and login routes
    """

    def test_random_urls(self, client):
        """Test a specific users all orders are found"""

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
        assert 'Created' in res_data['status']
        assert 'user@email.com' in str(res_data['data'])

    def test_invalid_registration(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(INVALID_USER),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Not a valid email address' in str(res_data['Message'])

    def test_user_exists(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(EXISTING_USER),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 409
        assert 'User already exists' in res_data['message']

    def test_empty_post_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(EMPTY_DATA),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Missing data for required field.' in str(res_data['Message'])

    def test_some_missing_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(SOME_MISSING),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Missing data for required field.' in str(res_data['Message'])

    def test_empty_strings_in_data(self, client):
        """ This method tests for a valid registration"""

        response = client.post(
            "/api/v2/auth/signup",
            data=json.dumps(EMPTY_STRINGS),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert 'Bad Request' in res_data['status']
        assert 'Value provided cannot be empty' in str(res_data['Message'])
