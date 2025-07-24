N, east, west, south, north = map(int, input().split())

probs = [east, west, south, north]
probs = [p / 100 for p in probs]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * (2 * N + 1) for _ in range(2 * N + 1)]
start_x, start_y = N, N

result = 0

def dfs(x, y, depth, prob):
    global result

    if depth == N:
        result += prob
        return
    
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not visited[nx][ny] and probs[d] > 0:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, prob * probs[d])
            visited[nx][ny] = False
    
visited[start_x][start_y] = True
dfs(start_x, start_y, 0, 1.0)

print(f"{result:.10f}")