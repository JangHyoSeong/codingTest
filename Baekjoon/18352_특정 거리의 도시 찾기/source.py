from collections import deque

N, M, K, X = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)

min_range = [float('inf')] * (N+1)
min_range[X] = 0

q = deque()
q.append([X, 0])

result = []

while q:
    now_node, count = q.popleft()

    for next_node in edge[now_node]:

        if count+1 < min_range[next_node]:
            min_range[next_node] = count+1
            if count+1 == K:
                result.append(next_node)
            elif count+1 < K:
                q.append([next_node, count+1])

result.sort()
if result:
    for node in result:
        print(node)
else:
    print(-1)