from collections import deque

M = int(input())
board = [list(input()) for _ in range(2)]

white_count = sum(row.count('.') for row in board)

INF = 10**9
dist = [[INF] * M for _ in range(2)]
q = deque()

for r in range(2):
    if board[r][0] == '.':
        dist[r][0] = 1
        q.append((r, 0))

while q:
    r, c = q.popleft()
    d = dist[r][c]

    if c + 1 < M and board[r][c+1] == '.' and dist[r][c+1] > d + 1:
        dist[r][c+1] = d + 1
        q.append((r, c+1))
    
    nr = r ^ 1
    if board[nr][c] == '.' and dist[nr][c] > d + 1:
        dist[nr][c] = d + 1
        q.append((nr, c))

min_path = min(dist[0][M-1], dist[1][M-1])
print(white_count - min_path)