N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N+1)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        visited[i] = True

        stack = [i]
        while stack:
            now = stack.pop()

            for next in edges[now]:
                if not visited[next]:
                    stack.append(next)
                    visited[next] = True

print(count)