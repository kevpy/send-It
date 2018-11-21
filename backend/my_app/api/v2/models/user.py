"""This module creates a user model."""
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash
from ....db.db_config import init_db


class User():
    """This class creates a new user object.
    It has a add_user method that stores a created user object to a list
    and a get_user method that gets  one specific user
    """

    def __init__(self):
        self.db = init_db()

    def add_user(self, data):
        """
        This method creates a new user and adds them to a list
        :param data:
        :return:
        """
        name = data['name']
        email = data['email']
        password = generate_password_hash(data['password'])

        if len(data) is 4:
            role = data['role']
        else:
            role = 'user'

        user = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        query = """INSERT INTO users (name, email, password, user_role) VALUES
                   (%(name)s, %(email)s, %(password)s, %(role)s)
        """
        cursor = self.db.cursor()
        cursor.execute(query, user)
        self.db.commit()
        del data['password']
        return data

    def get_user(self, email):
        """
        Takes in a user and returns a user
        :param email:
        :return: Returns a user
        """
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """SELECT * FROM users
               WHERE email='{}'""".format(email))
        data = cursor.fetchone()
        return data

    def check_admin(self, email):
        """
        Takes in an email address and and check if user is admin
        :param email:
        :return: Returns True if is Admin else False
        """
        user = self.get_user(email)
        if user['user_role'].lower() != 'admin':
            return False
        return True

    def verify_password(self, password, password_hash):
        return check_password_hash(password_hash, password)
