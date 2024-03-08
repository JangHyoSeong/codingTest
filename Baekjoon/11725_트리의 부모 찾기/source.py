from collections import deque

N = int(input())

visited = [False] * (N+1)
edge = [[] for _ in range(N+1)]
parent = [None] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

q = deque()
q.append(1)
visited[1] = True

while q:

    node = q.popleft()

    for i in edge[node]:
        if not visited[i]:
            parent[i] = node
            visited[i] = True
            q.append(i)
    
    
for i in range(2, N+1):
    print(parent[i])