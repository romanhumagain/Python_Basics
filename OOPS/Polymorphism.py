# Polymerphism means same function name but different signatures

# Creating class
class Animal:
    def sound(self):
        # Common method for all animals
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        # Specific implementation for Dog
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        # Specific implementation for Cat
        print("The cat meows.")

# Create instances of Animal, Dog, and Cat classes
animal = Animal()
dog = Dog()
cat = Cat()

# Polymorphism in action
animal.sound()  # Output: The animal makes a sound.
dog.sound()     # Output: The dog barks.
cat.sound()     # Output: The cat meows.
