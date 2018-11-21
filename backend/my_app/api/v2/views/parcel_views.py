"""
Creates views for parcels. These are POST, GET, PUT
"""

from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.parcel import ParcelModel
from ..models.user import User
from ..utils.schemas import ParceCreateSchema
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
            return make_response(jsonify({
                "Message": is_valid
            }), 400)

        parcel = ParcelModel()
        my_parcel = parcel.add_parcel(data, user_id)

        payload = {
            "Message": "Parcel Created",
            "data": my_parcel
        }
        res = make_response(jsonify(payload), 201)
        return res

    @jwt_required
    def get(self):
        parcel = ParcelModel()

        user = User()
        user_email = get_jwt_identity()
        check_role = user.check_admin(user_email)

        if not check_role:
            return make_response(jsonify({
                "Message": "You are not authorised to access this resource"
            }), 403)
        parcels = parcel.get_all()
        return make_response(jsonify({
            "Data": parcels
        }), 200)
