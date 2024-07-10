from heapq import heappop, heappush

N, K = map(int, input().split())
adj = [list(map(int, input())) for _ in range(N)]

pq = []
INF = 21e8

distance = [[INF] * N for _ in range(K+1)]

# node, dist, potion
heappush(pq, (0, 0, 0))

while pq:
    now_node, now_dist, now_potion = heappop(pq)

    if now_dist > distance[now_potion][now_node]:
        continue

    for next_node in range(N):
        if next_node != now_node:
            if now_potion < K:
                weight = adj[now_node][next_node] / 2
                new_dist = now_dist + weight

                if new_dist < distance[now_potion+1][next_node]:
                    distance[now_potion+1][next_node] = new_dist
                    heappush(pq, (next_node, new_dist, now_potion+1))
            
            weight = adj[now_node][next_node]
            new_dist = now_dist + weight

            if new_dist < distance[now_potion][next_node]:
                distance[now_potion][next_node] = new_dist
                heappush(pq, (next_node, new_dist, now_potion))

min_dist = distance[0][1]
for i in range(1, K+1):
    min_dist = min(min_dist, distance[i][1])

print(min_dist)