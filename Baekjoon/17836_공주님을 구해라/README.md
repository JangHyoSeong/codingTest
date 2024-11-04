# [17836] 공주님을 구해라

### **난이도**
골드 5
## **📝문제**
용사는 마왕이 숨겨놓은 공주님을 구하기 위해 (N, M) 크기의 성 입구 (1,1)으로 들어왔다. 마왕은 용사가 공주를 찾지 못하도록 성의 여러 군데 마법 벽을 세워놓았다. 용사는 현재의 가지고 있는 무기로는 마법 벽을 통과할 수 없으며, 마법 벽을 피해 (N, M) 위치에 있는 공주님을 구출해야만 한다.

마왕은 용사를 괴롭히기 위해 공주에게 저주를 걸었다. 저주에 걸린 공주는 T시간 이내로 용사를 만나지 못한다면 영원히 돌로 변하게 된다. 공주님을 구출하고 프러포즈 하고 싶은 용사는 반드시 T시간 내에 공주님이 있는 곳에 도달해야 한다. 용사는 한 칸을 이동하는 데 한 시간이 걸린다. 공주님이 있는 곳에 정확히 T시간만에 도달한 경우에도 구출할 수 있다. 용사는 상하좌우로 이동할 수 있다.



성에는 이전 용사가 사용하던 전설의 명검 "그람"이 숨겨져 있다. 용사가 그람을 구하면 마법의 벽이 있는 칸일지라도, 단숨에 벽을 부수고 그 공간으로 갈 수 있다. "그람"은 성의 어딘가에 반드시 한 개 존재하고, 용사는 그람이 있는 곳에 도착하면 바로 사용할 수 있다. 그람이 부술 수 있는 벽의 개수는 제한이 없다.

우리 모두 용사가 공주님을 안전하게 구출 할 수 있는지, 있다면 얼마나 빨리 구할 수 있는지 알아보자.
### **입력**
첫 번째 줄에는 성의 크기인 N, M 그리고 공주에게 걸린 저주의 제한 시간인 정수 T가 주어진다. 첫 줄의 세 개의 수는 띄어쓰기로 구분된다. (3 ≤ N, M ≤ 100, 1 ≤ T ≤ 10000)

두 번째 줄부터 N+1번째 줄까지 성의 구조를 나타내는 M개의 수가 띄어쓰기로 구분되어 주어진다. 0은 빈 공간, 1은 마법의 벽, 2는 그람이 놓여있는 공간을 의미한다. (1,1)과 (N,M)은 0이다.
### **출력**
용사가 제한 시간 T시간 이내에 공주에게 도달할 수 있다면, 공주에게 도달할 수 있는 최단 시간을 출력한다.

만약 용사가 공주를 T시간 이내에 구출할 수 없다면, "Fail"을 출력한다.
### **예제입출력**

**예제 입력1**

```
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
```

**예제 출력1**

```
10
```

**예제 입력2**

```
3 4 100
0 0 0 0
1 1 1 1
0 0 2 0
```

**예제 출력2**

```
Fail
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([(0, 0, False)])

while queue:
    x, y, gram = queue.popleft()
    time = visited[x][y][1 if gram else 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if table[nx][ny] != 1 or gram:
                new_time = time + 1

                if table[nx][ny] == 2 and not gram:
                    if new_time < visited[nx][ny][1]:
                        visited[nx][ny][1] = new_time
                        queue.append((nx, ny, True))

                elif gram and new_time < visited[nx][ny][1]:
                    visited[nx][ny][1] = new_time
                    queue.append((nx, ny, True))
                
                elif not gram and new_time < visited[nx][ny][0]:
                    visited[nx][ny][0] = new_time
                    queue.append((nx, ny, False))

result = min(visited[N-1][M-1])
if result <= T:
    print(result)
else:
    print("Fail")

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116280|152|PyPy3|1209
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys


col, row, limit_time = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(col)]
visit = [[0] * row for _ in range(col)]

move_list = [[1,0],[-1,00],[0,1],[0,-1]]

move_point = [[0,0]]
time = 0
sword_time = 1000000

while visit[-1][-1] == 0 and move_point:
    next_move_point = []
    for y, x in move_point:
        for ay, ax in move_list:
            dy, dx = y+ay, x+ax
            if 0<=dy<col and 0<=dx<row and visit[dy][dx] == 0 and maze[dy][dx] != 1:
                visit[dy][dx] = -1
                if maze[dy][dx] == 2:
                    sword_time = time+1 + (col-1-dy) + (row-1-dx)
                    continue
                next_move_point.append([dy,dx])
    move_point = next_move_point
    time += 1
    
if visit[-1][-1] == 0:
    time = sword_time
else:
    time = min(time, sword_time)
print(time if (visit[-1][-1] != 0 or sword_time != 1000000) and time <= limit_time else 'Fail')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20230660|31120|48|Python3|975
#### **📝해설**

```python
from collections import deque

N, M, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([(0, 0, False)])

while queue:
    x, y, gram = queue.popleft()
    time = visited[x][y][1 if gram else 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if table[nx][ny] != 1 or gram:
                new_time = time + 1

                if table[nx][ny] == 2 and not gram:
                    if new_time < visited[nx][ny][1]:
                        visited[nx][ny][1] = new_time
                        queue.append((nx, ny, True))

                elif gram and new_time < visited[nx][ny][1]:
                    visited[nx][ny][1] = new_time
                    queue.append((nx, ny, True))
                
                elif not gram and new_time < visited[nx][ny][0]:
                    visited[nx][ny][0] = new_time
                    queue.append((nx, ny, False))

result = min(visited[N-1][M-1])
if result <= T:
    print(result)
else:
    print("Fail")

```