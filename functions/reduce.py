# Reduce - apply a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value.

# reduce(function, sequence[, initial]) -> value
import functools
letters = ['A','B','C']
# Adds the letters in the list together
word = functools.reduce(lambda x,y: x+y,letters)
print(word)

# Example 2

# Adds the numbers in the list together
numbers = [1,2,3,4,5] # 5,20,60,120
result = functools.reduce(lambda x,y: x*y,numbers)
print(result)