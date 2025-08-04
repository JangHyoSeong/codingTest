import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
small_stones = set()
for _ in range(M):
    stone = int(sys.stdin.readline().rstrip())
    small_stones.add(stone)

if 2 in small_stones:
    print(-1)
    exit()

dp = [[False] * (142) for _ in range(N+1)]
dp[2][1] = True

q = deque([(2, 1, 1)])

result = -1
while q:
    pos, speed, count = q.popleft()

    if pos == N:
        result = count
        break

    for next_speed in [speed-1, speed, speed+1]:
        if next_speed < 1:
            continue

        next_pos = pos + next_speed
        if next_pos > N or next_pos in small_stones:
            continue

        if not dp[next_pos][next_speed]:
            dp[next_pos][next_speed] = True
            q.append((next_pos, next_speed, count + 1))

print(result)