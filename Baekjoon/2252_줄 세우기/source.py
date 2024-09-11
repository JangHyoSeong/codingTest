from collections import deque

N, M = map(int, input().split())

q = deque()
inDegree = [0] * (N+1)
edge = [[] for _ in range (N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    inDegree[b] += 1

for idx in range(1, N+1):
    if inDegree[idx] == 0:
        q.append(idx)

result = []
while q:
    now_node = q.popleft()
    result.append(now_node)

    for next_node in edge[now_node]:

        inDegree[next_node] -= 1
        if inDegree[next_node] == 0:
            q.append(next_node)
            
print(" ".join(map(str, result)))