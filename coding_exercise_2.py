age = int(input("Enter your age:"))

years_left = 90-age
month_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks and {month_left} months left.")