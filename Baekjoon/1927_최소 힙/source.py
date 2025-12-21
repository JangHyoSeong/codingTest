import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())

pq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if pq:
            print(heappop(pq))
        else:
            print(0)
    
    else:
        heappush(pq, x)