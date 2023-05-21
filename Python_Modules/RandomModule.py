# using random module to get the random number
import random

# to get the random number between 1 and 10

# using Random randint() method
print(random.randint(1,10))    # randint() method include both 1 and 10

# using randrange() method to get random number
print(random.randrange(1,10))   # randrange() method never include 10

# using random.uniform()
print(random.uniform(1,4)) # returns a random floating number between 1 and 4

# using Random choise() method
choice =[1, 3, 5, 7 ,8 ]
print(random.choice(choice))  # it only contains an element from choice

print(random.shuffle(choice))  # To shuffle the elements from the list

# using random.random()
print(random.random)  # It returns a random floating number between 0 and 1