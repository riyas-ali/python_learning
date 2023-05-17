import random

print("Start Infinity Dice Game")
sides = int(input("How many sides?: "))
play_game = "yes"


def dice_game(arg):
    dice = random.randint(1, arg)
    print("You rolled", dice)


while play_game == "yes":
    dice_game(sides)
    play_game = input("Roll again?: ")
