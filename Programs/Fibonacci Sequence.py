def fibonacci(stop):
    if stop > 0:
        a = 0
        b = 1
        if stop >= 1:
            print(a, end=" ")
        if stop >= 2:
            print(b, end=" ")
        if stop >= 3:
            for i in range(2, stop):
                if i <= stop:
                    c = a + b
                    a, b = b, c
                    print(c, end=" ")
    else:
        print('Please enter positive value')

fibonacci(int(input('Enter range ')))
