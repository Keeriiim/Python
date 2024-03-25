# map - A list of lists, applies a function to each item in an iterable (list,tuple, etc) and returns a list of the results.

# Example 1
store = [1,2,3,4,5]
def add_one(x):
    return x + 1
new_store = list(map(add_one, store))
print(new_store)

# Example 2
store [("shirt",20.00),
       ("pants",30.00),
       ("shoes",50.00)]

to_euros = lambda data: (data[0], data[1] * 0.82) # Converts the price to euros








# Solving problem with map & indexing
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇



letters = ['A','B','C']
string = list.index(letters,position[0]) # Plockar ut bokstaven från position[0] och kollar vilket index den har i listan [A,B,C]
number = position[1] # Plockar ut siffran från position[1]

# Skriver ut kartan(map) och ersätter rutan där skatten ska vara med ett X
map[int(number)-1][string] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")