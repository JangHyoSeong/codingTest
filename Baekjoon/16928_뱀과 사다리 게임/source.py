from collections import deque

N, M = map(int, input().split())

ladders = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

snakes = {}
for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

visited = [False] * 101
q = deque([[1, 0]])

visited[1] = True

while q:
    now, count = q.popleft()

    if now == 100:
        print(count)
        break

    for move in range(1, 7):
        next = now + move
        if next <= 100 and not visited[next]:
            visited[next] = True
            if ladders.get(next) is not None:
                visited[ladders[next]] = True
                q.append([ladders[next], count+1])
            
            elif snakes.get(next) is not None:
                visited[snakes[next]] = True
                q.append([snakes[next], count+1])
            
            else:
                q.append([next, count+1])
