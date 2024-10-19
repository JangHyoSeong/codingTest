def dfs(node, depth):
    if depth == 4:
        print(1)
        exit()

    visited[node] = True
    for next_node in edges[node]:
        if not visited[next_node]:
            dfs(next_node, depth+1)
    
    visited[node] = False

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * N

for i in range(N):
    dfs(i, 0)    

print(0)