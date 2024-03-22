from copy import deepcopy

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
route = []
for _ in range(M):
    x, y = map(int, input().split())
    route.append([x-1, y-1])

visited = [[False * N] for _ in range(N)]
valid = [False] * M
valid[0] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, visited, valid):

    now_visited = deepcopy(visited)
    now_visited[x][y] = True


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] != 1 and not visited[nx][ny]:
            DFS(nx, ny, now_visited)


