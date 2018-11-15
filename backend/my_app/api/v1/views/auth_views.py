"""
This module creates authentication views.
Both registration and login views.
"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from ..models.user_model import User
from ..validators import validate_json
from ..schemas import UserLoginSchema, UserPostSchema


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
        if user_exist is not None:
            return make_response(jsonify({
                "message": "User already exists"
            }), 409)
        else:
            new_user = user.add_user(data)
            return make_response(jsonify({
                "message": "User saved",
                "status": "Created",
                "data": new_user
            }), 201)


class Login(Resource):
    """This class creates a view for login/authentication"""

    def post(self):
        """
        Authenticates a user with an email and password
        :return: Returns a json response
        """
        user = User()
        schema = UserLoginSchema()
        data = request.get_json() or {}
        is_valid = validate_json(schema, data)

        if is_valid is not None:
            return make_response(jsonify({
                "Message": is_valid,
                "status": "Bad Request"
            }), 400)
        user = user.get_user(data['email'])
        if not user:
            return make_response(jsonify({
                "message": "User doesn't exists"
            }), 404)
        if data['password'] != user['password']:
            return make_response(jsonify({
                "message": "Incorrect Password",
            }), 400)

        access_token = create_access_token(identity=user['email'])
        return make_response(jsonify({
            "message": "Successful login",
            "token": access_token
        }), 200)
