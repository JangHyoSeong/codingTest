from heapq import heappop, heappush

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

pq = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]

for j in range(M):
    heappush(pq, (-table[0][j], 0, j))
    visited[0][j] = True
    if N > 1:
        heappush(pq, (-table[N-1][j], N-1, j))
        visited[N-1][j] = True

for i in range(1, N-1):
    heappush(pq, (-table[i][0], i, 0))
    visited[i][0] = True
    if M > 1:
        heappush(pq, (-table[i][M-1], i, M-1))
        visited[i][M-1] = True

count = 0
while count < K:
    value, x, y = heappop(pq)
    print(x+1, y+1)
    count += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            heappush(pq, (-table[nx][ny], nx, ny))
            visited[nx][ny] = True