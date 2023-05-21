# Join Two Sets
set1 = {"1", "2", "3", "5", "7"}
set2 = {"4","10", "12", "5"}

# The union() method returns a new set with all items from both sets:
newSet =set1.union(set2)
print(newSet)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
newSet = set1.intersection(set2)
print(newSet)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
newSet = set1.symmetric_difference(set2)
print(newSet)


# True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)