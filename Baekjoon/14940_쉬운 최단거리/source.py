from collections import deque

n, m = map(int, input().split())
table = []

flag = False
for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp)

    if not flag:
        for j in range(m):
            if temp[j] == 2:
                start = (i, j)
                flag = True
                break

dist = [[0] * m for _ in range(n)]
q = deque([start])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1 and not dist[nx][ny]:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if dist[i][j] == 0 and table[i][j] == 1:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()