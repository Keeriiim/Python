import shutil

# copyfile() - copies the contents of the source file to the destination file
# copy() -copyfile() + permission mode + destination can be a directory
# copy2() - copy() + copies metadata (file's creation and modification times)

shutil.copy('test.txt','copy.txt') # source, destination
