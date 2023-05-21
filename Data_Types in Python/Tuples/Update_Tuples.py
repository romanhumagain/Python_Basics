# once tuples are created, it cannot be changed
# converting tuples into list to change the tuples items

newTuples = ("roman", "humagain", "pcps college", "panauti")

newList =list(newTuples)
newList[2] = "khwopa college"
newTuples = tuple(newList)
print(newTuples)  # now the value is updated

# adding tuple to a tuple
tuple1 =("hi" ,"hello")
tuple2 = ("namaste",)

tuple1 = tuple1+tuple2
print(tuple1)

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)