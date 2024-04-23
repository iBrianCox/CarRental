from enum import Enum

class RentalPeriod(Enum):
    DAILY=1
    WEEKLY=2
    MONTHLY=3
    
    @staticmethod
    def from_str(label):
        if label == "days":
            return RentalPeriod.DAILY
        elif label == "weeks":
            return RentalPeriod.WEEKLY
        elif label == "months":
            return RentalPeriod.MONTHLY
        else:
            return None

class Car():
    def __init__(self, id, model, make, color, cost, doors, mileage,
                 rented, customer, rentalPeriod):
        self.id = id
        self.model = model
        self.make = make
        self.color = color
        self.cost = cost
        self.doors = doors
        self.mileage = mileage
        self.customer = customer
        self.rented = rented
        self.rental_period = rentalPeriod
        self.rental_cost = 0


