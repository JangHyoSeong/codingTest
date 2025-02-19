# [2636] 치즈

### **난이도**
골드 4
## **📝문제**
아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다. 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다. <그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.


![이미지](https://upload.acmicpc.net/9b0f0cfb-007d-4ea8-8e6f-e397728b5c8e/-/preview/)
<그림 1> 원래 치즈 모양

다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.


![이미지](https://upload.acmicpc.net/b099f661-9788-4183-bd62-1e98e6f184e7/-/preview/)
<그림 2> 한 시간 후의 치즈 모양


![이미지](https://upload.acmicpc.net/58fc0743-794b-4e27-84e8-fe491ec7bf3d/-/preview/)
<그림 3> 두 시간 후의 치즈 모양

<그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며, 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다. 그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다. <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.
### **출력**
첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

**예제 출력1**

```
3
5
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0
prev_cheese_count = 0

while True:
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    cheese_positions = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if table[nx][ny] == 1:
                    cheese_positions.append((nx, ny))
                else:
                    queue.append((nx, ny))
    
    if not cheese_positions:
        print(time)
        print(prev_cheese_count)
        break
    
    prev_cheese_count = len(cheese_positions)
    for x, y in cheese_positions:
        table[x][y] = 0
    
    time += 1
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34968|112|Python3|958
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
    prev = cnt = 0
    time = -1
    while queue:
        _queue = []
        prev = cnt
        cnt = 0
        while queue:
            r, c = queue.pop(0)
            for dr, dc in delta:
                if N > r+dr >= 0 and M > c+dc >= 0:
                    if board[r+dr][c+dc] < 0:
                        continue
                    if board[r+dr][c+dc] == 0:
                        queue.append((r+dr, c+dc))
                    else:
                        _queue.append((r+dr, c+dc))
                        cnt += 1
                    board[r+dr][c+dc] = -1
        queue = _queue
        time += 1
    print(time)
    print(prev)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|31120|32|Python3|904
#### **📝해설**

```python
from collections import deque

# 입력
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 탐색을 위한 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 출력을 위한 변수
time = 0
prev_cheese_count = 0

# BFS를 위한 반복
while True:

    # 방문 여부를 저장
    visited = [[False] * M for _ in range(N)]

    # BFS 탐색을 위한 큐(가장자리 공기에서 시작)
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    # 치즈가 녹을 위치를 저장
    cheese_positions = []

    # BFS
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if table[nx][ny] == 1:
                    cheese_positions.append((nx, ny)) # 치즈인 경우 녹일 목록에 추가
                else:
                    queue.append((nx, ny)) # 공기인 경우 탐색
    
    # 더이상 녹일 치즈가 없다면 종료
    if not cheese_positions:
        print(time)
        print(prev_cheese_count)
        break
    
    # 현재 남은 치즈 개수 저장
    prev_cheese_count = len(cheese_positions)

    # 치즈를 녹임
    for x, y in cheese_positions:
        table[x][y] = 0
    
    # 시간 증가
    time += 1
```