# sin(x) - x + 1

import numpy as np
x = 1
tol = 1e-6

for i in range(100):
    x_new = np.sin(x) + 1
    if abs(x-x_new) < tol:
        break
    x = x_new
print(f'Root (Iteration method): {x}')
