# 7.	A Program to find area of a triangle taking value of three sides from user

a, b, c = map(float, input("Enter the three sides of the triangle separated by spaces: ").split())
if a+b>c and b+c>a and c+a>b:
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f'Area of the triangle: {area:.2f}.')
else:
    print("The given sides do not form a valid triangle.")