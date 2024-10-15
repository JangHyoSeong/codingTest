N, K = map(int, input().split())
tasks = [list(map(int, input().split())) for _ in range(K)]

tasks.sort(key= lambda x: -x[0])

dp = [0] * (N+1)

for i in range(K):
    value, time = tasks[i]

    for j in range(N, time-1, -1):
        dp[j] = max(dp[j], dp[j-time] + value)

print(dp[N])