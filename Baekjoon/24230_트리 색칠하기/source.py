import sys

N = int(sys.stdin.readline().rstrip())
colors = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N+1)
visited[1] = True

count = 0

if colors[1] != 0:
    count += 1
stack = [1]

while stack:
    now_node = stack.pop()

    for next_node in edges[now_node]:
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
            if colors[next_node] != colors[now_node]:
                count += 1

print(count)