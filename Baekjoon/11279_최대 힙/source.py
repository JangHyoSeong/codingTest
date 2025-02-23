import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().rstrip())

max_heap = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if max_heap:
            print(-heappop(max_heap))
        else:
            print(0)
    else:
        heappush(max_heap, -num)