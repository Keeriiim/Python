# scope - a simple example of scope in Python


name = "Python"  # global scope (available everywhere in the file)
def f():
    name = "Code"  # local scope (available only in the function)
    print(name)