N, K = map(int, input().split())

dist = [[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    dist[a][b] = -1
    dist[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N + 1):
            if dist[i][k] == -1 and dist[k][j] == -1:
                dist[i][j] = -1
                dist[j][i] = 1

S = int(input())
for _ in range(S):
    x, y = map(int, input().split())
    print(dist[x][y])