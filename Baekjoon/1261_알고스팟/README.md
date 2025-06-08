# [1261] 알고스팟

### **난이도**
골드 4
## **📝문제**
알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.

(1, 1)과 (N, M)은 항상 뚫려있다.
### **출력**
첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
011
111
110
```

**예제 출력1**

```
3
```

**예제 입력2**

```
4 2
0001
1000
```

**예제 출력2**

```
0
```

**예제 입력3**

```
6 6
001111
010000
001111
110001
011010
100010
```

**예제 출력3**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(M)]

visited = [[int(21e8)] * N for _ in range(M)]
visited[0][0] = 0

q = deque()
q.append((0, 0))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if table[nx][ny] == 0 and visited[x][y] < visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]
            
            if table[nx][ny] == 1 and visited[x][y] + 1 < visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[M-1][N-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34976|232|Python3|739
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
from sys import stdin

m, n = map(int, input().split())
status = stdin.read().split() 

def dijkstra():
    COST = [[1e4]*m for _ in range(n)]
    COST[0][0] = 0
    deque = [(0, 0)]

    while True:
        x, y = deque.pop(0) 
        if x == m-1 and y == n-1:
            return COST[n-1][m-1]

        cost = COST[y][x]
        for x, y in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if not (0 <= x < m and 0 <= y < n):
                continue

            is_wall = status[y][x] == '1'
            new_cost = cost + (1 if is_wall else 0)

            if COST[y][x] <= new_cost:
                continue

            COST[y][x] = new_cost
            if is_wall:
                deque.append((x, y))
            else:
                deque.insert(0, (x, y))
print(dijkstra())

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
love_adela|31120|40|Python3|791
#### **📝해설**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(M)]

# 벽을 몇번 부수고 방문했는지 여부를 저장할 리스트
visited = [[int(21e8)] * N for _ in range(M)]

# 시작지점은 0으로 초기화
visited[0][0] = 0

# BFS를 위한 큐 선언
q = deque()
q.append((0, 0))

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    x, y = q.popleft()

    # 상하좌우 인접한 칸을 검사
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 인덱스를 벗어나지 않으면서
        if 0 <= nx < M and 0 <= ny < N:

            # 빈 방이라면, 더 적은 부순 횟수로 갱신할 수 있다면 이동 후 갱신
            if table[nx][ny] == 0 and visited[x][y] < visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]
            
            # 벽이라면, 벽을 한번 부순 횟수를 더해서, 이동횟수를 갱신할 수 있다면 갱신
            if table[nx][ny] == 1 and visited[x][y] + 1 < visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[M-1][N-1])
```