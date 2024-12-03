from collections import deque

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
virus_list = [[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):
        if table[i][j]:
            virus_list[table[i][j]].append((i, j))

q = deque()
for i in range(1, K+1):
    for virus in virus_list[i]:
        q.append((virus[0], virus[1], i, 0))

while q:
    x, y, virus, time = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0:
            if time == S:
                continue
            q.append((nx, ny, virus, time+1))
            table[nx][ny] = virus

print(table[X-1][Y-1])