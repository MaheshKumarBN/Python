# Default Arguments
def function_default(firstname, lastname, department, city='Bangalore'):
    print('Inside function_default')
    print('Name: %s %s' % (firstname, lastname), '\n''city: %s' % city, '\n''Department: %s' % department)
    print()


function_default('Mahesh', 'B N', 'Dev')


# Positional arguments
def function_positional(name, age):
    print('Inside function_positional')
    age += 5
    print('Name:', name, '\nAge:', age)
    print()


function_positional('Berry', 26)


# Here values gets assigned if we perform any operation on
# Age then here we will be getting error 'can only concatenate str (not "int") to str'
# function_positional(26, 'Alex')


# Keyword arguments
def function_keyword(age, name):
    print('Inside function_keyword')
    print('Name: %s\nAge: %d' % (name, age))
    print()


function_positional(name='Rahul', age=30)


# Any number of positional arguments (*args)
def any_num_pos_args(name, *args):
    print('Name: ', name)
    print(args)
    for i in args:
        print(i)
    print()


any_num_pos_args('Lokesh', 28, 'Bengaluru', 'Tester')


# Any number of keyword arguments (**kwargs)

def any_num_pos_args_with_keyword(**args):
    for a, b in args.items():
        print('%s: %s' % (a, b))
    print()


any_num_pos_args_with_keyword(name='Ranveer', age=32, location='Mumbai', department='HR')


# Function returning multiple values
def return_mul_values():
    a = 12
    b = 22
    return a, b


x, y = return_mul_values()
print(x + y)
