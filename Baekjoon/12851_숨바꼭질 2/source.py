from collections import deque

N, K = map(int, input().split())
q = deque([[N, 0]])

visited = [100000] * 100002

min_cnt = 100000
result = 0

if K < N:
    print(N-K)
    print(1)
else:
    while q:
        now, now_cnt = q.popleft()

        if now == K:
            if min_cnt == 100000 or min_cnt == now_cnt:
                result += 1
                min_cnt = now_cnt
            else:
                break

        for next in [now-1, now+1, now*2]:
            if 0 <= next <= 100001 and visited[next] >= now_cnt:
                if next == K:
                    q.append([next, now_cnt+1])
                else:
                    q.append([next, now_cnt+1])
                    visited[next] = now_cnt

    print(min_cnt)
    print(result)