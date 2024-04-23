import tkinter as tk
from Models.RentalAgency import RentalAgency
from Models.main import Model
from Views.main import View
from Models.Car import Car, RentalPeriod


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self.rental_agency = self.model.rentalAgency
        self._bind()


    def handle_radiobutton_selection(self):
        selected_period = self.frame.radio_button_selected.get()
        selection = RentalPeriod.from_str(selected_period)
        print("radio button selected: " + selected_period)
        
        self.frame.periodlabel.config(text="Rental Period: (" + selected_period + ")")
        
        self.frame.periodvalue.delete(0, "end")

        self.frame.available_cars_listbox.delete(0,'end')       
        
        for car in self.rental_agency.cars:
            if selection == car.rental_period:
                self.frame.available_cars_listbox.insert(car.id, car.model)
                
    def handle_rental_period_entry(self):
        print("period value: " + self.frame.periodvalue.get())
        
    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        rental_agency = self.model.rentalAgency
        
        # repopulate the listboxes
        self.frame.available_cars_listbox.delete(0, "end")
        self.frame.rented_cars_listbox.delete(0, "end")

        self.handle_radiobutton_selection()
            
        for rented_car in rental_agency.rentals:
            self.frame.rented_cars_listbox.insert(rented_car.id, rented_car.model)
        
        if current_user:
            username = current_user["username"]
            self.frame.header.config(text=f"Welcome, {username}!")
        else:
            self.frame.header.config(text=f"")
            
    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.available_cars_listbox.bind('<<ListboxSelect>>', self.available_car_selected)
        self.frame.rentbutton.config(command=self.rent_car)
        self.frame.returnbutton.config(command=self.return_car)

        self.frame.dailybutton.config(command=self.update_view)
        self.frame.weeklybutton.config(command=self.update_view)
        self.frame.monthlybutton.config(command=self.update_view)
        
        reg = self.model.rentalAgency.validate_input
        
    def clear_selected_car(self):
        self.frame.makevalue.config(text="")
        self.frame.modelvalue.config(text="")
        self.frame.costvalue.config(text="")
        self.frame.doorsvalue.config(text="")
        self.frame.colorvalue.config(text="")

    def available_car_selected(self, event) -> None:
        w = event.widget
        
        # handle the case where no car is selected but the event is triggered
        if not w.curselection():
            return
        
        selected_car = self.selected_available_car()
        print(selected_car)
        
        for car in self.model.rentalAgency.cars:
            if car.model == selected_car:
                self.frame.makevalue.config(text=car.make)
                self.frame.modelvalue.config(text=car.model)
                self.frame.costvalue.config(text=car.cost)
                self.frame.doorsvalue.config(text=car.doors)
                self.frame.colorvalue.config(text=car.color)
                break

    def selected_available_car(self):
        for i in self.frame.available_cars_listbox.curselection():
            return(self.frame.available_cars_listbox.get(i))
            
    def selected_rented_car(self):
        for i in self.frame.rented_cars_listbox.curselection():
            return(self.frame.rented_cars_listbox.get(i))
            
    def calculate_rental_cost(self, car_model):
        cost = 0
        rental_period = self.frame.periodvalue.get()
        rental_mode = self.frame.radio_button_selected.get()
        print("rental period: " + rental_period)
        
        car = self.rental_agency.selectAvailableCar(car_model)
        
        if rental_mode == "days":
            cost = int(car.cost) * int(rental_period)
        elif rental_mode == "weeks":
            cost = int(car.cost) * int(rental_period) * 7
        elif rental_mode == "months":
            cost = int(car.cost) * int(rental_period) * 30
            
        print("cost: " + str(cost))
        
        car.rental_cost = cost
        
        return cost
    
    def rent_car(self):
        # handle the case where no car is selected but the event is triggered
        if not self.frame.available_cars_listbox.curselection():
            return
        
        print("Renting car")
        
        self.clear_selected_car();

        selected_car = self.selected_available_car()
        
        self.calculate_rental_cost(selected_car)

        self.rental_agency.rentCar(selected_car)
        self.update_view()
         
    def return_car(self):
        # handle the case where no car is selected but the event is triggered
        if not self.frame.rented_cars_listbox.curselection():
            return
        
        print("Returning car")
        customer = self.model.rentalAgency.current_customer
        
        selected_car = self.selected_rented_car()
        self.rental_agency.returnCar(selected_car)
        
        car = self.rental_agency.selectAvailableCar(selected_car)       

        self.frame.bill_listbox.insert(tk.END, selected_car + " $" + str(car.rental_cost))
        customer.total_cost += car.rental_cost
        self.frame.total.config(text="Total: $" + str(customer.total_cost))
        
        car.rental_cost = 0;
        self.update_view()

