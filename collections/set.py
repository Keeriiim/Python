# set - collection which is unordered, unindexed. No duplicate values!
# Greate to use for sorting when there are alot of duplicates

utensils = {"fork", "spoon", "knife","fork"}
utensils.add("napkin")
utensils.remove("spoon")

for x in utensils:
    print(x)

utensils.add("napkin")

# union is used for combining two sets
dishes = {"bowl", "plate", "cup", "knife"}
dinner_table = utensils.union(dishes)
print(dinner_table)

# You can also use update to add items from another set
utensils.update(dishes)
print(utensils)

# check the difference
print(utensils.difference(dishes))
# check whats in common
print(utensils.intersection(dishes))