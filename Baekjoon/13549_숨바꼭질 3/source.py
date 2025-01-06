from collections import deque

N, K = map(int, input().split())

visited = [-1] * (100001)
visited[N] = 0

q = deque([N])

while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break

    if 0 <= now * 2 < 100001 and visited[now * 2] == -1:
        q.appendleft(now * 2)
        visited[now * 2] = visited[now]

    for next in (now-1, now+1):
        if 0 <= next < 100001 and visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1