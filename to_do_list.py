import os
import time

to_do_list = []


def print_list():
    print()
    count = 0
    for to_do in to_do_list:
        count += 1
        print(f"{count}. {to_do}")
    print()


while True:
    print("=== SIMPLE TO DO LIST MANAGER ===")
    activity = input("Do you want to view, add, edit or remove your to do list?: ").lower()
    if activity == "add":
        item = input(":> ")
        if item not in to_do_list:
            to_do_list.append(item)
        else:
            print("Item already in the list")
        time.sleep(1)
        os.system("clear")
        print_list()
    elif activity == "view":
        print_list()
    elif activity == "edit":
        index = int(input("Which one do you want edit?(item-no): "))
        print(to_do_list[index-1])
        to_do_list[index-1] = input("Update the item:> ")
        time.sleep(1)
        os.system("clear")
        print_list()
    elif activity == "remove":
        item = input("What do you want to remove?")
        if item in to_do_list:
            to_do_list.remove(item)
        else:
            print("Item not found in the list")
        time.sleep(1)
        os.system("clear")
        print_list()
