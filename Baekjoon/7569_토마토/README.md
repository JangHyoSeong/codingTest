# [7569] 토마토

### **난이도**
골드 5
## **📝문제**
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
### **입력**
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.
### **출력**
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
### **예제입출력**

**예제 입력1**

```
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
```

**예제 출력1**

```
-1
```

**예제 입력2**

```
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
```

**예제 출력2**

```
4
```

**예제 입력3**

```
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
```

**예제 출력3**

```
0
```

### **출처**
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2013 > 초등부 3번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

M, N, H = map(int, input().split())

tomatoes = []
for _ in range(H):
    one_floor = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(one_floor)

dh = [1, 0, 0, -1, 0, 0]
dx = [0, 1, 0, 0, -1, 0]
dy = [0, 0, 1, 0, 0, -1]

q = deque()
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                q.append([i, j, k, 0])
                visited[i][j][k] = True
            elif tomatoes[i][j][k] == -1:
                visited[i][j][k] = True
while q:
    h, x, y, day = q.popleft()

    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not visited[nh][nx][ny]:
            q.append([nh, nx, ny, day+1])
            tomatoes[nh][nx][ny] = 1
            visited[nh][nx][ny] = True

def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not visited[i][j][k]:
                    return False
    return True

if check():
    print(day)
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|217952|840|PyPy3|1192
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
q=[]
for i in range(b*c):q.append(list(map(int,input().split())))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
du=[b,-b]

w=[]
e=[]

for i in range(b*c):
    for j in range(a):
        if q[i][j]==1:
            w.append(i)
            e.append(j)

def jake(w,e):
    ww=[]
    ee=[]
    for aa in range(len(w)):
        i=w[aa]
        j=e[aa]
        for ii in range(4):
            nx=i+dx[ii]
            ny=j+dy[ii]
            if 0<=nx<b*c and 0<=ny<a:
                if i//b==nx//b:
                    if q[nx][ny]==0:
                        ww.append(nx)
                        ee.append(ny)
                        q[nx][ny]=1
        for ll in range(2):
            nnx=i+du[ll]
            if 0<=nnx<b*c:
                if q[nnx][j]==0:
                    ww.append(nnx)
                    ee.append(j)
                    q[nnx][j]=1

    return ww,ee

count=0
while True:
    count+=1
    w,e=jake(w,e)
    if len(w)==0:
        break

for i in range(b*c):
    for j in range(a):
        if q[i][j]==0:
            count=0
            break

print(count-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jake8648|152092|452|PyPy3|1126
#### **📝해설**

```python
from collections import deque

# 입력받음
M, N, H = map(int, input().split())

tomatoes = []
# 3차원 리스트인 tomatoes를 입력받음
for _ in range(H):
    one_floor = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(one_floor)

# 3차원 이동을 위한 리스트
dh = [1, 0, 0, -1, 0, 0]
dx = [0, 1, 0, 0, -1, 0]
dy = [0, 0, 1, 0, 0, -1]

# queue를 만들고, BFS를 진행하기 위한 세팅
q = deque()
# 3차원 visited 리스트를 만듦
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

# 모든 값을 순회하면서
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 토마토가 있는 부분은 q에 삽입하고 방문 처리
            if tomatoes[i][j][k] == 1:
                q.append([i, j, k, 0])
                visited[i][j][k] = True
            # 토마토가 썩은 부분도 방문처리를 진행함(이곳으로 이동하지 않을것)
            elif tomatoes[i][j][k] == -1:
                visited[i][j][k] = True

# BFS 시작
while q:
    # day : 현재까지 경과 일수
    h, x, y, day = q.popleft()

    # 6방향으로 이동
    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
    
        # 인덱스를 벗어나지 않고 방문하지 않았다면 방문
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not visited[nh][nx][ny]:
            # 새로운 위치를 경과일수 +1 해서 queue에 삽입
            q.append([nh, nx, ny, day+1])
            # 새롭게 토마토를 생성
            tomatoes[nh][nx][ny] = 1
            # 방문 처리
            visited[nh][nx][ny] = True

# 3차원 visited 리스트를 검사하면서, 방문하지 않은 곳이 있다면 false를 리턴
# 모두 방문했다면 True 리턴
def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not visited[i][j][k]:
                    return False
    return True

# True라면, 경과일수 출력 (BFS이기에 마지막으로 나온 day는 최대 경과일수)
if check():
    print(day)
# False라면 -1 출력
else:
    print(-1)
```