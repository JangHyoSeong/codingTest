from collections import deque

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]
for start_node in range(1, N+1):
    temp_edge = [0] + list(map(int, input().split()))
    for end_node in range(1, N+1):
        if temp_edge[end_node]:
            edges[start_node].append(end_node)
            edges[end_node].append(start_node)
    
travel = list(map(int, input().split()))

visited = [False] * (N+1)
q = deque()

q.append(travel[0])
visited[travel[0]] = True

while q:
    now_node = q.popleft()

    for next_node in edges[now_node]:
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = True

for city in travel:
    if not visited[city]:
        print('NO')
        break
else:
    print('YES')