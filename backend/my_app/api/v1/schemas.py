"""This modules provides schemas for model data"""
from marshmallow import Schema, fields
from .validators import is_empty


class UserPostSchema(Schema):
    """ This class creates a schema to validate user json post data"""
    name = fields.String(required=True, validate=is_empty)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=is_empty)
    role = fields.String(required=True, validate=is_empty)


class UserLoginSchema(Schema):
    """ This class creates a schema to validate user json post data"""
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=is_empty)


class ParceCreateSchema(Schema):
    """ This class creates a schema for creating a ne parcel order"""
    sender_id = fields.Integer(required=True)
    pickup_location = fields.String(required=True, validate=is_empty)
    destination = fields.String(required=True, validate=is_empty)
    weight = fields.String(required=True, validate=is_empty)
    status = fields.String(required=True, validate=is_empty)
    price = fields.String(required=True, validate=is_empty)
