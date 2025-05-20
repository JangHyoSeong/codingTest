import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[b].append(a)

max_count = 0
result = []
for i in range(1, N+1):
    visited = [False] * (N + 1)

    count = 1
    stack = [i]
    visited[i] = True

    while stack:
        now = stack.pop()

        for next in edges[now]:
            if not visited[next]:
                count += 1
                stack.append(next)
                visited[next] = True
    
    if max_count < count:
        result = [i]
        max_count = count
    
    elif max_count == count:
        result.append(i)

print(" ".join(map(str, result)))