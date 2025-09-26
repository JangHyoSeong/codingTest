import sys
from heapq import heappush, heappop

INF = float('inf')

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

start, end = map(int, sys.stdin.readline().rstrip().split())
weights = [0] * (N + 1)
weights[start] = INF

pq = [(-INF, start)]
while pq:
    
    now_weight, now_node = heappop(pq)
    now_weight *= -1

    if now_node == end:
        print(now_weight)
        break

    if now_weight < weights[now_node]:
        continue

    for next_weight, next_node in edges[now_node]:
        next_capacity = min(now_weight, next_weight)
        if next_capacity > weights[next_node]:
            weights[next_node] = next_capacity
            heappush(pq, (-next_capacity, next_node))