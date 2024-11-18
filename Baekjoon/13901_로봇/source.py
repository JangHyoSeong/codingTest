R, C = map(int, input().split())
k = int(input())

table = [[0] * C for _ in range(R)]
for _ in range(k):
    x, y = map(int, input().split())
    table[x][y] = 1

x, y = map(int, input().split())
table[x][y] = 1
dir = list(map(int, input().split()))
now_dir = 0

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
moved = 0
while True:

    nx, ny = x + move[dir[now_dir] - 1][0], y + move[dir[now_dir] - 1][1]
    
    if 0 <= nx < R and 0 <= ny < C and not table[nx][ny]:
        x, y = nx, ny
        table[nx][ny] = 1
        moved = 0

    else:
        now_dir = (now_dir + 1) % 4
        moved += 1
    
    if moved == 4:
        break
print(x, y)