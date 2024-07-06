from collections import deque

N = int(input())
start_x, start_y, target_x, target_y = map(int, input().split())

moves = [
    (-2, -1),
    (-2, 1),
    (0, -2),
    (0, 2),
    (2, -1),
    (2, 1)
]

q = deque()
q.append((start_x, start_y, 0))

visited = [[False] * N for _ in range(N)]
visited[start_x][start_y] = True

while q:
    x, y, count = q.popleft()

    if x == target_x and y == target_y:
        print(count)
        break

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

else:
    print(-1)