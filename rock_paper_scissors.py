import random

print("for Rock = 0\nfor Paper = 1\nfor Scissors = 2")
user_choice = int(input("Type your option:"))
machine_choice = random.randint(0, 2)

if user_choice > 2:
    print("Wrong Input, You lose..!")
else:
    if user_choice == 0:
        print("You: Rock")
    elif machine_choice == 1:
        print("You: Paper")
    else:
        print("You: Scissors")

    if machine_choice == 0:
        print("Computer: Rock")
    elif machine_choice == 1:
        print("Computer: Paper")
    else:
        print("Computer: Scissors")

    if user_choice == machine_choice:
        print("Game is Draw")
    elif user_choice == 0 and machine_choice == 2:
        print("You win")
    elif user_choice == 2 and machine_choice == 0:
        print("You lose")
    elif user_choice < machine_choice:
        print("You lose")
    elif user_choice > machine_choice:
        print("You win")

