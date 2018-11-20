""" This module holds data for tests """

# Data for user registration

VALID_USER = {
    "name": "Test2",
    "email": "user@email.com",
    "password": "password",
    "role": "user"
}

INVALID_USER = {
    "name": "Test",
    "email": "email.com",
    "password": "password",
    "role": "user"
}

EXISTING_USER = {
    "name": "Test",
    "email": "user@email.com",
    "password": "password",
    "role": "user"
}

SOME_MISSING = {
    "name": "Test",
    "password": "password",
    "role": "user"
}

EMPTY_STRINGS = {
    "name": "",
    "email": "user@email.com",
    "password": "password",
    "role": "user"
}

EMPTY_DATA = {}
