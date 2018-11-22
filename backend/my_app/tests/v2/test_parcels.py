"""
This test class tests the parcel_views
"""
from flask import json
from .data import CREATE_PARCEL, EMPTY_DATA, EMPTY_STRING_PARCEL
from .data import CHNG_DSTN, CHNG_DSTN_INVALID


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

    def test_admin_get_all_parcels(self, client, admin_token):
        response = client.get(
            "/api/v2/parcels",
            headers=dict(Authorization="Bearer " + admin_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'pending delivery' in str(res_data['Data'])

    def test_user_get_all_parcels(self, client, auth_token):
        response = client.get(
            "/api/v2/parcels",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 403
        assert 'You are not authorised to access this resource' in str(
            res_data['Message'])

    def test_admin_change_status(self, client, admin_token):
        response = client.put(
            "/api/v2/parcels/1/status",
            headers=dict(Authorization="Bearer " + admin_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Successfully updated status' in str(res_data['Message'])

    def test_non_admin_change_status(self, client, auth_token):
        response = client.put(
            "/api/v2/parcels/1/status",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 403
        assert 'You are not authorised to access this resource' in str(
            res_data['Message'])

    def test_admin_change_p_location(self, client, admin_token):
        response = client.put(
            "/api/v2/parcels/1/status",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Successfully updated status' in str(res_data['Message'])

    def test_non_admin_change_p_location(self, client, auth_token):
        response = client.put(
            "/api/v2/parcels/1/status",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 403
        assert 'You are not authorised to access this resource' in str(
            res_data['Message'])

    def test_invalid_data_change_p_location(self, client, admin_token):
        response = client.put(
            "/api/v2/parcels/1/status",
            data=json.dumps(CHNG_DSTN_INVALID),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Successfully updated status' in str(res_data['Message'])
