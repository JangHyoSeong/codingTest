from collections import deque

R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
water = []
visited = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if table[i][j] == "S":
            q.append((i, j, 0))
            visited[i][j] = True
        elif table[i][j] == "*":
            water.append((i, j))

while q:

    new_water = []
    new_queue = deque()

    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and table[nx][ny] == ".":
                table[nx][ny] = "*"
                new_water.append((nx, ny))

    water = new_water
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if table[nx][ny] == "D":
                    print(count+1)
                    exit()
                elif table[nx][ny] == ".":
                    new_queue.append((nx, ny, count+1))
                    visited[nx][ny] = True

    q = new_queue

print("KAKTUS")