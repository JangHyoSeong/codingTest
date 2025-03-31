N = int(input())
table = [list(map(int, input())) for _ in range(N)]

count = 0
result = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if table[i][j] == 0:
            continue
        
        count += 1
        stack = [(i, j)]
        table[i][j] = 0

        area_count = 1
        while stack:
            x, y = stack.pop()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if 0 <= nx < N and 0 <= ny < N and table[nx][ny]:
                    stack.append((nx, ny))
                    table[nx][ny] = 0
                    area_count += 1
        
        result.append(area_count)

print(count)
print("\n".join(map(str, sorted(result))))