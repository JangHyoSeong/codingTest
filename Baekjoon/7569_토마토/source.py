from collections import deque

# 입력받음
M, N, H = map(int, input().split())

tomatoes = []
# 3차원 리스트인 tomatoes를 입력받음
for _ in range(H):
    one_floor = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(one_floor)

# 3차원 이동을 위한 리스트
dh = [1, 0, 0, -1, 0, 0]
dx = [0, 1, 0, 0, -1, 0]
dy = [0, 0, 1, 0, 0, -1]

# queue를 만들고, BFS를 진행하기 위한 세팅
q = deque()
# 3차원 visited 리스트를 만듦
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

# 모든 값을 순회하면서
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 토마토가 있는 부분은 q에 삽입하고 방문 처리
            if tomatoes[i][j][k] == 1:
                q.append([i, j, k, 0])
                visited[i][j][k] = True
            # 토마토가 썩은 부분도 방문처리를 진행함(이곳으로 이동하지 않을것)
            elif tomatoes[i][j][k] == -1:
                visited[i][j][k] = True

# BFS 시작
while q:
    # day : 현재까지 경과 일수
    h, x, y, day = q.popleft()

    # 6방향으로 이동
    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
    
        # 인덱스를 벗어나지 않고 방문하지 않았다면 방문
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not visited[nh][nx][ny]:
            # 새로운 위치를 경과일수 +1 해서 queue에 삽입
            q.append([nh, nx, ny, day+1])
            # 새롭게 토마토를 생성
            tomatoes[nh][nx][ny] = 1
            # 방문 처리
            visited[nh][nx][ny] = True

# 3차원 visited 리스트를 검사하면서, 방문하지 않은 곳이 있다면 false를 리턴
# 모두 방문했다면 True 리턴
def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not visited[i][j][k]:
                    return False
    return True

# True라면, 경과일수 출력 (BFS이기에 마지막으로 나온 day는 최대 경과일수)
if check():
    print(day)
# False라면 -1 출력
else:
    print(-1)