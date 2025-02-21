from collections import deque

N = int(input())
visited = [-1] * (N+1)
visited[N] = 0

q = deque([N])

while q:
    now = q.popleft()

    if now == 1:
        break

    if now == 0:
        continue

    if now % 3 == 0:
        next = now // 3
        if visited[next] == -1:
            q.append(next)
            visited[next] = now

    if now % 2 == 0:
        next = now // 2
        if visited[next] == -1:
            q.append(next)
            visited[next] = now
    
    next = now - 1
    if visited[next] == -1:
        q.append(next)
        visited[next] = now

count = -1
now = 1
result = []
while visited[now] != -1:
    count += 1
    result.append(now)
    now = visited[now]

print(count)
print(" ".join(map(str, reversed(result))))