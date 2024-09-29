import math

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers)

arr = [0] * (max_num + 1)
for i in range(1, max_num + 1):
    arr[i] = arr[i - 1] + math.log10(i)

for m in numbers:
    print(int(arr[m]) + 1)
