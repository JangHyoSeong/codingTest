from collections import deque

N = int(input())
table = [list(map(int, input())) for _ in range(N)]

visited = [[int(21e8)] * N for _ in range(N)]
visited[0][0] = 0

q = deque()
q.append((0, 0, 0)) # x, y, 방 바꾼 갯수

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y, count = q.popleft()

    if count > visited[x][y]:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if table[nx][ny]:
                if visited[nx][ny] > count:
                    visited[nx][ny] = count
                    q.append((nx, ny, count))
            else:
                if visited[nx][ny] > count + 1:
                    visited[nx][ny] = count + 1
                    q.append((nx, ny, count+1))

print(visited[N-1][N-1])