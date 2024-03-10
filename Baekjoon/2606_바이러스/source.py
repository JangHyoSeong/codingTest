num_of_computers = int(input())
N = int(input())


graph = [[] for _ in range(num_of_computers+1)]
visited = [False] * (num_of_computers+1)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1
stack = [1]
visited[1] = True

while stack:
    now = stack.pop()
    count += 1

    for i in graph[now]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True

print(count)
