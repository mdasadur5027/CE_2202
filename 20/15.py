# 15.	Use math library to find deflection of a simply supported beam

import math as m

W = float(input("Enter the load applied at the center (in kN): "))
L = float(input("Enter the length of the beam (in meters): "))
E = 2e9 #Pa
I = 0.001

deflection = (W*m.pow(L,3))/(48*E*I)

print(f"The deflection of the beam is: {deflection:.6f} meters")