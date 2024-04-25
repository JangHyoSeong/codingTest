# [2206] 벽 부수고 이동하기

### **난이도**
골드 3
## **📝문제**
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
### **출력**
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
6 4
0100
1110
1000
0000
0111
0000
```

**예제 출력1**

```
15
```

**예제 입력2**

```
4 4
0111
1111
1111
1110
```

**예제 출력2**

```
-1
```
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())

table = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

q = deque([(0, 0, False)])
visited[0][0] = [1, 1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, is_break = q.popleft()
    
    if x == N-1 and y == M-1:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if is_break:
                if not visited[nx][ny][1] and table[nx][ny] == 0:
                    q.append((nx, ny, True))
                    visited[nx][ny][1] = visited[x][y][1] + 1
            else:
                if table[nx][ny] == 0 and not visited[nx][ny][0]:
                    q.append((nx, ny, False))
                    visited[nx][ny][0] = visited[x][y][0] + 1
                elif table[nx][ny] == 1 and not visited[nx][ny][1]:
                    q.append((nx, ny, True))
                    visited[nx][ny][1] = visited[x][y][0] + 1
            

if visited[N-1][M-1] == [0,0]:
    print(-1)
else:
    if visited[N-1][M-1][0] == 0:
        print(visited[N-1][M-1][1])
    elif visited[N-1][M-1][1] == 0:
        print(visited[N-1][M-1][0])
    else:
        print(min(visited[N-1][M-1]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|285496|1564|PyPy3|1299
#### **📝해설**

**알고리즘**
```
1. BFS
```
### **다른 풀이**

```python
import sys
from collections import deque
input = sys.stdin.readline
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = int(1e9)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist = [[INF] * m for _ in range(n)]
    dist[y][x] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m) or not (0 <= ny < n): continue
            if dist[ny][nx] != INF: continue
            dist[ny][nx] = dist[y][x] + 1
            if board[ny][nx] == 0:
                q.append((nx, ny))
    return dist

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

from_start = bfs(0, 0)
from_end = bfs(m - 1, n - 1)
ans = min(INF, from_start[n - 1][m - 1] + 1)
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ans = min(ans, from_start[i][j] + from_end[i][j] + 1)
        
print(ans if ans != INF else -1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
eastgi|169008|528|PyPy3|949
#### **📝해설**

```python
```

### **🔖정리**

1. 배운점