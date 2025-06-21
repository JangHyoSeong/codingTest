import sys
from heapq import heappush, heappop

def dijkstra(start, n, graph):
    dist = [int(21e8)] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heappop(heap)
        if cost > dist[now]:
            continue
        for weight, nxt in graph[now]:
            if dist[nxt] > cost + weight:
                dist[nxt] = cost + weight
                heappush(heap, (cost + weight, nxt))
    return dist

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N, M, T = map(int, sys.stdin.readline().rstrip().split())
    S, G, H = map(int, sys.stdin.readline().rstrip().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        edges[a].append((d, b))
        edges[b].append((d, a))
    
    destinations = []
    for _ in range(T):
        x = int(sys.stdin.readline().rstrip())
        destinations.append(x)
    
    dist_s = dijkstra(S, N, edges)
    dist_g = dijkstra(G, N, edges)
    dist_h = dijkstra(H, N, edges)

    answer = []

    for destination in destinations:
        route1 = dist_s[G] + dist_g[H] + dist_h[destination]
        route2 = dist_s[H] + dist_h[G] + dist_g[destination]

        if dist_s[destination] == route1 or dist_s[destination] == route2:
            answer.append(destination)
    
    print(" ".join(map(str, sorted(answer))))