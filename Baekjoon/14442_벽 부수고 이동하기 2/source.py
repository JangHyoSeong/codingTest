from collections import deque

# 입력받음
N, M, K = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]

# 각 벽 부순 횟수마다 visited배열을 만들어줌
visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 선언
visited[0][0][0] = True
q = deque([[0, 0, 0, 1]])

# 도달하지 못한다면 flag = False
flag = False

# BFS
while q:

    # popleft
    x, y, wall_count, dis = q.popleft()

    # 도착지에 도착했다면 break
    if x == N-1 and y == M-1:
        flag = True
        break

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스를 벗어나지 않는지 검사
        if 0 <= nx < N and 0 <= ny < M:
            
            # 벽 부수는 횟수가 남아있고, 벽을 만났고, 방문한적 없는 케이스라면 방문
            if wall_count < K and table[nx][ny] == 1 and not visited[wall_count+1][nx][ny]:
                visited[wall_count+1][nx][ny] = True
                q.append([nx, ny, wall_count+1, dis+1])

            # 벽을 부수지 않고, 아직 방문하지 않은 케이스라면 방문
            if table[nx][ny] == 0 and not visited[wall_count][nx][ny]:
                visited[wall_count][nx][ny] = True
                q.append([nx, ny, wall_count, dis+1])


# 출력
if flag:
    print(dis)
else:
    print(-1)