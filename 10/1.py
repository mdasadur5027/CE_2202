# 1.	Write a program to separate digits of a number 

# n = int(input('Input an integer number: '))
# n = str(n)
# for i in range(len(n)):
#     print(f'The {i+1}th digit is {n[i]}')

# n = int(input('Input an integer number: '))
# divident = n
# for i in range (len(str(n))):
#     remainder = divident%10
#     print(f'The {i+1}th digit is {remainder}')
#     divident = divident//10


n = int(input('Input an 3 digit number: '))
ones_digit = n%10
tens_digit = (n//10)%10
hundreds_digit = (n//10)//10
print(f'Ones digit: {ones_digit}\nTens digit: {tens_digit}\nHundreds digit: {hundreds_digit}')



    