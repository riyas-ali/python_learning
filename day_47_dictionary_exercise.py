import os, time, random
trumps = {"David": {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99},
          "Mr Spock": {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0},
          "Monica from Friends": {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0},
          "Professor X": {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}}

while True:
    print("TOP TRUMPS")
    print("Characters")
    for key in trumps:
        print(key)
    user = input("Pick your character: ").title()
    computer = random.choice(list(trumps.keys()))
    print("computer has picked", computer)
    answer = input("Choose your stat: Intelligence, Speed, Guile & Baldness Level: ").title()
    print(f"{user}: {trumps[user][answer]}")
    print(f"{computer}: {trumps[computer][answer]}")
    if trumps[user][answer] > trumps[computer][answer]:
        print(f"{user} Wins")
    elif trumps[user][answer] < trumps[computer][answer]:
        print(f"{computer} Wins")
    else:
        print("Draw")

    time.sleep(3)
    os.system("clear")
