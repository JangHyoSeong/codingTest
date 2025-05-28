C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
    exit()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

seats = [[0] * C for _ in range(R)]

x, y = 0, 0
direction = 0

for num in range(1, K + 1):
    seats[y][x] = num
    if num == K:
        print(x + 1, y + 1)
        break

    ny = y + dy[direction]
    nx = x + dx[direction]

    if ny < 0 or ny >= R or nx < 0 or nx >= C or seats[ny][nx] != 0:
        direction = (direction + 1) % 4
        ny = y + dy[direction]
        nx = x + dx[direction]

    y, x = ny, nx