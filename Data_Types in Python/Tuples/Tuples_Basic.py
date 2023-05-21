# tuples are used to store multiple items in a single variable
# tuples are immutable
# tuples are written with round bracket i.e. ()
# tuples allow duplicates

newTuple = ("apple", "banana", "mango", "apple")
print(newTuple)

# to print the length of tuple
print(len(newTuple))

# to create tuples with one item it required comma after the elements
newTuple = ("apple",)
print(type(newTuple))

# using tuple methods to create tuple
thisTuple = tuple(("tiger", "lion", "cat"))
print(thisTuple)

# to access tuple
print(thisTuple[1])

# using range of index to access
newTuple = ("name", "class", "address", "rollno", "college", "stdId")
print(newTuple[2:5])

# using negative index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# to check if items exixts
print("roman" in thistuple)