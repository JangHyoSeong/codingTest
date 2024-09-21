import sys
from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)

    for next in edges[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            q.append(next)

if len(result) == N:
    print(' '.join(map(str, result)))
else:
    print(-1)