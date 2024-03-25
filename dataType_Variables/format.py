 # str.format() - optional method that gives users more control when displaying output

animal = "dog"
item = "moon"

# The {} are placeholders that will be replaced by the arguments of the format method
print("The {} jumped over the {}".format(animal, item))

# Same method using indexing
print("The {0} jumped over the {0}".format(animal, item))

# Same method using
print("The {:<10} jumped over the {:>10}".format(animal, item))
# Same method using
print("The {:^10} jumped over the {:10}".format(animal, item))

#keyword arguments - this can not be done with the indexing method
print("The {animal} jumped over the {item}".format(animal="cat", item="fence"))

# f-string - a more modern way of formatting strings
text = "The {} jumped over the {}"
print(text.format(animal, item))

print(f"The {animal} jumped over the {item}")

# float controll
pi = 3.14159265359
number = 100000000
print(f"The value of pi is {pi:.2f}")

# display with comma
print("The value of pi is {:,}".format(number))
# binary display
print("The value of pi is {:b}".format(number))
# octal display
print("The value of pi is {:o}".format(number))
# hexadecimal display
print("The value of pi is {:x}".format(number))
# scientific notation
print("The value of pi is {:e}".format(number))

