'''Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.'''

# Loop through the set, and print the values:

thisSet = {"apple", "banana", "cherry"}

for x in thisSet:
  print(x)

# Check if "banana" is present in the set:
thisSet = {"apple", "banana", "cherry"}
print("banana" in thisSet)

'''Change Items
Once a set is created, you cannot change its items, but you can add new items.'''

# using copy() method to return copy of set
thisSett = thisSet.copy()
print(thisSett)

# Add an item to a set, using the add() method:
thisSet1= {"apple" ,"roman" , True ,7}
thisSet1.add("69")
print(thisSet1)

# To add items from another set into the current set, using the update() method.
thisSet2 = {"hi" , "hello", "namaste"}
thisSet1.update(thisSet2)

print(thisSet1)

# to remove item from the set using remove() methods
thisSet2.remove("hi")
print(thisSet2)

# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

