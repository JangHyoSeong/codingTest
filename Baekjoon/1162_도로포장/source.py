from heapq import heappush, heappop
import sys

INF = float('inf')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, time = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((time, b))
    edges[b].append((time, a))

dist = [[INF] * (K + 1) for _ in range(N+1)]
dist[1][0] = 0

# 거리, 노드, K
pq = [(0, 1, 0)]
while pq:
    now_dist, now_node, k = heappop(pq)

    if now_dist > dist[now_node][k]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if new_dist < dist[next_node][k]:
            dist[next_node][k] = new_dist
            heappush(pq, (new_dist, next_node, k))
        
        if k + 1 <= K and now_dist < dist[next_node][k+1]:
            dist[next_node][k+1] = now_dist
            heappush(pq, (now_dist, next_node, k+1))

print(min(dist[N]))