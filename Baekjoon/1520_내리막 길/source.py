# 입력 처리
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and heights[nx][ny] < heights[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

# 경로의 수 계산 및 출력
print(dfs(0, 0))