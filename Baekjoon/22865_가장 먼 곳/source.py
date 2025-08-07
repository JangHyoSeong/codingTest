import sys
from heapq import heappush, heappop

INF = int(21e8)

N = int(sys.stdin.readline().rstrip())
A, B, C = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    D, E, length = map(int, sys.stdin.readline().rstrip().split())
    edges[D].append((length, E))
    edges[E].append((length, D))

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, node = heappop(pq)
        if now_dist > dist[node]:
            continue

        for next_dist, next_node in edges[node]:
            new_dist = now_dist + next_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    
    return dist

dist_A = dijkstra(A)
dist_B = dijkstra(B)
dist_C = dijkstra(C)

answer = -1
max_min_dist = -1

for i in range(1, N+1):
    min_dist = min(dist_A[i], dist_B[i], dist_C[i])
    if min_dist > max_min_dist:
        max_min_dist = min_dist
        answer = i

    elif min_dist == max_min_dist and i < answer:
        answer = i

print(answer)