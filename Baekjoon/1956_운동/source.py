import sys
INF = int(21e8)

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(E)]

dist = [[INF] * (V+1) for _ in range(V+1)]
for a, b, c in edges:
    dist[a][b] = c

for i in range(1, V+1):
    dist[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

min_cycle = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j:
            min_cycle = min(min_cycle, dist[i][j] + dist[j][i])

print(min_cycle if min_cycle != INF else -1)