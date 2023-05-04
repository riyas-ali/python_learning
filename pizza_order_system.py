want_pizza = input("Do you want pizza(y/n)?:")

if want_pizza == "y" or want_pizza == "Y":
    pizza = input("Which size pizza do you want(s/m/l)?:")
    if pizza == "s" or pizza == "S":
        selected_pizza = "Small"
        bill = 100;
        print(f"{selected_pizza} pizza prize is {bill}")
    elif pizza == "m" or pizza == "M":
        selected_pizza = "Medium"
        bill = 200
        print(f"{selected_pizza} pizza prize is {bill}")
    else:
        selected_pizza = "Large"
        bill = 300
        print(f"{selected_pizza} pizza prize is {bill}")

    pepperoni = input("Do you want pepperoni (y/n)?:")
    if pepperoni == "y" or pepperoni == "Y":
        if selected_pizza == "Small":
            bill = bill + 30
        else:
            bill = bill + 50
        print(f"{selected_pizza} pizza and pepperoni prize is {bill}")

    extra_cheese = input("Do you want extra cheese (y/n)?:")
    if extra_cheese == "y" or extra_cheese == "Y":
        bill = bill + 20
        print(f"{selected_pizza} pizza with pepperoni and extra cheese prize is {bill}")
    print(f"Your total bill amount is {bill} rupees.")
else:
    print("Thank you for the visit!..")

print("Thank You... Visit Again!..")
