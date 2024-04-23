from tkinter import CENTER, DISABLED, Frame, Label, Button, Listbox, LabelFrame, Radiobutton, StringVar, Entry
from turtle import width
from typing import Self
from datetime import datetime

import Models.RentalAgency as RentalAgency

class RentalView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Rental View")
        self.header.grid(row=0, column=0,columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Available Cars
        self.labelframe_available=LabelFrame(self,text='Available Cars')
        self.labelframe_available.grid(row=1,column=0,padx=30,pady=15,sticky="n")
        
        self.radio_button_selected = StringVar()
        self.radio_button_selected.set('days')
        
        self.dailybutton = Radiobutton(self.labelframe_available, text='Daily', value='days', variable=self.radio_button_selected)
        self.dailybutton.grid(row=7, column=0, sticky="w")
        self.weeklybutton = Radiobutton(self.labelframe_available, text='Weekly', value='weeks', variable=self.radio_button_selected)
        self.weeklybutton.grid(row=8, column=0, sticky="w")
        self.monthlybutton = Radiobutton(self.labelframe_available, text='Monthly', value='months', variable=self.radio_button_selected)
        self.monthlybutton.grid(row=9, column=0, sticky="w")
       
        self.available_cars_listbox = Listbox(self.labelframe_available, height=10, width=25, bg='lightgrey', justify="left")
        self.available_cars_listbox.grid(row=1, column=0, sticky="w", padx=5, pady=10)
        
        # Car Details
        self.labelframe_details=LabelFrame(self,text='Car Details', width=255, height=275)
        self.labelframe_details.grid(row=1,column=1,padx=30,pady=15, sticky="n")

        self.costlabel = Label(self.labelframe_details,text='Cost:',justify="left", anchor="w", width=10)
        self.costlabel.grid(row=2,column=1,pady=10)
        self.costvalue=Label(self.labelframe_details,text=None, justify="left", anchor="w", width=16)
        self.costvalue.grid(row=2,column=2)

        self.makelabel=Label(self.labelframe_details,text='Make:',justify="left", anchor="w", width=10)
        self.makelabel.grid(row=3,column=1)
        self.makevalue=Label(self.labelframe_details,text=None,justify="left", anchor="w",width=16)
        self.makevalue.grid(row=3,column=2)
    
        self.modellabel=Label(self.labelframe_details,text='Model:',justify="left", anchor="w", width=10)
        self.modellabel.grid(row=4,column=1)
        self.modelvalue=Label(self.labelframe_details,text=None,justify="left", anchor="w",width=16,)
        self.modelvalue.grid(row=4,column=2)
        
        self.doorslabel=Label(self.labelframe_details,text='Doors:',justify="left", anchor="w", width=10)
        self.doorslabel.grid(row=5,column=1)
        self.doorsvalue=Label(self.labelframe_details,text=None,justify="left", anchor="w",width=16,)
        self.doorsvalue.grid(row=5,column=2)
    
        self.colorlabel=Label(self.labelframe_details,text='Color:',justify="left", anchor="w", width=10)
        self.colorlabel.grid(row=6,column=1)
        self.colorvalue=Label(self.labelframe_details,text=None,justify="left", anchor="w",width=16,)
        self.colorvalue.grid(row=6,column=2)
        

        # Rental Period Dates
        self.periodlabel = Label(self.labelframe_details,text='Rental Period: (daily)',justify="left", anchor="w", width=18)
        self.periodlabel.grid(row=7,column=1, sticky="w",pady=25)
        self.periodvalue = Entry(self.labelframe_details,width=5)
        self.periodvalue.grid(row=7,column=2, sticky="w",padx=15)
        # self.period = Label(self.labelframe_details,text='(Days)',width=5, justify="left", anchor="w")
        # self.period.grid(row=7,column=3, sticky="w")

        self.labelframe_details.grid_propagate(0)
        
        self.rentbutton = Button(self.labelframe_details, text="Rent")
        # self.rentbutton.config(state=DISABLED)
        self.rentbutton.grid(row=8, column=1, columnspan=2)
    
        # Rented Cars
        self.labelframe_rented=LabelFrame(self,text='Rented Cars', height=100, width=100)
        self.labelframe_rented.grid(row=2,column=0,padx=30,pady=5,sticky="n")
       
        self.rented_cars_listbox = Listbox(self.labelframe_rented, height=10, width=25, bg='lightgrey', justify="left")
        self.rented_cars_listbox.grid(row=2, column=0, sticky="n", padx=5, pady=10)

        self.returnbutton = Button(self.labelframe_rented, text="Return Car")
        self.returnbutton.grid(row=3, column=0, padx=0, pady=10, sticky="s")

        # Bill
        self.labelframe_bill=LabelFrame(self,text='Bill', height=100, width=100)
        self.labelframe_bill.grid(row=2,column=1,padx=30,pady=5,sticky="n")
        self.bill_listbox = Listbox(self.labelframe_bill, height=10, width=25, bg='lightgrey', justify=CENTER)
        self.bill_listbox.grid(row=2,column=1, sticky="ew", padx=5, pady=10)
        self.total = Label(self.labelframe_bill,text='Total: $0', width=15)
        self.total.grid(row=3,column=1,pady=10)
