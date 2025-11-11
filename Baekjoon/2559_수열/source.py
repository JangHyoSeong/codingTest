import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

temp_sum = sum(arr[:K])
max_sum = temp_sum
for i in range(K, N):
    temp_sum = temp_sum - arr[i-K] + arr[i]
    max_sum = max(max_sum, temp_sum)

print(max_sum)