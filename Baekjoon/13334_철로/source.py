import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
sections = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sections.append((min(a, b), max(a, b)))

D = int(sys.stdin.readline().rstrip())

sections = [s for s in sections if s[1] - s[0] <= D]
sections.sort(key=lambda x: x[1])

count = 0
pq = []
for start, end in sections:
    while pq and pq[0] < end - D:
        heappop(pq)
    heappush(pq, start)
    count = max(count, len(pq))

print(count)