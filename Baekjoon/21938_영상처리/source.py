import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
T = int(sys.stdin.readline().rstrip())

picture = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(0, M * 3, 3):
        rgb_sum = sum(table[i][j:j+3])

        if rgb_sum >= 3 * T:
            picture[i][j//3] = True

visited = [[False] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] or not picture[i][j]:
            continue

        stack = [(i, j)]
        visited[i][j] = True
        count += 1
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and picture[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

print(count)  