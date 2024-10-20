from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)

for _ in range(M):
    arr = list(map(int, input().split()))

    for i in range(1, arr[0]):
        edges[arr[i]].append(arr[i+1])
        inDegree[arr[i+1]] += 1

q = deque()
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()

    result.append(now)

    for next in edges[now]:
        inDegree[next] -= 1

        if inDegree[next] == 0:
            q.append(next)

if len(result) != N:
    print(0)
else:
    for num in result:
        print(num)
