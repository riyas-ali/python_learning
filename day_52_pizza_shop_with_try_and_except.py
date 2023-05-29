import os
import time

pizza = []

try:
    f = open("pizza.txt", "r")
    pizza = eval(f.read())
    f.close()
except:
    print("Error: No existing pizza list, using a blank list")


def add_pizza():
    time.sleep(1)
    os.system("clear")
    name = input("Name: ")
    toppings = input("Toppings: ")
    size = input("Size (s/m/l): ").lower()
    while True:
        try:
            qty = int(input("Quantity: "))
            break
        except:
            print("Error: Quantity must be a whole number")
    cost = 0
    if size == "s":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    else:
        cost = 14.99
    total = cost * qty
    total = round(total, 2)
    row = [name, toppings, size, qty, total]
    pizza.append(row)


def view_pizza():
    h1 = "Name"
    h2 = "Toppings"
    h3 = "Size"
    h4 = "Quantity"
    h5 = "Total"
    print(f"{h1:^10}{h2:^10}{h3:^10}{h4:^10}{h5:^10}")
    for row in pizza:
        print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
    time.sleep(2)


while True:
    time.sleep(1)
    os.system("clear")
    print("Rominos Pizza")
    menu = input("1: Add Pizza\n2: View Pizzas\n: ")
    if menu == "1":
        add_pizza()
    else:
        view_pizza()

    f = open("pizza.txt", "w")
    f.write(str(pizza))
    f.close()
