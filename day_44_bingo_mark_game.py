import random
import time
import os


def ran():
    number = random.randint(1, 100)
    return number


def pretty_print():
    for row in bingo:
        for item in row:
            print(item, end="\t|\t")
        print()


def created_card():
    global bingo
    numbers = []

    for i in range(8):
        numbers.append(ran())

    numbers.sort()
    bingo = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BG", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]
    ]


created_card()
exes = 0
while True:
    pretty_print()
    num = int(input("Next Number: "))
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "X"
                exes += 1
    if exes == 8:
        time.sleep(1)
        os.system("clear")
        pretty_print()
        print("You have won")
        break

    time.sleep(1)
    os.system("clear")
