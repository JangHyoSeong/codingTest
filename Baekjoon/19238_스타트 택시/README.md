# [19238] 스타트 택시

### **난이도**
골드 2
## **📝문제**
스타트링크가 "스타트 택시"라는 이름의 택시 사업을 시작했다. 스타트 택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.

택시 기사 최백준은 오늘 M명의 승객을 태우는 것이 목표이다. 백준이 활동할 영역은 N×N 크기의 격자로 나타낼 수 있고, 각 칸은 비어 있거나 벽이 놓여 있다. 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다. 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동한다.

M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다. 각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.

백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 연료는 한 칸 이동할 때마다 1만큼 소모된다. 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.

<그림 1>은 택시가 활동할 영역의 지도를 나타내며, 택시와 세 명의 승객의 출발지와 목적지가 표시되어 있다. 택시의 현재 연료 양은 15이다. 현재 택시에서 각 손님까지의 최단거리는 각각 9, 6, 7이므로, 택시는 2번 승객의 출발지로 이동한다.

<그림 2>는 택시가 2번 승객의 출발지로 가는 경로를, <그림 3>은 2번 승객의 출발지에서 목적지로 가는 경로를 나타낸다. 목적지로 이동할 때까지 소비한 연료는 6이고, 이동하고 나서 12가 충전되므로 남은 연료의 양은 15이다. 이제 택시에서 각 손님까지의 최단거리는 둘 다 7이므로, 택시는 둘 중 행 번호가 더 작은 1번 승객의 출발지로 이동한다.

<그림 4>와 <그림 5>는 택시가 1번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 남은 연료의 양은 15 - 7 - 7 + 7×2 = 15이다.

<그림 6>과 <그림 7>은 택시가 3번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 최종적으로 남은 연료의 양은 15 - 5 - 4 + 4×2 = 14이다.

모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.
### **입력**
첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.

다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.

다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.

그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.
### **출력**
모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다. 단, 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다. 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
```

**예제 출력1**

```
14
```

**예제 입력2**

```
6 3 13
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
6 3 100
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
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
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116320|320|PyPy3|3307
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
"""
BOJ : 스타트 택시

시작 시간 : 10시 01분
구상 완료 : 10시 07분
제출 시간 : 10시 38분
"""


# 400짜리 bfs 800번 해도 충분

def int_idx(num):
    return int(num) - 1


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m, f = map(int, input().split())
board = [list(map(int, input().split())) + [1] for _ in range(n)] + [[1] * n]
adj = [[[(i + di, j + dj) for di, dj in directions if not board[i + di][j + dj]] for j in range(n)] for i in range(n)]
csx, csy = map(int_idx, input().split())
start_site = [[None] * n for _ in range(n)]

for p in range(m):
    sx, sy, gx, gy = map(int_idx, input().split())
    start_site[sx][sy] = (gx, gy)


def solve():
    fuel = f
    cx, cy = csx, csy

    for move in range(m):
        visited = [[False] * n for _ in range(n)]
        q = [(cx, cy)]
        visited[cx][cy] = True
        while q and fuel:
            nq = []
            sq = []
            for x, y in q:
                if start_site[x][y]:
                    sq.append((x, y))
                for nx, ny in adj[x][y]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        nq.append((nx, ny))
            if sq:
                break
            fuel -= 1
            q = nq

        if not sq:
            print(-1)
            return

        cx, cy = min(sq)
        dx, dy = start_site[cx][cy]
        start_site[cx][cy] = None
        visited = [[False] * n for _ in range(n)]
        q = [(cx, cy)]
        visited[cx][cy] = True
        distance = 0
        arrived = False
        while q and fuel:
            nq = []
            fuel -= 1
            distance += 1
            for x, y in q:
                for nx, ny in adj[x][y]:
                    if nx == dx and ny == dy:
                        cx, cy = nx, ny
                        arrived = True
                        break
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        nq.append((nx, ny))
                if arrived:
                    break
            if arrived:
                break
            q = nq

        if not arrived:
            print(-1)
            return
        fuel += distance << 1

    print(fuel)
    return


solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
onionfarmer|31120|68|Python3|2290