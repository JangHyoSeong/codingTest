from collections import deque

T = int(input())

for testcase in range(T):
    h, w = map(int, input().split())
    table = [list(input()) for _ in range(h)]

    h += 2
    w += 2

    new_table = [['.'] * w for _ in range(h)]
    for i in range(1, h-1):
        for j in range(1, w-1):
            new_table[i][j] = table[i-1][j-1]
    

    keys = set(input())
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * w for _ in range(h)]
    q = deque([(0, 0)])
    visited[0][0] = True

    doors = {chr(c): [] for c in range(ord('A'), ord('Z') + 1)}

    count = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                cell = new_table[nx][ny]

                if cell == '*':
                    continue

                visited[nx][ny] = True

                if cell == '.':
                    q.append((nx, ny))
                
                elif cell == '$':
                    q.append((nx, ny))
                    count += 1

                elif 'a' <= cell <= 'z':
                    if cell not in keys:
                        keys.add(cell)
                        door_char = cell.upper()
                        while doors[door_char]:
                            q.append((doors[door_char].pop()))
                    
                    q.append((nx, ny))
                
                elif 'A' <= cell <= 'Z':
                    if cell.lower() in keys:
                        q.append((nx, ny))
                    else:
                        doors[cell].append((nx, ny))
    print(count)