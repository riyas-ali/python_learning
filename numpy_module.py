from numpy import *

arr = array([1, 2, 3, 4, 5, 6])
arr_2 = array([2, 4, 5, 1, 2, 3])
arr = array([1, 2, 3, 4, 5, 6], float)
print(arr)
print(arr.dtype)

arr1 = linspace(0, 15, 16)
print(arr1)

arr2 = arange(1, 15, 2)
print(arr2)

arr3 = logspace(1, 40, 5)
print(arr3)

arr4 = zeros(5, int)
print(arr4)

arr5 = ones(5, int)
print(arr5)

arr6 = arr + arr_2
print(arr6)
print(sin(arr6))
print(cos(arr6))
print(sqrt(arr6))
print(sum(arr6))
print(min(arr6))
print(max(arr6))
print(concatenate([arr, arr_2]))

# normal copy
arr1 = arr

# copying a array(shallow copy)
arr7 = arr.view()

# deep copy
arr8 = arr.copy()