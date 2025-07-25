import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
lectures = []

for _ in range(N):
    num, start, end = map(int, sys.stdin.readline().rstrip().split())
    lectures.append((start, end))

lectures.sort()
pq = []

for start, end in lectures:
    if pq and pq[0] <= start:
        heappop(pq)
    
    heappush(pq, end)

print(len(pq))