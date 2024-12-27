# 12.	Take a number from user and check whether the number is Odd or multiple of 3 

number = int(input("Enter a number: "))

if number % 2 != 0:
    print(f"{number} is Odd.")
elif number % 3 == 0:
    print(f"{number} is a Multiple of 3.")
else:
    print(f"{number} is neither Odd nor a Multiple of 3.")