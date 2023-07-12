class Vehicle:

    def __init__(self, name, max_speed, mileage):

        self.color = "White"

        self.name = name

        self.max_speed = max_speed

        self.mileage = mileage


    def __str__(self):

        return f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


class Bus(Vehicle):

    pass


class Car(Vehicle):

    pass


bus = Bus("School Volvo", 180, 12)

car = Car("Audi Q5", 240, 18)

print(bus)

print(car)
