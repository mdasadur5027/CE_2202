# 18.	A code to find sum of following series 1/n! , n even 
import math as m
n = int(input())

sum = 0

for i in range(0, n+1, 2):
    sum = sum + (1/m.factorial(i))
    if i == n:
        print(f'1/{i}!',end=" = ")
    print(f'1/{i}!',end=" + ")

print(sum)
