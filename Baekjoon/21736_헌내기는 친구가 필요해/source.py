import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
table = []
for i in range(N):
    arr = list(sys.stdin.readline().rstrip())
    table.append(arr)
    if "I" in arr:
        start = (i, arr.index("I"))

q = deque([start])
visited = [[False] * M for _ in range(N)]
visited[start[0]][start[1]] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if table[nx][ny] == "O":
                q.append((nx, ny))
                visited[nx][ny] = True

            elif table[nx][ny] == "P":
                count += 1
                q.append((nx, ny))
                visited[nx][ny] = True

print(count if count != 0 else "TT")