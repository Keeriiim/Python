class Animal:

    alive = True

    def eat (self):
        print("This animal is eating")

    def sleep (self):
        print("This animal is sleeping")

class Rabbit(Animal):
    pass
class Fish(Animal):
    pass
class Bear(Animal):
    def sleep(self): # Overriding the method sleep from the parent class
        print("This bear is sleeping")


rabbit = Rabbit()
fish = Fish()
bear = Bear()

rabbit.eat()
fish.sleep()
bear.sleep()
