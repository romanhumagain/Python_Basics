# function is a block of statement which can be used repetitavely in a program
# function is defined using def keyword

# using normal function
def simplefuncton():
    print("Trying normal function")

simplefuncton()

#  using function with argument
def sumFun(num1 , num2): # num1, num2 are the argument in the function
    num3 = num1 + num2
    print(num3)

# calling the function sum()
sumFun(3,9)

# using function with return statement
def myfun(num1 , num2 , num3):
    num4 = num1/num2/num3
    return num4

print(myfun(4,4,4))

# using function to find the factorial of a number

def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer = answer * i
    return answer

value = int(input("please enter a number to find the factorial: "))
ans = factorial(value)
print("the required factorial of",value,"is",ans)



