####### Q3

class Vehicle:
    def __init__(self, make, model, colour, seats, max_speed):
        self.make = make
        self.model = model
        self.colour = colour
        self.seats = seats
        self.max_speed = max_speed
    
    def __str__(self):
        return f"Vehicle summary: {self.make}, {self.model}, {self.colour}, {self.seats}, {self.max_speed}km/h"

    def rev_engine(self):
        return "VRRRRMMMM!"
my_car = Vehicle("Holden", "Barina", "White", 5, 220)

print(my_car.__str__())
print(my_car.rev_engine())
