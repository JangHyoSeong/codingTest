import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

pq = []
for card in cards:
    heappush(pq, card)

for i in range(M):
    a, b = heappop(pq), heappop(pq)
    card_sum = a + b
    heappush(pq, card_sum)
    heappush(pq, card_sum)

print(sum(pq))