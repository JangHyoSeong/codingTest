from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]

q = deque([(0, 0)])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and table[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
        
print(visited[N-1][M-1])