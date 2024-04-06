from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 델타 탐색을 위한 리스트 선언
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 결과값으로 사용할 max_safe
max_safe = 0


zero_list = [] # 초기 상태에서 빈공간의 위치를 저장할 리스트
virus = [] # 초기 상태에서 바이러스의 위치를 저장할 리스트

# 바이러스와 빈공간을 탐색하면서 저장해둠
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero_list.append((i, j))
        elif lab[i][j] ==2:
            virus.append((i, j))

# 0의 위치를 3개씩 묶어서 조합을 만들어줌
# 벽을 세울 위치를 가지게 됨
barricade = list(combinations(zero_list, 3))

# 모든 케이스를 검사
for case in barricade:
    # 깊은 복사로 연구실의 리스트를 복사함
    temp_lab = deepcopy(lab)

    # 이번 케이스에서 벽을 세워줌ㅈ
    for x, y in case:
        temp_lab[x][y] = 1
    
    # BFS를 위한 deque 선언, 초기값을 넣어줌
    q = deque(virus)
    # 이번 케이스에서의 안전 구역
    temp_safe = 0
    
    # BFS시작
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스를 벗어나지않고, 빈공간이라면 바이러스로 바꾸어주고, q에 삽입
            if 0 <= nx < N and 0 <= ny < M and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                q.append((nx, ny))

    # 연구소를 순회하면서 빈공간 개수를 세어줌
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 0:
                temp_safe += 1

    # max값을 갱신
    max_safe = max(temp_safe, max_safe)

print(max_safe)