from heapq import heappop, heappush

N = int(input())
M = int(input())

INF = 21e8

edges = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append([cost, end])

start, end = map(int, input().split())

pq = [(0, start)]
cost = [INF] * (N+1)
cost[start] = 0

while pq:
    now_cost, now_node = heappop(pq)

    if now_cost > cost[now_node]:
        continue

    for edge in edges[now_node]:
        next_cost, next_node = edge
        temp_sum_cost = now_cost + next_cost

        if temp_sum_cost < cost[next_node]:
            cost[next_node] = temp_sum_cost
            heappush(pq, [temp_sum_cost, next_node])

print(cost[end])