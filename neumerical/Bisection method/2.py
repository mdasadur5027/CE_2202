import numpy as np

# Function definition
def f(x):
    return x**2 - 3*x + 10  # Define your function here

# Bisection method
a, b = -5, 5
tol = 1e-6

# Ensure initial guesses bracket the root
if f(a) * f(b) > 0:
    print("The initial guesses do not bracket a root. Bisection cannot proceed.")
    exit()

for i in range(100):  # Max 100 iterations
    c = (a + b) / 2  # Midpoint

    if abs(b - a) < tol:  # Convergence check
        break

    # Update the interval
    if f(a) * f(c) < 0:  # Root is in the left subinterval
        b = c
    else:  # Root is in the right subinterval
        a = c

x = (a + b) / 2  # Final root approximation
print(f'Root (Bisection method): {x}')
