import Models.Car as Car
import Models.Customer as Customer

class RentalAgency():
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []
        self.initCars()
        self.current_customer = None
       # self.initCustomers()
        
        
    def initCars(self):
        self.cars.append(Car.Car(1,"911", "Porsche", "Black", "225", 2, 0, False, None, Car.RentalPeriod.DAILY))
        self.cars.append(Car.Car(1,"Portofino", "Ferrari", "Red", "375", 4, 0, False, None, Car.RentalPeriod.DAILY))
        self.cars.append(Car.Car(1,"Aventador", "Lamborghini", "Purple", "425", 2, 0, False, None, Car.RentalPeriod.DAILY))
        self.cars.append(Car.Car(1,"Superleggera", "Aston Martin", "Red", "395", 2, 0, False, None, Car.RentalPeriod.DAILY))
        self.cars.append(Car.Car(2,"Model 3", "Tesla", "Black", "78", 4, 0, False, None, Car.RentalPeriod.WEEKLY))
        self.cars.append(Car.Car(3,"Model S", "Tesla", "White", "99", 4, 0, False, None, Car.RentalPeriod.WEEKLY))
        self.cars.append(Car.Car(6,"Elantra", "Hyundai", "Green", "45", 4, 0, False, None, Car.RentalPeriod.WEEKLY))
        self.cars.append(Car.Car(6,"Arteon", "Volkswagen", "Gray", "75", 4, 0, False, None, Car.RentalPeriod.WEEKLY))
        self.cars.append(Car.Car(6,"CT4", "Cadillac", "Black", "75", 4, 0, False, None, Car.RentalPeriod.WEEKLY))
        self.cars.append(Car.Car(4,"Camry", "Toyota", "Red", "63", 4, 0, False, None, Car.RentalPeriod.MONTHLY))
        self.cars.append(Car.Car(5,"Corolla", "Toyota", "Blue", "29", 4, 0, False, None, Car.RentalPeriod.MONTHLY))
        self.cars.append(Car.Car(7,"Escort", "Ford", "Orange", "29", 4, 0, False, None, Car.RentalPeriod.MONTHLY))
        self.cars.append(Car.Car(7,"Mustang", "Ford", "Yellow", "85", 4, 0, False, None, Car.RentalPeriod.MONTHLY))
        self.cars.append(Car.Car(7,"Pathfinder", "Nissan", "Yellow", "29", 4, 0, False, None, Car.RentalPeriod.MONTHLY))
    
    def initCustomers(self, name):
        self.current_customer = Customer.Customer(name)
        
    def selectAvailableCar(self, car_model):
        for c in self.cars:
            if c.model == car_model:
                return c
            
    def selectRentedCar(self, car_model):
        for c in self.rentals:
            if c.model == car_model:
                return c
            
    def validate_input(self,input):
        if input.isdigit():
            return True
        else:
            return False
        

    def printAvailableCars(self):
        for car in self.cars:
            print("Model: "+car.model + " Id: " + str(car.id))

    def printRentedCars(self):
        for car in self.rentals:
            print("Model: "+car.model + " Id: " + str(car.id))
        
    def rentCar(self, car_model):
        car = self.selectAvailableCar(car_model)
        if car != None:
            car.rented = True
            
            self.current_customer.rented_cars.append(car)
            
            #add car to rentals
            self.rentals.append(car)
            #remove car from available cars
            self.cars.remove(car)
            print("Renting car") 

    def returnCar(self, car_model):
        car = self.selectRentedCar(car_model)
        if (car != None):
            car.rented = False
            car.customer = None
            self.current_customer.rented_cars.remove(car)
            
            #remove car from rentals
            self.rentals.remove(car)
            #add car to available cars
            self.cars.append(car)
            print("Returning car")
