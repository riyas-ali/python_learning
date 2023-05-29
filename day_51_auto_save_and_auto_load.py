import os
import time

todo_list = []

f = open("to_do.txt", "r")
todo_list = eval(f.read())
f.close()


def add():
    time.sleep(1)
    os.system("clear")
    name = input("Name: ").strip().capitalize()
    date = input("Due Date: ")
    priority = input("Priority: ").strip().capitalize()
    row = [name, date, priority]
    todo_list.append(row)
    print("Item Added")


def view(option):
    if option == "all":
        for row in todo_list:
            for item in row:
                print(item, end=" | ")
            print()
        print()
        time.sleep(2)
    else:
        priority = input("What priority?: ").strip().capitalize()
        item_found = False
        for row in todo_list:
            if priority in row:
                item_found = True
                for item in row:
                    print(item, end=" | ")
                print()
        if not item_found:
            print(f"No {priority} priority items")
        print()
        time.sleep(2)


def edit():
    time.sleep(1)
    os.system("clear")
    found = False
    view("all")
    find = input("Name of todo to edit: ").strip().capitalize()
    for row in todo_list:
        for item in row:
            if find == item:
                found = True
    if not found:
        print("Couldn't find that")
        return
    for row in todo_list:
        if find in row:
            todo_list.remove(row)
    name = input("Name: ").strip().capitalize()
    date = input("Due Date: ")
    priority = input("Priority: ").strip().capitalize()
    row = [name, date, priority]
    todo_list.append(row)
    print("Item Updated")


def remove():
    os.system("clear")
    view("all")
    find = input("Name of todo to remove: ").strip().capitalize()
    for row in todo_list:
        if find in row:
            todo_list.remove(row)


while True:
    time.sleep(1)
    os.system("clear")
    print("TODO List Management System")
    menu = int(input(f"1: Add\n2: View\n3: Edit\n4: Remove\n: "))
    if menu == 1:
        add()
    elif menu == 2:
        os.system("clear")
        options = int(input(f"1: All\n2: By Priority\n: "))
        if options == 1:
            view("all")
        else:
            view("priority")
    elif menu == 3:
        edit()
    else:
        remove()

    time.sleep(1)
    os.system("clear")
    f = open("to_do.txt", "w")
    f.write(str(todo_list))
    f.close()
