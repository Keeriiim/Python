from cars import Car

car_1 = Car('audi', 'a4', 2019, 'black')
print(car_1.get_descriptive_name())

car_2 = Car('bmw', 'x5', 2020, 'white')

# Chaning the class variable for one instance
print(car_2.wheels)
car_2.wheels = 5
print(car_1.wheels)
print(car_2.wheels)

print("\n")

# Changing the class variable for all NEW instances
Car.wheels = 6
print(car_1.wheels)
print(car_2.wheels)

car_3 = Car('mercedes', 'c200', 2021, 'red')
print(car_3.wheels)


# car_1.get_descriptive_name() with () will call the method and return the value
# car_1.get_descriptive_name without () will return the method itself, meaning the memory location of the method