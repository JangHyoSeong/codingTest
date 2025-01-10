from collections import deque

N, L, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
while True:
    opened = [[False] * N for _ in range(N)]
    open_flag = False

    for i in range(N):
        for j in range(N):
            if opened[i][j]:
                continue

            q = deque([(i, j)])
            union = [(i, j)]
            temp_sum = table[i][j]
            opened[i][j] = True

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not opened[nx][ny]:
                        if L <= abs(table[nx][ny] - table[x][y]) <= R:
                            q.append((nx, ny))
                            union.append((nx, ny))
                            temp_sum += table[nx][ny]
                            opened[nx][ny] = True
                            open_flag = True

            if len(union) > 1:
                new_population = temp_sum // len(union)
                for x, y in union:
                    table[x][y] = new_population

    if not open_flag:
        break

    count += 1

print(count)