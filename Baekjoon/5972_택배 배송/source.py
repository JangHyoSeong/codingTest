from heapq import heappush, heappop

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

dist = [float('inf')] * (N+1)
dist[1] = 0

pq = []
heappush(pq, (0, 1))
while pq:
    now_dist, now_node = heappop(pq)

    if dist[now_node] < now_dist:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(dist[-1])