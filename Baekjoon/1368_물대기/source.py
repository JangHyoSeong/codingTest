from heapq import heappush, heappop

N = int(input())
W = [int(input()) for _ in range(N)]
table = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N

pq = []

for i in range(N):
    heappush(pq, (W[i], i))

answer = 0
count = 0

while pq and count < N:
    cost, u = heappop(pq)
    if visited[u]:
        continue

    visited[u] = True
    answer += cost
    count += 1

    for v in range(N):
        if not visited[v]:
            heappush(pq, (table[u][v], v))

print(answer)