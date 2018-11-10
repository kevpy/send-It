"""Instance of Flask application"""
from flask import Flask
from flask_jwt_extended import JWTManager
from .api.v1 import version1_bp


def create_app():
    """Creates an instance of a flask application
    :returns returns an instance of a flask app
    """
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "secret"
    jwt = JWTManager(app)

    app.register_blueprint(version1_bp, url_prefix='/api/v1')

    return app
