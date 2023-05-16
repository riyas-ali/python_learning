import random

number = random.randint(1, 100)
while True:
    guessed_number = int(input("Guess a number between 1 - 100: "))
    if guessed_number == number:
        print("Your guess is correct..!")
        break
    else:
        print("Oops.! Try again..!")
