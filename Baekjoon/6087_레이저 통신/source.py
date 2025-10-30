from collections import deque

INF = int(21e8)

W, H = map(int, input().split())
table = [list(input()) for _ in range(H)]

points = []
for i in range(H):
    for j in range(W):
        if table[i][j] == "C":
            points.append((i, j))

start, end = points

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
q = deque()

for d in range(4):
    dist[start[0]][start[1]][d] = 0
    q.append((start[0], start[1], d))

while q:
    x, y, dir = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < H and 0 <= ny < W:
            if table[nx][ny] == "*":
                continue

            add = 0 if dir == d else 1

            if dist[nx][ny][d] > dist[x][y][dir] + add:
                dist[nx][ny][d] = dist[x][y][dir] + add

                if add == 0:
                    q.appendleft((nx, ny, d))
                else:
                    q.append((nx, ny, d))

print(min(dist[end[0]][end[1]]))