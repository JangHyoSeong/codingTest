from  heapq import heappop, heappush

N, M = map(int, input().split())
arr = list(map(int, input().split()))


pq = []
upset = 0
count = 0
for i in range(N):
    heappush(pq, (-arr[i]))

    upset += arr[i]
    if upset >= M:
        if pq:
            num = -heappop(pq)
        upset -= num * 2
        count += 1

print(count)