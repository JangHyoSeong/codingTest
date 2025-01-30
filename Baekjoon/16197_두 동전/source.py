from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

q = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)])
visited = set([(coins[0][0], coins[0][1], coins[1][0], coins[1][1])])

while q:
    x1, y1, x2, y2, count = q.popleft()
    
    if count >= 10:
        break
    
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        
        out1 = not (0 <= nx1 < N and 0 <= ny1 < M)
        out2 = not (0 <= nx2 < N and 0 <= ny2 < M)
        
        if out1 and out2:
            continue
        if out1 or out2:
            print(count + 1)
            exit()
        
        if not out1 and board[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if not out2 and board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        
        if (nx1, ny1, nx2, ny2) not in visited:
            visited.add((nx1, ny1, nx2, ny2))
            q.append((nx1, ny1, nx2, ny2, count + 1))

print(-1)