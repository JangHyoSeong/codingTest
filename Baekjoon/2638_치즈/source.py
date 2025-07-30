from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check_air():
    visited = [[False] * M for _ in range(N)]
    q = deque()

    q.append((0, 0))
    visited[0][0] = True

    air = [[0] * M for _ in range(N)]
    while q:
        x, y = q.popleft()
        air[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not table[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return air

def melt_cheese():
    air = check_air()
    melt = []

    for i in range(N):
        for j in range(M):
            if table[i][j] == 1:
                count = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]

                    if 0 <= nx < N and 0 <= ny < M and air[nx][ny] == 1:
                        count += 1
                
                if count >= 2:
                    melt.append((i, j))
    
    for x, y in melt:
        table[x][y] = 0
    
    return len(melt) > 0

time = 0
while True:
    if not melt_cheese():
        break

    time += 1

print(time)