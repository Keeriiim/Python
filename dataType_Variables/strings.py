name = " bro Jetski"

# String Methods
# 1. len() - returns the length of the string
print("len: " + str(len(name)))
# 2. strip() - removes any whitespace from the beginning or the end
print("strip: " + name.strip())
# 3. lower() - returns the string in lower case
print("lower: " + name.lower())
# 4. upper() - returns the string in upper case
print("upper: " + name.upper())
# 5. replace() - replaces a string with another string
print("replace: " + name.replace("b", "c"))
# 6. split() - splits the string into substrings if it finds instances of the separator
print("split: " + str(name.split("o")))
# 7. capitalize() - converts the first character to upper case
print("capitalize: " + name.strip().capitalize())
# 8. casefold() - converts string into lower case
print("casefold: " + name.casefold())
# 9. center() - returns a centered string
print("center: " + name.center(110))
# 10. count() - returns the number of times a specified value occurs in a string
print("count: " + str(name.count("o")))


# 11. isalpha() - returns True if all characters in the string are in the alphabet
print("isalpha: " + str(name.isalpha()))
# 12. isdigit() - returns True if all characters in the string are digits
print("isdigit: " + str(name.isdigit()))

# Print the string multiple times
print("Multiply: " + name * 3)