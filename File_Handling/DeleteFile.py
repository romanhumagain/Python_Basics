import os
# to delete the existing file

try:
    if os.path.exists("newFile1.txt"):
        os.remove("newFile1.txt")
    else:
        print("file doesn't exists")
except Exception as e:
    print("ERROR OCCURED: ", str(e))

#  to remove the folder if exixts
try:
    os.rmdir("NewFolder")   # rmdir function is used to remove the folder if exists

except Exception as e:
    print("ERROR OCCURED: ", str(e))