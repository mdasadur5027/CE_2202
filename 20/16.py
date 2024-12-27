# 16.	Use math library to find horizontal and vertical components of an inclined Force

import math as m

# print(m.sin(m.radians(90)))
def force_components(F, angle):
    Fx = F*m.cos(m.radians(angle))
    Fy = F*m.sin(m.radians(angle))
    return Fx, Fy

F = float(input("Enter the magnitude of the force (in N): "))
angle_deg = float(input("Enter the angle of the force (in degrees): "))

Fx, Fy = force_components(F, angle_deg)

print(f"Horizontal Component (Fx): {Fx:.2f} N")
print(f"Vertical Component (Fy): {Fy:.2f} N")

