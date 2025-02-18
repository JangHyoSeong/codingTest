N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[int(21e8)] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for edge in edges:
    graph[edge[0]][edge[1]] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

count = 0
for i in range(1, N+1):
    known_count = 0
    for j in range(1, N+1):
        if graph[i][j] == 1 or graph[j][i] == 1:
            known_count += 1
    
    if known_count == N-1:
        count += 1

print(count)