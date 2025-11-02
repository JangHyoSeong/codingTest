from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]
visited[0][0] = True

q = deque()
q.append((0, 0))

dx = [1, 0]
dy = [0, 1]

while q:
    x, y = q.popleft()

    if x == M-1 and y == N-1:
        print("Yes")
        break

    for d in range(2):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < M and 0 <= ny < N and table[nx][ny] and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True
else:
    print("No")