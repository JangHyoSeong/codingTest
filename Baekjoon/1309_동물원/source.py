MOD = 9901

N = int(input())

# dp[i][j] : i 위치에 j상태(0: 사자없음, 1: 왼쪽, 2: 오른쪽)
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

print(sum(dp[N-1]) % MOD)