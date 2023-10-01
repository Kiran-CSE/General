# Parent class
class Vehicle:
    def Vehicle_data(self):
        print("Hello from the Vehicle class!")

# Car Child class
class Car(Vehicle):
    def Car_data(self):
        print("Hello from the Car class!")

# Bike Child class
class Bike(Vehicle):
    def Bike_data(self):
        print("Hello from bike!")

# Objects based on Car
car01 = Car()
bike01 = Bike()

# Get Vehicle data
car01.Vehicle_data()
car01.Car_data()
print("=============")
bike01.Vehicle_data()
bike01.Bike_data()