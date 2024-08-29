def dfs(x, y, count, visited):
    
    global max_count

    if max_count < count:
        max_count = count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] not in visited:
            visited.add(table[nx][ny])
            dfs(nx, ny, count+1, visited)
            visited.remove(table[nx][ny])


R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_count = 0

dfs(0, 0, 1, set(table[0][0]))

print(max_count)