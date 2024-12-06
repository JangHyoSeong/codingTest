N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

max_area = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for height in range(1, 100):
    temp_area = 0

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] or table[i][j] <= height:
                visited[i][j] = True
                continue

            else:
                visited[i][j] = True
                temp_area += 1

                stack = [(i, j)]

                while stack:
                    x, y = stack.pop()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] > height:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    max_area = max(max_area, temp_area)

print(max_area)