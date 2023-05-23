while True:
    inp = input("Please enter a number -->")
    if int(inp)>100:
        break
    else:
        continue

# Example to find the first prime number greater than a number
inp_num = int(input("please enter a number between 10 to 20\n"))
if inp_num >10 and inp_num <20:
    for num in range(inp_num,25):
        if num%2 ==0:
            continue
        for i in range(3, int(num ** 0.5) +1,2):
            if num % i ==0:
                break
        else:
            print("The first prime number is : ", num)
            break
else:
    print("please provide only number between 10 and 20")

# using another example of continue statement
# Example: Print odd numbers in a range, skipping multiples of 3
for num in range(1, 10):
    if num % 2 == 0:
        continue
    if num % 3 == 0:
        continue
    print(num)