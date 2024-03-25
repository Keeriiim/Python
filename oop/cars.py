class Car:

    # __init__ - is the constructor method
    # self - is a global variable that represents the instance of the class, as .this in Java

    wheels = 4 # class variable - shared among all instances of the class, chaning it will change it for all instances
    def __init__(self, make, model, year,color):
        self.make = make # instance variable
        self.model = model
        self.year = year
        self.color = color

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.color} {self.make} {self.model}"
        return long_name.title()