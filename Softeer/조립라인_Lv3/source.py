import sys

N = int(input())
task = []

for i in range(N):
    task.append(list(map(int, input().split())))

dp = [[0, 0] for _ in range(N)]
dp[0] = [task[0][0], task[0][1]]

for i in range(1, N):
    dp[i][0] = task[i][0] + min(dp[i-1][0], dp[i-1][1] + task[i-1][3])
    dp[i][1] = task[i][1] + min(dp[i-1][1], dp[i-1][0] + task[i-1][2])

print(min(dp[N-1]))