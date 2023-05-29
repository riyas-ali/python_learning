import os
import time

inventory = []

try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    pass


def add_item():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("==========")
    item = input("Item to add: ").strip().capitalize()
    inventory.append(item)
    print("Added")


def view_item():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("==========")
    seen = []
    for item in inventory:
        if item not in seen:
            print(f"{item} {inventory.count(item)}")
            seen.append(item)
    time.sleep(2)


def remove_item():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("==========")
    item = input("Item to remove: ").strip().capitalize()
    if item in inventory:
        inventory.remove(item)
        print("Removed")
    else:
        print("You don't have the item")


while True:
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("==========")
    menu = input("1: Add\n2: View\n3: Remove\n: ")
    if menu == "1":
        add_item()
    elif menu == "2":
        view_item()
    else:
        remove_item()

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
