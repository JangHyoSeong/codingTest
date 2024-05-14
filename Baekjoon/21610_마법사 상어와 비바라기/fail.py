N, M = map(int, input().split())
bucket = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for command in range(M):
    dir, length = commands[command]
    
    clouds = []
    
    if command == 0:
        clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
        clouds_before = []
        
    else:
        for i in range(N):
            for j in range(N):
                if bucket[i][j] >= 2 and [i, j] not in clouds_before:
                    clouds.append([i, j])
                    bucket[i][j] -= 2
    clouds_before = []      
    clouds_num = len(clouds)
    for idx in range(clouds_num):
        nx = clouds[idx][0] + dx[dir] * length
        ny = clouds[idx][1] + dy[dir] * length
        
        nx %= N
        ny %= N
        
        bucket[nx][ny] += 1
        
        clouds_before.append([nx, ny])
    
    for idx in range(clouds_num):
        x, y = clouds_before[idx]
        
        for i in [-1, 1]:
            for j in [-1, 1]:
                if 0 <= x+i < N and 0 <= y+j < N and bucket[x+i][y+j] > 0:
                    bucket[x][y] += 1
                    
water_sum = 0
for i in range(N):
    for j in range(N):
        if bucket[i][j] >= 2 and [i, j] not in clouds_before:
            bucket[i][j] -= 2
        
        water_sum += bucket[i][j]
        
print(water_sum)