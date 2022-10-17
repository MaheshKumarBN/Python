from array import *

arr = array('i', [16, 18, 65, -2, 3])
print(arr.buffer_info())#(2034598821072, 5) here: 2034598821072 is array address and 5 is length of array

#To get length of array
print(len(arr))

#reversing the array
arr.reverse()
print(arr)

#to get type of array
print(arr.typecode)

#
#to copy one array to other

#way1
newArr = array(arr.typecode, (a for a in arr))
print(newArr)

#to print one element below the other
for e in newArr:
    print(e)

#using while loop to print array elements one below other
i = 0
while(i < len(newArr)):
    print(newArr[i])
    i += 1
