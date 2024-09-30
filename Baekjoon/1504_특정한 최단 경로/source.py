import sys
from heapq import heappop, heappush

N, E = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, now_node = heappop(pq)

        if distance[now_node] < now_dist:
            continue

        for next_node, next_dist in graph[now_node]:
            new_dist = next_dist + now_dist

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    return distance

dist_from_1 = dijkstra(1, edges, N)
dist_from_v1 = dijkstra(v1, edges, N)
dist_from_v2 = dijkstra(v2, edges, N)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(path1, path2)
print(result if result < float('inf') else -1)