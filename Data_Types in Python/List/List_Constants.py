# list constants are surrounded by square brackets
example_first =[1,34.69,'roman']
print(example_first)

#list elements can be any python object-even another list
example_second = ["roman" ,[45,69] , "PCPS"]
print(example_second)

# list can be empty too
print([])

# looking inside Lists......
animals = ['Tiger' ,'Lion' ,'Cheetah']
print(animals[1])  # printing the animal name which is at 1 index

#  Lists are mutable i.e. we can change the elements of a list using the index operator
numbers = [34,45,567,87,45]
numbers[2] = 6969  # changing the  elements which is at 2 index
print(numbers)

#  finding the number of elements in the list using len() function
name = ["roman" ,"humagain" ,"pcps" , "college"]
print(len(name))

# using negative index to get the elements
nums = [3,45,67,2,56,23]
print(nums[-2]) # negative indexing starts from last element with the index value of -1



