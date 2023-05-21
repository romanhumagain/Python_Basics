import os

try:
    if os.path.isfile("newfile.txt"):
        # File exists, open in append mode
        file = open("newfile.txt", "a")
    else:
        # File doesn't exist, create new file and open in write mode
        file = open("newfile.txt", "w")

    file.write("I am writing some content in the file.")
    file.close()  # Close the file after writing

    print("File operation completed successfully.")

except Exception as e:
    print("An error occurred:", str(e))
