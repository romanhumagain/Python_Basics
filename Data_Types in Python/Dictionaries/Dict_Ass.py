# Creating a dictionary

new_dict = {
    "variable":"A named location in memory used to store data.",
    "function":"A block of reusable code that performs a specific task.",
    "loop":"A control structure that repeats a block of code until a certain condition is met.",
    "dictionary":"A collection of key-value pairs.",
    "list": "A collection of items that are ordered and changeable."
            }
print("Please Choose one of the following word to get its meaning --->")
key_string = ",".join(new_dict.keys())
print(key_string)

word = input()
print("Its Meaning is --->",new_dict[word])


