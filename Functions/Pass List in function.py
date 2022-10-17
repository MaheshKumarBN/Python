lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]


def even_odd(input_list):
    odd = []
    even = []
    for num in input_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


even_list, odd_list = even_odd(lst)
print(even_list)
print(odd_list)
