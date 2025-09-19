from collections import deque

N = int(input())

build_time = [0] * (N + 1)
total_time = [0] * (N + 1)
indegree = [0] * (N+1)
result = [0] * (N+1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N+1):
    time, *arr = list(map(int, input().split()))
    build_time[i] = time

    for prev in arr[:-1]:
        graph[prev].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        total_time[i] = build_time[i]

while q:
    now = q.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        total_time[next] = max(total_time[next], total_time[now] + build_time[next])

        if indegree[next] == 0:
            q.append(next)

for i in range(1, N+1):
    print(total_time[i])