from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(M)]

visited = [[int(21e8)] * N for _ in range(M)]
visited[0][0] = 0

q = deque()
q.append((0, 0))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if table[nx][ny] == 0 and visited[x][y] < visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]
            
            if table[nx][ny] == 1 and visited[x][y] + 1 < visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[M-1][N-1])