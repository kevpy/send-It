"""Instance of Flask application"""
from flask import Flask, jsonify


def create_app():
    """Creates an instance of a flask application """
    app = Flask(__name__)

    @app.route('/test', methods=['GET'])
    def test():
        return jsonify({'status': 'Epic success', 'message': 'pong!'}), 200

    return app
