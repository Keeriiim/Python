friends = [('Rolf', 25), ('Anne', 37), ('Charlie', 11), ('Bob', 22), ('Jen', 16), ('Adam', 29)]

age = lambda data: data[1] # Stores a new freinds list with the ages of the people in the list 'age'

print(age(friends[0])) # Prints the age of the first person in the list 'friends'
filtered_list = filter(age,friends) # Filters out the people in the list 'friends' that are older than 18
print (list(filtered_list)) # Print list without adding the filter in lambda expression



# Filter - A list of lists, applies a function to each item in an iterable
# (list,tuple, etc) and returns a list of the results that are True.
age = lambda data: data[1] >= 18

filtered_list = filter(age,friends) # Filters out the people in the list 'friends' that are older than 18

print (list(filtered_list)) # Prints the list of people that are older than 18

# Example 2
students = [50,60,70,80,90]
filtered_list_students = filter(lambda i: i >= 60 ,students)
print("Students: " + str(list(filtered_list_students)))