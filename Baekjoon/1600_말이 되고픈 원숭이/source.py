from collections import deque

K = int(input())
W, H = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]

q = deque()
q.append((0, 0, 0))
visited = [[[0] * W for _ in range(H)] for _ in range(K+1)]

jump = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, current_jump = q.popleft()

    if x == H-1 and y == W-1:
        print(visited[current_jump][x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and table[nx][ny] == 0 and not visited[current_jump][nx][ny]:
            visited[current_jump][nx][ny] = visited[current_jump][x][y] + 1
            q.append((nx, ny, current_jump))
    

    if current_jump < K:
        for i in range(8):
            nx = x + jump[i][0]
            ny = y + jump[i][1]

            if 0 <= nx < H and 0 <= ny < W and table[nx][ny] == 0 and not visited[current_jump+1][nx][ny]:
                visited[current_jump+1][nx][ny] = visited[current_jump][x][y] + 1
                q.append((nx, ny, current_jump+1))
else:
    print(-1)