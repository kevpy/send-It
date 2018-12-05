"""This modules provides validators for models"""
import re
from marshmallow import ValidationError
from flask import jsonify, make_response


def validate_url_params(value):
    """
    Takes in a url wild card and checks if it is an id.
    :param value:
    :raises: Raises an exception
    """
    try:
        my_id = int(value)
    except Exception:
        return make_response(
            jsonify(
                {
                    "Message": "Please provide a valid parcel id - integer "
                }
            ), 400)


def is_empty(value):
    """
    Takes in a parameter value and strips if of space characters.
    If the value is an empty string it raises a ValidationError
    :param value:
    :raises: Raises ValidationError
    """
    if value.strip() == '':
        raise ValidationError('Value provided cannot be empty')


def is_admin(value):
    """ Takes in a value and checks the value if it is admin
    If the value is not admin, it raises a ValidationError
    :params value:
    :raises: Raises ValidationError
    """
    role = value.lower()
    if role != 'admin':
        raise ValidationError('Wrong value for input provided')


def is_strong(value):
    """ Takes in a value and checks the value if it has atleast
    a 1 lowercase, 1 uppercase, and 1 numeric character in it.
    If the value is not admin, it raises a ValidationError
    :params value:
    :raises: Raises ValidationError
    """
    pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})")
    if pattern.match(value) is None:
        raise ValidationError(
            'Value should be at least 1 digit, 1 lower, 1 uppercase and 6 characters long')


def is_digit(value):
    """ Takes in a string and checks the value if it is composed of digits.
    If the value is not admin, it raises a ValidationError
    :params value:
    :raises: Raises ValidationError
    """
    test = value.isdigit()
    if test:
        raise ValidationError('You cannot have only numbers for a name')


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


def err_message(message):
    """
    This function takes in a Marshmallow error message.
    It mutates the dict message into a simple dictionary
    object to easily consume.
    :param message:
    :return: Returns a dictionary
    """
    msg = {}
    for k, v in message.items():
        msg[k] = v[0]
    print(msg)
    return make_response(jsonify(msg), 400)
