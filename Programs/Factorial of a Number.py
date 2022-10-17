def factorial(num):
    res = 1
    if num == 0:
        return res
    elif num == 1:
        return res
    else:
        for i in range(2, num + 1):
            res *= i
    return res


print('Factorial of a given Number is: %d' % factorial(int(input('Enter a number to find its factorial '))))
