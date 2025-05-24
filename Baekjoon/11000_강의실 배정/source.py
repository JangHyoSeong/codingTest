import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort(key= lambda x : x)

pq = []
for s, t in arr:
    if pq and pq[0] <= s:
        heappop(pq)
    
    heappush(pq, t)

print(len(pq))