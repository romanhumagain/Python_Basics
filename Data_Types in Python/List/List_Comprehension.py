# list comprehension is the elegant way to define and create lists based on existing lists
# list comprehension is more faster and compact than normal function and loops for creating lists


# some examples are
lists = []
for i in range(1,101):  # to get the elements from 1 to 100
    lists.append(i)     # to add the retrived elements in lists using append function
print(lists)

# using list comprehension to create lists and filtering the elements
newList = [n for n in range(1 ,101) if n%2==0 ]
print(newList)

# converting string to list using list comprehension
String = "roman humagain"
newList = [ lists for lists in String]
print(newList)

# using normal way to convert string to list using list() function
My_string = "roman humagain"
newList = list(My_string)
print(newList)

# using split() to convert string to list
print(My_string.split())


