from numpy import *

# We can perform all array function here

arr1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr1)

arr2 = matrix('10 20 30; 40 50 60')
print(arr2)

# to convert multi D to 1-D
arr = arr2.flatten()
print(arr)

# to convert 1-D array into 2-D
arr3 = array([9, 8, 7, 6, 5, 4, 3, 2, 1])
arr4 = arr3.reshape(3, 3)
print(arr4)

# to convert 1-D array into 3-D
arr5 = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12])
arr6 = arr5.reshape(2, 2, 3)
print(arr6)

# Multiply two Matrices
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('9 8 7; 6 5 4; 3 2 1')
print(m1 * m2)

# to find Diagonal elements in a matrix
print(diag(m1))

# to find sum of Diagonal elements in a matrix
print(sum(diag(m1)))

# to get Dimension of a matrix
print(ndim(m1))

# to print number of rows and colums of the matrix
print(shape(m1))

# to get size of a matrix
print(m1.size)

# to print length of the matrix
print(len(m1))
