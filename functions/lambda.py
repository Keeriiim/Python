# lambda - function written in one line using lambda keyword, accepts any number of arguments but only one expression. (shortcut)

# Syntax: lambda arguments: expression
double = lambda x: x * 2
print(double(5)) #10

multiply = lambda x, y: x * y
print(multiply(5, 2)) #10

stringy = lambda x: f"Hello, {x}"
print(stringy("World")) #Hello, World

age_check = lambda x: True if x >= 18 else False
print(age_check(21)) #True