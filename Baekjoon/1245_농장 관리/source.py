from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

near = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
visited = [[False] * M for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        visited[i][j] = True
        q = deque([(i, j)])
        flag = True

        now_height = table[i][j]

        while q:
            x, y = q.popleft()

            for d in range(8):
                nx, ny = x + near[d][0], y + near[d][1]

                if 0 <= nx < N and 0 <= ny < M:

                    if table[nx][ny] > now_height:
                        flag = False

                    if table[nx][ny] == table[i][j] and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    
        
        if flag:
            count += 1

print(count)