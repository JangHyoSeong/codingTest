from heapq import heappush, heappop

N, M = map(int, input().split())
visible = list(map(int, input().split()))

edges = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a].append((t, b))
    edges[b].append((t, a))

pq = [(0, 0)]
dist = [float('inf')] * N
dist[0] = 0

while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        if visible[next_node] and next_node != N - 1:
            continue

        new_dist = now_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(dist[N - 1] if dist[N - 1] != float('inf') else -1)