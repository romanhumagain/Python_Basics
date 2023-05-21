# FUNCTION FOR REMOVING ELEMENTS FROM LIST....................

my_lists1 = [33,45,56,34,23]
# to delete the elements which is at 1 index using del() function
del(my_lists1[1])
print(my_lists1)

my_lists2 = [2,5,6,8,9]
# using pop() function to delete the elements at index 1
print(my_lists2.pop(1))  # pop() function can return value and delete too but del() function only delete value
print(my_lists2)

# using remove() function to remove the elements by directly passing the elements to be deleted
my_lists3 = [45,56,34,56]
print((my_lists3.remove(34)))
print(my_lists3)

# using clear() function to clear the whole list
my_lists4 =[34,45,56,67,78]
my_lists4.clear()
print(my_lists4)

# FUNCTIONS FOR UPDATING ELEMENTS IN LIST........................

# using insert() function to add element at the specific index
my_lists5 = [4,56,78,23,1,44]
my_lists5.insert(2,9999)  #inserting element at the 2 index
print(my_lists5)

# using append() function to add elements
my_lists5.append(45)  #append function cannot add more than 1 element
print(my_lists5)

# using extend function to insert elements
my_lists6 = [44 ,67,78]
my_lists6.extend([45,56,34])
print(my_lists5)

# SOME OTHER LISTS FUNCTION

# use of count() function to count specific element
myList =[45 ,56,34,67,3,68,9,23,45]
print(myList.count(45))

# use of max() and min() function to find the highest and lowest element in the list
print(max(myList))
print(min(myList))

# using sort() function to sort the elements in the list
myList.sort()
print(myList)

# using reverse() function to reverse the elements in the list
myList.reverse()
print(myList)

# using index() function to find the index number of specific elements
myList =["roman" , "humagain"]
print(myList.index("humagain"))

