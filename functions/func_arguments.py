# A functionless argument
def hello():
    print("Hello, World!")

hello() #calling the function



# A function with an argument
def hello(name):
    print(f"Hello, {name}!")

hello("John") #calling the function



# A function with keyword arguments
def hello(first,middle,last):
    print(f"Hello, {first} {middle} {last}!")

#Order does not matter if we define the keyword arguments
hello(last="Smith",first="John",middle="Doe")


# A function with a return value
def hello(name):
    return f"Hello, {name}!"

greeting = hello("John") #The return value is stored in the variable greeting



#Nested functions
def outer_function():
    print("This is the outer function")
    def nested_function():
        print("This is the nested function")
    nested_function()

outer_function() #calling the outer function


# *args and **kwargs

# *args - a special operator we can pass to functions, args can be named anything
def add(*args):
    print(args) #args is a tuple
    return sum(args)

print(add(1,2,3,4,5)) #calling the function

# **kwargs - parameter that will pack all arguments into a dictionary, used when we don't know how many arguments will be passed to a function
def calculate(n,**kwargs):
    print(kwargs) #kwargs is a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2,add=3,multiply=5)) #calling the function