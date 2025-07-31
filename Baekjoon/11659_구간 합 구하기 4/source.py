import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[b] - prefix_sum[a-1])