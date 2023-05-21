# USING ZIP() FUNCTION TO ITERATE OVER 2+ LISTS AT THE SAME TIME

myList1 = [34,45,67,78,89]
myList2 = [22,33,44,55,66]

# using for loop to iterarte both list at the same time
for a, b in zip(myList1,myList2):
    print(a,b)
print("done !!")


# without using zip function to iterate both list
for i in range(len(myList1)):
    print(myList1[i] ,myList2[i])
