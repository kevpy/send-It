"""Instance of Flask application"""
import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from .api.v1 import version1_bp


def create_app():
    """Creates an instance of a flask application
    :returns returns an instance of a flask app
    """
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY') or "secret"
    jwt = JWTManager(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    app.register_blueprint(version1_bp, url_prefix='/api/v1')

    @app.errorhandler(404)
    def url_doesnt_exist(error):
        return jsonify({
            "Message": "The requested resource does not exist"
        }), 404

    return app
