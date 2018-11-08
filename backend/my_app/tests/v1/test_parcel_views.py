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

    def test_get_all_orders(self, client):
        """ This function tests getting of all parcel orders"""

        response = client.get("/api/v1/parcels")

        assert response.status_code == 200
