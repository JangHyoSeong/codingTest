from heapq import heappop, heappush

N = int(input())
pq = []
for _ in range(N):
    heappush(pq, int(input()))

num_of_cards = N
count = 0
while num_of_cards > 1:
    a, b = heappop(pq), heappop(pq)

    count += a+b
    heappush(pq, a+b)
    num_of_cards -= 1

print(count)