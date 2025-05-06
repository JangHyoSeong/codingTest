import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + arr[i][0] <= N:
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])