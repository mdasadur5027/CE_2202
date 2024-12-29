# x^2 -3x +10
import numpy as np
x = 1
tol = 1e-6

for i in range(100):
    x_new = (3*x - 10)**0.5
    if abs(x_new-x)<tol:
        break
    x = x_new
print(f'Root (Iteration method): {x}')