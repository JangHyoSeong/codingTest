import sys
from collections import deque

L, N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

q = deque()
for pos in arr:
    q.append((pos, 0))

visited = set(arr)
count = 0

while q:

    if count == K:
        break

    now_pos, dist = q.popleft()
    print(dist)

    for d in [1, -1]:
        next_pos = now_pos + d

        if 0 <= next_pos <= L and next_pos not in visited:
            q.append((next_pos, dist + 1))
            visited.add(next_pos)
    
    count += 1