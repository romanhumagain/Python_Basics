import random
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = " abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbols = "~!@#$%^&*()?|"

String = upper_case + lower_case + number +symbols
length =16
print(String)
# The "".join() function is used to join the randomly selected characters together,
# creating a single string representing the password.

password = "".join(random.sample(String,length))

print("Your newly Password is", password)
