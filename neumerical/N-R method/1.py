# N-R method
# sinx - x + 1
import numpy as np 

x = 0.5
tol = 1e-6

for i in range(100):
    fx = np.sin(x) - x + 1
    dfx = np.cos(x) - 1

    if abs(fx) < tol:
        break

    if dfx == 0:
        print('Zero derivative.\nNo Solution Found')

    x = x - (fx/dfx)

# if abs(fx) < tol:
#     print(f'Root (Newton Raphson): {x}')
else:
    print('Exceeded maximum iteration.\nNo Solution Found')
print(f'Root (Newton Raphson): {x}')



## solution 2
# x = 0.5
# tol = 1e-6

# while True:
#     fx = np.sin(x) - x + 1
#     dfx = np.cos(x) - 1

#     if abs(fx) < tol:
#         break

#     if dfx == 0:
#         print('Zero derivative.\nNo Solution Found')

#     x = x - (fx/dfx)

# if abs(fx) < tol:
#     print(f'Root (Newton Raphson): {x}')
# else:
#     print('Exceeded maximum iteration.\nNo Solution Found')



