N, M, K = map(int, input().split())

table = [[False] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    table[r-1][c-1] = True

visited = [[False] * M for _ in range(N)]
max_count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if visited[i][j] or not table[i][j]:
            continue

        count = 1
        stack = [(i, j)]
        visited[i][j] = True

        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and table[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
        
        max_count = max(max_count, count)

print(max_count)