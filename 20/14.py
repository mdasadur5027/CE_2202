# 14.	Use math library to find cross-sectional area, surface area and volume of a cylinder

import math as m

d = float(input('Enter the diameter of the cylinder: '))
h = float(input('Enter the height of the cylinder: '))

cross_sectional_area = m.pi*m.pow((d/2),2)
surface_area = 2*m.pi*(d/2)*((d/2)+h)
volume = cross_sectional_area*h

print(f'Cross sectional area of the cylinder: {round(cross_sectional_area,2)}')
print(f'Surface area of the cylinder: {round(surface_area,2)}')
print(f'Volume of the cylinder: {volume:.2f}')
