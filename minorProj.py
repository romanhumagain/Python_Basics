import random

# creating choice to select
computer_choices = ["scissor", "paper", "rock"]
'''
rock Vs paper -> paper wins
rock Vs scissor -> rock wins
scissor Vs paper -> scissor wins
'''

while True:
    user_point = 0
    computer_point = 0

    game_choice = int(input('''
    Game Started. Do You Want To Continue?
    1 -> Start
    2 -> Exit
    '''))

    if game_choice == 1:
        # to run the game for 3 rounds
        for round in range(1, 4):
            user_input = int(input('''
            1 -> Rock
            2 -> Scissor
            3 -> Paper
            '''))
            if user_input == 1:
                user_choice = "rock"
            elif user_input == 2:
                user_choice = "scissor"
            elif user_input == 3:
                user_choice = "paper"
            else:
                print("Invalid Choice !!!")
                break

            computer_choice = random.choice(computer_choices)
            print("Your Choice is {}".format(user_choice))
            print("Computer Choice is {}".format(computer_choice))

            if computer_choice == user_choice:
                print("Game Draw !!")
                user_point += 1
                computer_point += 1
            elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and
                                                                              computer_choice == "rock") or (
                    user_choice == "scissor" and computer_choice == "paper"):
                user_point += 1
                print("Congratulations! You Win")
            else:
                print("Computer Wins")
                computer_point +=1

        if user_point == computer_point:
            print("Final Game Draw....")
        elif user_point > computer_point:
            print("Congratulations! You Win")
        elif user_point < computer_point:
            print("Computer Wins")

        print("User Point is {}".format(user_point))
        print("Computer Point is {}".format(computer_point))

    else:
        break
