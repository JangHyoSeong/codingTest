INF = float('inf')

N, M = map(int, input().split())
dist = [[INF] * N for _ in range(N)]
path = [[0] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0
    path[i][i] = '-'

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
    path[a-1][b-1] = b
    path[b-1][a-1] = a

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]


for i in range(N):
    print(" ".join(map(str, path[i])))