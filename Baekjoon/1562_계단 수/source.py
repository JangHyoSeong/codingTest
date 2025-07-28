MOD = 1000000000

N = int(input())

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for length in range(2, N+1):
    for digit in range(10):
        for bit in range(1 << 10):
            if digit > 0:
                dp[length][digit][bit | (1 << digit)] += dp[length - 1][digit - 1][bit]
                dp[length][digit][bit | (1 << digit)] %= MOD
            
            if digit < 9:
                dp[length][digit][bit | (1 << digit)] += dp[length - 1][digit + 1][bit]
                dp[length][digit][bit | (1 << digit)] %= MOD

result = 0
for i in range(10):
    result = (result + dp[N][i][(1 << 10) - 1]) % MOD

print(result)