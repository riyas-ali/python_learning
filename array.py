from array import *

arr = array("i", [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

val = int(input("Enter the value for search: "))

k = 0
for i in arr:
    if i == val:
        print(k)
        break
    k += 1

# defualt function
print(arr.index(val))