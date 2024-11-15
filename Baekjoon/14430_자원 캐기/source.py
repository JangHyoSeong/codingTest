N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = table[0][0]

for i in range(1, N):
    dp[i][0] += dp[i-1][0]
    if table[i][0]:
        dp[i][0] += 1

for i in range(1, M):
    dp[0][i] += dp[0][i-1]
    if table[0][i]:
        dp[0][i] += 1

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if table[i][j]:
            dp[i][j] += 1
print(dp[N-1][M-1])