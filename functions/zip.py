# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets etc)
#                   creates a zip object with paired elemenets stored in tuples for each element

# Example 1
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")


users = zip(usernames,passwords)

for i in users:
    print(i)

print()
# Example 2
users_dict = dict(zip(usernames,passwords))
print (type(users_dict))

for key,value in users_dict.items():
    print(key,value)
print()
# Example 3
users_list = list(zip(usernames,passwords))
print(type(users_list))

for i in users_list:
    print(i)