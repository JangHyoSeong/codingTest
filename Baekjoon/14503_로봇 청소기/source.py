N, M = map(int, input().split())
x, y, dir = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    can_clean = False
    if table[x][y] == 0:
        table[x][y] = 2
        count += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
            can_clean = True
            break

    if can_clean:
        while True:
            dir = (dir - 1) % 4
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]

            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
                x = nx
                y = ny
                break
    else:
        nx = x - direction[dir][0]
        ny = y - direction[dir][1]

        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] != 1:
            x = nx
            y = ny
        else:
            break

print(count)