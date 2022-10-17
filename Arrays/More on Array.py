from numpy import *

arr1 = array([5, 6, 2, 1, 9], int)
arr2 = arr1

print(arr1)  # [5 6 2 1 9]
print(arr2)  # [5 6 2 1 9]

print(id(arr1))  # 2376183632240
print(id(arr2))  # 2376183632240

# Let's make changes in one array and check
arr2[3] = 13

print(arr1)  # [5 6 2 13 9]
print(arr2)  # [5 6 2 13 9]

print(id(arr1))  # 2376183632240
print(id(arr2))  # 2376183632240

# In normal copy there will be only one object which is referred by arr1 and arr2
# original array will be changed if there is any change in any of the array
