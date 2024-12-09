# [4179] 불

### **난이도**
골드 3
## **📝문제**
지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.

불은 각 지점에서 네 방향으로 확산된다.

지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.

지훈이와 불은 벽이 있는 공간은 통과하지 못한다.
### **입력**
입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

각각의 문자들은 다음을 뜻한다.

- #: 벽
- .: 지나갈 수 있는 공간
- J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
- F: 불이 난 공간  
J는 입력에서 하나만 주어진다.
### **출력**
지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 4
####
#JF#
#..#
#..#
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

def bfs_escape(R, C, maze):
    fire_time = [[-1] * C for _ in range(R)]
    jihun_time = [[-1] * C for _ in range(R)]
    fire_queue = deque()
    jihun_queue = deque()

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire_queue.append((i, j))
                fire_time[i][j] = 0
            elif maze[i][j] == 'J':
                jihun_queue.append((i, j))
                jihun_time[i][j] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fire_queue:
        x, y = fire_queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and fire_time[nx][ny] == -1 and maze[nx][ny] == '.':
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

    while jihun_queue:
        x, y = jihun_queue.popleft()

        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return jihun_time[x][y] + 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and jihun_time[nx][ny] == -1 and maze[nx][ny] == '.':
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))

    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [input().strip() for _ in range(R)]

print(bfs_escape(R, C, maze))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|14116|376|PyPy3|1521
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
from collections import deque
import sys

input=sys.stdin.readline

N,M=map(int,input().split())
data=[str(input().rstrip()) for _ in range(N)]
queue=deque([])
visited=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if data[i][j]=='F':
            queue.append((i,j,1))
            visited[i][j]=-1
        elif data[i][j]=='J':
            start=(i,j,0)
queue.append(start)
visited[start[0]][start[1]]=1
p=[(0,1),(0,-1),(1,0),(-1,0)]
d=True
while queue:
    x,y,z=queue.popleft()
    if (x==0 or x==N-1 or y==0 or y==M-1) and z==0:
        print(visited[x][y])
        d=False
        break
    for a,b in p:
        dx,dy=x+a,y+b
        if dx<0 or dx>=N or dy<0 or dy>=M:
            continue
        elif data[dx][dy]=='#' or visited[dx][dy]!=0:
            continue
        else:
            queue.append((dx,dy,z))
            if z==1:
                visited[dx][dy]=-1
            else:
                visited[dx][dy]=visited[x][y]+1
if d:
    print('IMPOSSIBLE')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mmt_1234|133304|340|PyPy3|1000
#### **📝해설**

```python
from collections import deque

def bfs_escape(R, C, maze):
    # 불이 위치까지 도달하는시간, 지훈이 위치까지 도달하는 시간을 저장할 리스트
    fire_time = [[-1] * C for _ in range(R)]
    jihun_time = [[-1] * C for _ in range(R)]

    # 불의 이동을 위한 큐
    fire_queue = deque()
    # 지훈의 이동을 위한 큐
    jihun_queue = deque()


    # 불의 위치와 지훈의 초기 위치를 큐에 삽입
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire_queue.append((i, j))
                fire_time[i][j] = 0
            elif maze[i][j] == 'J':
                jihun_queue.append((i, j))
                jihun_time[i][j] = 0

    # 상하좌우 이동을 위한 리스트
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 불 BFS
    while fire_queue:
        x, y = fire_queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and fire_time[nx][ny] == -1 and maze[nx][ny] == '.':
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

    # 지훈 BFS
    while jihun_queue:
        x, y = jihun_queue.popleft()

        # 탈출하는 경우
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return jihun_time[x][y] + 1
        
        # 탈출하지 못했다면
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 상하좌우로 이동
            if 0 <= nx < R and 0 <= ny < C and jihun_time[nx][ny] == -1 and maze[nx][ny] == '.':

                # 지훈이 불보다 빠르게 이동 가능한 경우만 고려
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))

    # 도착하지 못했다면 임파서블
    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [input().strip() for _ in range(R)]

print(bfs_escape(R, C, maze))
```