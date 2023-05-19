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


game_round = 1
winner = None

print("⚔️ BATTLE TIME ⚔️")
person_1 = input("Name your lengend: ")
person_1_health = health()
person_1_strength = strength()
print(person_1)
print("HEALTH:", person_1_health)
print("STRENGTH:", person_1_strength)
person_2 = input("Who are they battling?: ")
print(person_2)
person_2_health = health()
person_2_strength = strength()
print("HEALTH:", person_2_health)
print("STRENGTH:", person_2_strength)

while True:
    time.sleep(2)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print("The battle begins!")
    person_1_dice = roll_dice(6)
    person_2_dice = roll_dice(6)

    difference = abs(person_1_strength - person_2_strength) + 1

    if person_1_dice > person_2_dice:
        person_2_health -= difference
        if game_round == 1:
            print(person_1, "Wins the first blow")
        else:
            print(person_1, "wins round", game_round)

    elif person_2_dice > person_1_dice:
        person_1_health -= difference
        if game_round == 1:
            print(person_2, "Wins the first blow")
        else:
            print(person_2, "wins round", game_round)
    else:
        print("Their sword clash and they draw round", game_round)

    print(person_1)
    print("HEALTH:", person_1_health)
    print()
    print(person_2)
    print("HEALTH:", person_2_health)

    if person_1_health <= 0:
        print(person_1, "has died")
        winner = person_2
        break
    elif person_2_health <= 0:
        print(person_2, "has died")
        winner = person_1
        break
    else:
        print("And They are both standing for the next round")
        game_round += 1
time.sleep(2)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print(winner, "has won in", game_round, "rounds")
