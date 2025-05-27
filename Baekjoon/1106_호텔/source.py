C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [int(1e9)] * (C + 100)
dp[0] = 0

for cost, customer in arr:
    for i in range(customer, C + 100):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))