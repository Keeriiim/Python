class Car:
    color = None
class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color
    print(f"The {vehicle.__class__.__name__} is now {vehicle.color}")


car1 = Car()
motorcycle1 = Motorcycle()
change_color(car1, "red")
change_color(motorcycle1, "blue")

