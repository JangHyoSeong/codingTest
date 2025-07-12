import sys

V = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    node = data[0]
    idx = 1
    while data[idx] != -1:
        neighbor = data[idx]
        weight = data[idx + 1]
        graph[node].append((neighbor, weight))
        graph[neighbor].append((node, weight))

        idx += 2

def dfs(start):
    visited = [False] * (V + 1)
    distance = [0] * (V + 1)
    stack = [(start, 0)]

    while stack:
        node, dist = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        distance[node] = dist
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                stack.append((neighbor, dist + weight))
    return distance

dist = dfs(1)
farthest_node = dist.index(max(dist))

far_dist = dfs(farthest_node)
print(max(far_dist))