N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (N+1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

max_sum = 0
for i in range(M, N+1):
    max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-M])

print(max_sum)