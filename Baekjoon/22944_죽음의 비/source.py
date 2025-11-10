from collections import deque

N, H, D = map(int, input().split())
table = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if table[i][j] == "S":
            start_x, start_y = i, j

visited = [[-1] * N for _ in range(N)]

q = deque()
q.append((start_x, start_y, H, 0, 0))
visited[start_x][start_y] = H

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, hp, cost, step = q.popleft()

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        nh, nc = hp, cost

        if table[nx][ny] == 'E':
            print(step + 1)
            exit()

        if table[nx][ny] == 'U':
            nc = D

        if nc > 0:
            nc -= 1
        else:
            nh -= 1

        if nh <= 0:
            continue

        if visited[nx][ny] < nh + nc:
            visited[nx][ny] = nh + nc
            q.append((nx, ny, nh, nc, step + 1))

print(-1)