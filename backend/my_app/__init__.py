"""Instance of Flask application"""
import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from .api.v1 import version1_bp
from .api.v2 import v2_bp
from .db.db_config import create_tables


def create_app(config_name):
    """Creates an instance of a flask application
    :returns returns an instance of a flask app
    """
    app = Flask(__name__)
    create_tables()
    app.config["JWT_SECRET_KEY"] = os.environ.get('SECRET_KEY') or "secret"
    jwt = JWTManager(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    app.register_blueprint(version1_bp, url_prefix='/api/v1')
    app.register_blueprint(v2_bp, url_prefix='/api/v2')

    @app.errorhandler(404)
    def url_doesnt_exist(error):
        return jsonify({
            "Message": "The requested resource does not exist"
        }), 404

    @jwt.unauthorized_loader
    def no_token(e):
        return jsonify({
            "Message": "Authorization token is needed"
        }), 400

    @jwt.expired_token_loader
    def expired_token():
        return jsonify({
            "Message": "Unauthorized, your token is expired."
        }), 401

    @app.route('/')
    def home():
        return 'Welcome to SendIt app'

    return app
