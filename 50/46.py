import numpy as np
num = list(map(int, input().split()))

num_sorted = np.sort(num)
print(num_sorted)
print(num_sorted[::-2])