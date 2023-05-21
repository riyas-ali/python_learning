names = []


def printList():
    print()
    for i in names:
        print(i)
    print()


while True:
    first_name = input("First name > ").strip().capitalize()
    last_name = input("Last name > ").strip().capitalize()
    full_name = f"{first_name} {last_name}"
    if full_name not in names:
        names.append(full_name)
    else:
        print("Error!..Duplicate Found")
    printList()
