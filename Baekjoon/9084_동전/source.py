T = int(input())
result = []
for testcase in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
            
    result.append(dp[M])
for c in result:
    print(c)