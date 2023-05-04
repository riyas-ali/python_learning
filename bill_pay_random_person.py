import random

names = input("Enter names separate by commas: ").split(",")
random_index = random.randrange(len(names))
# print(f"{names[random_index]} will pay the bill")


# 2nd method
random_person = random.randint(0, len(names)-1)
# print(f"{names[random_person]} will pay the bill")

# 3rd method
selected_person = random.choice(names)
print(f"{selected_person} will pay the bill")
