import math

pi = 3.14
x = -1
y = 2
z = 5

# 1. abs() - returns the absolute value of a number
print("abs: " + str(abs(x)))

# 2. ceil() - returns the smallest integer greater than or equal to a number
print("ceil: " + str(math.ceil(pi)))

# 3. floor() - returns the largest integer less than or equal to a number
print("floor: " + str(math.floor(pi)))

# 4. pow() - returns the value of x to the power of y
print("pow: " + str(math.pow(2, 3)))

# 5. sqrt() - returns the square root of a number
print("sqrt: " + str(math.sqrt(16)))

# 6. exp() - returns e raised to the power of x
print("exp: " + str(math.exp(2)))

# 7. log() - returns the natural logarithm of a number, or the logarithm of number to base
print("log: " + str(math.log(16)))

# 8. max() - returns the largest number in a list
print("max: " + str(max([x,y,z])))

# 9. min() - returns the smallest number in a list
print("min: " + str(min([x,y,z])))
