mokedex = {}


def pretty_print():
    print(f"Name\tType\tHP\tMP")
    for key, value in mokedex.items():
        print(f"{key:^10}|{value['type']:^6}|{value['hp']:^6}|{value['mp']:^6}")


while True:
    print("Add your Beast!")
    name = input("Name: ").title()
    type = input("Type: ")
    hp = input("HP: ")
    mp = input("MP: ")
    mokedex[name] = {"type": type, "hp": hp, "mp": mp, }
    print("--------------------")
    print()
    pretty_print()
