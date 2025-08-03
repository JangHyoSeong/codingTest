import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)

sockets = [0] * M
idx = 0
for i in range(N):
    if idx == 0:
        sockets[idx] += arr[i]
        idx = (idx + 1) % M
        continue

    sockets[idx] += arr[i]
    if sockets[idx] == sockets[idx - 1]:
        idx = (idx + 1) % M

print(sockets[0])