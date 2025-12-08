import sys
from collections import deque

n, T = map(int, sys.stdin.readline().rstrip().split())
nodes = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[(x, y)] = -1

nodes[(0, 0)] = 0

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    if y == T:
        break

    for dx in range(-2, 3, 1):
        for dy in range(-2, 3, 1):
            nx, ny = x + dx, y + dy

            if nodes.get((nx, ny)) is not None:
                if nodes[(nx, ny)] == -1:
                    q.append((nx, ny))
                    nodes[(nx, ny)] = nodes[(x, y)] + 1

else:
    print(-1)
    exit()

print(nodes[(x, y)])