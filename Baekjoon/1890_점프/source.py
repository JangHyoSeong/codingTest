N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if table[i][j] == 0:
            break

        jump = table[i][j]
        
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]

        if i + jump < N:
            dp[i + jump][j] += dp[i][j]

print(dp[N-1][N-1])