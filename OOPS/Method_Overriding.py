'''
When a child class inherits from a parent class and both classes have a method with the same name,
the method in the child class will override the method in the parent class. This is a form of method overriding
'''

class Shape:
    def area(self):
        print("Calculating area of a generic shape.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return 3.14 * self.radius**2

# Create instances of Rectangle and Circle classes
shape = Shape()
rectangle = Rectangle(5, 3)
circle = Circle(2)

shape.area()
print(rectangle.area())  # Output: 15
print(circle.area())     # Output: 12.56
