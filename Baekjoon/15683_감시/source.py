from copy import deepcopy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

# 현재 cctv의 위치, 종류를 담을 리스트
cctvs = []

# cctv의 정보를 리스트에 담아줌
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append([i, j, office[i][j]])

# cctv의 총 개수
cctv_count = len(cctvs)

# 사각지대의 최소값을 선언
min_count = N * M

# 각각 현재 cctv기준 아래, 위, 왼쪽, 오른쪽의 사각지대를 없애는 함수들
def check_down(x, y, office):
    while x < N:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        x += 1
    
    return office

def check_up(x, y, office):
    while x >= 0:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        x -= 1
    
    return office

def check_left(x, y, office):
    while y >= 0:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        y -= 1

    return office

def check_right(x, y, office):
    while y < M:
        if office[x][y] == 0:
            office[x][y] = -1
        elif office[x][y] == 6:
            break
        y += 1

    return office

# 재귀적으로 호출되며 완전탐색을 실행할 함수
# 인덱스를 늘려가며, 모든 경우의수를 탐색함
def check_blind(idx, office):
    global min_count

    # 모든 cctv의 방향을 정했다면
    if idx == cctv_count:
        count = 0

        # 사각지대의 개수를 셈
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    count += 1

        # 최소값 갱신이 가능하다면 갱신
        if min_count > count:
            min_count = count
        
        return

    # 현재 인덱스의 cctv 정보
    x, y, cctv = cctvs[idx]
    
    # 모든 방향을 고려하여 완전탐색
    if cctv == 1:
        nx = x
        temp_office = deepcopy(office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        nx = x
        temp_office = deepcopy(office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        check_blind(idx+1, temp_office)
        
    if cctv == 2:
        nx = x
        temp_office = deepcopy(office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        ny = y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 3:

        nx, ny = x, y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 4:
        nx, ny = x, y

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        check_blind(idx+1, temp_office)

        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

    if cctv == 5:

        nx, ny = x, y
        temp_office = deepcopy(office)
        temp_office = check_left(x, ny, temp_office)
        temp_office = check_right(x, ny, temp_office)
        temp_office = check_down(nx, y, temp_office)
        temp_office = check_up(nx, y, temp_office)
        check_blind(idx+1, temp_office)

check_blind(0, office)
print(min_count)