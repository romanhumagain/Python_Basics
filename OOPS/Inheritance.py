'''
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

# creating class named Car
class Car:
    def __init__(self, windows, doors, engine_type):  # constructor
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type
    # creating method
    def driving(self):
        print("Car is used for driving")

# creating new class Audi and inheriting from the Car class
class Audi(Car):
    def __init__(self,windows, doors, engine_type, horsepower):
        # to inheritate the feature of the Car class, super() function is used
        super().__init__(windows, doors, engine_type)
        self.horsepower =horsepower

audiCr7 = Audi(4, 6, "Diseal", 400)

print(audiCr7.engine_type)
print(audiCr7.horsepower)
# calling the methods from class
audiCr7.driving()
