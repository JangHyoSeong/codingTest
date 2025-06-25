from collections import deque

T = int(input())
for testcase in range(T):
    M, N, K = map(int, input().split())
    table = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        table[y][x] = True

    count = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(M):
            if not table[i][j]:
                continue

            table[i][j] = False
            count += 1
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    if 0 <= nx < N and 0 <= ny < M and table[nx][ny]:
                        q.append((nx, ny))
                        table[nx][ny] = False
    print(count)