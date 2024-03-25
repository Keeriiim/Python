# Every .py file is a module. The main module is the file that is executed.
import messages

messages.print_message()

help("modules")
# from messages import * - import all functions from the module
# from messages import print_message - import only the print_message function
# print_message() - call the function
# import messages as msg - import the module with a different name
# msg.print_message() - call the function with the new name

# help(modules) - will print all avalible modules for python
# https://docs.python.org/3/py-modindex.html