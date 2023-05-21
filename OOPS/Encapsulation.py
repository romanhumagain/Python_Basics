class Car:
    # creating parameterized constructor
    def __init__(self,windows, doors, engine_type):
        # making the attributes of Car class private
        self.__windows = windows
        self.__doors = doors
        self.__engine_type = engine_type

    # creating getter method
    def get_windows(self):
        return self.__windows
    def get_doors(self):
        return self.__doors
    def get_engineType(self):
        return self.__engine_type

    # creating setter method
    def set_windows(self, windows):
        self.__windows = windows
    def set_doors(self, doors):
        self.__doors = doors
    def set_engineType(self, engine_type):
        self.__engine_type = engine_type

# creating object of the class and passing the arguments
my_car = Car(4, 4, "Diseal")

# using getter method to get the windows , door and engine type
print("the number of windows in the car is {}".format(my_car.get_windows()))
print("the number of the door in the car is {}".format(my_car.get_doors()))
print("the type of engine in the car is {}".format(my_car.get_engineType()))

# using setter methods to update the windows, door and engine type
my_car.set_windows(5)
my_car.set_doors(5)
my_car.set_engineType("Petrol")

print(" ")

# getting the updated value using getter method
print("The number of windows in the car is {}".format(my_car.get_windows()))
print("The number of the door in the car is {}".format(my_car.get_doors()))
print("The type of engine in the car is {}".format(my_car.get_engineType()))
