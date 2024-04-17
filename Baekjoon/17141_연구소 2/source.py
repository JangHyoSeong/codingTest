from itertools import combinations
from collections import deque

def check_time(N):
    temp_max = 0
    for i in range(N):
        for j in range(N):
            if temp_max < visited[i][j]:
                temp_max = visited[i][j]
            elif visited[i][j] == -1:
                return -1
    
    return temp_max


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

can_virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            can_virus.append([i, j])

virus_comb = list(combinations(can_virus, M))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

min_time = N * N
can_make = False

for case in virus_comb:

    visited = [[-1] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 1:
                visited[i][j] = 0
                
    q = deque(case)
    flag = False
    
    for x, y in case:
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        if flag:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and lab[nx][ny] != 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > min_time:
                    flag = True

    if flag:
        continue
    
    temp_max = check_time(N)

    if temp_max < min_time and temp_max != -1:
        min_time = temp_max
        can_make = True

if can_make:
    print(min_time)
else:
    print(-1)