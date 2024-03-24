num = 123
string = "Hello "

# Concatenation
# You cant concatenate string with integer without converting it to string
# You can not name ur string str which is already a built-in function
print("Concatenation: ", string + str(num))

#f strings
print(f"This statement: {num}, "*2 + " will be printed using f string 2 times")

# Print
print("Alternatively you can just \"escape\" the quote")

# Print the first char of hello
print("hello"[0])

# slicing = creating a substring by extracting elements from a string using indexing [] or slicing [:]
# indexing[start:stop:step]
name = "Obamas Pankakes"
first_name = name[:6] # or name[0:6]
print(first_name)
last_name = name[7:] # or name[7:len(name)]
print(last_name)
funky_name = name[::2] # or name[0:len(name):2], prints every second letter starting from the first
print(funky_name)
reversed_name = name[::-1] # or name[0:len(name):-1], prints the name reversed
print(reversed_name)

# slicinf[start,stop,step]
# Slicing web addresses
slice = slice(4, -4)
web = "www.wikipedia.com"
print(web[slice]) # prints wikipedia

# Don't use strip() to remove www. from web address as it will remove all w's
print(web.strip("www."))


