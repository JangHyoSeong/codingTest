# [문제번호] 문제제목

### **난이도**
골드 3
## **📝문제**
인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.

```
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
```
M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.
```
* 6 5 4 - - 2
5 6 - 3 - 0 1
4 - - 2 - 1 2
3 - 2 1 2 2 3
2 2 1 0 1 - -
1 - 2 1 2 3 4
0 - 3 2 3 4 *
```
시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.
```
0 1 2 3 - - 2
1 2 - 3 - 0 1
2 - - 2 - 1 2
3 - 2 1 2 2 3
3 2 1 0 1 - -
4 - 2 1 2 3 4
* - 3 2 3 4 *
```
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
### **입력**

### **출력**

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
4
```

**예제 입력2**

```
7 5
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
3
```

**예제 입력3**

```
7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
```

**예제 출력3**

```
-1
```
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from itertools import combinations
from collections import deque

def check_lab(N):
    temp_max = 1
    for i in range(N):
        for j in range(N):
            if lab[i][j] != 0:
                continue
            if lab[i][j] != 2 and visited[i][j] == 0:
                return -1
            if temp_max < visited[i][j]:
                temp_max = visited[i][j]

    return temp_max-1

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
            
virus_comb = list(combinations(virus, M))
result = N * N

dx = [1, 0, -1, 0]
dy = [0 ,1, 0, -1]

for case in virus_comb:
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for x, y in case:
        visited[x][y] = 1
        q.append((x, y))
        
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y  +dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if lab[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif lab[nx][ny] == 2:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    temp_max = check_lab(N)
    
    if temp_max != -1 and result > temp_max:
        result = temp_max


if result == N*N:
    print(-1)
else:
    print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|115240|272|PyPy3|1511
#### **📝해설**

**알고리즘**
```
1. BFS
2. 조합
```
### **다른 풀이**

```python
N, M = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]

virus = []
empty = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==0:
            empty+=1
        elif arr[i][j]==2:
            virus.append((i,j))

ans = N**2
def dfs(n,s, lst):
    global ans
    if n==M:
        ans = min(ans ,bfs(lst, empty))
        return

    for i in range(s,len(virus)):
        dfs(n+1, i+1, lst+[i])

def bfs(lst, empty):
    v = [[0]*N for _ in range(N)]
    q = []
    for i in lst:
        ci,cj = virus[i]
        q.append((ci,cj))
        v[ci][cj]=1
    t = 0
    if empty==0:
        return 0
    while q:
        temp_q = []
        for i in range(len(q)):
            ci,cj = q[i]
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1:
                    v[ni][nj]=1
                    temp_q.append((ni,nj))
                    if arr[ni][nj]==0:
                        empty-=1
        if empty==0:
            return t+1
        t+=1
        q = temp_q
    return N**2
dfs(0,0,[])
if ans==N**2:
    print(-1)
else:
    print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kys1124|111308|196|PyPy3|1195
#### **📝해설**

```python
```