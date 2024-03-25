import os

path = 'C:/Users/kerim/Desktop/TempProject'
# path = 'C:\\Users\\kerim\\Desktop\\TempProject'

if os.path.exists(path):
    if os.path.isdir(path):
        print("This is a directory")
    elif os.path.isfile(path):
        print("This is a file")


# Override the local txt file
with open('test.txt', 'w') as file:
    file.write('mush mash')

# Open a txt file from the relative path, ie the same directory as the script
with open('test.txt', 'r') as file:
    print(file.read())

# Override the local txt file
with open('test.txt', 'w') as file:
    file.write('Testing')

with open('test.txt', 'r') as file:
    print(file.read())

# Append to the local txt file
with open('test.txt', 'a') as file:
    file.write('\nAppending')
with open('test.txt', 'r') as file:
    print(file.read())


# Open a txt file from the absolute path
'''file = 'C:\\Users\\kerim\\Desktop\\tenta.txt'
with open(file,'r') as file: # 'r' is for read but it is not necessary
    print(file.read())
'''


