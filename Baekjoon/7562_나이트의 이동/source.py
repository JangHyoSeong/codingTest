from collections import deque

T = int(input())

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for testcase in range(T):
    N = int(input())
    start= list(map(int, input().split()))
    target = list(map(int, input().split()))

    q = deque([start])
    visited = [[-1] * N for _ in range(N)]
    visited[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        if [x, y] == target:
            break
        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    print(visited[target[0]][target[1]])