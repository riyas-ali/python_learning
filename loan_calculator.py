print("Loan Calcualtor")
amount = int(input("Loan amount?: "))
tenure = int(input("Loan tenure?: "))
interest = float(input("Loan interest?: "))

interest_per_year = (interest / 100) * amount
interest_and_amount = amount

for year in range(tenure):
    interest_and_amount += interest_per_year
    print(f"Year {year + 1} is {interest_and_amount}")

print(f"You paid {interest_and_amount - amount} in interest")