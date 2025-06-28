import sys
sys.setrecursionlimit(1_000_000)

R, C = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]
answer = [[0] * C for _ in range(R)]
destination = [[(-1, -1) for _ in range(C)] for _ in range(R)]

direction = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def dfs(x, y):
    if destination[x][y] != (-1, -1):
        return destination[x][y]
    
    min_val = table[x][y]
    move_x, move_y = -1, -1

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if table[nx][ny] < min_val:
                min_val = table[nx][ny]
                move_x, move_y = nx, ny

    if move_x == -1:
        destination[x][y] = (x, y)
    else:
        destination[x][y] = dfs(move_x, move_y)

    return destination[x][y]

for i in range(R):
    for j in range(C):
        x, y = dfs(i, j)
        answer[x][y] += 1

for row in answer:
    print(" ".join(map(str, row)))