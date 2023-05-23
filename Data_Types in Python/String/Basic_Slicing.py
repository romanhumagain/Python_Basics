# Basic Slicing Example----------------------------
String = "Hello, My Name is Roman Humagain"

# Extract a substring
# To get the index
print(String.find("R"))
print(String.find("in"))

# To print Roman Humagain from the above string
substring = String[18:32]
print(substring)

# Get the first five character
first_five = String[:5]
print(first_five)

# Get the last eight character
last_eight = String[-8:]
print(last_eight)

# Intermediate Slicing example----------------------
newString = "Python is Awesome!"

# Extract every 2nd character
second_character =newString[0: :2]
print(second_character)

# Reverse the string
reverse_string = newString[-1: :-1]
print(reverse_string)

# Extract a substring in steps of 3
substring_steps = newString[3:13:3]
print(substring_steps)
