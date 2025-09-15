from collections import deque

T = int(input())

for testcase in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    q = deque((priority, idx) for idx, priority in enumerate(priorities))

    count = 0
    while q:
        cur = q.popleft()
        if any(cur[0] < other[0] for other in q):
            q.append(cur)
        else:
            count += 1
            if cur[1] == M:
                print(count)
                break