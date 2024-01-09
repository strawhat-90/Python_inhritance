# Create a Python class called “Car” with attributes like make, model, and year.
# Then, create an object of the “Car” class and print its details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating an object of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)

# Printing the details of the car
print("Car Details:")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
