from numpy import *

# Deep copy: copy data from one array to another with different address and
# if we make changes to any one of the array changes will not be affected in other array.
# find the below example

arr3 = array([8, 6, 3, 9, 0], int)
arr4 = arr3.copy()

print(arr3)  # [8 6 3 9 0]
print(arr4)  # [8 6 3 9 0]

print(id(arr3))  # 2232301222864
print(id(arr4))  # 2232301223152

# Lets change the value of one element in arr4
arr4[1] = 34
print('After change in arr4')
print(arr3)  # [8 6 3 9 0]
print(arr4)  # [8 34  3  9  0]
