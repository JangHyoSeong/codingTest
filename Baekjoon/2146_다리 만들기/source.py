from collections import deque

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

island_idx = 1
for i in range(N):
    for j in range(N):
        if table[i][j] == 1 and visited[i][j] == 0:
            q = deque([(i, j)])
            visited[i][j] = island_idx
            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = island_idx
        
            island_idx += 1

q = deque()
dist = [[-1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]

                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    q.append((i, j))
                    dist[i][j] = 0
                    break

answer = int(21e8)

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            
            elif visited[nx][ny] != visited[x][y]:
                answer = min(answer, dist[x][y] + dist[nx][ny])

print(answer)