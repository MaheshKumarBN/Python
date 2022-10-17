a = 10
print(id(a))


def something():
    a = 15
    x = globals()['a']
    print(id(x))
    print('inside function',  a)

    globals()['a'] = 100


something()
print('outside', a)
