MOD = 1000000

password = list(map(int, input()))

N = len(password)
dp = [0] * (N + 1)

dp[0] = 1

if password[0] == 0:
    print(0)
    exit()

dp[1] = 1
for i in range(2, N+1):
    one = password[i-1]
    two = password[i-2] * 10 + password[i-1]

    if 1 <= one <= 9:
        dp[i] += dp[i-1]
    if 10 <= two <= 26:
        dp[i] += dp[i-2]
    
    dp[i] %= MOD

print(dp[N])