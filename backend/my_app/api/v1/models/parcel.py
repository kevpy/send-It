"""This is the parcel model."""


class ParcelModel:
    """This class creates, gets, updates a parcel oerder"""
    parcels = []

    def __init__(self):
        pass

    def add_parcel(self,
                   sender_id,
                   pickup_location,
                   destination, weight,
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
        parcel_id = len(ParcelModel.parcels) + 1

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
