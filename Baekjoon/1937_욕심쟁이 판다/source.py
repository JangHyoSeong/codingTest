import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] > table[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        
    
    return dp[x][y]

result = 0
for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))

print(result)