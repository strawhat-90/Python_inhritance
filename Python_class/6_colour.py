# Define a class attribute “color” with a default value white. i.e., Every Vehicle
# should be white.

class Vehicle:
    
    color = "white"

    def __init__(self, model):
        self.model = model

car1 = Vehicle("Sedan")
car2 = Vehicle("SUV")

print(f"Car 1 - Model: {car1.model}, Color: {car1.color}")
print(f"Car 2 - Model: {car2.model}, Color: {car2.color}")
