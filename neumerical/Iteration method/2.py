# e^x - 4x
import numpy as np
x = 1
tol = 1e-6

for i in range(100):
    x_new = np.exp(x)/4
    # print(x_new)
    if abs(x_new - x)<tol:
        break
    x = x_new
print(f'Root (Iteration method): {x}')