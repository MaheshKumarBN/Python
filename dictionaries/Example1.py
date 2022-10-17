phonebook = {}
phonebook['Mahesh'] = 9060369339
phonebook['Berry'] = 7019986073
print(phonebook)

phonebook1 = {
    'Berry' : 7019986073,
    'Mahesh' : 9060369339
}
print(phonebook1)

phonebook2 = {
    'Berry' : 7019986073,
    'Mahesh' : 9060369339
}
for name, number in phonebook2.items():
    print('Phone number of %s is %s' %(name, number))

del phonebook2['Mahesh']
print(phonebook2)

phonebook1.pop('Mahesh')
print(phonebook1)


#Excercise

#Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook3 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# your code goes here
phonebook3.update({'Jake': 938273443})
print(phonebook3)

# or

# phonebook3['Jake'] = 938273443
# print(phonebook3)

# testing code
if "Jake" in phonebook3:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook3:
    print("Jill is not listed in the phonebook.")
