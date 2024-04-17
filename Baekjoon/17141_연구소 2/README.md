# [17141] 연구소 2

### **난이도**
골드 4
## **📝문제**
인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.

```
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
```
M = 3이고, 바이러스를 아래와 같이 놓은 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 바이러스를 놓은 위치는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.

```
6 6 5 4 - - 2
5 6 - 3 - 0 1
4 - - 2 - 1 2
3 - 2 1 2 2 3
2 2 1 0 1 - -
1 - 2 1 2 3 4
0 - 3 2 3 4 5
```
시간이 최소가 되는 방법은 아래와 같고, 5초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.

```
0 1 2 3 - - 2
1 2 - 3 - 0 1
2 - - 2 - 1 2
3 - 2 1 2 2 3
3 2 1 0 1 - -
4 - 2 1 2 3 4
5 - 3 2 3 4 5
```
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
### **입력**
첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
### **출력**
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
```

**예제 출력1**

```
5
```

**예제 입력2**

```
7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
```

**예제 출력2**

```
5
```

**예제 입력3**

```
7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
```

**예제 출력3**

```
4
```
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations
from collections import deque

def check_time(N):
    temp_max = 0
    for i in range(N):
        for j in range(N):
            if temp_max < visited[i][j]:
                temp_max = visited[i][j]
            elif visited[i][j] == -1:
                return -1
    
    return temp_max


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

can_virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            can_virus.append([i, j])

virus_comb = list(combinations(can_virus, M))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

min_time = N * N
can_make = False

for case in virus_comb:

    visited = [[-1] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 1:
                visited[i][j] = 0
                
    q = deque(case)
    flag = False
    
    for x, y in case:
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        if flag:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and lab[nx][ny] != 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > min_time:
                    flag = True

    if flag:
        continue
    
    temp_max = check_time(N)

    if temp_max < min_time and temp_max != -1:
        min_time = temp_max
        can_make = True

if can_make:
    print(min_time)
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|115508|244|PyPy3|1621
#### **📝해설**

**알고리즘**
```
1. BFS
2. 브루트포스 알고리즘
```

### **다른 풀이**

```python
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def back_tacking(N, M, n=0, selected=[]):
    m = len(selected)
    if M == m:
        return [selected[:]]

    arr = []
    for i in range(n, N):
        if N - i < M - m:
            continue

        selected.append(i)
        arr += back_tacking(N, M, i + 1, selected)
        selected.pop()
    return arr


def bfs(N, board, visited, sx, sy, idx):
    queue = deque([(sx, sy)])
    visited[(sx, sy)][idx] = 0
    time = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] or visited[(nx, ny)][idx] != 9999:
                    continue
                visited[(nx, ny)][idx] = time
                queue.append((nx, ny))
        time += 1


def simulation(virus, pos_logs, best):
    max_val = 0
    for logs in pos_logs:
        min_val = 9999
        for v in virus:
            if min_val > logs[v]:
                min_val = logs[v]
        if min_val >= best:
            return best
        elif min_val > max_val:
            max_val = min_val
    return max_val


def solution(N, M, board):
    pos = [(x, y) for y in range(N) for x in range(N) if board[y][x] == 2]
    PN = len(pos)
    visited = {}
    for y in range(N):
        for x in range(N):
            if board[y][x] == 2:
                board[y][x] = 0
                visited[(x, y)] = [9999] * PN
            elif not board[y][x]:
                visited[(x, y)] = [9999] * PN

    for idx, (x, y) in enumerate(pos):
        bfs(N, board, visited, x, y, idx)

    pos_logs = list(visited.values())
    answer = 9999
    for virus in back_tacking(len(pos), M):
        answer = simulation(virus, pos_logs, answer)

    return answer if answer != 9999 else -1


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
|audxo112|34280|116|Python3|2067
#### **📝해설**

```python
from itertools import combinations
from collections import deque

# visited에서 최대 가중치를 확인
# -1인 곳이 있으면 바이러스를 퍼트리지 못했다는 뜻
def check_time(N):
    temp_max = 0
    for i in range(N):
        for j in range(N):
            if temp_max < visited[i][j]:
                temp_max = visited[i][j]
            elif visited[i][j] == -1:
                return -1
    
    return temp_max


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

can_virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            can_virus.append([i, j])

virus_comb = list(combinations(can_virus, M))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

min_time = N * N
can_make = False

for case in virus_comb:

    visited = [[-1] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 1:
                visited[i][j] = 0
                
    q = deque(case)
    flag = False
    
    for x, y in case:
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        if flag:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and lab[nx][ny] != 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > min_time:
                    flag = True

    if flag:
        continue
    
    temp_max = check_time(N)

    if temp_max < min_time and temp_max != -1:
        min_time = temp_max
        can_make = True

if can_make:
    print(min_time)
else:
    print(-1)
```