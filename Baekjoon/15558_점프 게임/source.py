import sys
from collections import deque

N, k = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(2)]

visited = [[False] * N for _ in range(2)]
visited[0][0] = True
q = deque([(0, 0, 0)])

while q:
    line, idx, time = q.popleft()

    for dx, dy in [(line, idx + 1), (line, idx - 1), (1 - line, idx + k)]:
        if dy >= N:
            print(1)
            exit()
        
        if dy <= time:
            continue

        if arr[dx][dy] == 0 or visited[dx][dy]:
            continue

        visited[dx][dy] = True
        q.append((dx, dy, time + 1))

print(0)