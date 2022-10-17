nums = [23, 46, 76, 89, 91]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('Number which is divisible by 5 not found')