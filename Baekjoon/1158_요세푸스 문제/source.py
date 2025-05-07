from collections import deque

N, K = map(int, input().split())

q = deque(range(1, N+1))

count = 0
result = []
while q:
    temp = q.popleft()
    count += 1

    if count == K:
        result.append(temp)
        count = 0
    else:
        q.append(temp)

print("<" + ", ".join(map(str, result)) + ">")