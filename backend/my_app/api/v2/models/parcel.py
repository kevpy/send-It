"""This is the parcel model."""
from psycopg2.extras import RealDictCursor
from ....db.db_config import init_db


class ParcelModel:
    """This class creates, gets, updates a parcel oerder"""

    def __init__(self):
        self.db = init_db()

    def add_parcel(self, data, user_id):
        """
        This method creates a new parcel delivery order

        :param data::
        :return: returns a dictionary object of a newly created parcel
                order
        """
        user_id = user_id
        parcel_details = data['parcel_details']
        recipient = data['recipient']
        pickup_location = data['pickup_location']
        destination = data['destination']
        weight = data['weight']
        price = data['price']

        parcel = {
            'user_id': user_id,
            'parcel_details': parcel_details,
            'recipient': recipient,
            'origin': pickup_location,
            'destination': destination,
            'weight': int(weight),
            'price': int(price)
        }
        query = """INSERT INTO parcels
                        (user_id, parcel_details,
                         recipient, weight, origin,
                         destination, price)
                  VALUES
                       ({}, '{}', '{}', {}, '{}', '{}', {})
                """.format(user_id, parcel_details,
                           recipient, weight, pickup_location,
                           destination, price)
        cursor = self.db.cursor()
        cursor.execute(query, parcel)
        self.db.commit()

        return parcel

    def get_all(self):
        """ This method gets all parcels in the application"""
        query = """ SELECT * FROM parcels """

        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        parcels = cursor.fetchall()
        return parcels

    def get_one_parcel(self, parcel_id):
        """
        Takes in a user and returns a user
        :param email:
        :return: Returns a user
        """
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """SELECT * FROM parcels
               WHERE parcel_id='{}'""".format(parcel_id))
        data = cursor.fetchone()
        return data

    def change_status(self, parcel_id):
        """This function changes the status of a parcel"""
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """UPDATE parcels
                   SET status = '{}'
                   WHERE parcel_id = {}
                   AND status = '{}'
                   """.format('delivered',
                              parcel_id,
                              'pending delivery')
        cursor.execute(query)
        self.db.commit()
        parcel = self.get_one_parcel(parcel_id)
        return parcel

    def change_present_location(self, current_location, parcel_id):
        """This function changes the status of a parcel"""
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """UPDATE parcels
                   SET current_location = '{}'
                   WHERE parcel_id = {}
                   """.format(current_location,
                              parcel_id)
        cursor.execute(query)
        self.db.commit()
        parcel = self.get_one_parcel(parcel_id)
        return parcel

    def change_destination(self, destination, parcel_id):
        """
        This method updates the destination of a parcel
        :param parcel_id:
        :param destination:
        :return: Returns none
        """
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """UPDATE parcels
                           SET destination = '{}'
                           WHERE parcel_id = {}
                           AND status = '{}'
                           """.format(destination,
                                      parcel_id,
                                      'pending delivery')
        cursor.execute(query)
        parcel = self.get_one_parcel(parcel_id)
        return parcel
