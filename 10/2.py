# 2.	Write a program to calculate the Area and Perimeter of a triangle (90˚)

b = float(input('Enter the base of the right-angled triangle: '))
h = float(input('Enter the height of the right-angled triangle: '))

area = .5 * b * h
perimeter = b + h + (b**2+h**2)**.5

print(f'Area of the triangle: {round(area,2)}\nPerimeter of the triangle: {round(perimeter,2)}')