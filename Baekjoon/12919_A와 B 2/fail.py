from collections import deque

S = input()
T = input()

T_length = len(T)
visited = {}

q = deque([S])

while q:
    now = q.popleft()

    if now == T:
        print(1)
        break

    if len(now) < T_length:
        next_1 = now + 'A'
        next_2 = 'B' + now[::-1]
        if visited.get(next_1) is None:
            q.append(next_1)
            visited[next_1] = True
        if visited.get(next_2) is None:
            q.append(next_2)
            visited[next_2] = True

else:
    print(0)