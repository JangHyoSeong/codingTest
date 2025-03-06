import sys

N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

max_dist = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True

    stack = [(i, 0)]
    while stack:
        now, dist = stack.pop()
        max_dist = max(max_dist, dist)
        for next_dist, next_node in edges[now]:
            if visited[next_node]:
                continue

            stack.append((next_node, next_dist + dist))
            visited[next_node] = True

print(max_dist)