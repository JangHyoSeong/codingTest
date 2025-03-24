import sys
from heapq import heappush, heappop

N, M, R = map(int, sys.stdin.readline().rstrip().split())
items = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((l, b))
    edges[b].append((l, a))

max_item = 0
for i in range(1, N+1):
    dist = [int(21e8)] * (N+1)
    dist[i] = 0

    pq = [(0, i)]

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            new_dist = next_dist + now_dist

            if new_dist < dist[next_node]:
                heappush(pq, (new_dist, next_node))
                dist[next_node] = new_dist

    temp_item = 0
    for i in range(1, N+1):
        if dist[i] <= M:
            temp_item += items[i]

    max_item = max(max_item, temp_item)

print(max_item)