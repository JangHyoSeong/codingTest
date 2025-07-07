from collections import deque

table = [[0] * 501 for _ in range(501)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            table[i][j] = -1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            table[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[int(21e8)] * 501 for _ in range(501)]

dist[0][0] = 0
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 500 and 0 <= ny <= 500:
            if table[nx][ny] == 1:
                continue

            cost = 1 if table[nx][ny] == -1 else 0
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost

                if cost == 0:
                    q.appendleft((nx, ny))
                else:
                    q.append((nx, ny))

print(dist[500][500] if dist[500][500] != int(21e8) else -1)