from collections import deque

N, K = map(int, input().split())

q = deque([(N, 0)])
visited = [False] * (100002)
visited[N] = True

while q:
    now, count = q.popleft()
    if now == K:
        print(count)
        break

    for next in [now-1, now+1, now*2]:
        if 0 <= next <= 100001 and not visited[next]:
            q.append((next, count+1))
            visited[next] = True
