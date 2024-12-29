# sin(x) - x + 1
import numpy as np
a, b = 1, 2
tol = 1e-6

for i in range(100):
    c = (a+b)/2

    if np.sin(a) - a + 1 <0:
        if np.sin(c) - c +1 >0:
            b = c
        else: 
            a = c
    else:
        if np.sin(c) - c + 1 <0:
            b = c
        else:
            a = c
    if abs(a-b)<tol:
        break
x = (a+b)/2
print(f'Root (Bisection method): {x}')

