N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for y in range(N):
    for x in range(2, N):
        if table[y][x] == 1:
            continue

        if table[y][x-1] == 0:
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]

        if y-1 >= 0 and table[y-1][x] == 0:
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
        
        if y-1 >= 0 and x-1 >= 0:
            if table[y-1][x] == 0 and table[y][x-1] == 0 and table[y-1][x-1] == 0:
                dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[N-1][N-1]))