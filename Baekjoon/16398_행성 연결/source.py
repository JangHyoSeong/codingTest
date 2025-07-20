import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

visited = [False] * N
pq = []
heappush(pq, (0, 0))

total_cost = 0

while pq:
    cost, now = heappop(pq)

    if visited[now]:
        continue

    visited[now] = True
    total_cost += cost

    for next_node in range(N):
        if not visited[next_node]:
            heappush(pq, (graph[now][next_node], next_node))
    
print(total_cost)