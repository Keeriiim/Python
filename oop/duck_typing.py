# This is an example of duck typing in python
# Duck typing is a concept related to dynamic typing, where the type or class of an object is less important than the methods it defines.

class duck():
    def walk(self):
        print("This duck walks")
    def talk(self):
        print("This duck quacks")

class dog():
    def walk(self):
        print("This dog walks")
    def talk(self):
        print("This dog barks")

class eagle():
    def talk(self):
        print("This eagle screeches")


class person():

    def catch(self, animal):
        animal.walk()
        animal.talk()

duck_instance = duck()

# This will work because the duck class has the walk and talk methods
# No need for __init__ method because ur not adding the duck_instance in person(here)
person_instance = person()
person_instance.catch(duck_instance)

eagle_instance = eagle()
# Will not work because the eagle class does not have the walk method
# person_instance.catch(eagle_instance)
