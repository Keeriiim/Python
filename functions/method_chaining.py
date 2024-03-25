class Car:
    def driving(self):
        print("Driving a car")
        return self
    def stopping(self):
        print("Stopping a car")
        return self
    def honking(self):
        print("Honking a car")
        return self

car = Car()


# This will only work because the methods are returning self
car.\
    driving().\
    stopping().\
    honking() # This will not work because the methods are not returning anything