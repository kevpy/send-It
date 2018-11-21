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
