# Simple example of abstraction
from abc import ABC, abstractmethod
# creating class named Animal
class Animal(ABC):
    # Creating constructor
    def __init__(self, name):
        self.name = name
    @abstractmethod
    # creating methods
    def make_sound(self):
        pass

# creating another class Dog and inheriting feature from Class Animal
class Dog(Animal):
    def make_sound(self):
       return "Wooff!"

# creating class Cat and inherting feature from class Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating animal list and initializing with two instance of classes: Dog and Cat
animals = [Dog("Johny"), Cat("Cutie")]

# using for loop

for animal in animals:
    print(animal.name + ": " + animal.make_sound())