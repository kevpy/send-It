"""This modules provides validators for models"""
from marshmallow import Schema, fields, ValidationError


class UserPostSchema(Schema):
    """ This class creates a schema to validate user json post data"""
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)


class UserLoginSchema(Schema):
    """ This class creates a schema to validate user json post data"""
    email = fields.Email(required=True)
    password = fields.String(required=True)


def validate_json(my_schema, json=None):
    """
        This function takes in a schema and a json data object.
        It then validate the json object from the schema.
        :param my_schema:
        :param json:
        :return: Returns None, or a validation error message.
        """
    try:
        my_schema.load(json)
    except ValidationError as e:
        return e.messages
