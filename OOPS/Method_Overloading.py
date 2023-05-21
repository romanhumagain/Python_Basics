# Simple example of method overloading
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def add(self, num1, num2, num3):
        return num1 + num2 + num3

# Create an instance of the Calculator class
calc = Calculator()

print(calc.add(2, 3))         # Output: TypeError: add() missing 1 required positional argument: 'c'
print(calc.add(2, 3, 4))      # Output: 9