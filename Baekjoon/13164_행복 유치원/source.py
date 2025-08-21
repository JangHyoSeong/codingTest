import sys
from heapq import heapify, heappop

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

gaps = [-(arr[i+1] - arr[i]) for i in range(N-1)]
heapify(gaps)

for _ in range(K-1):
    heappop(gaps)

print(-sum(gaps))