N, K = map(int, input().split())

dp = [0] * (K+1)
for i in range(N):
    weight, value = map(int, input().split())

    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j-weight] + value)

print(dp[K])