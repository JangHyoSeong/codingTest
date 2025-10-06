from collections import deque

N, M, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

spore = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] or table[i][j] == 1:
            continue

        q = deque([(i, j)])
        visited[i][j] = True

        now_area = 1
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    now_area += 1
        
        if now_area % K:
            spore = spore + (now_area // K) + 1
        else:
            spore += now_area // K

if spore <= M and spore != 0:
    print("POSSIBLE")
    print(M - spore)
else:
    print("IMPOSSIBLE")