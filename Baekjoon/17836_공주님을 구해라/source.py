from collections import deque

N, M, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([(0, 0, False)])

while queue:
    x, y, gram = queue.popleft()
    time = visited[x][y][1 if gram else 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if table[nx][ny] != 1 or gram:
                new_time = time + 1

                if table[nx][ny] == 2 and not gram:
                    if new_time < visited[nx][ny][1]:
                        visited[nx][ny][1] = new_time
                        queue.append((nx, ny, True))

                elif gram and new_time < visited[nx][ny][1]:
                    visited[nx][ny][1] = new_time
                    queue.append((nx, ny, True))
                
                elif not gram and new_time < visited[nx][ny][0]:
                    visited[nx][ny][0] = new_time
                    queue.append((nx, ny, False))

result = min(visited[N-1][M-1])
if result <= T:
    print(result)
else:
    print("Fail")
