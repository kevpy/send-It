from flask import Blueprint
from flask_restful import Api
from .views.auth_views import Register, Login
from .views.parcel_views import (Parcels, ChangeStatus, CancelOrder,
                                 ChangePresentLocation, ChangeOrderDestination,
                                 GetSpecificOrder, GetAllUsersParcels)

v2_bp = Blueprint('api_routes_v2', __name__)

api_v2 = Api(v2_bp)

api_v2.add_resource(Register, '/auth/signup')
api_v2.add_resource(Login, '/auth/login')
api_v2.add_resource(Parcels, '/parcels')
api_v2.add_resource(ChangeStatus, '/parcels/<parcel_id>/status')
api_v2.add_resource(ChangePresentLocation, '/parcels/<parcel_id>/presentLocation')
api_v2.add_resource(ChangeOrderDestination, '/parcels/<parcel_id>/destination')
api_v2.add_resource(CancelOrder, '/parcels/<parcel_id>/cancel')
api_v2.add_resource(GetSpecificOrder, '/parcels/<parcel_id>')
api_v2.add_resource(GetAllUsersParcels, '/users/<user_id>/parcels')
