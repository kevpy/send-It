"""This is the parcel model."""
import uuid


class ParcelModel:
    """This class creates, gets, updates a parcel oerder"""
    parcels = []

    def add_parcel(self, data):
        """
        This method creates a new parcel delivery order

        :param data::
        :return: returns a dictionary object of a newly created parcel
                order
        """
        sender_id = data['sender_id']
        pickup_location = data['pickup_location']
        destination = data['destination']
        weight = data['weight']
        status = data['status']
        price = data['price']

        parcel_id = uuid.uuid4().int >> 64

        parcel = {
            'parcel_id': parcel_id,
            'sender_id': sender_id,
            'pickup_location': pickup_location,
            'destination': destination,
            'weight': weight,
            'status': status,
            'price': price
        }

        ParcelModel.parcels.append(parcel)

        return parcel

    def get_all(self):
        """Gets all parcel orders"""
        return ParcelModel.parcels

    def get_specific_parcel(self, parcel_id):
        """
        Gets a specific parcel order when given a parcel id
        :param parcel_id:
        :return: returns a parcel order or None
        """
        parcel = next((item for item in ParcelModel.parcels
                       if item['parcel_id'] == parcel_id), None)
        return parcel

    def cancel_order(self, parcel_id, data):
        """
        Gets a parcel order and changes it's status to canceled.
        :param parcel_id:
        :param data:
        :return:
        """
        parcel = self.get_specific_parcel(parcel_id)

        if parcel is not None:
            parcel['status'] = data['status']
            return parcel
        return None

    def get_user_orders(self, user_id):
        """
        Get all orders belonging to a specific user
        :param user_id:
        :return: returns all parcel orders for a specific user or None
        """
        parcels = [item for item in ParcelModel.parcels
                   if item['sender_id'] == user_id]

        return parcels
