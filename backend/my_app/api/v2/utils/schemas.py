from marshmallow import Schema, fields
from .validators import is_empty


class UserPostSchema(Schema):
    """This class creates a validation schema to validate user json post data.
    """
    name = fields.String(required=True, validate=is_empty)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=is_empty)
    role = fields.String(required=True, validate=is_empty)


class UserLoginSchema(Schema):
    """T
    his class creates a validation schema to validate user json post data.
    """
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=is_empty)
