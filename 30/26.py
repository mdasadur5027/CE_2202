A =[[1,2,4],
    [2,50,11],
    [66,9,13]]

# trace = A[0][0]+A[1][1]+A[2][2]
# print(trace)
trace = 0
for i in range(3):
    for j in range(3):
        if i == j :
            trace += A[i][j]
print(trace)