N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

INF = 21e8
dp = [0] * (K+1)

for coin in coins:
    if coin <= K:
        dp[coin] = 1

for i in range(K+1):
    if dp[i] == 0:
        continue
    for coin in coins:
        if i+coin <= K:
            if dp[i+coin] == 0:
                dp[i+coin] = dp[i] + 1
            else:
                dp[i+coin] = min(dp[i+coin], dp[i] + 1)

if dp[K]:
    print(dp[K])
else:
    print(-1)