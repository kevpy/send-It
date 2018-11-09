"""
This module creates authentication views.
Both registration and login views.
"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.user_model import User
from ..validators import UserPostSchema


class Register(Resource, User):
    """ This class creates a view for registering a new user"""

    def __init__(self):
        pass

    def post(self):
        """
        Saves a new user
        :return: Returns a json response.
        """
        validator = UserPostSchema()
        data = request.get_json() or {}
        is_valid = validator.validate_post(data)

        if is_valid is not None:
            return make_response(jsonify({
                "Message": is_valid,
                "status": "Bad Request"
            }), 400)
        user_exist = self.get_user(data['email'])
        if user_exist is not None:
            return make_response(jsonify({
                "message": "User already exists"
            }), 409)
        else:
            self.add_user(data)
            print(User.users)
            return make_response(jsonify({
                "message": "User saved",
                "status": "Created"
            }), 201)
