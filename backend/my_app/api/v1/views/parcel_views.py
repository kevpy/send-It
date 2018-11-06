"""
Creates views for parcels. These are POST, GET, PUT
"""

from flask import request, make_response, jsonify
from flask_restful import Api, Resource
from ..models.parcel import ParcelModel
from ...v1 import version1_bp

parcels_bp = Api(version1_bp)


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

    def get(self, parcelId):
        """
        Gets a single parcel order
        :param parcelId:
        :return: Returns a json response
        """
        if not parcelId or not isinstance(int(parcelId), int):
            return make_response(
                jsonify({
                    "Message": "Please provide a valid parcel id(int)",
                    "status": 404
                }))
        single_parcel = self.get_specific_parcel(parcelId)
        if single_parcel is not None:
            return make_response(jsonify({"parcel": single_parcel, "status": 200}))
        return make_response(
                jsonify({
                    "Parcel": "No parcel found",
                    "status": 404
                }))


parcels_bp.add_resource(Parcels, "/parcels")
parcels_bp.add_resource(SpecificParcel, "/parcels/<int:parcelId>")
