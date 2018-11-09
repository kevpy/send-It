"""This modules provides validators for models"""
from marshmallow import Schema, fields, ValidationError


class UserPostSchema(Schema):
    """ This class creates a schema to validate user json post data"""
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

    def validate_post(self, json=None):
        valid = UserPostSchema()
        try:
            valid.load(json)
        except ValidationError as e:
            return e.messages


class UserLoginSchema(Schema):
    """ This class creates a schema to validate user json post data"""
    email = fields.Email(required=True)
    password = fields.String(required=True)

    def validate_login(self, json=None):
        valid = UserLoginSchema()
        try:
            valid.load(json)
        except ValidationError as e:
            return e.messages
