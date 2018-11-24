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
        price = weight * 2

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
                       (%s, %s, %s, %s, %s, %s, %s)
                """
        cursor = self.db.cursor()
        cursor.execute(query,
                       (user_id,
                        parcel_details,
                        recipient, weight,
                        pickup_location,
                        destination, price))
        self.db.commit()

        return parcel

    def get_all(self):
        """ This method gets all parcels in the application"""
        query = """ SELECT * FROM parcels """

        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        parcels = cursor.fetchall()
        return parcels

    def get_percel_by_id(self, parcel_id):
        """
        Takes in a user and returns a user
        :param parcel_id:
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
                   SET status = %s
                   WHERE parcel_id = %s
                   """

        cursor.execute(query, ('delivered', parcel_id))
        self.db.commit()
        parcel = self.get_percel_by_id(parcel_id)
        return parcel

    def change_present_location(self, current_location, parcel_id):
        """This function changes the status of a parcel"""
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """UPDATE parcels
                   SET current_location = %s
                   WHERE parcel_id = %s
                   """
        cursor.execute(query, (current_location, parcel_id))
        self.db.commit()
        parcel = self.get_percel_by_id(parcel_id)
        return parcel

    def change_destination(self, destination, parcel_id):
        """
        This method updates the destination of a parcel
        :param parcel_id:
        :param destination:
        :return: Returns parcel
        """
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """UPDATE parcels
                           SET destination = %s
                           WHERE parcel_id = %s
                           AND status = %s
                           """
        cursor.execute(query, (destination, parcel_id, 'pending delivery'))
        parcel = self.get_percel_by_id(parcel_id)
        return parcel

    def cancel_order(self, parcel_id):
        """
        This function cancels an order if it is yet to be delivered
        :param parcel_id:
        :return: Returns a parcel
        """
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """UPDATE parcels
                           SET status = %s
                           WHERE parcel_id = %s
                           AND status = %s
                           """
        cursor.execute(query, ('cancelled', parcel_id, 'pending delivery'))
        self.db.commit()
        parcel = self.get_percel_by_id(parcel_id)
        return parcel

    def get_user_parcels(self, user_id):
        """
        This functions gets all parcels that belong to one user
        Takes in user_id as a parameter
        :param user_id:
        :return: Returns parcels
        """
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """SELECT * FROM parcels
                    WHERE user_id = %s
                """
        cursor.execute(query, (user_id,))
        parcels = cursor.fetchall()
        return parcels
