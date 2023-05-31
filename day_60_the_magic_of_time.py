import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

event = datetime.date(year, month, day)

difference = event - today
difference = difference.days
if difference > 0:
    print(difference)
elif difference < 0:
    print("😭")
else:
    print("🥳")