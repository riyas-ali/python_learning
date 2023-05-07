# break

list1 = ["hi", "hello", "welcome"]
names = ["riyas", "shareef", "uwais"]

for item in list1:
    for name in names:
        print(item, name)
        if item == "hello" and name == "shareef":
            break  # exiting inner loop
    print("out from inner loop")
print("out from outer loop")

# continue

count = 1
for i in range(1, 11):
    if i == 7:
        continue  # It helps to skip next iteration
    else:
        print(i)

# pass

for i in range(5):
    pass  # currently no statement but future there put some statement


def get_item():
    pass
