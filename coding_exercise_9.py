user_input = input("Enter Numbers separated by space:")
numbers_list = user_input.split()
count = 0
max_number = 0

for i in numbers_list:
    count += 1

for i in range(count):
    numbers_list[i] = int(numbers_list[i])

for i in numbers_list:
    if max_number < i:
        max_number = i

print(f"The maximum number is: {max_number}")