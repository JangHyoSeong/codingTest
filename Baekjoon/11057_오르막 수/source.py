N = int(input())
MOD = 10007

dp = [[0] * 10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for n in range(2, N+1):
    for d in range(10):
        dp[n][d] = sum(dp[n-1][:d+1]) % MOD

print(sum(dp[N]) % MOD)