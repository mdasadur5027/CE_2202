# 6.	A Program to find roots of a quadratic equation taking input of constant from user

a, b, c = map(float, input('Enter the constant of the quadratic equation seperated by comma: ').split(','))
d = b*b - 4*a*c
if d<0:
    print('The equation have no real root.')
else:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print(f'The roots are: x1 = {x1:.2f} and x2 = {x2:.2f}')