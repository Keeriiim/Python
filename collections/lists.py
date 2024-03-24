# *********** 1D Lists ***********
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food[0])  # pizza

# You can also use negative indexing
print(food[-1])  # pudding


# You can also use slicing
print(food[0:2])  # ['pizza', 'hamburger']

# You can also use slicing with negative indexing
print(food[-2:])  # ['spaghetti', 'pudding']

# Slicing a slice
# print(food[1:3])  # ['hamburger', 'hotdog']
print(food[1:3][0])  # hamburger
print(food[1:3][0][3])  # index 3 as letter b in hamburger

#Adding an item to the list
food.append("ice cream")
food.append("cake")
print(food)  # ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'pudding', 'ice cream', 'cake']

#Removing an item from the list
food.remove("cake")
print(food)  # ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'pudding', 'ice cream']
# food.remove([5]) This will throw an error because the item is not in the list

# food.pop() - removes the last item in the list
# food.insert(0, "cake") - inserts an item at a specific index
# food.sort() - sorts the list
# food.clear() - removes all items in the list



# *********** 2D Lists ***********
drinks = ["soda", "juice", "water"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["ice cream", "cake"]
food1 = [drinks, dinner, dessert]
print(food1)
print(food1[0][0])  # soda


