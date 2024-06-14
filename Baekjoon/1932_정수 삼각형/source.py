N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (i+1) for i in range(N)]

dp[0][0] = triangle[0][0]

if N == 1:
    print(triangle[0][0])
    exit()

dp[1][0] = dp[0][0] + triangle[1][0]
dp[1][1] = dp[0][0] + triangle[1][1]

if N == 2:
    print(max(dp[1]))
    exit()

for i in range(2, N):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[N-1]))