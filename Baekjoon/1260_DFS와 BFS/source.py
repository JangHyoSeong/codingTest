from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

def dfs(node, visited, result):
    visited[node] = True
    result.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited, result)

def bfs(start):
    visited = [False] * (n + 1)
    result = []
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        result.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
    return result

visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(v, visited_dfs, dfs_result)

bfs_result = bfs(v)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))