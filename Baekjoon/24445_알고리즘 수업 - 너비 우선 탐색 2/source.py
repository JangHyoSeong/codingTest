import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, N+1):
    edges[i].sort(reverse=True)

q = deque([R])
visited = [0] * (N + 1)
visited[R] = 1

count = 1
while q:
    now = q.popleft()

    for next_node in edges[now]:
        if not visited[next_node]:
            count += 1
            q.append(next_node)
            visited[next_node] = count

for i in range(1, N+1):
    print(visited[i])