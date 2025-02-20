import sys
import math

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
count_arr = [0] * N

count = 0
for i in range(1, N):
    ratio = math.ceil(math.log2(arr[i-1] / arr[i])) + count_arr[i-1]
    if ratio > 0:
        count_arr[i] = max(0, ratio)
        count += count_arr[i]

print(count)