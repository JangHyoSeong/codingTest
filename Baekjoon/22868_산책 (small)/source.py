import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

S, E = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, N+1):
    edges[i].sort()


visited = [0] * (N+1)
q = deque([(S, 0)])
visited[S] = -1

while q:
    now, dist = q.popleft()
    if now == E:
        break

    for next_node in edges[now]:
        if not visited[next_node]:
            visited[next_node] = now
            q.append((next_node, dist + 1))
    
result = dist

now_node = E
blocked_node = set()

while now_node != S:
    before_node = visited[now_node]
    blocked_node.add(now_node)
    now_node = before_node

visited = [False] * (N+1)
q = deque([(E, 0)])
visited[E] = True

while q:
    now, dist = q.popleft()

    if now == S:
        break

    for next_node in edges[now]:
        if not visited[next_node] and next_node not in blocked_node:
            visited[next_node] = True
            q.append((next_node, dist + 1))

result += dist
print(result)