from marshmallow import Schema, fields
from .validators import is_empty, is_digit, is_strong, is_admin


class UserPostSchema(Schema):
    """This class creates a validation schema to validate user json post data.
    """
    name = fields.String(required=True, validate=[is_empty, is_digit])
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=[is_empty, is_strong])
    role = fields.String(allow_none=True, validate=[is_empty, is_admin])


class UserLoginSchema(Schema):
    """T
    his class creates a validation schema to validate user json post data.
    """
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=is_empty)


class ParceCreateSchema(Schema):
    """
    This class creates a validation schema for creating a new parcel order.
    """
    recipient = fields.String(required=True, validate=is_empty)
    parcel_details = fields.String(required=True, validate=is_empty)
    pickup_location = fields.String(required=True, validate=is_empty)
    destination = fields.String(required=True, validate=is_empty)
    weight = fields.Integer(required=True)
    # price = fields.Integer(required=True)


class LocationSchema(Schema):
    """
    This class creates a validation schema for Location.
    """
    location = fields.String(required=True, validate=[is_empty, is_digit])
