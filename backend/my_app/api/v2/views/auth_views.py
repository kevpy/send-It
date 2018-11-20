"""
This module creates authentication views.
Both signup and login views.
"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from ..models.user import User
from ..utils.schemas import UserPostSchema
from ..utils.validators import validate_json


class Register(Resource):
    """ This class creates a view for registering a new user"""

    def post(self):
        """
        Saves a new user
        :return: Returns a json response.
        """
        user = User()
        schema = UserPostSchema()
        data = request.get_json() or {}
        is_valid = validate_json(schema, data)

        if is_valid is not None:
            return make_response(jsonify({
                "Message": is_valid,
                "status": "Bad Request"
            }), 400)
        user_exist = user.get_user(data['email'])
        print(user_exist)
        if user_exist is not None:
            return make_response(jsonify({
                "message": "User already exists"
            }), 409)
        new_user = user.add_user(data)
        return make_response(jsonify({
            "message": "User saved",
            "status": "Created",
            "data": new_user
        }), 201)
