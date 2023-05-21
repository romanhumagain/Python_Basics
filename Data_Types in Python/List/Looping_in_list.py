example_one =[3,45,56,2,56,45]

# using for loop
for i in example_one: # i is the iteration variable
    print(i)  # printing the elements of the loop using for loop
print("Done !")

# lists and Definate Loops
friends = ['roman' ,'anup' , 'bijen' , 'sushant']

for friend in friends:    # friend is the iteration variable in the loop
    print("Happy Birthday: ", friend)
print("All Done !")

# using loop in lists in another way....
for i in list(range(len(friends))):
    print("Happy New Year " ,friends[i])

# using loop to convert string to list
newList = []

for i in list(range(1,4)):
    value = input("please Enter " +str(i) +"st" +" Number: ")
    newList.append(value)
print(newList)


