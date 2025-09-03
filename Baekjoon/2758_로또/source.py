T = int(input())

cases = [list(map(int, input().split())) for _ in range(T)]

max_n = max(case[0] for case in cases)
max_m = max(case[1] for case in cases)

dp = [[0] * (max_m + 1) for _ in range(max_n+1)]

for j in range(1, max_m + 1):
    dp[1][j] = 1

for i in range(2, max_n + 1):
    for j in range(1, max_m + 1):
        for k in range(1, j // 2 + 1):
            dp[i][j] += dp[i-1][k]

answer = [[0] * (max_m + 1) for _ in range(max_n + 1)]
for i in range(1, max_n + 1):
    for j in range(1, max_m + 1):
        answer[i][j] = answer[i][j - 1] + dp[i][j]

for n, m in cases:
    print(answer[n][m])