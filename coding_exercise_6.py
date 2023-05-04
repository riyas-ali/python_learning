age = int(input("What is you age?:"))
bill = 0

if age>3:
    print("Can Ride")
    if age < 12:
        bill = 150
    elif age < 18:
        bill = 250
    else:
        bill = 500

    want_photo = input("Do you want photo(y/n)?:")
    if want_photo == "y" or want_photo == "Y":
        bill += 50
    print(f"Your bill is {bill}")
else:
    print("Can't Ride")
print("Thank you..Enjoy the Ride!")