from collections import deque

board = [list(input()) for _ in range(8)]

walls = set()
for i in range(8):
    for j in range(8):
        if board[i][j] == "#":
            walls.add((i, j))

q = deque()
q.append((7, 0))

while True:

    visited = [[False] * 8 for _ in range(8)]
    new_q = deque()

    while q:
        x, y = q.popleft()
        
        if (x, y) in walls:
            continue

        if x == 0 and y == 7:
            print(1)
            exit()

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:
                    if (nx, ny) not in walls:
                        new_q.append((nx, ny))
                        visited[nx][ny] = True
    q = new_q
    if not new_q:
        break
    
    new_walls = set()

    for wall in walls:
        if wall[0] == 7:
            continue

        new_walls.add((wall[0]+1, wall[1]))
    walls = new_walls

print(0)