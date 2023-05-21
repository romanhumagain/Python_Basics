import math

'''
Basic arithmetic functions:--------------
math.sqrt(x):       Returns the square root of x.
math.pow(x, y):     Returns x raised to the power of y.
math.exp(x):        Returns e (Euler's number) raised to the power of x.
math.log(x, base):  Returns the logarithm of x with the given base (default base is e).
math.log10(x):      Returns the base-10 logarithm of x.

Rounding and truncation:---------------
math.ceil(x):       Returns the smallest integer greater than or equal to x.
math.floor(x):      Returns the largest integer less than or equal to x.
math.trunc(x):      Returns the truncated integer value of x (removes the decimal part).

Trigonometric functions:
math.sin(x), math.cos(x), math.tan(x):    Returns the trigonometric sine, cosine, and tangent of x, respectively.
math.asin(x), math.acos(x), math.atan(x): Returns the inverse trigonometric sine, cosine, and tangent of x, respectively.

Constants:
math.pi:  Represents the mathematical constant π (pi).
math.e:   Represents the mathematical constant e (Euler's number).

Other commonly used functions:
math.abs(x):        Returns the absolute value of x.
math.degrees(x):    Converts angle x from radians to degrees.
math.radians(x):    Converts angle x from degrees to radians.
math.factorial(x):  Returns the factorial of x.
'''

# using math.ceil() method
numb1 = 20.454
newNumb =math.ceil(numb1)  # ceil() is used to round up the value of numb1 to the nearest integer.
print(newNumb)

# using math.fabs()
numb2 = -20
newNumb = math.fabs(numb2)  # math.fabs returns the absolute value
print(newNumb)

# using math.factorial() to find the factorial of a number
numb1 = 5
factNumb = math.factorial(numb1)
print(factNumb)

# using math.floor()
numb3 =10.5
newNumb = math.floor(numb3)  # math.floor() method is used to round a number down to the nearest integer
print(newNumb)

# using math.fsum()
newList = [20, 10, 30]
newSum = math.fsum(newList)  # It returns the sum of items in the list
print(newSum)

# using math.sqrt()
x = 16
print(math.sqrt(x))  # returns the square root of x