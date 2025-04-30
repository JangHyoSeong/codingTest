# [2665] 미로만들기

### **난이도**
골드 4
## **📝문제**
n×n 바둑판 모양으로 총 n2개의 방이 있다. 일부분은 검은 방이고 나머지는 모두 흰 방이다. 검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다. 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다. 윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고, 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.

시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데, 아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다. 부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.

아래 그림은 n=8인 경우의 한 예이다.

[이미지](https://www.acmicpc.net/upload/images/MW747ysuRPRpii4KaUvptRDAx46g.png)

위 그림에서는 두 개의 검은 방(예를 들어 (4,4)의 방과 (7,8)의 방)을 흰 방으로 바꾸면, 시작방에서 끝방으로 갈 수 있지만, 어느 검은 방 하나만을 흰 방으로 바꾸어서는 불가능하다. 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.

단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.
### **입력**
첫 줄에는 한 줄에 들어가는 방의 수 n(1 ≤ n ≤ 50)이 주어지고, 다음 n개의 줄의 각 줄마다 0과 1이 이루어진 길이가 n인 수열이 주어진다. 0은 검은 방, 1은 흰 방을 나타낸다.
### **출력**
첫 줄에 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
```

**예제 출력1**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
table = [list(map(int, input())) for _ in range(N)]

visited = [[int(21e8)] * N for _ in range(N)]
visited[0][0] = 0

q = deque()
q.append((0, 0, 0)) # x, y, 방 바꾼 갯수

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y, count = q.popleft()

    if count > visited[x][y]:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if table[nx][ny]:
                if visited[nx][ny] > count:
                    visited[nx][ny] = count
                    q.append((nx, ny, count))
            else:
                if visited[nx][ny] > count + 1:
                    visited[nx][ny] = count + 1
                    q.append((nx, ny, count+1))

print(visited[N-1][N-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34968|76|Python3|803
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
import heapq
input = sys.stdin.readline

line = int(input())

graph = [[] for _ in range(line+1)]
for i in range(1, line+1):
    graph[i] = [0] + list(map(str, input().strip()))
# print(line, graph)

def BFS():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    heap = []
    visited = [[0] * (line+1) for _ in range(line+1)]
    
    heapq.heappush(heap, [0, 1, 1])
    
    while heap:
        count, y, x = heapq.heappop(heap)
        visited[y][x] = 1
        if y == line and x == line:
            print(count)
            return

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 < ty <= line and 0 < tx <= line and visited[ty][tx] == 0 :
                visited[ty][tx] = 1
                if graph[ty][tx] == '0':
                    heapq.heappush(heap, [count+1, ty, tx])
                else: heapq.heappush(heap, [count, ty, tx])




BFS()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
lotus0110|33188|36|Python3|910
#### **📝해설**

```python
from collections import deque

N = int(input())
table = [list(map(int, input())) for _ in range(N)]

# 해당 위치까지 방문할 때, 방을 바꾼 횟수
visited = [[int(21e8)] * N for _ in range(N)]
visited[0][0] = 0

q = deque()
q.append((0, 0, 0)) # x, y, 방 바꾼 갯수

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS 시작
while q:
    x, y, count = q.popleft()

    # 만약 현재 지점이 이미 최소값이 아니라면 넘어감
    if count > visited[x][y]:
        continue

    # 상하좌우를 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 인덱스를 벗어나지 않으면서
        if 0 <= nx < N and 0 <= ny < N:

            # 흰 방이라면
            if table[nx][ny]:

                # 방 변경 횟수가 최소가 될 수 있는 곳으로만 이동
                if visited[nx][ny] > count:
                    visited[nx][ny] = count
                    q.append((nx, ny, count))
            
            # 검은 방이라면
            else:
                # 방 변경 횟수를 1 늘림
                if visited[nx][ny] > count + 1:
                    visited[nx][ny] = count + 1
                    q.append((nx, ny, count+1))

print(visited[N-1][N-1])
```