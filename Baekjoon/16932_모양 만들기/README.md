# [16932] 모양 만들기

### **난이도**
골드 3
## **📝문제**
N×M인 배열에서 모양을 찾으려고 한다. 배열의 각 칸에는 0과 1 중의 하나가 들어있다. 두 칸이 서로 변을 공유할때, 두 칸을 인접하다고 한다.

1이 들어 있는 인접한 칸끼리 연결했을 때, 각각의 연결 요소를 모양이라고 부르자. 모양의 크기는 모양에 포함되어 있는 1의 개수이다.

배열의 칸 하나에 들어있는 수를 변경해서 만들 수 있는 모양의 최대 크기를 구해보자.
### **입력**
첫째 줄에 배열의 크기 N과 M이 주어진다. 둘째 줄부터 N개의 줄에는 배열에 들어있는 수가 주어진다.
### **출력**
첫째 줄에 수 하나를 변경해서 만들 수 있는 모양의 최대 크기를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
0 1 1
0 0 1
0 1 0
```

**예제 출력1**

```
5
```

**예제 입력2**

```
5 4
1 1 0 0
1 0 1 0
1 0 1 0
0 1 1 0
1 0 0 1
```

**예제 출력2**

```
10
```

**예제 입력3**

```
3 4
0 1 0 1
0 0 0 1
1 1 0 1
```

**예제 출력3**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

max_area = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if table[i][j] == 0:

            table[i][j] = 1
            visited = set()
            visited.add((i, j))

            temp_area = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and table[nx][ny]:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                        temp_area += 1
            max_area = max(max_area, temp_area)
            table[i][j] = 0

print(max_area)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|456232|7812|PyPy3|831
#### **📝해설**

**알고리즘**
```
1. DFS
```

### **다른 풀이**

```python
import sys
from collections import deque

input = sys.stdin.readline
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
size = [0] * 10**6
cnt = 2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q = deque()
            q.append((i, j))
            graph[i][j] = cnt
            size[cnt] = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                        graph[nx][ny] = cnt
                        size[cnt] += 1
                        q.append((nx, ny))

            cnt += 1

res = max(size)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cur = 1
            adj = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    adj.add(graph[ni][nj])
            for k in adj:
                cur += size[k]
            res = max(cur, res)
print(res)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ljw1029boj|140184|380|PyPy3|1174
#### **📝해설**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

max_area = 0

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 이차원 리스트를 검사하면서 0인 지점을 모두 1로 바꾸어봄
for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            
            # 1로 바꾼 지점부터 주위 칸들을 검사
            table[i][j] = 1
            # set를 통해 방문처리
            visited = set()
            visited.add((i, j))

            # 현재 영역의 넓이
            temp_area = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and table[nx][ny]:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                        temp_area += 1
            max_area = max(max_area, temp_area)
            table[i][j] = 0

print(max_area)
```