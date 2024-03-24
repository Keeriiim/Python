grade = input("Place ur grade here from A-D: ").upper()

if grade == "A":
    print("Your Excellet")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Average")
elif grade == "D":
    print("Poor")



# Better way to write it is

def grade(grade):
    if grade == "A": return "Your Excellet"
    elif grade == "B": return "Good"
    elif grade == "C": return "Average"
    elif grade == "D": return "Poor"
    return "F"


