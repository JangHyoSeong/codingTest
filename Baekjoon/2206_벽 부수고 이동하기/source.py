from collections import deque

N, M = map(int, input().split())

table = [list(map(int, input())) for _ in range(N)]

# 벽을 부수고 이동했을 때, 부수지 않고 이동했을 때 두 경우를 나누어 visited 배열 선언
# 두 경우를 나누지 않는다면 제대로 값이 구해지지 않음
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# q에는 현재 위치, 벽을 부쉈는지 여부를 삽입
q = deque([(0, 0, False)])
# 시작위치의 방문처리
visited[0][0] = [1, 1]

# 델타 탐색을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS 시작
while q:
    x, y, is_break = q.popleft()
    
    # 도착한다면 종료
    if x == N-1 and y == M-1:
        break
    
    # 4방향으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 인덱스를 벗어나지 않는다면
        if 0 <= nx < N and 0 <= ny < M:
            
            # 만약 이미 벽을 부수고 이동중이라면
            if is_break:
                # visited[][][1]를 통해 방문 여부 결정
                # 아직 방문하지 않았고 이동가능하다면 Q에 삽입
                if not visited[nx][ny][1] and table[nx][ny] == 0:
                    q.append((nx, ny, True))
                    # 방문 처리를 통해 이동 거리 저장
                    visited[nx][ny][1] = visited[x][y][1] + 1
            # 아직 벽을 부수고 이동하지 않았다면
            else:
                # 벽이없고 방문하지 않았다면 이동
                if table[nx][ny] == 0 and not visited[nx][ny][0]:
                    q.append((nx, ny, False))
                    visited[nx][ny][0] = visited[x][y][0] + 1
                # 벽이 있고 방문하지 않았다면 벽을 부수고 이동
                elif table[nx][ny] == 1 and not visited[nx][ny][1]:
                    q.append((nx, ny, True))
                    visited[nx][ny][1] = visited[x][y][0] + 1
            

# 만약 도착점에 도착하지 못했다면 -1출력
if visited[N-1][M-1] == [0,0]:
    print(-1)
    
# 결과에 0이 있다면 다른 값을 출력
# 둘 다 도착했다면 더 작은 값을 출력
else:
    if visited[N-1][M-1][0] == 0:
        print(visited[N-1][M-1][1])
    elif visited[N-1][M-1][1] == 0:
        print(visited[N-1][M-1][0])
    else:
        print(min(visited[N-1][M-1]))