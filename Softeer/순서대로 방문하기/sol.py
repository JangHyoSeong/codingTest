import sys
from copy import deepcopy

# N : 배열의 가로세로 크기, M : 주어진 방문경로의 개수
N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
route = []

# 반드시 거쳐가야 할 경로를 route리스트에 저장
for _ in range(M):
    x, y = map(int, input().split())
    route.append([x-1, y-1])

# 방문 여부를 포함할 visited
visited = [[False] * N for _ in range(N)]

# 델타 탐색을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def DFS(x, y, visited, now_idx):
		# DFS 함수
    global cnt
    
	  # 각 분기마다 자신의 visited를 가지는 방식
	  # N이 4이하의 정수이기 때문에 경우의 수가 적어서 가능
    now_visited = deepcopy(visited)
    # 방문 표시
    now_visited[x][y] = True

		# 현재 위치가 들러야하는 경로상에 있는데
    if [x, y] in route:
		    # 지금 여기가 방문해야하는 순서가 아니라면 종료
        if [x, y] != route[now_idx]:
            return
        # 방문해야 하는 순서가 맞다면 다음 순서로 가야한다고 표시
        else:
            now_idx += 1

    # 그래서 만약 모두 순서에 맞게 방문했다면 cnt를 1증가 후 종료
    if now_idx == M:
        cnt += 1
        return


		# 상하좌우로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 인덱스 내부이고, table이 1이 아니고, 방문한적없다면 방문
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] != 1 and not now_visited[nx][ny]:
            
            DFS(nx, ny, now_visited, now_idx)
            

DFS(route[0][0], route[0][1], visited, 0)

print(cnt)