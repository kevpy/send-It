"""
Creates views for parcels. These are POST, GET, PUT
"""

from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.parcel import ParcelModel
from ..models.user_model import User
from ..schemas import ParceCreateSchema, ParceCancelSchema
from ..validators import validate_json


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
                "Message": is_valid,
                "status": "Bad Request"
            }), 400)

        parcel = ParcelModel()
        my_parcel = parcel.add_parcel(data, user_id)

        payload = {
            'status': 'Created',
            "message": "Parcel Created",
            "data": my_parcel
        }
        res = make_response(jsonify(payload), 201)
        return res

    @jwt_required
    def get(self):
        """Gets all parcel orders
        :return: Returns a json response
        """
        parcel = ParcelModel()

        payload = {"status": "OK", "Parcels": parcel.get_all()}

        res = make_response(jsonify(payload), 200)
        return res


class SpecificParcel(Resource):
    """This class gets a single parcel order"""

    @jwt_required
    def get(self, parcel_id):
        """
        Gets a single parcel order
        :param parcelId:
        :return: Returns a json response
        """
        try:
            parcel_id = int(parcel_id)
        except Exception:
            return make_response(jsonify({
                "Message": "Please provide a valid parcel id(int)",
                "status": "Bad request"
            }), 400)
        parcel = ParcelModel()

        single_parcel = parcel.get_specific_parcel(parcel_id)
        if single_parcel is not None:
            return make_response(jsonify({
                "parcel": single_parcel, "status": "OK"
            }), 200)
        return make_response(
            jsonify({
                "Parcel": "No parcel found",
                "status": "Not Found"
            }), 404)


class CancelOrder(Resource):
    """This class cancels an order"""

    @jwt_required
    def put(self, parcel_id):
        """
        Updates the status of a parcel order to canceled
        :param parcel_id:
        :return: Returns a json response
        """
        schema = ParceCancelSchema()
        parcel = ParcelModel()
        data = request.get_json() or {}

        check_valid = validate_json(schema, data)

        if check_valid is not None:
            return make_response(jsonify({
                "Message": check_valid,
                "status": "Bad Request"
            }), 400)
        change = parcel.cancel_order(parcel_id, data)

        if change is not None:
            return make_response(jsonify({
                "Message": "success",
                "status": "Accepted",
                "data": change
            }), 202)
        return make_response(jsonify({
            "Message": "The order requested does not exist",
            "status": "Not Found"
        }), 404)


class UserOrders(Resource):
    """This class gets all orders for a user"""

    @jwt_required
    def get(self, user_id):
        """
        Gets all orders belonging to a specific user
        :param user_id:
        :return: returns a json response of user's orders
        """

        parcel = ParcelModel()
        try:
            user_id = int(user_id)
        except Exception:
            return make_response(
                jsonify(
                    {
                        "Message": "Please provide a valid parcel id(int)",
                        "status": "Bad request"
                    }
                ), 400)
        parcels = parcel.get_user_orders(user_id)
        if len(parcels) > 0:
            return make_response(jsonify(
                {
                    "Parcels": parcels,
                    "status": "OK"
                }
            ), 200)
        return make_response(jsonify(
            {
                "Message": "Requested resources not found",
                "status": "Not Found"
            }
        ), 404)
