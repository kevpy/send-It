"""This is the parcel model."""
import uuid
from flask import jsonify, make_response


class ParcelModel:
    """This class creates, gets, updates a parcel oerder"""
    parcels = [
        {
            "parcel_id": 1,
            "sender_id": 1,
            "pickup_location": "Nakuru",
            "destination": "Nairobi",
            "weight": "10KG",
            "status": "pending delivery"
        },
        {
            "parcel_id": 2,
            "sender_id": 2,
            "pickup_location": "Nakuru",
            "destination": "Eldoret",
            "weight": "5KG",
            "status": "pending delivery"
        },
        {
            "parcel_id": 3,
            "sender_id": 2,
            "pickup_location": "Nairobi",
            "destination": "Mombasa",
            "weight": "1KG",
            "status": "pending delivery"
        }
    ]

    def add_parcel(self,
                   sender_id,
                   pickup_location,
                   destination,
                   weight,
                   status='penging_delivery'):
        """
        This method creates a new parcel delivery order

        :param sender_id:
        :param pickup_location:
        :param destination:
        :param weight:
        :param status:
        :return: returns a dictionary object of a newly created parcel
                order
        """
        parcel_id = uuid.uuid4().int >> 64

        parcel = {
            'parcel_id': parcel_id,
            'sender_id': sender_id,
            'pickup_location': pickup_location,
            'destination': destination,
            'weight': weight,
            'status': status
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

    def cast_id(self, my_id):
        """
        Casts a provided id to an integer
        :param my_id:
        :return:
        """
        try:
            check_id = int(my_id)
        except Exception:
            return make_response(
                jsonify(
                    {
                        "Message": "Please provide a valid parcel id(int)",
                        "status": "Bad request"
                    }
                ), 400)
        else:
            return check_id
