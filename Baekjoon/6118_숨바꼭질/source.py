import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [-1] * (N+1)
visited[1] = 0

q = deque([1])
while q:
    now = q.popleft()

    for next in edges[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1

max_dist = 0
max_dist_idx = 0
same_dist_count = 1
for i in range(1, N+1):
    if max_dist < visited[i]:
        max_dist = visited[i]
        max_dist_idx = i
        same_dist_count = 1
    
    elif max_dist == visited[i]:
        same_dist_count += 1

print(max_dist_idx, max_dist, same_dist_count)