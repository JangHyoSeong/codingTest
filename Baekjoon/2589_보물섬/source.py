from collections import deque

L, W = map(int, input().split())
table = [list(input()) for _ in range(L)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_dist = 0

for i in range(L):
    for j in range(W):
        if table[i][j] == 'W':
            continue

        visited = [[False] * W for _ in range(L)]
        visited[i][j] = True
        q = deque([[i, j, 0]])
        
        while q:
            x, y, count = q.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                
                if 0 <= nx < L and 0 <= ny < W and not visited[nx][ny] and table[nx][ny] == 'L':
                    q.append((nx, ny, count+1))
                    visited[nx][ny] = True

        max_dist = max(max_dist, count)
print(max_dist)