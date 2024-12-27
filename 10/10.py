# 10.	Write a Python program to calculate the shear force in a simply supported beam with a point load at the center. The program will take the load and the length of the beam as inputs.

p = float(input('Enter the point load in kN: '))
L = float(input('Enter the length of the beam in m: '))
x = float(input('Enter the point at which we are calculating in m (from left):'))

V = p / 2 if x < (L / 2) else -p / 2
M = V*x if x <=(L/2) else V*(L-x)

print(f'Shear force at {x}m: {V} kN')
print(f'Bending moment at {x}m: {M} kNm')

