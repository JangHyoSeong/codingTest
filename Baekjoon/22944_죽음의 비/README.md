# [22944] 죽음의 비

### **난이도**
골드 3
## **📝문제**
가로, 세로 길이가 
$N$인 정사각형 격자가 있다. 해당 격자에는 두 곳을 제외한 모든 곳에 체력을 1씩 감소시키는 죽음의 비가 내리고 있다. 죽음의 비가 안내리는 곳은 현재 있는 위치와 안전지대라는 곳이다. 현재 있는 위치에도 곧 비가 내릴 예정이라 빨리 이 죽음의 비를 뚫고 안전지대로 이동해야한다.

다행히도 격자에는 죽음의 비를 잠시 막아주는 우산이 
$K$개 존재한다. 우산에는 내구도 
$D$라는 개념이 존재한다. 우산에 비를 맞으면 내구도가 1씩 감소하고, 내구도가 0이 되는 순간 우산은 사라진다. 문제에서 주어지는 우산의 내구도는 모두 
$D$로 동일하다.

격자에서 이동을 할 때 다음과 같이 순서로 진행된다.

1. 상하좌우로 이동한다. 만약 이동할 곳이 격자 밖이라면 이동할 수 없다. 
2. 이동한 곳이 안전지대라면 반복을 종료한다.
3. 이동한 곳에 우산이 있다면 우산을 든다. 만약, 이동할 때부터 우산을 가지고 있다면 가지고 있는 우산을 버리고 새로운 우산으로 바꾼다.
버린 우산은 더 이상 사용할 수 없다.
4. 죽음의 비를 맞았을 때, 우산을 가지고 있다면 우산의 내구도가 1이 감소하고 만약 우산을 가지고 있지 않는다면 체력이 1 감소한다.
5. 만약 우산의 내구도가 0이 되면 들고 있는 우산이 사라진다.
6. 만약 체력이 0이 되면 죽는다...
7. 아직 체력이 남았다면 안전지대까지 위 과정을 반복한다.

현재 있는 위치에서 안전지대로 얼마나 빠르게 이동할 수 있는지 구해주자.
### **입력**
첫 번째 줄에 정사각형 격자의 한변의 길이인 
$N$와 현재 체력 
$H$, 우산의 내구도 
$D$가 공백으로 구분되어 주어진다.

다음 
$N$개의 줄에는 정사각형 격자의 정보가 
$N$개의 문자로 붙어서 주어진다. 이때 주어지는 문자는 우산은 "U", 현재 있는 위치 "S", 안전지대 "E", 빈 칸 "."만 존재한다. 현재 있는 위치 "S"와 안전지대 "E"는 반드시 1개 존재한다.
### **출력**
안전지대로 이동할 때 최소 이동 횟수를 출력한다. 만약 안전지대로 이동하지 못하는 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 10 4
S..U
....
....
...E
```

**예제 출력1**

```
6
```

**예제 입력2**

```
4 2 6
S..U
....
....
...E
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
4 3 3
S..U
....
....
...E
```

**예제 출력3**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, H, D = map(int, input().split())
table = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if table[i][j] == "S":
            start_x, start_y = i, j

visited = [[-1] * N for _ in range(N)]

q = deque()
q.append((start_x, start_y, H, 0, 0))
visited[start_x][start_y] = H

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, hp, cost, step = q.popleft()

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        nh, nc = hp, cost

        if table[nx][ny] == 'E':
            print(step + 1)
            exit()

        if table[nx][ny] == 'U':
            nc = D

        if nc > 0:
            nc -= 1
        else:
            nh -= 1

        if nh <= 0:
            continue

        if visited[nx][ny] < nh + nc:
            visited[nx][ny] = nh + nc
            q.append((nx, ny, nh, nc, step + 1))

print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|41080|1544|Python3|985
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/62858e6576584934b6d2db90001acd5b

import sys
sys.setrecursionlimit(10**4)

def input():
    return sys.stdin.readline().rstrip()

n, h, d = map(int, input().split())

visit = [[False] * n for _ in range(n)]
umbs = []
for i in range(n):
    line = input()
    for j in range(n):
        if line[j] == 'U':
            umbs.append([i, j])
        elif line[j] == 'S':
            start = [i, j]
        elif line[j] == 'E':
            end = [i, j]

INF = 99999999
answer = INF

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(cur):
    global answer, n
    y, x, health, durability, cnt = cur
    dist = abs(end[0] - y) + abs(end[1] - x)
    if dist <= health + durability:
        answer = min(answer, cnt + dist)
        return
    else:
        for umb in umbs:
            uy, ux = umb
            if visit[uy][ux]: continue
            dist2 = abs(uy - y) + abs(ux - x)
            if dist2 - 1 >= health + durability: continue
            visit[uy][ux] = True
            if dist2 <= durability:
                dfs((uy, ux, health, d, cnt + dist2))
            else:
                dfs((uy, ux, health + durability - dist2, d, cnt + dist2))
            visit[uy][ux] = False

dfs((start[0], start[1], h, 0, 0))

if answer == INF:
    print(-1)
else:
    print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rzhang|33332|92|Python3|1340
#### **📝해설**

```python
from collections import deque

N, H, D = map(int, input().split())
table = [list(input().strip()) for _ in range(N)]

# 시작 위치 확인
for i in range(N):
    for j in range(N):
        if table[i][j] == "S":
            start_x, start_y = i, j

# 방문 여부 및 그 장소 도달할 때 체력 + 우산 내구도가 얼마나 남아있는지
visited = [[-1] * N for _ in range(N)]

# BFS를 위한 큐
q = deque()

# 현재 x, y 위치, 현재 체력, 우산 내구도, 이동 거리
q.append((start_x, start_y, H, 0, 0))

# 시작 위치 방문 처리
visited[start_x][start_y] = H

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    x, y, hp, cost, step = q.popleft()

    # 상하좌우를 탐색하면서
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]

        # 인덱스를 벗어난다면 고려하지 않음
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        
        # 이동 후 체력과 우산 내구도
        nh, nc = hp, cost

        # 도착지점이라면 종료
        if table[nx][ny] == 'E':
            print(step + 1)
            exit()

        # 우산이 있는 위치라면 내구도를 교체
        if table[nx][ny] == 'U':
            nc = D

        # 현재 내구도가 남아있다면 내구도를 깎음
        if nc > 0:
            nc -= 1
        
        # 아니라면 체력을 깎음
        else:
            nh -= 1

        # 체력이 0이 된다면 고려하지 않음
        if nh <= 0:
            continue
        
        # 현재 방문이 전의 방문보다 체력 + 내구도가 더 높다면
        if visited[nx][ny] < nh + nc:
            # 방문
            visited[nx][ny] = nh + nc
            q.append((nx, ny, nh, nc, step + 1))

# 도착지점에 도착하지 못한 경우 -1 출력
print(-1)
```