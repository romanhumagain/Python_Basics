nums = [ 3,5,56,34,67,85]

# to get the element 56 ,34 and 67 from the above list
print(nums[2:5])

# using nested list i.e list inside list and retriving value from nested list
numbers = [1,'hello' , 'world', [34,57,78]]

# to get the value of 57 and 78 from the above nested list
print(numbers[3][1:3])

# slicing with triple arguments
lists = [ 2,45,7,34,8,78,9,88]

# to get 45 ,34 ,78 ,88 from above lists
print(lists[1: :2])

# using negative indexing for above
print(lists[-1: :-2])

# to retrive all the value from the elements 7
print(lists[2:])