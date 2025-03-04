N, M = map(int, input().split())
K = int(input())

blocked = set()
for _ in range(K):
    a, b, c, d = map(int, input().split())
    blocked.add(((a, b), (c, d)))
    blocked.add(((c, d), (a, b)))

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        if i == 0 and j == 0:
            continue

        if i > 0 and ((i-1, j), (i, j)) not in blocked:
            dp[i][j] += dp[i-1][j]

        if j > 0 and ((i, j-1), (i, j)) not in blocked:
            dp[i][j] += dp[i][j-1]

print(dp[N][M])