from collections import deque

def bfs_escape(R, C, maze):
    fire_time = [[-1] * C for _ in range(R)]
    jihun_time = [[-1] * C for _ in range(R)]
    fire_queue = deque()
    jihun_queue = deque()

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire_queue.append((i, j))
                fire_time[i][j] = 0
            elif maze[i][j] == 'J':
                jihun_queue.append((i, j))
                jihun_time[i][j] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fire_queue:
        x, y = fire_queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and fire_time[nx][ny] == -1 and maze[nx][ny] == '.':
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

    while jihun_queue:
        x, y = jihun_queue.popleft()

        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return jihun_time[x][y] + 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and jihun_time[nx][ny] == -1 and maze[nx][ny] == '.':
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))

    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [input().strip() for _ in range(R)]

print(bfs_escape(R, C, maze))