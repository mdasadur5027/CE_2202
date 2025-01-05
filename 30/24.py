import numpy as np 

def matrix_mul(a,b):
    return np.dot(a,b)

A = np.array(
    [
        [1,2,4],
        [2,50,6],
        [66,9,2],
        [9,3,4]
    ]
)
B = np.array(
    [
        [1,2,4,4],
        [2,50,6,11],
        [66,9,2,13]
    ]
)

# print(A+B)
print(matrix_mul(A,B))
print(np.trace(B))

