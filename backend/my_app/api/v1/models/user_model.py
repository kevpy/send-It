""" This module creates a model for users"""
import uuid


class User():
    """This class creates a new user object.
    It has a add_user method that stores a created user object to a list
    and a get_user method that gets  one specific user
    """
    users = [{
        "user_id": 1,
        "name": "Test",
        "email": "test@email.com",
        "password": "password",
        "role": "user"
    }]

    def __init__(self):
        pass

    def add_user(self, data):
        """
        This method creates a new user and adds them to a list
        :param data:
        :return:
        """
        name = data['name']
        email = data['email']
        password = data['password']
        role = data['role']

        user_id = uuid.uuid4().int >> 64

        user = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        self.users.append(user)
        return user

    def get_user(self, email):
        user = next((user for user in User.users
                     if user['email'] == email), None)
        return user
