# Dictionaries {key_value_pairs} - Hashing - JSON

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "USA": "Washington"
}

# capitals.pop() - removes the last item in the dictionary or the item with the key specified
# capitals.clear() - removes all the items in the dictionary
# capitals.update() - updates the dictionary with the specified key-value pairs

# Adds a new key pair to the dictionary
capitals.update({"Nigeria": "Abuja", "Ghana": "Accra"}) # Adding items to the dictionary
# Updates an existing key pair in the dictionary
capitals.update({"Nigeria": "Lagos"})







programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Adding an item to the dictionary
programming_dictionary[
    "Loop"] = "The action of doing something over and over again"

#Looping through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    score = student_scores[names]
    if score >= 91:
        student_grades.update({names: "Outstanding"})
    elif score < 91 and score > 80:
        student_grades.update({names: "Exceeds Expectations"})
    elif score < 81 and score > 70:
        student_grades.update({names: "Acceptable"})
    else:
        student_grades.update({names: "Fail"})

# 🚨 Don't change the code below 👇
print(student_grades)

#Nested dictionaries, like JSON CODE
print()

#Nesting
# The idea is to have one key to one value , the value can both
# be a list [] or a dictionary {}
capitals ={
  "france":"Paris",
  "Germany":"Berlin"
}

#Nesting a list in a list
letters = ["A","B",["C","D"]]

#Nesting a list in a dictionary
travel_log0 = {
  "France":["Paris","Lille","Dijon"],
  "Germany":["Berlin","Hamburg","Stuttgart"]
}

#Nesting a dictionary in a dictionary
travel_log1 = {
    "france": {
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits": 12
    },
    "germany": {
        "cities_visited": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 4
    },
}

print(travel_log1)

#Nesting a dictionary in a list
travel_log2 = [
  {
    "country":"france",
    "cities_visited": ["paris", "lille", "dijon"],
    "total_visits": 12
  },
  {
    "country":"germany",
    "cities_visited": ["berlin", "hamburg", "stuttgart"],
    "total_visits": 4
  }
]

print("\n")
print(travel_log2)


# Dictionary comprehensions - A way to create a new dictionary by performing an operation on each item in an existing dictionary

# Example 1 - dictionary = {new_key: expression for (key,value) in iterable if conditional}
dictionary ={'englad':'london',
             'spain':'barcelona',
             'germany':'berlin'}
print(dictionary.get('cities'))

dict_new = {key : value for (key,value) in dictionary.items() if value[0] == "b"}
print(dict_new)

# Example 2 - dictionary = {new_key: expression for (key,value) in iterable}
cities_in_F = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# Example 3 - dictionary = {new_key: (if/else) for (key,value) in iterable}
dict_new2 = {key : (value if value[0] == "b" else "-") for (key,value) in dictionary.items()}
print(dict_new2)

# Example 4 - dictionary = {new_key: function() for (key,value) in iterable}
def check(value):
    if value >= 75:
        return 'HOT'
    elif value >= 69:
        return 'WARM'
    else:
        return 'COLD'

dict_new_3 = {key: check(value) for (key,value) in cities_in_F.items()}
print(dict_new_3)



