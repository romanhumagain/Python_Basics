
'''
"r" - Read ->Default value. Opens a file for reading, error if the file does not exist

"a" - Append -> Opens a file for appending, creates the file if it does not exist

"w" - Write -> Opens a file for writing, creates the file if it does not exist

"x" - Create -> Creates the specified file, returns an error if the file exists
'''

# Opening a file
file = open("python_file.txt" , "r")  # "r" is the mode for readin

# to read file
content = file.read()

# to print the content from the file
print(content)

# to read the first line of the file
print(file.readline())


# Read Only Parts of the File
content = file.read(10)
print(content)

# to close the file
file.close()

