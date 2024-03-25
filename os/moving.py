import os

source = 'copy.txt'
destination = 'folder/'

try:
    if os.path.exists(source):
        if os.path.exists(destination):
            print('Folder already exists, moving the file into it')
            os.replace(source, destination + source)

        else :
            os.makedirs(destination)
            print('created folder')
finally:
    print('Goodbye')