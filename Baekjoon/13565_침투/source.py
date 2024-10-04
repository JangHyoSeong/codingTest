M, N = map(int, input().split())
table = [list(input()) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

stack = []
for i in range(N):
    if table[0][i] == '0':
        stack.append([0, i])
        visited[0][i] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while stack:
    x, y = stack.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] == '0':
            if nx == M-1:
                print('YES')
                exit()
            visited[nx][ny] = True
            stack.append([nx, ny])

print('NO')
