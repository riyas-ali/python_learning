def new_print(color, word):
    if color == "red":
        print("\033[31m", word, sep="", end="")
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
new_print("red", "new program ")
new_print("reset", "I can just call red('call')")
new_print("red", " and ")
new_print("reset", "that word will appear in the ")
new_print("blue", "color I set it to.")
print()
new_print("reset", "With no")
new_print("green", " weird gaps. ")
print()
new_print("reset", "Epic.")
print()

