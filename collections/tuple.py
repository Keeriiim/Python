# tuple - collections which is ordered and unchangeable. Allows duplicate members. Used to group together related data


student = ("John",21,"male","John")
print(student)

# print the first item in the tuple
print(student[0])
print(student.count("John"))
print(student.index(21))



# Sorted tuple
students = ("John", "Jane", "Doe", "Doe")
sorted_students = sorted(students, reverse = True) # reverse = True will sort in descending order
print(sorted_students)

# Advanced tuple sorting

students_grader = [("John", "F",60),
                     ("Jane", "A",100),
                     ("Doe", "C",75),
                     ("Doe", "B",80)]

# Sort by grade
grade = lambda x: x[2]
students_grader.sort(key = grade)
print(students_grader)

tuple_students_grades = (("John", "F",60),
                     ("Jane", "A",100),
                     ("Doe", "C",75),
                     ("Doe", "B",80))

sorted_tuple_students_grades = sorted(tuple_students_grades, key = lambda x: x[1])

print(sorted_tuple_students_grades)
