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


parcels_bp.add_resource(Parcels, "/parcels")
