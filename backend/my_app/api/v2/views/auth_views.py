"""
This module creates authentication views.
Both signup and login views.
"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt_identity
from ..models.user import User
from ..utils.schemas import UserPostSchema, UserLoginSchema
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
                "Message": is_valid
            }), 400)
        user_exist = user.get_user(data['email'].lower())
        if user_exist is not None:
            return make_response(jsonify({
                "Message": "User with given email address exist"
            }), 409)
        new_user = user.add_user(data)
        return make_response(jsonify({
            "Message": "User saved successfully",
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
            }), 400)
        check_user = user.get_user(data['email'])
        if not check_user:
            return make_response(jsonify({
                "Message": "User doesn't exists"
            }), 404)
        check_pass = user.verify_password(
            data['password'], check_user['password'])
        if not check_pass:
            return make_response(jsonify({
                "Message": "Incorrect Password",
            }), 400)

        access_token = create_access_token(identity=check_user['email'])
        return make_response(jsonify({
            "Message": "Successful login",
            "token": access_token
        }), 200)


def check_role():
    user = User()
    user_email = get_jwt_identity()
    role = user.check_admin(user_email)
    return role


def check_user():
    user = User()
    user_email = get_jwt_identity()
    get_user = user.get_user(user_email)
    return get_user
