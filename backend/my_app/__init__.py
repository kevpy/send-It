"""Instance of Flask application"""
from flask import Flask, jsonify
from .api.v1 import version1_bp, parcels_bp


def create_app():
    """Creates an instance of a flask application
    :returns returns an instance of a flask app
    """
    app = Flask(__name__)

    parcels_bp.init_app(app)
    app.register_blueprint(version1_bp, url_prefix='/api/v1')

    return app
