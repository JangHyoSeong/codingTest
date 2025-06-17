import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

arr.sort(reverse=True)

max_weight = 0
for i in range(N):
    weight = arr[i] * (i + 1)
    max_weight = max(max_weight, weight)

print(max_weight)