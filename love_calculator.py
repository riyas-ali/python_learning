first_person_name = input("What is your Name?")
second_person_name = input("What is your Lover name?")

name = first_person_name + second_person_name

t = name.lower().count('t')
r = name.lower().count('r')
u = name.lower().count('u')
e = name.lower().count('e')

l = name.lower().count('l')
o = name.lower().count('o')
v = name.lower().count('v')
e = name.lower().count('e')

left_side = t + r + u + e
right_side = l + o + v + e
percent = int(str(left_side) + str(right_side))

if percent < 10 or percent > 90:
    print(f"Your love score is {percent}% and you go together like coke and mentos")
elif percent >= 40 and percent <= 50:
    print(f"Your love score is {percent}% and you are alright together")
else:
    print(f"Your love score is {percent}%")