# [2589] 보물섬

### **난이도**
골드 5
## **📝문제**
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

[이미지](https://www.acmicpc.net/upload/images/c1bYIsKpI6m317EAx.jpg)

예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.

[이미지](https://www.acmicpc.net/upload/images/XqDkWCRUWbzZ.jpg)

보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.
### **출력**
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
```

**예제 출력1**

```
8
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

L, W = map(int, input().split())
table = [list(input()) for _ in range(L)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_dist = 0

for i in range(L):
    for j in range(W):
        if table[i][j] == 'W':
            continue

        visited = [[False] * W for _ in range(L)]
        visited[i][j] = True
        q = deque([[i, j, 0]])
        
        while q:
            x, y, count = q.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                
                if 0 <= nx < L and 0 <= ny < W and not visited[nx][ny] and table[nx][ny] == 'L':
                    q.append((nx, ny, count+1))
                    visited[nx][ny] = True

        max_dist = max(max_dist, count)
print(max_dist)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|117972|828|PyPy3|768
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **😅개선점**

1. 시간이 널널해서 모든 점에서 BFS를 진행했지만, 더 좋은 방법이 있지 않을까

### **다른 풀이**

```python
from collections import deque
def bfs(si,sj):
    q = deque()
    v = [[0] * (M + 2) for _ in range(N + 2)]

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if v[ni][nj]==0 and arr[ni][nj]=='L':
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return v[ci][cj]-1

N, M = map(int,input().split())
arr = ["W"*(M+2)]+["W"+input()+"W" for _ in range(N)]+["W"*(M+2)]
mx = 0
ai,aj = 0,0
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]=='W': continue
        if arr[i-1][j]=='L' and arr[i+1][j]=='L': continue
        if arr[i][j-1]=='L' and arr[i][j+1]=='L': continue
        t = bfs(i,j)
        if mx<t:
            mx=t
            ai,aj = i,j
print(mx)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
smile_again|114756|212|PyPy3|827
#### **📝해설**

```python
from collections import deque

L, W = map(int, input().split())
table = [list(input()) for _ in range(L)]

# 상하좌우이동을 위한 리스트
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 최대 이동거리
max_dist = 0

# 모든 테이블의 점을 순회
for i in range(L):
    for j in range(W):
        # 육지가 아니라면 넘김
        if table[i][j] == 'W':
            continue
        
        # BFS 탐색을 위한 방문 여부 저장
        visited = [[False] * W for _ in range(L)]
        visited[i][j] = True

        # x, y, 이동거리
        q = deque([[i, j, 0]])
        
        # BFS
        while q:
            x, y, count = q.popleft()

            # 상하좌우 탐색
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                
                # 방문할 수 있는 위치면 방문
                if 0 <= nx < L and 0 <= ny < W and not visited[nx][ny] and table[nx][ny] == 'L':
                    q.append((nx, ny, count+1))
                    visited[nx][ny] = True

        # BFS이므로 마지막으로 나온 count가 가장 멀리 이동한 거리
        # 거리 갱신
        max_dist = max(max_dist, count)
print(max_dist)
```