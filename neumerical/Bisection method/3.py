# x^sin2 - 4
import numpy as np

def f(x):
    return x**np.sin(2) - 4

a, b = 1, 4
tol = 1e-6

if f(a)*f(b) > 0:
        print('The initial guesses do not bracket a root. Bisection cannot proceed.')

else:
    for i in range(100):
        c = (a+b)/2
    
        if abs(a-b) < tol :
            break
    
        if f(a)*f(c) < 0:
            b = c
        else:
            a =c 
    
    x = (a+b)/2
    print(f'Root (Bisection method): {x}')
        
    
