# Dictionaries are used to store data value in key:value pairs
# Dictionaries is a collection which is ordered ,changeable
# Dictionaries do not allow duplicates

# Dictionary methods ----------------------------------------------------

'''clear()	      Removes all the elements from the dictionary
copy()	          Returns a copy of the dictionary
fromkeys()	      Returns a dictionary with the specified keys and value
get()	          Returns the value of the specified key
items()	          Returns a list containing a tuple for each key value pair
keys()	          Returns a list containing the dictionary's keys
pop()	          Removes the element with the specified key
popitem()	      Removes the last inserted key-value pair
setdefault()	  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	      Updates the dictionary with the specified key-value pairs
values()	      Returns a list of all the values in the dictionary'''

newDict = {
    "Name" : "Roman",  # Name is the key and Roman is the Value
    "Surname":"Humagain",
    "College":"PCPS"
}
print(newDict)

#  to print the college value of the dictionary
print(newDict["College"])

# to print the length of the dictionary
print(len(newDict))

# the value of dictionary can be of any data type
newDict1 ={
    "Name":"Roman",
    "Educated":True,
    "Age":22,
    "College":["LNA" ,"KHWOPA" ,"PCPS"]
}
print(newDict1["College"])

# using dict() method to make the dictionary
thisdict = dict(name = "Roman", country = "Nepal")
print(thisdict)

thisdict["name"] ="Aswin"   # dictionary are mutable i.e it can be updated
print(thisdict)

# using key() and value() methods to get all the key and value of the dictionaries
keys = thisdict.keys()
values = thisdict.values()
print(keys)
print(values)

# using items() methods to get the items in the list
items = thisdict.items()
print(items)

# to find the available key in the dictionaries in the list or not
print("hi" in newDict)
print(dir(newDict))

# The update() method will update the dictionary with the items from dictiionary
#
# The argument must be a dictionary, or an iterable object with key:value pairs.

newDict2 ={"name" : "roman" , "age " : 22 , "address" : "panauti"}
print("newdict2:",newDict2)

# using update method to update the values
newDict2.update({"name": "Aswin"})
print(newDict2)

# adding new items in the dictionary
newDict2["College"] = "PCPS..."
print(newDict2)

# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# using copy() methods to copy one dictionary to another
tryDict = {"bike":"duke" ,"price":34322 ,"brand":"KTM"}

TRYDICT = tryDict.copy()
print("new copied dictionary: ", TRYDICT)

# using get method to get the value of the keys
print(tryDict.get("price"))