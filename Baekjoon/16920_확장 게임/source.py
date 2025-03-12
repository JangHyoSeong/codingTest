from collections import deque

N, M, P = map(int, input().split())
move_dist = [0] + list(map(int, input().split()))

table = [list(input().strip()) for _ in range(N)]
castles = [deque() for _ in range(P+1)]

for i in range(N):
    for j in range(M):
        if table[i][j] not in  [".", "#"]:
            castles[int(table[i][j])].append((i,j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while any(castles[i] for i in range(1, P+1)):
    for player in range(1, P+1):
        if not castles[player]:
            continue

        q = castles[player]
        steps = move_dist[player]
        new_castles = deque()

        for _ in range(steps):
            if not q:
                break

            for _ in range(len(q)):
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == ".":
                        table[nx][ny] = str(player)
                        new_castles.append((nx, ny))

            q.extend(new_castles)
            new_castles.clear()

result = [0] * (P+1)
for i in range(N):
    for j in range(M):
        if table[i][j].isdigit():
            result[int(table[i][j])] += 1

print(" ".join(map(str, result[1:])))