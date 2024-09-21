import sys
from collections import deque

N, M = map(int, input().split())
cards = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    cards[a] += 1
    cards[b] -= 1

is_valid = [False] * (N+1)
for card in cards:
    if not is_valid[card]:
        is_valid[card] = True
    else:
        print(-1)
        exit()

print(' '.join(map(str, cards[1:])))