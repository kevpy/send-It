from flask import Blueprint
from flask_restful import Api
from .views.auth_views import Register

version2_bp_auth = Blueprint('api_v2', __name__)

api_auth_v2 = Api(version2_bp_auth)

api_auth_v2.add_resource(Register, '/auth/signup')
