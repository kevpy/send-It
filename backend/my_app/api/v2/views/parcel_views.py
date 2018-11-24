"""
Creates views for parcels. These are POST, GET, PUT
"""

from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from .auth_views import check_role, check_user
from ..models.parcel import ParcelModel
from ..utils.schemas import ParceCreateSchema, LocationSchema
from ..utils.validators import validate_json, validate_url_params


class Parcels(Resource):
    """This class provides access operation for GET and POST methods
    for a parcel order or parcels
    """

    @jwt_required
    def post(self):
        """Saves a new parcel item
        :return: Returns a json response
        """

        get_user = check_user()
        user_id = get_user['user_id']

        schema = ParceCreateSchema()
        data = request.get_json() or {}
        is_valid = validate_json(schema, data)

        if is_valid is not None:
            return make_response(jsonify({"Message": is_valid}), 400)

        parcel = ParcelModel()
        my_parcel = parcel.add_parcel(data, user_id)

        payload = {"Message": "Parcel Created", "data": my_parcel}
        res = make_response(jsonify(payload), 201)
        return res

    @jwt_required
    def get(self):
        parcel = ParcelModel()

        role = check_role()

        if not role:
            return make_response(
                jsonify({
                    "Message":
                        "You are not authorised to access this resource"
                }), 403)
        parcels = parcel.get_all()
        return make_response(jsonify({"Data": parcels}), 200)


class ChangeStatus(Resource):
    """
    This class changes the status of a parcel order from
    pending delivery to delivered
    """

    @jwt_required
    def put(self, parcel_id):
        """This function allows admin to change status of all parcels"""
        parcel = ParcelModel()

        role = check_role()

        param = validate_url_params(parcel_id)
        if param is not None:
            return param

        if not role:
            return make_response(
                jsonify({
                    "Message":
                        "You are not authorised to access this resource"
                }), 403)
        change = parcel.change_status(parcel_id)
        return make_response(
            jsonify({
                "Message": "Successfully updated status",
                "data": change
            }), 202)


class ChangePresentLocation(Resource):
    """
    This class changes the present location of a parcel order from
    from an empty value to given value
    """

    @jwt_required
    def put(self, parcel_id):
        """This function allows admin to change status of all parcels"""
        parcel = ParcelModel()

        schema = LocationSchema()
        data = request.get_json() or {}
        is_valid = validate_json(schema, data)

        param = validate_url_params(parcel_id)
        if param is not None:
            return param

        if is_valid is not None:
            return make_response(jsonify({"Message": is_valid}), 400)

        role = check_role()

        if not role:
            return make_response(
                jsonify({
                    "Message":
                        "You are not authorised to access this resource"
                }), 403)
        if parcel.get_percel_by_id(parcel_id) is None:
            return make_response(jsonify({
                "Message": "Parcel does not exist"
            }), 404)
        change = parcel.change_present_location(data['location'], parcel_id)
        return make_response(
            jsonify({
                "Message": "Successfully updated present location",
                "data": change
            }), 202)


class ChangeOrderDestination(Resource):
    """
    This class allows a user to change the destination of a parcel order
    """

    @jwt_required
    def put(self, parcel_id):
        """This function allows admin to change status of all parcels"""
        parcel = ParcelModel()

        schema = LocationSchema()
        data = request.get_json() or {}
        is_valid = validate_json(schema, data)

        get_user = check_user()
        user_id = get_user['user_id']

        param = validate_url_params(parcel_id)
        if param is not None:
            return param

        if is_valid is not None:
            return make_response(jsonify({"Message": is_valid}), 400)

        my_parcel = parcel.get_percel_by_id(parcel_id)
        if my_parcel is None:
            return make_response(jsonify({
                "Message": "Parcel does not exist"
            }), 404)
        if my_parcel['user_id'] != user_id:
            return make_response(jsonify({
                "Message": "Unauthorized, you cannot cancel this order"
            }), 401)
        if my_parcel['status'] == 'delivered' or my_parcel['status'] == 'cancelled':
            return make_response(jsonify({
                "Message": "Parcel is already delivered or cancelled"
            }), 405)
        change = parcel.change_destination(data['location'], parcel_id)
        return make_response(
            jsonify({
                "Message": "Successfully updated the destination",
                "data": change
            }), 202)


class CancelOrder(Resource):
    """
    This class allows a user to change the destination of a parcel order
    """

    @jwt_required
    def put(self, parcel_id):
        """This function allows admin to change status of all parcels"""
        parcel = ParcelModel()

        get_user = check_user()
        user_id = get_user['user_id']

        param = validate_url_params(parcel_id)
        if param is not None:
            return param

        my_parcel = parcel.get_percel_by_id(parcel_id)
        if my_parcel is None:
            return make_response(jsonify({
                "Message": "Parcel does not exist"
            }), 404)
        if my_parcel['user_id'] != user_id:
            return make_response(jsonify({
                "Message": "Unauthorized, you cannot cancel this order"
            }), 401)
        if my_parcel['status'] == 'delivered' or \
                my_parcel['status'] == 'cancelled':
            return make_response(jsonify({
                "Message": "Parcel is already delivered or canceled"
            }), 405)
        change = parcel.cancel_order(parcel_id)
        return make_response(
            jsonify({
                    "Message": "Successfully cancelled the parcel order",
                "data": change
            }), 202)


class GetSpecificOrder(Resource):
    """ This Class gets a specific parcel order"""

    @jwt_required
    def get(self, parcel_id):
        """
        This function allows a user to get a specific order they own.
        Also allows an admin to get any specific order
        :param parcel_id:
        :return: returns a json response
        """
        parcel = ParcelModel()

        param = validate_url_params(parcel_id)
        if param is not None:
            return param

        get_user = check_user()
        user_id = get_user['user_id']
        user_role = get_user['user_role']

        my_parcel = parcel.get_percel_by_id(parcel_id)
        if my_parcel is None:
            return make_response(jsonify({
                "Message": "Parcel requested does not exist"
            }), 404)

        if int(user_id) != int(my_parcel['user_id']) and user_role.lower() != 'admin':
            return make_response(jsonify({
                "Message": "You are not authorised to access this resource"
            }), 401)
        return make_response(jsonify({
                "Data": my_parcel
        }))


class GetAllUsersParcels(Resource):
    """ This Resource returns all parcels that belong to a specific user """

    @jwt_required
    def get(self, user_id):
        parcel = ParcelModel()

        param = validate_url_params(user_id)
        if param is not None:
            return param

        get_user = check_user()

        if user_id != str(get_user['user_id']):
            return make_response(jsonify({
                "Message": "You are not authorised to access this resource"
            }))
        if get_user['user_id'] is None:
            return make_response(jsonify({
                "Message": "Sorry the specified user does not exist"
            }), 404)
        parcels = parcel.get_user_parcels(get_user['user_id'])
        if parcels is None:
            return make_response(jsonify({
                "Message": "No parcels found for the user"
            }), 404)
        return make_response(jsonify({
            "Parcels": parcels
        }), 200)
