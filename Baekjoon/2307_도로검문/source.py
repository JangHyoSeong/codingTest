import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((t, b))
    edges[b].append((t, a))

dist = [float('inf')] * (N+1)
dist[1] = 0

prev = [-1] * (N+1)

pq = []
heappush(pq, (0, 1))

while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist

        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            prev[next_node] = now_node
            heappush(pq, (new_dist, next_node))
    
min_time = dist[N]

path_edges = []
cur = N
while prev[cur] != -1:
    path_edges.append((prev[cur], cur))
    cur = prev[cur]

max_gap = 0
for case in path_edges:
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    pq = []
    heappush(pq, (0, 1))

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            if (next_node, now_node) == case or (now_node, next_node) == case:
                continue

            new_dist = now_dist + next_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    if dist[N] == float('inf'):
        print(-1)
        exit()

    else:
        max_gap = max(dist[N] - min_time, max_gap)

print(max_gap)