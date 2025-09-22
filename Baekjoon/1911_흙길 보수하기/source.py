import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
ponds = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

ponds.sort()

count = 0
last = 0
for i in range(N):
    while last < ponds[i][1]:
        count += 1
        if last < ponds[i][0]:
            last = ponds[i][0] + L
        else:
            last += L

print(count)