# Nested dictionary means putting a dictionary inside another dictionary
# Its a collection of dictionaries into one single dictionary

# creating a nested dictionary

course = {
    "python" : {"duration" : "2 months" , "fees" : 30000} ,
    "java" : {"duration" : "2 months" , "fees" : 20000},
    "javascript" : {"duration" : "1.5 months" , "fees" : 15000}
}

print(course)

# to print the fees of the java
print(course["java"]["fees"])

# using for loop to get all the items in the dictionary
for a ,b in course.items():
    print(a,b["fees"],b["duration"])

# updating the value in the dictionary
course["python"]["fees"] = 2766119619
print(course["python"]["fees"])

