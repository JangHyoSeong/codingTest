N = int(input())
table = [list(input()) for _ in range(N)]

def dfs(x, y, visited, grid, color):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_regions(grid):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited, grid, grid[i][j])
                count += 1
    return count

normal_count = count_regions(table)
for i in range(N):
    for j in range(N):
        if table[i][j] in 'RG':
            table[i][j] = 'R'
colorblind_count = count_regions(table)

print(normal_count, colorblind_count)