import sys
from heapq import heappush, heappop

INF = int(21e8)

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    n, d, c = map(int, sys.stdin.readline().rstrip().split())

    edges = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        edges[b].append((s, a))

    infected = [INF] * (n+1)
    infected[c] = 0
    pq = [(0, c)]

    while pq:
        now_time, now_node = heappop(pq)
        
        if now_time > infected[now_node]:
            continue

        for next_time, next_node in edges[now_node]:
            new_time = now_time + next_time

            if new_time < infected[next_node]:
                heappush(pq, (new_time, next_node))
                infected[next_node] = new_time
    
    count = 0
    last_infected = 0
    for i in range(1, n+1):
        if infected[i] != INF:
            count += 1
            last_infected = max(last_infected, infected[i])
    
    print(count, last_infected)