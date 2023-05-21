# Stack is a linear data structure
# Stores items in a Last-in/First-out (LIFO) or First-in/Last-out (FILO)

# Stack Operators
'''
Push    -> Inserting an elements
Pop     -> Deleting an elements (Last Element)
Peek    -> Display the last element
Display -> Display List
 '''

newList = []

while True:
    choice =int(input('''
    1. Push Elements
    2. Pop Elements
    3. Peek Element
    4. Display Element
    5. Exit
    '''))

    if choice == 1:
        list = input("Enter the value: ")
        newList.append(list)
        print(newList)
    elif choice == 2:
        if len(newList) == 0:
            print("Empty List Couldn't Delete Element")
        else:
            deletedItem =newList.pop()
            print(deletedItem)
            print(newList)

    elif choice == 3:
        if len(newList) == 0:
            print("Empty List Couldn't Delete Element")
        else:
            print("Last Stack Value: " ,newList[-1])

    elif choice == 4:
        print("Display Stack: ", newList)
    elif choice == 5:
        print("done")
        break


# THE QUEUE IS A LINEAR DATA STRUCTURE
# STORES ITEMS IN THE FIRST IN FIRST OUT (FIFO) MANNER

newList = []

while True:
    choice =int(input('''
    1. Push Elements
    2. Pop First Elements
    3. Front Element
    4. Last Element
    5. Display Stack
    6. Exit
    '''))

    if choice == 1:
        list = input("Enter the value: ")
        newList.append(list)
        print(newList)
    elif choice == 2:
        if len(newList) == 0:
            print("Empty List Couldn't Delete Element")
        else:
            del newList[0]
            print(newList)

    elif choice == 3:
        if len(newList) == 0:
            print("Empty List Couldn't Delete Element")
        else:
            print("First Queue Value: " ,newList[0])

    elif choice == 4:
        if len(newList) == 0:
            print("Empty List Couldn't Delete Element")
        else:
            print("Last Queue Value: ", newList[-1])
    elif choice == 5:
        print("Display Queue: "+ newList)
    elif choice == 6:
        print("done")
        break