import numpy as np

A = np.array(
    [
        [1,4],
        [3,8]
    ]
)
B = np.array(
    [
        [3,9],
        [13,81]
    ]
)
B_inv = np.linalg.inv(B)
C = np.dot(A,B_inv)
print(C)