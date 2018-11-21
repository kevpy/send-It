""" This module holds data for tests """

# Data for user registration

VALID_USER = {
    "name": "Test2",
    "email": "user@email.com",
    "password": "PassW0rd"
}

INVALID_USER = {
    "name": "Test",
    "email": "email.com",
    "password": "PassW0rd",
    "role": "user"
}

EXISTING_USER = {
    "name": "Test",
    "email": "user@email.com",
    "password": "PassW0rd"
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

# Login view test data
INVALID_EMAIL_LOGIN = {
    "email": "testemail.com",
    "password": "password"
}

WRONG_LOGIN_PASSWORD = {
    "email": "user@email.com",
    "password": "wrong"
}

USER_NOT_EXIST_LOGIN = {
    "email": "new@email.com",
    "password": "password"
}

CREATE_TEST_USER = {
    "name": "Test",
    "email": "test@email.com",
    "password": "Passw0rd"
}

# Data for parcels
CREATE_PARCEL = {
    "recipient": "Kezzy",
    "parcel_details": "Spare parts",
    "pickup_location": "Mombasa",
    "destination": "Nairobi",
    "price": 2,
    "weight": 5
}

EMPTY_STRING_PARCEL = {
    "recipient": "Kezzy",
    "parcel_details": "Spare parts",
    "pickup_location": "",
    "destination": "Nairobi",
    "price": 2,
    "weight": 5
}

MISSING_OPTIONS = {
    "recipient": "Kezzy",
    "parcel_details": "Spare parts",
    "pickup_location": " ",
    "price": 2,
    "weight": 5
}
