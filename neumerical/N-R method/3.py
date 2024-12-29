# N-R method
# x^2 - 3x + 10

import numpy as np
x = 1
tol = 1e-6

for i in range(100):
    fx = x**2 -3*x + 10
    dfx = 2*x -3
    if abs(fx) < tol:
        break
    if dfx == 0:
        print('Zero Derivative. No Solution Found')
        break

    x = x - (fx/dfx)

if abs(fx) < tol:
    print(f'Root (Newton Raphson): {x}')
else:
    print('Exceeded maximum iteration.\nNo Solution Found')