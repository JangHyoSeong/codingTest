N, M, K = map(int, input().split())
table = [list(input()) for _ in range(N)]
target = input()
target_len = len(target)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dp = [[[-1] * target_len for _ in range(M)] for _ in range(N)]

def dfs(x, y, idx):
    if idx == len(target):
        return 1
    
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]
    
    count = 0
    for i in range(4):
        for step in range(1, K+1):
            nx, ny = x + dx[i] * step, y + dy[i] * step
            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == target[idx]:
                count += dfs(nx, ny, idx + 1)

    dp[x][y][idx] = count
    return count

result = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == target[0]:
            result += dfs(i, j, 1)

print(result)