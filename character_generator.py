import os
import random
import time


def roll_dice(side):
    result = random.randint(1, side)
    return result


def health():
    health_status = ((roll_dice(6) * roll_dice(12)) / 2) + 10
    return health_status


def strength():
    strength_status = ((roll_dice(6) * roll_dice(8)) / 2) + 12
    return strength_status


while True:
    print("⚔️ CHARACTER BUILDER ⚔️")
    name = input("Name your Legend: \n :")
    type_is = input("Character Type (Human, Elf, Wizard, Orc: \n :")
    print(name)
    print("Health:", health())
    print("Strength:", strength())
    print("May your name go down in Legend...")
    resume = input("Create Another Character?: ")
    if resume == "no" or resume == "No":
        break
    time.sleep(1)
    os.system("clear")
