from flask import Blueprint
from flask_restful import Api
from .views.parcel_views import (Parcels, SpecificParcel, CancelOrder,
                                 UserOrders)

version1_bp = Blueprint('api', __name__)

api = Api(version1_bp)

api.add_resource(Parcels, "/parcels")
api.add_resource(SpecificParcel, "/parcels/<parcel_id>")
api.add_resource(CancelOrder, "/parcels/<int:parcel_id>/cancel")
api.add_resource(UserOrders, "/users/<user_id>/parcels")
