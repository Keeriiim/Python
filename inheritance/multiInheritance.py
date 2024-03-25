class Prey:
    def prey_method(self):
        print("Prey method called")

class Predator():
    def predator_method(self):
        print("Predator method called")

class fish(Prey, Predator):
    pass

fish_instance = fish()
fish_instance.predator_method()
fish_instance.prey_method()