import sys
from heapq import heappush, heappop

V, E = map(int, input().split())
start_node = int(input())

edges = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, length = map(int, sys.stdin.readline().rstrip().split())
    edges[start].append((length, end))

dist = [float('inf')] * (V+1)
dist[start_node] = 0

pq = []
heappush(pq, (0, start_node))

while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if dist[next_node] > new_dist:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])