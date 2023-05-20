def color_change(color):
    if color == "red":
        return "\033[31m"
    elif color == "white":
        return "\033[0m"
    elif color == "blue":
        return "\033[34m"
    elif color == "yellow":
        return "\033[33m"
    elif color == "green":
        return "\033[32m"
    elif color == "purple":
        return "\033[35m"


title = f"{color_change('red')}={color_change('white')}={color_change('blue')}={color_change('yellow')} Music App {color_change('blue')}={color_change('white')}={color_change('red')}="
print(f"            {title: ^35}")
print(f"🔥▶️ {color_change('white')}Radio Gaga")
print(f"\t{color_change('yellow')}queen")

prev = "prev"
next_is = "next"
pause = "pause"
print(f"{color_change('white')}{prev: <35}")
print(f"{color_change('green')}{next_is: ^35}")
print(f"{color_change('purple')}{pause: >35}")

divider = "-------------------------------"
print(f"{color_change('white')}{divider: >35}")

print()
text = "WELCOME TO"
print(f"{color_change('white')}{text: ^35}")
text = "-- ARMBOOK --"
print(f"{color_change('blue')}{text: ^35}")
text = "Definitely not a rip off"
print(f"{color_change('yellow')}{text: >35}")
text = "of a certain other social"
print(f"{color_change('yellow')}{text: >35}")
text = "networking site"
print(f"{color_change('yellow')}{text: >35}")
text = "Honest."
print(f"{color_change('red')}{text: >35}")
text = "Username:"
username = input(f"{color_change('white')}{text: >35}")
text = "Password:"
password = input(f"{color_change('white')}{text: >35}")