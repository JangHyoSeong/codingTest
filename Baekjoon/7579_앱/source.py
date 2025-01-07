N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

costs_sum = sum(costs)

dp = [[0] * (costs_sum + 1) for _ in range(N + 1)]

result = int(21e8)

for i in range(1, N+1):
    for j in range(0, costs_sum + 1):
        if (j < costs[i]):
            dp[i][j] = dp[i-1][j]
        
        else:
            dp[i][j] = max(dp[i-1][j-costs[i]] + memories[i], dp[i-1][j])

        if (dp[i][j] >= M):
            result = min(result, j)

print(result)