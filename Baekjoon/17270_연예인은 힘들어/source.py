from heapq import heappush, heappop

INF = int(21e8)

V, M = map(int, input().split())

edges = [[] for _ in range(V+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
J, S = map(int, input().split())

def find_min_dist(start_node):
    dist = [INF] * (V+1)
    dist[start_node] = 0

    pq = [(0, start_node)]
    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            new_dist = dist[now_node] + next_dist

            if new_dist < dist[next_node]:
                heappush(pq, (new_dist, next_node))
                dist[next_node] = new_dist
    
    return dist

J_dist = find_min_dist(J)
S_dist = find_min_dist(S)

min_dist = INF
min_dist_nodes = []

for v in range(1, V+1):

    if v not in [J, S]:
        now_dist_sum = J_dist[v] + S_dist[v]

        if min_dist > now_dist_sum:
            min_dist = now_dist_sum
            min_dist_nodes = [v]
        
        elif min_dist == now_dist_sum:
            min_dist_nodes.append(v)

min_J_dist = INF
answer_node = 0

for node in min_dist_nodes:
    if J_dist[node] > S_dist[node]:
        continue

    if min_J_dist > J_dist[node]:
        min_J_dist = J_dist[node]
        answer_node = node

print(answer_node if answer_node else -1)