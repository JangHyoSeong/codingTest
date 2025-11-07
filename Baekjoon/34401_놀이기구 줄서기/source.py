import sys
from collections import deque
from heapq import heappush, heappop

N, P, K = map(int, sys.stdin.readline().rstrip().split())
groups = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
groups.sort(key=lambda x : x[0])

q = deque()
pq = []

now_time = 0
end_idx = 0
end_teams = 0
answer = 0

while end_teams < N:

    if not q and not pq and end_idx < N:
        if now_time < groups[end_idx][0]:
            now_time = groups[end_idx][0]
            if now_time % P != 0:
                now_time = (now_time // P+1) * P
    
    while end_idx < N and groups[end_idx][0] <= now_time:
        q.append(groups[end_idx])
        end_idx += 1

    capacity = K

    while pq and capacity > 0:
        a, t = pq[0]

        if a <= capacity:
            heappop(pq)
            capacity -= a
            answer += (now_time - t)
            end_teams += 1
        else:
            break
    
    while q and capacity > 0:
        t, a = q.popleft()
        if a <= capacity:
            capacity -= a
            answer += (now_time - t)
            end_teams += 1
        
        else:
            heappush(pq, (a, t))
    
    now_time += P

print(answer)