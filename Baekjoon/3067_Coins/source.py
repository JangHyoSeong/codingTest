import sys

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())

    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
    
    print(dp[M])