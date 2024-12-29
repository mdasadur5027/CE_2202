# N-R method
# e^x - 4
import numpy as np 

x = 0.5
tol = 1e-6

for i in range(100):
    fx = np.exp(x) - 4*x
    dfx = np.exp(x) - 4

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