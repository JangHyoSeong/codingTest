import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    edges[u].append((w, v))

start, end = map(int, sys.stdin.readline().rstrip().split())

INF = int(21e8)
dist = [INF] * (N+1)
parent = [-1] * (N+1)

pq = []
heappush(pq, (0, start))
dist[start] = 0

while pq:
    now_dist, now_node = heappop(pq)

    if dist[now_node] < now_dist:
        continue

    for next_dist, next_node in edges[now_node]:
        
        new_dist = next_dist + dist[now_node]
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            parent[next_node] = now_node
            heappush(pq, (new_dist, next_node))

print(dist[end])

path = []
node = end
while node != -1:
    path.append(node)
    node = parent[node]

path.reverse()
print(len(path))
print(" ".join(map(str, path)))