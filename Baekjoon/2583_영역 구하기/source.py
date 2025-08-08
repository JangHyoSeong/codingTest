from pprint import pprint

M, N, K = map(int, input().split())

table = [[False] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            table[y][x] = True

count = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
area = []
for i in range(M):
    for j in range(N):
        if table[i][j]:
            continue

        count += 1
        stack = [(i, j)]
        table[i][j] = True
        size = 1
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < M and 0 <= ny < N and not table[nx][ny]:
                    stack.append((nx, ny))
                    size += 1
                    table[nx][ny] = True
        
        area.append(size)

print(count)
print(" ".join(map(str, sorted(area))))