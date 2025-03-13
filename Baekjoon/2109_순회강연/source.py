import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort(key= lambda x : x[1])

pq = []
for p, d in arr:
    heappush(pq, p)
    if len(pq) > d:
        heappop(pq)

print(sum(pq))