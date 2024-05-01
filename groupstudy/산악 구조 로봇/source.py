import sys
sys.stdin = open('input.txt')

# 다이스트라 사용을 위한 heappush, heappop 불러오기
from heapq import heappush, heappop

T = int(input())

for testcase in range(1, T):

    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    
    # 터널의 정보를 담을 딕셔너리
    tunnels = {}
    for _ in range(M):
        temp = list(map(int, input().split()))
        # 터널의 키 값은 터널 입구의 좌표. value는 출구의 좌표와 연료 소모량
        # 양방향으로 만들어줌
        # 한 위치에 여러개의 터널이 있을수 있으니, value는 리스트로 저장
        if tunnels.get((temp[0]-1, temp[1]-1)) is None:
            tunnels[(temp[0]-1, temp[1]-1)] = [(temp[2]-1, temp[3]-1, temp[4])]
        else:
            tunnels[(temp[0]-1, temp[1]-1)].append((temp[2]-1, temp[3]-1, temp[4]))
        
        if tunnels.get((temp[2]-1, temp[3]-1)) is None:
            tunnels[(temp[2]-1, temp[3]-1)] = [(temp[0]-1, temp[1]-1, temp[4])]
        else:
            tunnels[(temp[2]-1, temp[3]-1)].append((temp[0]-1, temp[1]-1, temp[4]))
    
    # 임의의 큰 수. 다이스트라 최소값 계산을 위한 테이블을 정의해줌
    INF = 21e8
    fuel_table = [[INF] * N for _ in range(N)]

    # 상하좌우 이동을 위한 리스트
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 다이스트라를 위한 우선순위 큐 정의. 현재까지의 연료 소모량과 시작 위치 좌표를 넣어줌
    pq = []
    heappush(pq, (0, 0, 0))
    # 시작위치의 연료 소모량을 0으로 초기화
    fuel_table[0][0] = 0

    # 다이스트라 시작
    while pq:
        # 우선순위 큐에서 값을 빼옴.
        now_fuel, x, y = heappop(pq)

        # 현재 연료소모량이 이미 현재위치에서 최소가 안된다면 이 경우는 계산하지 않음
        if fuel_table[x][y] < now_fuel:
            continue
        
        # 현재 위치에서 터널이 존재하는지 검사
        is_tunnel = tunnels.get((x, y))
        
        # 터널이 존재한다면 (None이 아니라면)
        if is_tunnel is not None:

            for tunnel in is_tunnel:
                # 다음위치로 이동할때 드는 연료량, 터널이 이어진 위치
                next_fuel, nx, ny = tunnel[2], tunnel[0], tunnel[1]
                
                # 다음위치로 이동할때까지 사용한 누적 연료량 계산
                new_fuel = now_fuel + next_fuel

                # 만약 이번 이동이 최저값이라면 fuel_table을 갱신, heappush(이동)
                if new_fuel < fuel_table[nx][ny]:
                    fuel_table[nx][ny] = new_fuel
                    heappush(pq, (new_fuel, nx, ny))

        # 상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스를 벗어나지 않는다면
            if 0 <= nx < N and 0 <= ny < N:
                # 사용 연료량 계산
                if table[nx][ny] - table[x][y] > 0:
                    next_fuel = (table[nx][ny] - table[x][y]) * 2
                elif table[nx][ny] - table[x][y] == 0:
                    next_fuel = 1
                else:
                    next_fuel = 0

                # 터널때 했던 작업과 같은 작업 진행
                new_fuel = next_fuel + now_fuel

                if new_fuel >= fuel_table[nx][ny]:
                    continue

                fuel_table[nx][ny] = new_fuel

                heappush(pq, (new_fuel, nx, ny))
    
    # 다이스트라 작업이 종료되면 도착위치는 항상 최소값이 들어가게 됨
    print(f'#{testcase} {fuel_table[N-1][N-1]}')