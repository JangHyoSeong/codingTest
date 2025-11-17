N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

min_point = int(21e8)
start_x, start_y = 0, 0
for i in range(N):
    for j in range(M):
        if min_point > table[i][j]:
            start_x, start_y = i, j
            min_point = table[i][j]

if min_point != 0:
    table[start_x][start_y] = 0

print(sum(sum(row) for row in table))