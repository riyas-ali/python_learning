myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
percent = int(input("What percentage do you want to tip?: "))
total_bill = percent/100*myBill+myBill
answer = total_bill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
