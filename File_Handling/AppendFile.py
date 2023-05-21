# to write the in the existing file
file = open("newfile.txt", "a")  
file.wrte("Using Append function in python")  # to write in the file
file.close()

# to read the file after writing in the file
file = open("newfile.txt","r")
content = file.read()
print(content)