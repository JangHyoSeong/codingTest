table = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def is_valid(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for x in range(19):
    for y in range(19):
        if table[x][y] != 0:
            color = table[x][y]
            for d in range(4):
                count = 1
                nx, ny = x + dx[d], y + dy[d]
                
                while is_valid(nx, ny) and table[nx][ny] == color:
                    count += 1
                    if count == 5:
                        px, py = x - dx[d], y - dy[d]
                        if is_valid(px, py) and table[px][py] == color:
                            break
                        nx, ny = nx + dx[d], ny + dy[d]
                        if is_valid(nx, ny) and table[nx][ny] == color:
                            break
                        print(color)
                        print(x + 1, y + 1)
                        exit(0)
                    nx, ny = nx + dx[d], ny + dy[d]

print(0)