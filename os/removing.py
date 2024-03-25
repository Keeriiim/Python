import os

# os.remove - removes a file
# os.rmdir - removes an empty folder


try:
    if os.path.exists('folder'):
        if os.path.exists('folder/copy.txt'):
            os.replace('folder/copy.txt', 'copy.txt')
            os.rmdir('folder')
            print('File moved, folder deleted')
        else:
            os.rmdir('folder')
finally:
    print('Goodbye')

# Removing a folder containning files
# import shutil
# shutil.rmtree('folder')
