from itertools import combinations
from collections import deque


def check_lab(N):
    # 모든 바이러스를 퍼트릴 때 걸린 시간을 측정할 함수
    temp_max = 1
    for i in range(N):
        for j in range(N):
            # 연구소의 벽이라면 검사하지 않음
            if lab[i][j] != 0:
                continue
            
            # 빈공간이면서 아직 방문하지 않은 곳이 있다면 -1 리턴
            if lab[i][j] != 2 and visited[i][j] == 0:
                return -1
            
            # 아니라면 방문 한 곳 중에 가장 늦게 방문한 곳에 temp_max 저장
            if temp_max < visited[i][j]:
                temp_max = visited[i][j]

    # 리턴은 temp_max -1 (시작 지점은 0일째로 여기는데 현재 편의상 1일째로 초기화했기 때문)
    return temp_max-1

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스가 있는 위치를 리스트에 저장
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
            
# M개의 바이러스를 고르는 조합을 생성
virus_comb = list(combinations(virus, M))

# 날짜를 최대값으로 선언
result = N * N

dx = [1, 0, -1, 0]
dy = [0 ,1, 0, -1]

# 모든 바이러스를 고르는 케이스를 검사
for case in virus_comb:
    
    # q에 시작 위치를 삽입
    q = deque()
    # visited 리스트를 선언
    visited = [[0] * N for _ in range(N)]
    for x, y in case:
        visited[x][y] = 1
        q.append((x, y))
    
    # BFS 시작
    while q:
        x, y = q.popleft()
        
        # 4방향으로 탐색하면서
        for i in range(4):
            nx = x + dx[i]
            ny = y  +dy[i]
            
            # 인덱스를 벗어나지 않고 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 빈 공간이라면 q에 삽입, visited 처리
                if lab[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    # BFS가 끝난 후 걸린 날짜를 검사함
    temp_max = check_lab(N)
    
    # -1로 return하지 않았다면, 최대 날짜와 비교해서 적은 값으로 갱신
    if temp_max != -1 and result > temp_max:
        result = temp_max

# result가 초기값에서 변하지 않았다면 -1출력
if result == N*N:
    print(-1)
# 아니라면 result 출력
else:
    print(result)