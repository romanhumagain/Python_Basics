# to find the greatest and smallest number using for loop
largest_number =0
smallest_number = None

numbers = [3,4,6,345,23,13,45,54,676,343,123,565,78]
for i in numbers:
    if i>largest_number:
        largest_number = i
    if smallest_number is None:
        smallest_number = i
print(largest_number)
print(smallest_number)

# to get the sum and total count
numbers1 = [10 , 20 , 30 ,40 ,50]
count =0
sum = 0

for i in numbers1:
    count = count+1
    sum +=i
print("The required sum is" , sum)
print("The total count is " ,count)

# for loop with range() in pyhton
for i in list(range(4)): # i is the itiration varible
    print("Welcome")

for i in list(range(3 ,9 ,2)):  # increment with 2
    print(i)

# ------------------------------------------------------------
# Using list in for loop
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
