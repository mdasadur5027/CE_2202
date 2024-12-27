# 13.	Take a number from user and check whether the number is a output of following equation 2X+3

n = int(input('Enter a number: '))

if (n-3)%2 == 0:
    print(f"{n} is a valid output of the equation 2X + 3.")
else:
    print(f"{n} is NOT a valid output of the equation 2X + 3.")