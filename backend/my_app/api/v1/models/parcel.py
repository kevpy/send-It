"""This is the parcel model."""
import uuid


class ParcelModel:
    """This class creates, gets, updates a parcel oerder"""
    parcels = []

    def add_parcel(self, data, user_id):
        """
        This method creates a new parcel delivery order

        :param data::
        :return: returns a dictionary object of a newly created parcel
                order
        """
        sender_id = user_id
        parcel_details = data['parcel_details']
        pickup_location = data['pickup_location']
        destination = data['destination']
        weight = data['weight']
        price = data['price']

        parcel_id = uuid.uuid4().int >> 64

        parcel = {
            'parcel_id': parcel_id,
            'sender_id': sender_id,
            'parcel_details': parcel_details,
            'pickup_location': pickup_location,
            'destination': destination,
            'weight': weight,
            'status': "pending delivery",
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

        if parcel is not None and parcel_id == int(data['parcel_id']):
            parcel['status'] = "canceled"
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
