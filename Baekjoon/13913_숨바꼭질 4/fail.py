from collections import deque

N, K = map(int, input().split())
min_cnt = 21e8
result = []
visited = {}
q = deque()

q.append([N, 0, [N]])

while q:
    N, cnt, footprints = q.popleft()
    new_footprints = footprints[:]

    if visited.get(N) is None:
        visited[N] = cnt
    else:
        continue

    if cnt > min_cnt:
        continue
    if N < 0:
        continue

    if N == K:
        if min_cnt > cnt:
            min_cnt = cnt
            result = footprints

    elif N > K:
        q.append([N-1, cnt+1, footprints + [N-1]])

    else:
        q.append([N*2, cnt+1, footprints + [N*2]])
        q.append([N+1, cnt+1, footprints + [N+1]])
        q.append([N-1, cnt+1, footprints + [N-1]])

print(min_cnt)
print(' '.join(map(str, result)))