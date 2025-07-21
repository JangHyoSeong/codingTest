import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    dist[i][i] = 0

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    dist[a][b] = min(dist[a][b], cost)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0

for i in range(1, N+1):
    print(" ".join(map(str, dist[i][1:])))