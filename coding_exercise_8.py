user_input = input("Type heights separate by space:")

heights = user_input.split()
count = 0
total = 0
for height in heights:
    count += 1

for i in range(count):
    heights[i] = int(heights[i])

for i in heights:
    total += i

avg = total/count
print(round(avg))