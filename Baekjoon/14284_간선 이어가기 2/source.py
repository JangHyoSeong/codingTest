import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

s, t = map(int, sys.stdin.readline().rstrip().split())
dist = [float('inf')] * (N+1)
dist[s] = 0

pq = [(0, s)]
while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if dist[next_node] > new_dist:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
print(dist[t])