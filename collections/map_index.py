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