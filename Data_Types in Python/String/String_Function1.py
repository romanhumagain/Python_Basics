# using string function

str1 = "My name is Roman Humagain and I am learning python"

# to make all the letter in upper case
newStr1 = str1.upper()
print(newStr1)

# to make all the letter in lower case
newStr1 = str1.lower()
print(newStr1)

# to make all the first letter in upper case of each word
newStr1 =str1.title()
print(newStr1)

# to make the first letter of a center in an upper case
newStr1 = str1.capitalize()
print(newStr1)

#  using string functions

str1 = "My name is Roman Humagain and I am learning Python_Project(Basic)"

# to find the index of the string
print(str1.find("n"))

# to find the index of the string
print(str1.index("R"))

str1 ="mynameisromanhumagain"
# to know where the string contails all character or not
print(str1.isalpha())  # if there is space it returns false

# to know where the string contails all dight or not
print(str1.isdigit())

# to know where the string contails only dight/character or not
print(str1.isalnum())
