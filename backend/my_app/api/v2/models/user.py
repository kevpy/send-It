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
        role = data['role']

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
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """SELECT * FROM users
               WHERE email='{}'""".format(email))
        data = cursor.fetchone()
        return data

    def verify_password(self, password, password_hash):
        return check_password_hash(password_hash, password)
