import sys
from collections import deque

def bfs(start, edges, visited, stop_at=None):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        if stop_at is not None and now == stop_at:
            continue
        for next in edges[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

N, M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
edges_re = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edges[start].append(end)
    edges_re[end].append(start)

S, T = map(int, sys.stdin.readline().split())

visited_StoT = [False] * (N+1)
bfs(S, edges, visited_StoT, stop_at=T)

visited_StoT_re = [False] * (N+1)
bfs(T, edges_re, visited_StoT_re)

visited_TtoS = [False] * (N+1)
bfs(T, edges, visited_TtoS, stop_at=S)

visited_TtoS_re = [False] * (N+1)
bfs(S, edges_re, visited_TtoS_re)

count = 0
for i in range(1, N+1):
    if i == S or i == T:
        continue
        
    if visited_StoT[i] and visited_StoT_re[i] and visited_TtoS[i] and visited_TtoS_re[i]:
        count += 1

print(count)