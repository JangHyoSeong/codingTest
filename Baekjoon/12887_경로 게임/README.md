# [12887] 경로 게임

### **난이도**
골드 5
## **📝문제**
현정이는 경로 게임을 하고 있다.

경로 게임은 정사각형 칸으로 이루어져 있는 직사각형 격자판에서 진행된다. 격자판의 행의 개수는 항상 2이며, 열의 개수는 양수이다. 각 칸은 검정색 또는 하얀색으로 칠해져 있다.

격자에서 왼쪽-오른쪽 경로는 시작 칸이 가장 왼쪽 열에 있는 칸이고, 마지막 칸이 가장 오른쪽 열에 있는 경로이다. 이때, 경로 상의 모든 칸은 하얀색이어야 하며, 경로상에서 연속하는 칸은 모두 인접해야 한다.

격자판의 하얀색 칸을 검정색 칸으로 바꾼 경우에도 왼쪽-오른쪽 경로가 존재할 수도 있다. 이때, 왼쪽-오른족 경로가 존재하면서 바꿀 수 있는 하얀색 칸의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 열의 개수 M이 주어진다. (M ≤ 50)

둘째 줄부터 두 개의 줄에 게임판의 상태가 주어진다. '.'는 하얀색을, '#'는 검정색을 나타낸다.

왼쪽-오른쪽 경로가 항상 존재하는 게임판만 입력으로 주어진다.
### **출력**
첫째 줄에 바꿀 수 있는 하얀색 칸의 개수의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
#....
...#.
```

**예제 출력1**

```
2
```

**예제 입력2**

```
1
#
.
```

**예제 출력2**

```
0
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

M = int(input())
board = [list(input()) for _ in range(2)]

white_count = sum(row.count('.') for row in board)

INF = 10**9
dist = [[INF] * M for _ in range(2)]
q = deque()

for r in range(2):
    if board[r][0] == '.':
        dist[r][0] = 1
        q.append((r, 0))

while q:
    r, c = q.popleft()
    d = dist[r][c]

    if c + 1 < M and board[r][c+1] == '.' and dist[r][c+1] > d + 1:
        dist[r][c+1] = d + 1
        q.append((r, c+1))
    
    nr = r ^ 1
    if board[nr][c] == '.' and dist[nr][c] > d + 1:
        dist[nr][c] = d + 1
        q.append((nr, c))

min_path = min(dist[0][M-1], dist[1][M-1])
print(white_count - min_path)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34968|68|Python3|675
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

M = int(input())
board = [list(input()) for _ in range(2)]

# 현재 보드에 흰색이 몇개있는지 셈
white_count = sum(row.count('.') for row in board)

# 해당 칸까지 어느만큼 이동했는지 거리를 저장
INF = 10**9
dist = [[INF] * M for _ in range(2)]

# BFS를 위한 큐
q = deque()

# 시작 지점 확인
for r in range(2):
    if board[r][0] == '.':
        dist[r][0] = 1
        q.append((r, 0))

# BFS 시작
while q:
    r, c = q.popleft()
    d = dist[r][c]

    # 다음 칸으로 이동 가능한지 확인
    if c + 1 < M and board[r][c+1] == '.' and dist[r][c+1] > d + 1:
        dist[r][c+1] = d + 1
        q.append((r, c+1))
    
    # 위 아래 이동
    nr = r ^ 1
    if board[nr][c] == '.' and dist[nr][c] > d + 1:
        dist[nr][c] = d + 1
        q.append((nr, c))

# 끝까지 갔을 때, 몇 칸을 이동했는지 확인
min_path = min(dist[0][M-1], dist[1][M-1])

# 최단거리에 포함되지 않는 흰색은 바꿀 수 있음
print(white_count - min_path)
```