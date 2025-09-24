from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_dist = -1
max_sum = 0

for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            continue
        
        if table[i][j] + 9 < max_sum:
            continue
        
        visited = [[-1] * M for _ in range(N)]
        visited[i][j] = 0
        q = deque([(i, j)])

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M:
                    if table[nx][ny] and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

        dist = visited[x][y]
        if dist == max_dist:
            max_dist = dist
            max_sum = max(max_sum, table[i][j] + table[x][y])
        
        elif dist > max_dist:
            max_dist = dist
            max_sum = table[i][j] + table[x][y]

print(max_sum if max_dist != -1 else 0)