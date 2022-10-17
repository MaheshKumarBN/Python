names = []
size = int(input('Enter Size of list '))
for i in range(size):
    names.append(input('Enter the name to add '))


def count_name_length(user_names):
    names_with_size_greater_than_5 = []
    for name in user_names:
        if len(name) > 5:
            names_with_size_greater_than_5.append(name)
    return names_with_size_greater_than_5


name_list = count_name_length(names)
print(name_list)
