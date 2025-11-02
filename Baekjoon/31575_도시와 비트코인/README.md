# [31575] 도시와 비트코인

### **난이도**
실버 3
## **📝문제**
전날에 비해 비트코인의 시세가 백만원이나 오른 어느 아침, 진우는 거래소에 가서 비트코인을 매도하려고 한다. 현재 비트코인의 시세가 점점 떨어지고 있기 때문에 진우는 최대한 빨리 거래소에 가야 한다.

도시는 가로 
$N$, 세로 
$M$ 크기의 격자 모양으로 이루어졌다. 진우는 북서쪽 끝에 있고 거래소는 남동쪽 끝에 있다. 도시의 일부 구역은 공터 또는 도로라서 진우가 지나갈 수 있지만, 어떤 구역은 건물이 있어서 진우가 갈 수 없다.

진우는 최대한 빨리 거래소에 가야 하므로, 동쪽(오른쪽) 또는 남쪽(아래쪽)으로만 이동하여 거래소로 도착할 수 있어야 한다. 진우를 도와 거래소로 갈 수 있는지 구하는 프로그램을 작성하여라. 진우의 현재 위치가 거래소일 수 있다.
### **입력**
첫 번째 줄에 도시의 가로 크기 
$N$과 세로 크기 
$M$ (
$1 \le N, M \le 300$)이 주어진다.

두 번째 줄부터 
$M$개의 줄에는 도시의 형태를 나타내는 
$N$개의 정수가 공백을 사이에 두고 주어진다. 각 칸이 1인 경우 진우가 갈 수 있는 칸을 의미하고 0인 경우 진우가 갈 수 없는 칸을 의미한다.

왼쪽 위의 끝 칸과 오른쪽 아래의 끝 칸은 모두 1이다.
### **출력**
첫 번째 줄에 진우가 거래소로 갈 수 있으면 Yes를, 그렇지 않으면 No를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 4
1 1 1 1 1
0 1 0 0 1
1 0 0 0 1
0 0 0 1 1
```

**예제 출력1**

```
Yes
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]
visited[0][0] = True

q = deque()
q.append((0, 0))

dx = [1, 0]
dy = [0, 1]

while q:
    x, y = q.popleft()

    if x == M-1 and y == N-1:
        print("Yes")
        break

    for d in range(2):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < M and 0 <= ny < N and table[nx][ny] and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True
else:
    print("No")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34944|176|Python3|574
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline

n,m=map(int,input().split()) # col, row
board=[list(map(int,input().split())) for _ in range(m)]
visited=[[False]*n for _ in range(m)]

def in_range(x,y):
    return 0<=x<m and 0<=y<n

def dfs(i,j):
    dxs=[0,1]
    dys=[1,0]
    stack=[(i,j)]
    while stack:
        x,y=stack.pop()
        visited[x][y]=True
        # print(f"x,y:{x},{y}")
        if x==m-1 and y==n-1:
            return 'Yes'
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if in_range(nx,ny) and not visited[nx][ny] and board[nx][ny]==1:
                stack.append((nx,ny))
    return 'No'

print(dfs(0,0))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ehsrnfgml|31575|32804|48|Python3|664