# [2638] 치즈

### **난이도**
골드 3
## **📝문제**
N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다. 따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.


![이미지](https://upload.acmicpc.net/a4998beb-104c-4e37-b3d7-fd91cd81464a/-/preview/)
<그림 1>

<그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다. 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.


![이미지](https://upload.acmicpc.net/e5d519ee-53ea-40a6-b970-710cca0db128/-/preview/)
<그림 2>


![이미지](https://upload.acmicpc.net/a00b876a-86dc-4a82-a030-603a9b1593cc/-/preview/)
<그림 3>

모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다. 그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시된다. 또한, 각 0과 1은 하나의 공백으로 분리되어 있다.
### **출력**
출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check_air():
    visited = [[False] * M for _ in range(N)]
    q = deque()

    q.append((0, 0))
    visited[0][0] = True

    air = [[0] * M for _ in range(N)]
    while q:
        x, y = q.popleft()
        air[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not table[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return air

def melt_cheese():
    air = check_air()
    melt = []

    for i in range(N):
        for j in range(M):
            if table[i][j] == 1:
                count = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]

                    if 0 <= nx < N and 0 <= ny < M and air[nx][ny] == 1:
                        count += 1
                
                if count >= 2:
                    melt.append((i, j))
    
    for x, y in melt:
        table[x][y] = 0
    
    return len(melt) > 0

time = 0
while True:
    if not melt_cheese():
        break

    time += 1

print(time)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35016|660|Python3|1261
#### **📝해설**

**알고리즘**
```
1. 구현
2. BFS
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    board[0][0] = -1
    queue = [(0, 0)]
    time = -1
    while queue:
        _queue = []
        while queue:
            r, c = queue.pop(0)
            for dr, dc in delta:
                if N > r+dr >= 0 and M > c+dc >= 0:
                    if board[r+dr][c+dc] < 0:
                        continue
                    if board[r+dr][c+dc] == 0:
                        queue.append((r+dr, c+dc))
                        board[r+dr][c+dc] = -1
                    elif board[r+dr][c+dc] == 1:
                        board[r+dr][c+dc] += 1
                    else:
                        _queue.append((r+dr, c+dc))
                        board[r+dr][c+dc] = -1
        queue = _queue
        time += 1
    print(time)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|31120|40|Python3|948
#### **📝해설**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동을 위한 벡터 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 공기가 어느부분에 있는지 저장할 함수
def check_air():

    # 방문 여부
    visited = [[False] * M for _ in range(N)]
    q = deque()

    # 가장자리는 치즈가 없으니 가장자리부터 탐색을 시작
    q.append((0, 0))
    visited[0][0] = True

    # 공기인지 여부를 저장할 리스트(0: 공기가 없음, 1: 공기가 있음)
    air = [[0] * M for _ in range(N)]

    # BFS 시작
    while q:
        x, y = q.popleft()

        # queue에 있었다면 공기
        air[x][y] = 1

        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 치즈가 없는 곳이라면 공기
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not table[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return air

# 치즈를 녹이는 함수
def melt_cheese():

    # 이번 탐색에서 공기 여부를 확인
    air = check_air()

    # 이번 작업으로 녹일 치즈들의 좌표 리스트
    melt = []

    # 모든 좌표를 순회하면서
    for i in range(N):
        for j in range(M):

            # 치즈가 있다면 시작
            if table[i][j] == 1:
                count = 0
                
                # 상하좌우에 공기가 2개 이상 있다면 녹임
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]

                    if 0 <= nx < N and 0 <= ny < M and air[nx][ny] == 1:
                        count += 1
                
                if count >= 2:
                    melt.append((i, j))
    
    for x, y in melt:
        table[x][y] = 0
    
    return len(melt) > 0

# 치즈가 없을때까지 반복
time = 0
while True:
    if not melt_cheese():
        break

    time += 1

print(time)
```