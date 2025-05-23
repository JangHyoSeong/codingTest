# [18405] 경쟁적 전염

### **난이도**
골드 5
## **📝문제**
NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.



1초가 지난 후에 시험관의 상태는 다음과 같다.



2초가 지난 후에 시험관의 상태는 다음과 같다.



결과적으로 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류는 3번 바이러스다. 따라서 3을 출력하면 정답이다.
### **입력**
첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)
### **출력**
S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1 0 2
0 0 0
3 0 0
2 3 2
```

**예제 출력1**

```
3
```

**예제 입력2**

```
3 3
1 0 2
0 0 0
3 0 0
1 2 2
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
virus_list = [[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):
        if table[i][j]:
            virus_list[table[i][j]].append((i, j))

q = deque()
for i in range(1, K+1):
    for virus in virus_list[i]:
        q.append((virus[0], virus[1], i, 0))

while q:
    x, y, virus, time = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0:
            if time == S:
                continue
            q.append((nx, ny, virus, time+1))
            table[nx][ny] = virus

print(table[X-1][Y-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116148|152|PyPy3|799
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

Map = [ list(map(int,input().split()))+[-1] for _ in range(N) ]
Map.append ( [-1]*(N+1))

S, R, C = map(int,input().split())
C -= 1
R -= 1

que = {(R,C)}
V = set()
for i in range(S+1):
    nq = set()
    for r,c in que:
        if Map[r][c]:
            V.add(Map[r][c])
        else:
            Map[r][c] = -1

            for nr, nc in ( (r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if Map[nr][nc]>=0:
                    nq.add ((nr,nc))
    if V:
        break

    que = nq

if V:
    print(min(V))
else:
    print(0)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
cdw2241|31256|44|Python3|604
#### **📝해설**

```python
from collections import deque

# 입력받기
N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 상하좌우이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 바이러스의 시작시 위치를 저장할 리스트
virus_list = [[] for _ in range(K+1)]

# 바이러스 시작 위치를 저장
for i in range(N):
    for j in range(N):
        if table[i][j]:
            virus_list[table[i][j]].append((i, j))

# BFS를 위한 queue 선언
q = deque()

# queue에 오름차순으로 바이러스의 위치를 삽입
for i in range(1, K+1):
    for virus in virus_list[i]:

        # 바이러스 위치, 바이러스 숫자, 현재 시간
        q.append((virus[0], virus[1], i, 0))


# BFS 시작
while q:
    x, y, virus, time = q.popleft()

    # 상하좌우 4방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 인덱스를 벗어나지 않고, 방문한적 없다면 방문
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0:

            # 다음 이동이 시간을 초과한다면 이동하지 않음
            if time == S:
                continue

            # queue에 삽입, 방문처리
            q.append((nx, ny, virus, time+1))
            table[nx][ny] = virus

print(table[X-1][Y-1])
```