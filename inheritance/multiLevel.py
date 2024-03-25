class Organism:
    print("Organism class created")

class Animal(Organism):
    print("Animal class created")

class Mammal(Animal):
    print("Mammal class created")


mammal = Mammal()