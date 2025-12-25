import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    visited = [-1] * (N+1)
    visited[a] = 0

    q = deque()
    q.append(a)

    while q:
        now = q.popleft()

        for next_dist, next_node in edges[now]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now] + next_dist
                if next_node == b:
                    q = deque()
                    break
                q.append(next_node)
    
    print(visited[b])