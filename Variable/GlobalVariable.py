# global variable is the variable that is created outside the function and which can be accessed from anywhere

newNum = 36

# creating function
def myfunc():
    print(newNum)

# calling the function
myfunc()

# modifying the global variable inside the function using keyword global:--------------------
def modify_global():
    global newNum
    newNum = 69
    print(newNum)
# calling function
modify_global()

print(newNum)

# using Nested functions accessing a global variable:------------------
x = 10
def outer_function():
    def inner_function():
        print(x)
    inner_function()

outer_function()

# Global variable shadowing:---------------------------------
num1= 10
def modify_number():
    num1 = 20  # Local variable with the same name as the global variable
    print(num1)

modify_number()  # Output: 20
print(num1)  # Output: 10