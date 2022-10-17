num = int(input('Enter a number to check if it is prime or not '))
for i in range(2, int((num+1)/2)):
    if num % i == 0:
        print('%d is Not Prime' % num)
        break
else:
    print('%d is Prime' % num)