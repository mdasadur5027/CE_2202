# 5.	Show summation of all digits of a user given number

n = int(input('Enter an integer number: '))
sum = 0
for i in range(len(str(n))):
    sum += int(str(n)[i])
print(f'Summation of the digits: {sum}')