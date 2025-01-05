import numpy as np

###solve 1
# mat_A = []
# row = []
# for i in range(2):
#     for j in range(2):
#         n = int(input())
#         row.append(n)
#     mat_A.append(row)
#     row = []

# print(np.array(mat_A))

####solve 2
# mat_A = []

# for i in range(2):
#     row = list(map(int, input(f'Row {i+1}: ').split()))
#     # print(row)
#     mat_A.append(row)

# print(mat_A)


####solve 3

def input_matrix(name, row):
    mat = []
    for i in range(row):
        input_row = list(map(int, input(f'Row {i+1} of matrix {name}: ').split()))
        mat.append(input_row)
    
    return  mat

A = input_matrix('A', 2)
B = input_matrix('B', 2)

print(np.array(A))
print(B)