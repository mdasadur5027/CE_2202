# 9.	Write a Python program to calculate the bending stress in a beam. 
# The program will take the moment of inertia, the distance from the neutral axis, and the applied moment as inputs

I = float(input('Enter the moment of inertia (I) in m^4: '))
y = float(input('Enter distance from neutral axis (y) in m: '))
M = float(input('Enter moment (M) in Nm: '))

bending_stress = (M*y)/I
print(f'The bending stress is {bending_stress:.2f} Pa')