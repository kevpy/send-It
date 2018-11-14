""" This module holds data for testing various views and tests"""

# Data for tests setup
create_test_order = {
    "sender_id": 1,
    "parcel_id": 1,
    "pickup_location": "Nakuru",
    "destination": "Eldoret",
    "weight": "10KG",
    "status": "pending delivery",
    "price": "KES500"
}

create_test_user = {
    "name": "Test",
    "email": "test@email.com",
    "password": "password",
    "role": "user"
}

# Data for parcel views
create_order = {
    "sender_id": 1,
    "pickup_location": "Nakuru",
    "destination": "Eldoret",
    "weight": "10KG",
    "status": "pending delivery",
    "price": "KES500"
}

cancel_order = {
    "sender_id": 1,
    "pickup_location": "Nakuru",
    "destination": "Eldoret",
    "weight": "10KG",
    "status": "canceled"
}

empty_data = {}

# Data for auth_views
valid_user = {
    "name": "Test2",
    "email": "user@email.com",
    "password": "password",
    "role": "user"
}

invalid_user = {
    "name": "Test",
    "email": "email.com",
    "password": "password",
    "role": "user"
}

existing_user = {
    "name": "Test",
    "email": "test@email.com",
    "password": "password",
    "role": "user"
}

some_missing = {
    "name": "Test",
    "password": "password",
    "role": "user"
}

empty_data = {}

invalid_email_login = {
    "email": "testemail.com",
    "password": "password"
}

wrong_login_password = {
    "email": "test@email.com",
    "password": "wrong"
}

user_doesnt_exist_login = {
    "email": "new@email.com",
    "password": "password"
}
