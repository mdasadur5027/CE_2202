# 3.	Write a program to calculate the cross sectional area, surface area, volume of a cylinder 

# Cross sectional area = pi*r^2
# Volume = pi*r^2*h
# Area of the curvature = 2*pi*r*h
# Surface area = 2*pi*r*h+2*pi*r^2

d = float(input('Enter the diameter of the cylinder: '))
h = float(input('Enter the height of the cylinder: '))

pi = 3.1415

cross_sectional_area = pi*((d/2)**2)
surface_area = 2*pi*(d/2)*((d/2)+h)
volume = cross_sectional_area*h

print(f'Cross sectional area of the cylinder: {round(cross_sectional_area,2)}')
print(f'Surface area of the cylinder: {round(surface_area,2)}')
print(f'Volume of the cylinder: {volume:.2f}')
