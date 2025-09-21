from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]

# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direction_bit = [1, 2, 4, 8]

room_size = []
room_id = 1

for i in range(M):
    for j in range(N):
        if visited[i][j] != 0:
            continue

        q = deque([(i, j)])
        visited[i][j] = room_id
        size = 1
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < M and 0 <= ny < N:
                    if not (table[x][y] & direction_bit[d]) and visited[nx][ny] == 0:
                        visited[nx][ny] = room_id
                        q.append((nx, ny))
                        size += 1
        
        room_size.append(size)
        room_id += 1

max_after_removal = 0

for i in range(M):
    for j in range(N):
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < M and 0 <= nj < N:
                if visited[i][j] != visited[ni][nj]:
                    combined = room_size[visited[i][j] - 1] + room_size[visited[ni][nj] - 1]
                    max_after_removal = max(max_after_removal, combined)

print(len(room_size))
print(max(room_size))
print(max_after_removal)