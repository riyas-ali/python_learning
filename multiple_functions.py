import random

print("⚔️Character stats generator⚔️")
haveACharacter = "yes"


def dice(side):
    result_is = random.randint(1, side)
    return result_is


def dice_6_and_8():
    roll_6_sided_dice = dice(6)
    roll_8_sided_dice = dice(8)
    result_is = roll_6_sided_dice * roll_8_sided_dice
    return result_is


while haveACharacter == "yes":
    warrior = input("Name Your Warrior: ")
    result = dice_6_and_8()
    print(f"{warrior} health is {result} hp")
    haveACharacter = input("Want to create another warrior?: ")
