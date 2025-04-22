N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

max_area = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if table[i][j] == 0:

            table[i][j] = 1
            visited = set()
            visited.add((i, j))

            temp_area = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and table[nx][ny]:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                        temp_area += 1
            max_area = max(max_area, temp_area)
            table[i][j] = 0

print(max_area)