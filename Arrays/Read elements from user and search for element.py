from array import *

a = array('i', [])
size = int(input('Enter size of an array '))
for i in range(size):
    ele = int(input('Enter next Element '))
    a.append(ele)

print(a)

#Search for element in array given by user
search_ele = int(input('Enter search Element '))

# k = 1
# for s in a:
#     if search_ele == s:
#         print('%d found at position %d' %(search_ele, k))
#         break
#     k += 1
# else:
#     print('%d not found in an array' %search_ele)

#Or
print('%d found at position %d' %(search_ele, a.index(search_ele)+1))