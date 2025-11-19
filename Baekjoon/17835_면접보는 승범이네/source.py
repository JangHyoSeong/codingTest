import sys
from heapq import heappush, heappop

INF = float('inf')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().rstrip().split())
    edges[v].append((c, u))

cities = list(map(int, sys.stdin.readline().rstrip().split()))

pq = []
dist = [INF] * (N+1)
for city in cities:
    dist[city] = 0
    heappush(pq, (0, city))

while pq:
    cost, now = heappop(pq)
    if cost > dist[now]:
        continue

    for next_cost, next_city in edges[now]:
        new_cost = next_cost + cost

        if dist[next_city] > new_cost:
            dist[next_city] = new_cost
            heappush(pq, (new_cost, next_city))

max_dist = -1
city_num = -1

for i in range(1, N+1):
    if dist[i] > max_dist:
        max_dist = dist[i]
        city_num = i

print(city_num)
print(max_dist)