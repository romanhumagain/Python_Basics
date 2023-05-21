# classes are the real world entity ot object
# class contains attributes (Properties of the class)
# class contains methods (action of the class)

# creating class
class Car:
    def __init__(self, windows, tyres, engine): # Constructor
        # self is used to call the attribute of the class directly
        self.windows = windows
        self.tyres = tyres
        self.engine = engine
    def selfDriving(self, horsepower):
        print("The car horsepower is {}".format(horsepower))


# inititalizing the object of the class Car
newObj1 = Car(4, 4, "Diesel")
print("The number windows in the car is {}".format(newObj1.windows)) # using string format
print("The number of tyres in the car is {}".format(newObj1.tyres))

# calling the function
newObj1.selfDriving("3672")

# advanced class and object example: ---------------

# creating class
class BankAccount:
    # initializing class variable
    bank_name = "Kumari Bank pvt.Ltd"
    bank_branch = "Kushadevi"

    # creating constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Creating instance method
    def depositAmount(self, amount):
        self.balance +=amount
        print("{} is deposited into Account {}. And the new balance is {}".format(amount, self.account_number, self.balance))

    # Creating instance method
    def withdrawAmount(self,amount):
        if self.balance >=amount:
            self.balance -= amount
            print("{} is successfully withdrew from the {}. And the new balance is {}".format(amount, self.account_number, self.balance))
        else:
            print("you have Insufficient Balance")

    # Creating instance method
    def display_balance(self):
        print("Account: {}, Balance {}".format(self.account_number, self.balance))

# creating object of the class BankAccount
account1 = BankAccount(55500837332, 2000)

# Accessing class variable
print("The Name of this bank is {} and this is located at {}".format(account1.bank_name, account1.bank_branch))

# Accessing class methods
account1.depositAmount(2000)
account1.withdrawAmount(1000)

# Accessing object attributes
account1.display_balance()