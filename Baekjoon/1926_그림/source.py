H, W = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(H)]

count = 0
max_large = 0

visited = [[False] * W for _ in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        
        if canvas[i][j] == 1:
            visited[i][j] = True
            temp_large = 1
            count += 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()

                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]

                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and canvas[nx][ny] == 1:
                        visited[nx][ny] = True
                        temp_large += 1
                        stack.append((nx, ny))
            
            max_large = max(max_large, temp_large)

print(count)
print(max_large)