def average(marks):
    return sum(marks)/len(marks)

marks = list(map(float, input().split()))
avg = average(marks)

count = 0
for i in range(len(marks)):
    if marks[i]<avg:
        count +=1

print(avg)
print(count)

