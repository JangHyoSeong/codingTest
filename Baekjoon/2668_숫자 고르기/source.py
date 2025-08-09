N = int(input())

arr = [0]
for _ in range(N):
    num = int(input())
    arr.append(num)

visited = [False] * (N + 1)
cycle = set()

def dfs(start: int, current: int, path: list):
    visited[current] = True
    path.append(current)
    next_node = arr[current]

    if not visited[next_node]:
        dfs(start, next_node, path)
    
    else:
        if next_node in path:
            idx = path.index(next_node)
            for node in path[idx:]:
                cycle.add(node)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i, i, [])

print(len(cycle))
for num in sorted(cycle):
    print(num)