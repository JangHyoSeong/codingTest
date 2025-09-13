N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + arr[i]

dp = [[float('-inf')] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(M+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])

        if j > 0:
            for k in range(1, i+1):
                if k >= 2:
                    dp[i][j] = max(dp[i][j], dp[k-2][j-1] + (prefix[i] - prefix[k-1]))
                elif k == 1 and j == 1:
                    dp[i][j] = max(dp[i][j], prefix[i])

print(dp[N][M])