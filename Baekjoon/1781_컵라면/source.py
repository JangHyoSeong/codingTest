from heapq import heappush, heappop

N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]

problems.sort(key= lambda x : (x[0], -x[1]))

pq = []
day = 0

for problem in problems:
    heappush(pq, problem[1])
    day += 1

    if day > problem[0]:
        heappop(pq)
        day -= 1

print(sum(pq))