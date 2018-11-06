"""
Creates views for parcels. These are POST, GET, PUT
"""

from flask import request, make_response, jsonify
from flask_restful import Resource
from ..models.parcel import ParcelModel


class Parcels(Resource):
    """This class provides access operation for GET and POST methods
    for a parcel order or parcels
    """

    def __init__(self):
        pass

    def post(self):
        """Saves a new parcel item
        :return: Returns a json response
        """
        data = request.get_json() or {}

        parcel = ParcelModel()
        parcel.add_parcel(
            sender_id=data['sender_id'],
            pickup_location=data['pickup_location'],
            destination=data['destination'],
            weight=data['weight'],
            status=data['status'])

        payload = {'status': 'created'}
        res = make_response(jsonify(payload), 201)
        res.content_type = 'application/json;charset=utf-8'
        return res

    def get(self):
        """Gets all parcel orders
        :return: Returns a json response
        """
        parcel = ParcelModel()

        payload = {"Status": "OK", "Parcels": parcel.get_all()}

        res = make_response(jsonify(payload), 200)
        res.content_type = 'application/json;charset=utf-8'
        return res


class SpecificParcel(Resource, ParcelModel):
    """This class gets a single parcel order"""

    def __init__(self):
        pass

    def get(self, parcel_id):
        """
        Gets a single parcel order
        :param parcelId:
        :return: Returns a json response
        """
        try: parcel_id = int(parcel_id)
        except: return make_response(
                jsonify(
                    {
                        "Message": "Please provide a valid parcel id(int)",
                        "status": "Bad request"
                    }
                ), 400)
        single_parcel = self.get_specific_parcel(parcel_id)
        if single_parcel is not None:
            return make_response(jsonify(
                {
                    "parcel": single_parcel, "status": "OK"
                }
            ), 200)
        return make_response(
                jsonify({
                    "Parcel": "No parcel found",
                    "status": "Not Found"
                }), 404)


class CancelOrder(Resource, ParcelModel):
    """This class cancels an order"""

    def put(self, parcel_id):
        """
        Updates the status of a parcel order to canceled
        :param parcel_id:
        :return: Returns a json response
        """
        data = request.get_json() or {}
        change = self.cancel_order(parcel_id, data)

        if change is not False:
            return make_response(jsonify(
                {
                    "Message": "success",
                    "status": "Accepted"
                }
            ), 202)
        return make_response(jsonify(
            {
                "Message": "The order requested does not exist",
                "status": "Not Found"
            }
        ), 404)


class UserOrders(Resource, ParcelModel):
    """This class gets all orders for a user"""

    def get(self, user_id):
        """
        Gets all orders belonging to a specific user
        :param user_id:
        :return: returns a json response of user's orders
        """
        try: user_id = int(user_id)
        except: return make_response(
                jsonify(
                    {
                        "Message": "Please provide a valid parcel id(int)",
                        "status": "Bad request"
                    }
                ), 400)
        parcels = self.get_user_orders(user_id)
        if len(parcels) > 0:
            return make_response(jsonify(
                {
                    "Parcels": parcels,
                    "Status": "Ok"
                }
            ), 200)
        return make_response(jsonify(
            {
                "Message": "Requested resources not found",
                "status": "Not Found"
            }
        ), 404)
