import os, time

while True:
    print("HIGH SCORE TABLE")
    name = input("INITIALS: ").upper()
    score = input("score: ")

    f = open("high.score", "a+")
    f.write(f"{name} {score}\n")
    f.close()

    print("ADDED")
    time.sleep(1)
    os.system("clear")
