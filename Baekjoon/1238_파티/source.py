from heapq import heappop, heappush
INF = 21e8

def dijkstra(start, target):

    distance = [INF] * (N+1)
    distance[start] = 0
    
    pq = []
    heappush(pq, (0, start))
    
    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for to in graph[now]:
            next_node, next_dist = to[0], to[1]
            new_dist = next_dist + dist
            
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return distance[target]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

max_time = 0
for i in range(1, N+1):
    temp_time_go = dijkstra(i, X)
    temp_time_back = dijkstra(X, i)

    max_time = max(max_time, temp_time_back + temp_time_go)

print(max_time)