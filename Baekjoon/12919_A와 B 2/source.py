from collections import deque

S = input()
T = input()

S_length = len(S)
visited = {}

q = deque([T])

while q:
    now = q.popleft()

    if now == S:
        print(1)
        break

    if len(now) > S_length:
        if now[-1] == 'A':
            next = now[:-1]
            if visited.get(next) is None:
                q.append(next)
                visited[next] = True
        
        if now[0] == 'B':
            next = now[:0:-1]
            q.append(next)
            visited[next] = True


else:
    print(0)