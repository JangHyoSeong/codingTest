N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (T+1)
for subject in arr:
    for i in range(T, subject[0] - 1, -1):
        dp[i] = max(dp[i - subject[0]] + subject[1], dp[i])

print(dp[T])