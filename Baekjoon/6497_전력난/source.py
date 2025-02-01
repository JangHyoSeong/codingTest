import sys
from heapq import heappop, heappush

while True:
    M, N = map(int, sys.stdin.readline().rstrip().split())
    if M == 0 and N == 0:
        break

    edges = [[] for _ in range(M)]
    total_weight = 0

    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        edges[x].append((z, y))
        edges[y].append((z, x))
        total_weight += z

    visited = [False] * M
    pq = [(0, 0)]
    min_weight = 0

    while pq:
        weight, u = heappop(pq)

        if visited[u]:
            continue
        visited[u] = True
        min_weight += weight

        for w, v in edges[u]:
            if not visited[v]:
                heappush(pq, (w, v))

    print(total_weight - min_weight)