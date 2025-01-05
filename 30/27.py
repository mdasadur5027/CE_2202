import numpy as np

num = []
for i in range(4):
    n = int(input())
    num.append(n)

print(np.sort(num))
print(np.sort(num)[::-1])