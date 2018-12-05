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
        assert 'Missing data for required field.' in str(res_data['weight'])

    def test_empty_string(self, client, auth_token):
        """ Tests for case where empty json string is posted"""

        response = client.post(
            "/api/v2/parcels",
            data=json.dumps(EMPTY_STRING_PARCEL),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Value provided cannot be empty' in str(
            res_data['pickup_location'])

    def test_no_data(self, client, auth_token):
        """ Tests for case where no json data is posted"""

        response = client.post(
            "/api/v2/parcels",
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        assert response.status_code == 400

    def test_admin_get_all_parcels(self, client, admin_token):
        """ This method tests for admin getting all parcels"""
        response = client.get(
            "/api/v2/parcels",
            headers=dict(Authorization="Bearer " + admin_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'pending delivery' in str(res_data['Data'])

    def test_user_get_all_parcels(self, client, auth_token):
        """ This method tests for user get all parcels"""
        response = client.get(
            "/api/v2/parcels",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 403
        assert 'You are not authorised to access this resource' in str(
            res_data['Message'])

    def test_change_destination(self, client, auth_token):
        """ This method tests for changing destination with valid data"""
        response = client.put(
            "/api/v2/parcels/1/destination",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Successfully updated the destination' in str(res_data[
            'Message'])

    def test_invalid_url_change_destination(self, client, admin_token):
        """This method tests for changing destination with invalid url"""
        response = client.put(
            "/api/v2/parcels/a/destination",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Please provide a valid parcel id - integer' in str(res_data[
            'Message'])

    def test_invalid_data_change_destination(self, client, admin_token):
        """ This method test invalid data in change destination"""
        response = client.put(
            "/api/v2/parcels/1/destination",
            data=json.dumps(CHNG_DSTN_INVALID),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Value provided cannot be empty' in str(res_data[
            'location'])

    def test_order_not_exist_change_destination(self, client, admin_token):
        """This method test for non existing parcel in change destination"""
        response = client.put(
            "/api/v2/parcels/1000/destination",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Parcel does not exist' in str(res_data['Message'])

    def test_admin_change_status(self, client, admin_token):
        """This method tests for admin change status"""
        response = client.put(
            "/api/v2/parcels/1/status",
            headers=dict(Authorization="Bearer " + admin_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Successfully updated status' in str(res_data['Message'])

    def test_non_admin_change_status(self, client, auth_token):
        """This method tests for non admin change status"""
        response = client.put(
            "/api/v2/parcels/1/status",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 403
        assert 'You are not authorised to access this resource' in str(
            res_data['Message'])

    def test_invalid_url_change_status(self, client, auth_token):
        """This method tests for invalid url in change status"""
        response = client.put(
            "/api/v2/parcels/a/status",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Please provide a valid parcel id - integer' in str(
            res_data['Message'])

    def test_admin_change_p_location(self, client, admin_token):
        """This method tests for admin change of present location"""
        response = client.put(
            "/api/v2/parcels/1/presentLocation",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 202
        assert 'Successfully updated present location' in str(res_data[
                                                              'Message'])

    def test_non_admin_change_p_location(self, client, auth_token):
        """This method tests for non admin change of present location"""
        response = client.put(
            "/api/v2/parcels/1/presentLocation",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 403
        assert 'You are not authorised to access this resource' in str(
            res_data['Message'])

    def test_invalid_data_change_p_location(self, client, admin_token):
        """This method tests for invalid data in change of present location"""
        response = client.put(
            "/api/v2/parcels/1/presentLocation",
            data=json.dumps(CHNG_DSTN_INVALID),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Value provided cannot be empty' in str(res_data['location'])

    def test_invalid_url_change_p_location(self, client, admin_token):
        """This method tests for invalid url in change of present location"""
        response = client.put(
            "/api/v2/parcels/a/presentLocation",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Please provide a valid parcel id - integer' in \
            str(res_data['Message'])

    def test_absent_id_change_p_location(self, client, admin_token):
        """This method tests for absent id in change of present location"""
        response = client.put(
            "/api/v2/parcels/1000/presentLocation",
            data=json.dumps(CHNG_DSTN),
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Parcel does not exist' in str(res_data['Message'])

    def test_cancel_order_invalid_url(self, client, auth_token):
        """This method tests for invalid url in cancel order"""
        response = client.put(
            "/api/v2/parcels/a/cancel",
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 400
        assert 'Please provide a valid parcel id - integer ' in \
            str(res_data['Message'])

    def test_cancel_order_no_parcel(self, client, auth_token):
        """This method tests for no parcel exist in cancel order"""
        response = client.put(
            "/api/v2/parcels/1000/cancel",
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Parcel does not exist' in str(res_data['Message'])

    def test_cancel_order_unauthorized(self, client, admin_token):
        """This method tests for unauthorized user in cancel order"""
        response = client.put(
            "/api/v2/parcels/1/cancel",
            headers=dict(Authorization="Bearer " + admin_token),
            content_type='application/json;charset=utf-8')

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        assert 'Unauthorized, you cannot cancel this order' in \
            str(res_data['Message'])

    def test_get_specific_order(self, client, auth_token):
        """ This function tests getting a specific order"""

        response = client.get(
            "/api/v2/parcels/1",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'current_location' in str(res_data['Data'])

    def test_admin_get_specific_order(self, client, admin_token):
        """ This function tests admin getting a specific order order"""
        response = client.get(
            "/api/v2/parcels/1",
            headers=dict(Authorization="Bearer " + admin_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'current_location' in str(res_data['Data'])

    def test_get_specific_order_absent(self, client, auth_token):
        """ This function tests absence of a specific order"""

        response = client.get(
            "/api/v2/parcels/1000",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 404
        assert 'Parcel requested does not exist' in str(res_data['Message'])

    def test_get_users_all_orders(self, client, auth_token):
        """ This function tests getting a specific users all orders"""

        response = client.get(
            "/api/v2/users/1/parcels",
            headers=dict(Authorization="Bearer " + auth_token))

        res_data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert 'current_location' in str(res_data['Parcels'])
