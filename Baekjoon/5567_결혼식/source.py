from collections import deque

N = int(input())
M = int(input())

parent = list(range(N+1))

edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N+1)

visited[1] = True
q = deque([(1, 0)])
count = 0

while q:
    now, depth = q.popleft()

    for next in edges[now]:
        if visited[next]:
            continue
        
        if depth < 2:
            q.append((next, depth+1))
            visited[next] = True
            count += 1

print(count)