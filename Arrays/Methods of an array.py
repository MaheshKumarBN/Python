from numpy import *

arr1 = array([5, 6, 2, 1, 9], int)
arr2 = array([14, 34, 76, 89, 58], int)

# to add a number to whole array
arr1 += 5
print(arr1)  # [10 11  7  6 14]

# add 2 arrays
print(arr1 + arr2)  # [24 45 83 95 72]

# Sorting an array
arr2.sort()
print(arr2)  # [14 34 58 76 89]

# combine 2 array
print(concatenate([arr1, arr2]))  # [10 11  7  6 14 14 34 58 76 89]

# to find minimum value in an array
print(min(arr1))  # 6

# to find maximum value in an array
print(max(arr1))  # 14

# to find sum of an array
print(sum(arr1))  # 48

# to find square root of an array
print(sqrt(arr1))  # [3.16227766 3.31662479 2.64575131 2.44948974 3.74165739]

# to find log, sin, cos of an array
print(log(arr1))  # [2.30258509 2.39789527 1.94591015 1.79175947 2.63905733]
print(sin(arr1))  # [-0.54402111 -0.99999021  0.6569866  -0.2794155   0.99060736]
print(cos(arr1))  # [-0.83907153  0.0044257   0.75390225  0.96017029  0.13673722]

# to find unique in array
arr3 = array([21, 45, 32, 89, 21], int)
print(unique(arr3))  # [21 32 45 89]

# to find product of two array
print(arr1 * arr2)  # [ 140  374  406  456 1246]
