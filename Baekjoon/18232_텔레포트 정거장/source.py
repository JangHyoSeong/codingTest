import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
S, E = map(int, sys.stdin.readline().rstrip().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)

q = deque()
q.append(S)

visited = [-1] * (N+1)
visited[S] = 0

while q:
    now = q.popleft()

    for next in edges[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if next == E:
                print(visited[next])
                break
    
    for dx in [-1, 1]:
        next = now + dx

        if 1 <= next <= N and visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if next == E:
                print(visited[next])
                break