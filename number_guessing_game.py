print("Number guessing Game")
print("Guess the number 1 - 100")
guessed_number = 50
count = 0
user_input = 0
while True:
    user_input = int(input("What is your guess?: "))
    count += 1
    if user_input < 0:
        print("Iam done")
        exit()
    elif user_input == guessed_number:
        print("Correct!")
        print("It took you", count, "guesses to get it correct!")
        break
    elif user_input > guessed_number:
        print("Too high")
    elif user_input < guessed_number:
        print("Too low")
    else:
        print("This is not a number I recognize.")
