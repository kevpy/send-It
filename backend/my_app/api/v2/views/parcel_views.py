"""
Creates views for parcels. These are POST, GET, PUT
"""

from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.parcel import ParcelModel
from ..models.user import User
from ..utils.schemas import ParceCreateSchema, LocationSchema
from ..utils.validators import validate_json


class Parcels(Resource):
    """This class provides access operation for GET and POST methods
    for a parcel order or parcels
    """

    @jwt_required
    def post(self):
        """Saves a new parcel item
        :return: Returns a json response
        """
        user = User()
        user_email = get_jwt_identity()
        get_user = user.get_user(user_email)
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

        user = User()
        user_email = get_jwt_identity()
        check_role = user.check_admin(user_email)

        if not check_role:
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

        user = User()
        user_email = get_jwt_identity()
        check_role = user.check_admin(user_email)

        if not check_role:
            return make_response(
                jsonify({
                    "Message":
                    "You are not authorised to access this resource"
                }), 403)
        parcel.change_status(parcel_id)
        return make_response(
            jsonify({
                "Message": "Successfully updated status"
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

        if is_valid is not None:
            return make_response(jsonify({"Message": is_valid}), 400)

        user = User()
        user_email = get_jwt_identity()
        check_role = user.check_admin(user_email)

        if not check_role:
            return make_response(
                jsonify({
                    "Message":
                    "You are not authorised to access this resource"
                }), 403)
        if parcel.get_one_parcel(parcel_id) is None:
            return make_response(jsonify({
                "Message": "Parcel does not exist"
            }), 404)
        parcel.change_present_location(data['location'], parcel_id)
        return make_response(
            jsonify({
                "Message": "Successfully updated present location"
            }), 202)
