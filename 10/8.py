# 8. A Program to use famous energy equation of Einstein by taking variable input from user and show the result with units

m = float(input('Enter the mass in kg: '))

c = 3e8 # m/s
E = m*c*c
print(f'The energy is: {E:.2e} J')