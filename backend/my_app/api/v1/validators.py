"""This modules provides validators for models"""
from marshmallow import ValidationError


def is_empty(value):
    """
    Takes in a parameter value and strips if of space characters.
    If the value is an empty string it raises a ValidationError
    :param value:
    :raises: Raises ValidationError
    """
    if value.strip() == '':
        raise ValidationError('Value provided cannot be empty')


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
