beast = {"name": None, "type": None, "move": None, "HP": None, "MP": None}
print("MOKE BEAST")


for name, value in beast.items():
    beast[name] = input(f"{name}: ")

if beast["type"] == "water":
    print("\033[34m")
elif beast["type"] == "fire":
    print("\033[31m", )
elif beast["type"] == "air":
    print("\033[0m")
elif beast["type"] == "earth":
    print("\033[32m")

print()

for name, value in beast.items():
    print(f"{name}: {value}")

