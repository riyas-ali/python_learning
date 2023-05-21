def color_change(letter):
    if letter == "r":
        print("\033[31m", end="")
    elif letter == " ":
        print("\033[0m", end="")
    elif letter == "b":
        print("\033[34m", end="")
    elif letter == "y":
        print("\033[33m", end="")
    elif letter == "g":
        print("\033[32m", end="")
    elif letter == "p":
        print("\033[35m", end="")


sentence = input("What sentence do you want rainbow-ising?: ")
for letter in sentence:
    color_change(letter.lower())
    print(letter, end="")
print()

