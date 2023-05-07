total = 0
number = int(input("Enter a number\n:"))

while True:
    total += number
    number = int(input("Enter number for calculation. for quit enter 0\n:"))
    if number == -1 or number == 0:
        break
else:
    print("Else block statement")

print(f"The total is: {total}")