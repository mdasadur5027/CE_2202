# 4.	Take input of a number with three digits and show the number with digits in reverse order

# n = int(input('Enter a three digit number: '))
# print(f'The number in reverse order {str(n)[::-1]}')

n = int(input('Enter a three digit number: '))
print(f'The number in reverse order: ', end="")
print(n%10, end="")
print((n//10)%10, end="")
print((n//10)//10)