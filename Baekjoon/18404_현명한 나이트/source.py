from collections import deque

N, M = map(int, input().split())
X, Y = map(int, input().split())
targets = [list(map(int, input().split())) for _ in range(M)]

move_table = [[21e8] * N for _ in range(N)]
move_table[X-1][Y-1] = 0

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

q = deque([(X-1, Y-1)])
while q:
    x, y = q.popleft()

    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < N and 0 <= ny < N and move_table[nx][ny] > move_table[x][y] + 1:
            move_table[nx][ny] = move_table[x][y] + 1
            q.append((nx, ny))

for target in targets:
    print(move_table[target[0]-1][target[1]-1], end=" ")
