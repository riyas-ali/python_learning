import os
import random
import time


def add():
    os.system("clear")
    idea = input("idea: ")
    f = open("my_idea.txt", "a+")
    f.write(f"{idea}\n")
    f.close()


def show():
    os.system("clear")
    f = open("my_idea.txt", "r")
    ideas = f.read().split("\n")
    if [] in ideas:
        ideas.remove([])
    f.close()
    idea = random.choice(ideas)
    print(idea)
    time.sleep(2)
    os.system("clear")


while True:
    menu = input("1: Add idea\n2: Show a random idea\n: ")
    if menu == "1":
        add()
    else:
        show()
