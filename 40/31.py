num = list(map(int, input().split()))
# print(num)
sum = 0
for i in range(len(num)):
    if num[i]%2 !=0:
        sum += num[i]

print(sum)