MOD = 1000000009

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_n = max(numbers)

# dp[i][j]: i를 만들 때 마지막에 사용한 수가 j인 경우의 수
dp = [[0] * 4 for _ in range(max_n + 1)]

if max_n >= 1:
    dp[1][1] = 1

if max_n >= 2:
    dp[2][2] = 1

if max_n >= 3:
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

for i in range(4, max_n + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

for n in numbers:
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)