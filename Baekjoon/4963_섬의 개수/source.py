from collections import deque

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    table = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    count = 0
    for i in range(h):
        for j in range(w):
            if table[i][j] and not visited[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and table[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True

    print(count)