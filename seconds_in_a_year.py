total_days = int(input("How many days are in this year? "))

hours_in_a_day = 24
minutes_in_an_hour = 60
seconds_in_a_minute = 60

total_seconds = total_days * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute

if total_days == 365:
    print("No of seconds in a year are", "{:,}".format(total_seconds))
elif total_days == 366:
    print("No of seconds in a leapyear are", "{:,}".format(total_seconds))
else:
    print("Wrong number..!, Try again...")
