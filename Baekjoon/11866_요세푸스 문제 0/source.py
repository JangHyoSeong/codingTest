from collections import deque

N, K = map(int, input().split())
q = deque(list(range(1, N+1)))

result = []
while q:
    q.rotate(-(K-1))
    result.append(q.popleft())

print("<" + ", ".join(map(str, result)) + ">")