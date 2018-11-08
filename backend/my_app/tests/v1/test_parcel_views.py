"""
This test class tests the parcel_views
"""
from flask import json

create_order = {
    "sender_id": 1,
    "pickup_location": "Nakuru",
    "destination": "Eldoret",
    "weight": "10KG",
    "status": "pending delivery"
}

cancel_order = {
    "sender_id": 1,
    "pickup_location": "Nakuru",
    "destination": "Eldoret",
    "weight": "10KG",
    "status": "canceled"
}

empty_data = {}


class TestParcelViews(object):
    """
    Tests the views for all http methods availed on test views
    """

    def test_post_order(self, client):
        """ Tests create a new parcel order """

        response = client.post(
            "/api/v1/parcels",
            data=json.dumps(create_order),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert 'Created' in res_data['status']

    def test_empty_data(self, client):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v1/parcels",
            data=json.dumps(empty_data),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Bad Request' in res_data['status']

    def test_no_data(self, client):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v1/parcels",
            content_type='application/json;charset=utf-8')

        assert response.status_code == 400

    def test_get_all_orders(self, client):
        """ This function tests getting of all parcel orders"""

        response = client.get("/api/v1/parcels")

        res_data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'OK' in res_data['status']

    def test_get_specific_order_found(self, client):
        """Test one specific order found"""

        response = client.get("/api/v1/parcels/1")
        res_data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'OK' in res_data['status']

    def test_get_specific_order_not_found(self, client):
        """Test one specific order not found"""

        response = client.get("/api/v1/parcels/10")
        res_data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'Not Found' in res_data['status']

    def test_get_specific_order_invalid_id(self, client):
        """Test one specific when given invalid order_id"""

        response = client.get("/api/v1/parcels/a")
        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Bad request' in res_data['status']

    def test_cancel_an_order_if_order_exist(self, client):
        """Test canceling an order if order exists"""

        response = client.put(
            "api/v1/parcels/1/cancel",
            data=json.dumps(cancel_order),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 202
        assert 'Accepted' in res_data['status']

    def test_cancel_an_order_if_order_doesnt_exist(self, client):
        """Test canceling an order if order doesn't exists"""

        response = client.put(
            "api/v1/parcels/10/cancel",
            data=json.dumps(cancel_order),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'Not Found' in res_data['status']

    def test_found_users_all_orders(self, client):
        """Test a specific users all orders are found"""

        response = client.get("/api/v1/users/2/parcels")
        res_data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'OK' in res_data['status']

    def test_not_found_order_for_user(self, client):
        """Test a specific user's orders none are found"""

        response = client.get("/api/v1/users/10/parcels")
        res_data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'Not Found' in res_data['status']

    def test_invalid_user_id(self, client):
        """Test one specific when given invalid user_id"""

        response = client.get("/api/v1/users/a/parcels")
        res_data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Bad request' in res_data['status']
