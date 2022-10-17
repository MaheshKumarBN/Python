# Function  with no args and no return
def function1():
    print('function1()')
    print("Hello!! Welcome!!!")
    print()

function1()

# function with args and no return
def function2(x):
    print('function2()')
    print('x:',x)
    print()

function2(10)

# function without args and return
def function3():
    print('function3()')
    return(20+30)

print(function3())
print()

# function with args and return
def function4(x, y):
    print('function4()')
    return x+y

print(function4(12, 45))
print()