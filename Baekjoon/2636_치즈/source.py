from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0
prev_cheese_count = 0

while True:
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    cheese_positions = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if table[nx][ny] == 1:
                    cheese_positions.append((nx, ny))
                else:
                    queue.append((nx, ny))
    
    if not cheese_positions:
        print(time)
        print(prev_cheese_count)
        break
    
    prev_cheese_count = len(cheese_positions)
    for x, y in cheese_positions:
        table[x][y] = 0
    
    time += 1