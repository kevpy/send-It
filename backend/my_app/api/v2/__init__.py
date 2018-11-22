from flask import Blueprint
from flask_restful import Api
from .views.auth_views import Register, Login
from .views.parcel_views import (Parcels, ChangeStatus,
                                 ChangePresentLocation)

version2_bp_auth = Blueprint('api_v2', __name__)
v2_bp = Blueprint('api_routes_v2', __name__)

api_auth_v2 = Api(version2_bp_auth)
api_v2 = Api(v2_bp)

api_auth_v2.add_resource(Register, '/auth/signup')
api_auth_v2.add_resource(Login, '/auth/login')
api_v2.add_resource(Parcels, '/parcels')
api_v2.add_resource(ChangeStatus, '/parcels/<parcel_id>/status')
api_v2.add_resource(ChangePresentLocation, '/parcels/<parcel_id>/presentLocation')
