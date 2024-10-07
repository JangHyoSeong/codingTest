from heapq import heappop, heappush

N, M, t = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

total_cost = 0
visited = [False] * (N+1)
heap = []
visited_cities = 1
current_increase = 0

visited[1] = True
for cost, next in edges[1]:
    heappush(heap, (cost, next))

while visited_cities < N:
    cost, city = heappop(heap)

    if visited[city]:
        continue

    total_cost += cost + current_increase
    visited[city] = True
    visited_cities += 1
    current_increase += t

    for next_cost, next in edges[city]:
        if not visited[next]:
            heappush(heap, (next_cost, next))

print(total_cost)