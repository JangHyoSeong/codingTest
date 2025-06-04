import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N + 1)
prefix_sum[1] = arr[0]
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

left, right = 0, N-1
for i in range(1, N+1):
    if prefix_sum[i] >= S:
        right = i
        break
else:
    print(0)
    exit()

left = 0
min_length = N
while right <= N and left < right:
    if prefix_sum[right] - prefix_sum[left] >= S:
        min_length = min(min_length, right - left)
        left += 1
    else:
        right += 1

print(min_length)