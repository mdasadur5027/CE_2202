# 17.	Use math library to find height of a building up to 2 decimal places when user knows the distance of building from a point and the angle subtended by the building at that point
import math as m

d = float(input('Enter distance (in m): '))
angle = float(input('Enter Angle (in deg): '))

height = d* m.tan(m.radians(angle))

print(f'The building height is {height} m')