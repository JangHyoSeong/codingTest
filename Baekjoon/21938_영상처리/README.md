# [21938] 영상처리

### **난이도**
실버 2
## **📝문제**
간단하지만 귀찮은 영상처리 과제가 주어졌다. 과제의 명세는 다음과 같다.

세로 길이가 
$N$이고 가로 길이가 
$M$인 화면은 총 
$N$ × 
$M$개의 픽셀로 구성되어 있고 
$(i, j)$에 있는 픽셀은 
$R_{i,j}$ (Red), 
$G_{i,j}$ (Green), 
$B_{i,j}$ (Blue) 3가지 색상의 의미를 담고 있다. 각 색상은 0이상 255이하인 값으로 표현 가능하다.

모든 픽셀에서 세 가지 색상을 평균내어 경계값 
$T$보다 크거나 같으면 픽셀의 값을 255로, 작으면 0으로 바꿔서 새로운 화면으로 저장한다.

새로 만들어진 화면에서 값이 255인 픽셀은 물체로 인식한다. 값이 255인 픽셀들이 상하좌우로 인접해있다면 이 픽셀들은 같은 물체로 인식된다.

화면에서 물체가 총 몇 개 있는지 구하는 프로그램을 작성하시오.
### **입력**
화면의 세로 
$N$, 가로 
$M$ 값이 공백으로 구분되어 주어진다.

두 번째 줄부터 
$N + 1$줄까지 
$i$번째 가로를 구성하고 있는 픽셀의 
$R_{i,j}$, 
$G_{i,j}$, 
$B_{i,j}$의 값이 공백으로 구분되어 총 
$M$개 주어진다.

마지막 줄에는 경계값 
$T$가 주어진다.
### **출력**
화면에 있는 물체의 개수를 출력하라. 만약 물체가 없으면 0을 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
3 3
255 255 255 100 100 100 255 255 255
100 100 100 255 255 255 100 100 100
255 255 255 100 100 100 255 255 255
101
```

**예제 출력1**

```
5
```

**예제 입력2**

```
2 2
124 150 123 100 100 100
103 103 103 183 5 3
255
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
T = int(sys.stdin.readline().rstrip())

picture = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(0, M * 3, 3):
        rgb_sum = sum(table[i][j:j+3])

        if rgb_sum >= 3 * T:
            picture[i][j//3] = True

visited = [[False] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] or not picture[i][j]:
            continue

        stack = [(i, j)]
        visited[i][j] = True
        count += 1
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and picture[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

print(count)  
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|66632|1212|Python3|988
#### **📝해설**

**알고리즘**
```
1. BFS, DFS
```

### **다른 풀이**

```python
from collections import deque

dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for di, dj in dirr:
            a = x+di
            b = y+dj
            if not (0<=a<N and 0<=b<M):
                continue
            if board[a][b] == 1:
                board[a][b] = 0
                q.append((a, b))

N, M = map(int, input().split())
picture = []
for _ in range(N):
    picture.append(list(map(int, input().split())))
T = int(input())
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        rgb = 0
        for k in range(3):
            rgb += picture[i][3*j+k]
        if (rgb / 3) >= T:
            board[i][j] = 1
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dajulie|134424|324|PyPy3|880
#### **📝해설**

```python
import sys

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
T = int(sys.stdin.readline().rstrip())

# 그 부분에 물체가 있다면 True, 아니라면 False
picture = [[False] * M for _ in range(N)]

for i in range(N):

    # 3칸이 하나의 픽셀이므로 3칸씩 확인
    for j in range(0, M * 3, 3):

        # 그 칸의 rgb 총합
        rgb_sum = sum(table[i][j:j+3])

        # 평균이 T보다 크다면 그 칸에는 물체가 존재
        if rgb_sum >= 3 * T:
            picture[i][j//3] = True

# DFS할때 방문 여부를 저장할 리스트
visited = [[False] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0

# 모든 칸을 순회하면서
for i in range(N):
    for j in range(M):

        # 이미 방문했거나, 픽셀이 없다면 넘어감
        if visited[i][j] or not picture[i][j]:
            continue
        
        # 현재 칸부터 DFS 시작
        stack = [(i, j)]
        visited[i][j] = True
        count += 1
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and picture[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

print(count)  
```