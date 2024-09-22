import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for time in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append([time, b])
    edges[b].append([time, a])

dist = [float('inf')] * (N+1)
dist[1] = 0

pq = []
heappush(pq, (0, 1))

while pq:
    time, now = heappop(pq)

    if now == N:
        break

    if time > dist[now]:
        continue

    for period, next in edges[now]:
        wait_time = (period - (time % M)) % M
        next_time = time + wait_time + 1

        if next_time < dist[next]:
            dist[next] = next_time
            heappush(pq, (next_time, next))

print(dist[N])