import sys
sys.setrecursionlimit(100000)

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x, y):
    if y == C - 1:
        return True

    for dir in range(3):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
    return False

answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)