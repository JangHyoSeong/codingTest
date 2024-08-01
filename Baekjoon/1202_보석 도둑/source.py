from sys import stdin
from heapq import heappush, heappop

N, K = map(int, stdin.readline().rstrip().split())
jewels = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
bags = []
for _ in range(K):
    bags.append(int(stdin.readline().rstrip()))

bags.sort()
jewels.sort(key=lambda x : x[0])

pq = []
result = 0

jewel_idx = 0
for bag in bags:
    while jewel_idx < N:
        if bag >= jewels[jewel_idx][0]:
            heappush(pq, -jewels[jewel_idx][1])
            jewel_idx += 1
        else:
            break
    if pq:
        result -= heappop(pq)
    
print(result)