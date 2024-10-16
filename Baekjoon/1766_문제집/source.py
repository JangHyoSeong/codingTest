from heapq import heappush, heappop

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    inDegree[b] += 1

for i in range(1, N+1):
    if edges[i]:
        edges[i].sort()

pq = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        heappush(pq, i)

result = []
while pq:
    now = heappop(pq)

    result.append(now)

    for next in edges[now]:
        inDegree[next] -= 1

        if inDegree[next] == 0:
            heappush(pq, next)

print(" ".join(map(str, result)))