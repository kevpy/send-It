"""
This test class tests the parcel_views
"""
from flask import json
from .data import CREATE_PARCEL, EMPTY_DATA, EMPTY_STRING_PARCEL


class TestParcelViews(object):
    """
    Tests the views for all http methods availed on test views
    """

    def test_post_order(self, client, auth_token):
        """ Tests create a new parcel order """

        response = client.post(
            "/api/v2/parcels",
            data=json.dumps(CREATE_PARCEL),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 201
        assert 'Parcel Created' in str(res_data['Message'])

    def test_empty_data(self, client, auth_token):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v2/parcels",
            data=json.dumps(EMPTY_DATA),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Missing data for required field.' in str(res_data['Message'])

    def test_empty_string(self, client, auth_token):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v2/parcels",
            data=json.dumps(EMPTY_STRING_PARCEL),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Value provided cannot be empty' in str(res_data['Message'])

    def test_no_data(self, client, auth_token):
        """ Tests for case where empty json data is posted"""

        response = client.post(
            "/api/v2/parcels",
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        assert response.status_code == 400
