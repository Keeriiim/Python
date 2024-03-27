
# This is the main module
# 1. The __name__ variable is a special variable that is created when a module is imported.
# 2. The __name__ variable is set to the name of the module.
# 3. When the module is run directly, the __name__ variable is set to __main__.
# 4. This allows you to check if the module is being run directly or being imported.
# 5. This is useful when you have a module that can be run as a standalone program or imported into another module.


# If i run this module directly, the __name__ variable is set to __main__. and all other modules
# that are imported will have their __name__ variable set to the name of the module.
import module_two
print(module_two.__name__)