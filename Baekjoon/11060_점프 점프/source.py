N = int(input())
maze = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):

    jump = maze[i]
    for j in range(1, jump+1):
        if i+j < N:
            dp[i+j] = min(dp[i]+1, dp[i+j])

if dp[N-1] == float('inf'):
    print(-1)
else:
    print(dp[N-1])