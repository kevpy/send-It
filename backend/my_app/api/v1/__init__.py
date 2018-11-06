from flask import Blueprint

version1_bp = Blueprint('api', __name__)

from my_app.api.v1.views.parcel_views import parcels_bp
