# to read the content in the file line by line using loop

file = open("python_file.txt", "r")

# using for loop
for line in file:
    print(line)
    file.close()