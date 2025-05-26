# [2146] 다리 만들기

### **난이도**
골드 3
## **📝문제**
여러 섬으로 이루어진 나라가 있다. 이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다. 하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다. 그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다. 이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 다음은 세 개의 섬으로 이루어진 나라의 지도이다.

![이미지](https://www.acmicpc.net/JudgeOnline/upload/201008/bri.PNG)

위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다. 가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.

![이미지](https://www.acmicpc.net/JudgeOnline/upload/201008/b2.PNG)

물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나, 위의 경우가 놓는 다리의 길이가 3으로 가장 짧다(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.
### **입력**
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.
### **출력**
첫째 줄에 가장 짧은 다리의 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
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

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

island_idx = 1
for i in range(N):
    for j in range(N):
        if table[i][j] == 1 and visited[i][j] == 0:
            q = deque([(i, j)])
            visited[i][j] = island_idx
            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = island_idx
        
            island_idx += 1

q = deque()
dist = [[-1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]

                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    q.append((i, j))
                    dist[i][j] = 0
                    break

answer = int(21e8)

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            
            elif visited[nx][ny] != visited[x][y]:
                answer = min(answer, dist[x][y] + dist[nx][ny])

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35076|100|Python3|1578
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def cc(i, j):
    stack = [(i, j)]
    a[i][j] = -1

    while stack:
        y, x = stack.pop()
        for dy, dx in delta:
            ny, nx = y+dy, x+dx

            if 0<=ny<n and 0<=nx<n:
                if a[ny][nx] == 1:
                    a[ny][nx] = -1
                    stack.append((ny, nx))
                elif a[ny][nx] == 0:
                    a[ny][nx] = id
                    nxt_queue.append((ny, nx))
                elif 1 < a[ny][nx] < id:
                    print(1); exit()

def bfs(nxt_queue):
    dist = 2
    temp = 0
    while (queue:= nxt_queue) and not temp:
        nxt_queue = []
        for y, x in queue:
            cur = a[y][x]
            for dy, dx in delta:
                ny, nx = y+dy, x+dx

                if 0<=ny<n and 0<=nx<n:
                    if a[ny][nx] == 0:
                        a[ny][nx] = cur
                        nxt_queue.append((ny, nx))
                    elif 1 < a[ny][nx] < cur:
                        temp = dist+1
                    elif cur < a[ny][nx]:
                        return dist
        dist += 2
    
    return temp

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]

id = 2
nxt_queue = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 1: 
            cc(i, j); id += 1

print(bfs(nxt_queue))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|31120|40|Python3|1411
#### **📝해설**

```python
from collections import deque

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 해당 위치에 섬이 있는지 여부를 저장할 리스트
visited = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 각 섬마다 인덱스를 부여
island_idx = 1
for i in range(N):
    for j in range(N):
        if table[i][j] == 1 and visited[i][j] == 0:
            q = deque([(i, j)])
            visited[i][j] = island_idx
            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = island_idx
        
            island_idx += 1

# 섬의 가장자리만을 큐에 저장
q = deque()

# 섬과 떨어져있는 거리를 저장할 리스트
dist = [[-1] * N for _ in range(N)]

# 모든 위치를 탐색하면서
for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]

                # 현재 섬에 포함되고, 다음 위치가 육지가 아닐경우 큐에 담음
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    q.append((i, j))
                    dist[i][j] = 0
                    break

# 다리길이
answer = int(21e8)

# BFS
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 인덱스를 벗어나지 않으면서
        if 0 <= nx < N and 0 <= ny < N:

            # 섬이 아닌 땅이라면
            if visited[nx][ny] == 0:

                # 섬의 크기를 늘리고 방문처리
                visited[nx][ny] = visited[x][y]
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            
            # 다른 섬의 영역에 닿았다면 그때 결과를 저장
            elif visited[nx][ny] != visited[x][y]:
                answer = min(answer, dist[x][y] + dist[nx][ny])

print(answer)
```