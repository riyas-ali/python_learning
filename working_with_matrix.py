from numpy import *

arr1 = array([[1, 2, 3],[4, 5, 6]])
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# print(arr1.flatten())
# print(arr1.reshape(3, 2))

m = matrix(arr1)
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
print(diagonal(m))
print(diagonal(m))
m3 = m1 * m2;
print(m3)