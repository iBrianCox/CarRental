from .auth import Auth
from Models.RentalAgency import RentalAgency


class Model:
    def __init__(self):
        self.auth = Auth()
        self.rentalAgency = RentalAgency()
