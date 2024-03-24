# while loop = a statement that will execute it's block of code,
# as long as it's condition remains TRUE !!!

name1 = ""
while len(name1) == 0:
    name1 = input("Enter your name: ")

print(f"Hello {name1}!")

name2 = None
while not name2:
    name2 = input("Enter your name2: ")

print(f"Hello {name2}!")