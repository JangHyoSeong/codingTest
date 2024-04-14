from collections import deque

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

def find_shark():
    # 상어의 위치를 찾음
    for i in range(N):
        for j in range(N):
            if table[i][j] == 9:
                # 상어가 있던 위치는 0으로 초기화
                table[i][j] = 0
                # 현재 위치, 현재 크기, 먹은 물고기 수
                return [i, j, 2, 0]
shark = find_shark()

# 동서남북 한칸씩 이동하기 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 상어의 초기위치를 deque에 삽입, 물고기를 먹기까지의 이동횟수가 됨
q = deque([(shark[0], shark[1], 0)])

# 총 이동횟수
count = 0
# 방문 여부를 나타내는 리스트   
visited = [[False] * N for _ in range(N)]
visited[shark[0]][shark[1]] = True

# 현재 같은 거리에 있고, 먹을 수 있는 물고기 정보를 저장할 리스트
can_eat = []

# BFS
while q or can_eat:
    # 현재위치, 현재 먹기까지 이동횟수
    if q:
        x, y, temp_count = q.popleft()

    # 만약 먹을 수 있는 물고기가 있다면
    # 그 물고기를 먹기까지의 거리가 현재 이동거리보다 짧다면
    # 혹은 q가 비어서 더이상 이동할 곳이 없는데 먹을 물고기가 있다면
    if can_eat and (can_eat[0][2] < temp_count or q == deque()):
        # 먹는 로직을 수행할것임
        # 일단 먹을 수 있는 물고기중 하나를 빼서 먹을 물고기로 저장
        left_top = can_eat.pop()

        # 먹을 수 있는 물고기를 모두 순회하면서
        while can_eat:
            # 맨 위 왼쪽에 있는 물고기를 left_top에 저장
            temp_eat = can_eat.pop()
            if left_top[0] > temp_eat[0]:
                left_top = temp_eat
            elif left_top[0] == temp_eat[0]:
                if left_top[1] > temp_eat[1]:
                    left_top = temp_eat
        
        
        # 먹을 물고기를 정하고 나면, 그 위치를 0으로 초기화
        table[left_top[0]][left_top[1]] = 0

        # 하나 먹음
        shark[3] += 1
        
        # 먹어서 현재 사이즈와 같아졌다면 사이즈를 증가하고, 먹은 숫자를 0으로 초기화
        if shark[3] == shark[2]:
            shark[2] += 1
            shark[3] = 0

        # q를 현재위치부터 다시 시작
        q = deque([(left_top[0], left_top[1], 0)])
        
        # 현재 물고기를 먹기까지의 이동 횟수를 총 이동횟수에 더해줌
        count += left_top[2]
        # 방문 여부 리스트 다시 초기화
        visited = [[False] * N for _ in range(N)]
        visited[left_top[0]][left_top[1]] = True
        continue

    # 현재 위치가 먹을 수 있는 물고기라면 can_eat에 넣어줌
    if table[x][y] != 0 and table[x][y] < shark[2]:
        can_eat.append([x, y, temp_count])


    # 다음 위치로 탐색을 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 방문 가능한 위치면 q에 삽입
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if table[nx][ny] <= shark[2]:
                q.append((nx, ny, temp_count+1))
                visited[nx][ny] = True

print(count)