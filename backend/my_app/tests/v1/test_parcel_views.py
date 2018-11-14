"""
This test class tests the parcel_views
"""
from flask import json
from .data import create_order, cancel_order, empty_data


class TestParcelViews(object):
    """
    Tests the views for all http methods availed on test views
    """

    def test_post_order(self, client, auth_token):
        """ Tests create a new parcel order """

        response = client.post(
            "/api/v1/parcels",
            data=json.dumps(create_order),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 201
        assert 'Created' in res_data['status']
        assert 'pending delivery' in str(res_data['data'])

    def test_empty_data(self, client, auth_token):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v1/parcels",
            data=json.dumps(empty_data),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Bad Request' in res_data['status']
        assert 'Missing data for required field.' in str(res_data['Message'])

    def test_no_data(self, client, auth_token):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v1/parcels",
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        assert response.status_code == 400

    def test_get_all_orders(self, client, auth_token):
        """ This function tests getting of all parcel orders"""

        response = client.get(
            "/api/v1/parcels",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'OK' in res_data['status']
        assert 'pending delivery' in str(res_data['Parcels'])

    def test_get_specific_order_found(self, client, auth_token):
        """Test one specific order found"""

        response = client.get(
            "/api/v1/parcels/1",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'OK' in res_data['status']
        assert 'pending delivery' in str(res_data['parcel'])

    def test_get_specific_order_not_found(self, client, auth_token):
        """Test one specific order not found"""

        response = client.get(
            "/api/v1/parcels/10",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Not Found' in res_data['status']
        assert 'No parcel found' in str(res_data['Parcel'])

    def test_get_specific_order_invalid_id(self, client, auth_token):
        """Test one specific when given invalid order_id"""

        response = client.get(
            "/api/v1/parcels/a",
            headers=dict(Authorization="Bearer " + auth_token))
        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Bad request' in res_data['status']
        assert 'Please provide a valid parcel id(int)' in str(
            res_data['Message'])

    def test_cancel_an_order_if_order_exist(self, client, auth_token):
        """Test canceling an order if order exists"""

        response = client.put(
            "api/v1/parcels/1/cancel",
            data=json.dumps(cancel_order),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Accepted' in res_data['status']
        assert 'canceled' in str(res_data['data'])

    def test_cancel_an_order_if_order_doesnt_exist(self, client, auth_token):
        """Test canceling an order if order doesn't exists"""

        response = client.put(
            "api/v1/parcels/10/cancel",
            data=json.dumps(cancel_order),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Not Found' in res_data['status']
        assert 'The order requested does not exist' in str(res_data['Message'])

    def test_found_users_all_orders(self, client, auth_token):
        """Test a specific users all orders are found"""

        response = client.get(
            "/api/v1/users/1/parcels",
            headers=dict(Authorization="Bearer " + auth_token),)
        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'OK' in res_data['status']
        assert 'pending delivery' in str(res_data['Parcels'])

    def test_not_found_order_for_user(self, client, auth_token):
        """Test a specific user's orders none are found"""

        response = client.get(
            "/api/v1/users/10/parcels",
            headers=dict(Authorization="Bearer " + auth_token),)
        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Not Found' in res_data['status']
        assert 'Requested resources not found' in str(res_data['Message'])

    def test_invalid_user_id(self, client, auth_token):
        """Test one specific when given invalid user_id"""

        response = client.get(
            "/api/v1/users/a/parcels",
            headers=dict(Authorization="Bearer " + auth_token),)
        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Bad request' in res_data['status']
        assert 'Please provide a valid parcel id(int)' in str(
            res_data['Message'])
