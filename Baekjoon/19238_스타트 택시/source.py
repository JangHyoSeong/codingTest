from collections import deque

# 상수 정의
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start_x, start_y, fuel, table, target):
    N = len(table)
    visited = [[False] * N for _ in range(N)]
    q = deque([(start_x, start_y, 0)])  # (x, y, distance)
    visited[start_x][start_y] = True
    
    # BFS로 목표 위치까지 최단 거리 찾기
    while q:
        x, y, dist = q.popleft()
        if fuel < dist:  # 연료가 부족하면 실패
            return -1, -1, -1
        if (x, y) == target:
            return x, y, dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    
    return -1, -1, -1  # 도달할 수 없으면 실패

def find_closest_customer(taxi_x, taxi_y, fuel, customers, table):
    # BFS로 가장 가까운 승객 찾기
    # 손님이 여러명일 경우 거리, 행, 열 우선순위 고려
    # 손님을 찾으면 그 좌표와 이동 거리를 반환
    
    N = len(table)
    visited = [[False] * N for _ in range(N)]
    q = deque([(taxi_x, taxi_y, 0)])  # (x, y, distance)
    visited[taxi_x][taxi_y] = True
    candidates = []
    
    while q:
        x, y, dist = q.popleft()
        if fuel < dist:
            break  # 연료가 부족하면 종료
        
        # 승객이 있는지 확인
        if (x, y) in customers:
            candidates.append((dist, x, y))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    
    if not candidates:
        return -1, -1, -1
    
    # 승객 거리, 행, 열 순으로 정렬
    candidates.sort()
    return candidates[0][1], candidates[0][2], candidates[0][0]

N, M, fuel = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1  # 인덱스 맞추기 위해 -1
taxi_y -= 1

customers = []
destinations = {}
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    customers.append((sx-1, sy-1))  # 출발지
    destinations[(sx-1, sy-1)] = (ex-1, ey-1)  # 목적지

for _ in range(M):
    # 가장 가까운 승객 찾기
    target_x, target_y, dist_to_customer = find_closest_customer(taxi_x, taxi_y, fuel, customers, table)
    if target_x == -1:
        print(-1)
        exit()
    
    # 승객까지 이동
    fuel -= dist_to_customer
    if fuel < 0:
        print(-1)
        exit()
    
    # 승객 목적지까지 이동
    dest_x, dest_y = destinations[(target_x, target_y)]
    taxi_x, taxi_y, dist_to_destination = bfs(target_x, target_y, fuel, table, (dest_x, dest_y))
    if taxi_x == -1:
        print(-1)
        exit()
    
    # 연료 충전
    fuel -= dist_to_destination
    if fuel < 0:
        print(-1)
        exit()
    
    fuel += dist_to_destination * 2
    
    # 손님을 목적지에 데려다 줬으니 리스트에서 제거
    customers.remove((target_x, target_y))

# 모든 승객을 이동시킨 경우 남은 연료 출력
print(fuel)