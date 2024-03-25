# Abstract class - Prevents an user from creating an object of that class
# Abstract class - Contains abstract methods
# abc - Abstract Base Class
from abc import ABC, abstractmethod
class Organism:
    # Abstract method - Forces an user to implement the method in the derived class that has declaration but no implementation
    @abstractmethod
    def eat(self):
        pass

class Animal(Organism):
    def eat(self):
        return "Animal is eating"

