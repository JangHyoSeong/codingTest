from collections import deque

N, K = map(int, input().split())
ponds = list(map(int, input().split()))

visited = set(ponds)
q = deque()

for pond in ponds:
    q.append((pond, 0))

house_count = 0
total_unhappiness = 0

while house_count < K:
    current_pos, current_dist = q.popleft()

    for next_pos in [current_pos - 1, current_pos + 1]:
        if next_pos not in visited:
            visited.add(next_pos)
            total_unhappiness += current_dist + 1
            house_count += 1

            if house_count == K:
                break

            q.append((next_pos, current_dist + 1))

print(total_unhappiness)