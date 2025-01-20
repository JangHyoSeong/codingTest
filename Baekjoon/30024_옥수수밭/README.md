# [30024] 옥수수밭

### **난이도**
골드 4
## **📝문제**
옥수수밭 주인 민석이는 한 해 동안 열심히 기른 옥수수를 수확하려고 한다. 옥수수밭은 
$N$행 
$M$열의 격자로 생각할 수 있는데, 격자의 각 칸에는 한 그루의 옥수수가 심어져 있다. 민석이는 각 옥수수의 가치를 측정해서 서로 다른 정수 
$1,2,\cdots ,N\times M$을 부여했다.

![이미지](https://upload.acmicpc.net/8bfc31ad-3ecd-4a0b-aafe-9ef98a081e27/-/preview/)

민석이는 처음에 옥수수밭 바깥에 위치한다. 민석이는 옥수수밭 바깥을 돌아다니면서 옥수수밭 바깥과 인접한 칸의 옥수수를 수확할 수 있다. 또는 옥수수밭 안에서 옥수수를 수확한 칸으로만 돌아다니면서 현재 위치한 칸에서 상하좌우로 인접한 칸의 옥수수를 수확할 수 있다.

그런데, 민석이는 옥수수의 생산량 조절을 위해서 
$K$그루의 옥수수만 수확하려고 한다. 민석이는 현재 수확할 수 있는 옥수수 중에서 가장 가치가 높은 옥수수를 수확하는 과정을 
$K$번 반복한다. 민석이가 수확하는 옥수수의 위치를 순서대로 구해보자.
### **입력**
첫째 줄에 정수 
$N, M(1 \le N, M \le 1\,000)$이 공백으로 구분되어 주어진다.

둘째 줄부터 
$N$개의 줄에 걸쳐 
$M$개의 정수가 공백으로 구분되어 주어진다. 
$N$개의 줄 중 
$i$번째 줄의 
$j$번째 정수는 격자에서 
$i$번째 줄의 
$j$번째 칸의 옥수수의 가치를 의미하는 정수 
$a_{ij}(1 \le a_{ij} \le N \times M)$다.

마지막 줄에 정수 
$K(1\le K \le \min(N \times M, 100\,000))$가 주어진다.
### **출력**
$K$개의 줄에 민석이가 수확하는 옥수수의 위치 
$i,j(1\le i\le N;1\le j\le M)$를 순서대로 출력한다. 
$i,j$는 격자의 
$i$번째 행, 
$j$번째 열을 의미한다.
### **예제입출력**

**예제 입력1**

```
4 5
1 18 2 3 4
12 17 15 20 5
11 14 19 13 6
10 9 16 8 7
6
```

**예제 출력1**

```
1 2
2 2
4 3
3 3
2 3
2 4
```

**예제 입력2**

```
3 3
9 8 1
4 5 2
6 3 7
4
```

**예제 출력2**

```
1 1
1 2
3 3
3 1
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappop, heappush

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

pq = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]

for j in range(M):
    heappush(pq, (-table[0][j], 0, j))
    visited[0][j] = True
    if N > 1:
        heappush(pq, (-table[N-1][j], N-1, j))
        visited[N-1][j] = True

for i in range(1, N-1):
    heappush(pq, (-table[i][0], i, 0))
    visited[i][0] = True
    if M > 1:
        heappush(pq, (-table[i][M-1], i, M-1))
        visited[i][M-1] = True

count = 0
while count < K:
    value, x, y = heappop(pq)
    print(x+1, y+1)
    count += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            heappush(pq, (-table[nx][ny], nx, ny))
            visited[nx][ny] = True
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|146460|668|PyPy3|899
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
2. BFS
```

#### **📝해설**

```python
from heapq import heappop, heappush

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

# 최대힙을 사용해서 큰 숫자가 먼저 나오게끔 함
pq = []

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 방문 여부를 저장할 리스트
visited = [[False] * M for _ in range(N)]

# 상하좌우 테두리를 우선순위큐에 삽입
for j in range(M):
    heappush(pq, (-table[0][j], 0, j))
    visited[0][j] = True
    if N > 1:
        heappush(pq, (-table[N-1][j], N-1, j))
        visited[N-1][j] = True

for i in range(1, N-1):
    heappush(pq, (-table[i][0], i, 0))
    visited[i][0] = True
    if M > 1:
        heappush(pq, (-table[i][M-1], i, M-1))
        visited[i][M-1] = True

# K번 반복
count = 0
while count < K:
    value, x, y = heappop(pq)
    print(x+1, y+1)
    count += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            heappush(pq, (-table[nx][ny], nx, ny))
            visited[nx][ny] = True
```