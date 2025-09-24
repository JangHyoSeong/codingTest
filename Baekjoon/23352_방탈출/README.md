# [23352] 방탈출

### **난이도**
골드 5
## **📝문제**
여러 방들로 둘러싸인 구역을 탈출해야 한다. 알맞은 비밀번호를 입력하면 탈출할 수 있다.

구역의 지도는 
$N \times M$ 크기의 격자판으로 나타낼 수 있으며 각 칸은 방을 의미하고 각 칸에는 0부터 9까지의 숫자가 적혀있는데 이는 해당하는 방에 적힌 숫자를 의미한다.

상하좌우 4가지 방향으로만 움직일 수 있으며, 0이 적힌 방은 들어갈 수 없다.

비밀번호의 힌트는 다음과 같다.

1. 임의의 방에서 다른 방으로 이동할 때는 항상 두 방 사이의 최단 경로로 이동한다.
2. 1번을 만족하는 경로 중 가장 긴 경로의 시작 방과 끝 방에 적힌 숫자의 합  
만약 위 2가지 조건을 만족하는 경로가 여러 개라면, 시작 방과 끝 방에 적힌 숫자의 합이 가장 큰 값이 비밀번호가 된다.

시작 방과 끝 방은 동일한 위치일 수도 있다.

<예시> 
$5 \times 5$ 형태의 지도가 주어질 때, 위의 2가지 조건을 만족하는 경로는 다음과 같다.

![이미지](https://upload.acmicpc.net/9b335e35-1fb0-494d-b517-a0480eb097a9/-/preview/0)

이 때 비밀번호가 무엇인지를 구해라.

만약 비밀번호를 만들 수 없는 경우 0을 출력한다.
### **입력**
첫줄에 지도의 세로 크기 
$N$(
$1 \le N \le 50$), 가로 크기 
$M$(
$1 \le M \le 50$)이 공백을 두고 주어진다.

둘째 줄부터 
$N$줄에 걸쳐 각 방들의 정보 
$A$(
$0 \le A \le 9$)가 공백을 두고 주어진다.
### **출력**
올바른 비밀번호를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5
1 2 3 4 5
0 0 4 0 0
0 0 5 0 0
8 7 6 7 8
9 0 7 0 0
```

**예제 출력1**

```
14
```

**예제 입력2**

```
2 2
1 2
3 4
```

**예제 출력2**

```
5
```

**예제 입력3**

```
5 6
2 0 7 4 0 2
0 8 5 0 3 0
6 9 5 7 7 2
6 9 3 9 9 7
0 8 7 4 0 3
```

**예제 출력3**

```
7
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_dist = -1
max_sum = 0

for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            continue

        visited = [[-1] * M for _ in range(N)]
        visited[i][j] = 0
        q = deque([(i, j)])

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < M:
                    if table[nx][ny] and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

        dist = visited[x][y]
        if dist == max_dist:
            max_dist = dist
            max_sum = max(max_sum, table[i][j] + table[x][y])
        
        elif dist > max_dist:
            max_dist = dist
            max_sum = table[i][j] + table[x][y]

print(max_sum if max_dist != -1 else 0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|116608|760|PyPy3|1032
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

max_path_cnt = -1
max_password = -1
for i in range(N):
    for j in range(M):
        if not lst[i][j]:
            continue

        q = [(i, j)]
        used = [[0] * M for _ in range(N)]
        used[i][j] = 1

        while q:
            nq = []

            for y, x in q:
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                        used[ny][nx] = used[y][x] + 1
                        q.append((ny, nx))

            q = nq

        path_cnt = used[y][x]
        password = lst[i][j] + lst[y][x]

        if path_cnt == 1:
            continue

        if max_path_cnt < path_cnt or (max_path_cnt == path_cnt and max_password < password):
            max_path_cnt = path_cnt
            max_password = password

print(max_password if max_password > 0 else 0)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
celpegor216|117644|588|PyPy3|1022
#### **📝해설**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 최대 거리
max_dist = -1

# 최대 숫자 합
max_sum = 0

# 모든 좌표를 확인하면서
for i in range(N):
    for j in range(M):

        # 시작할 수 없는 곳이라면 넘어감
        if table[i][j] == 0:
            continue
        
        # 끝부분이 최대숫자여도 최대값을 넘지 못한다면 넘어감
        if table[i][j] + 9 < max_sum:
            continue
        
        # 방문 여부 저장 및 거리가 얼마나 떨어져있는지 저장
        visited = [[-1] * M for _ in range(N)]

        # 시작위치 초기화
        visited[i][j] = 0
        q = deque([(i, j)])

        # BFS 시작
        while q:
            x, y = q.popleft()

            # 현재 위치 기준 상하좌우 확인
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                # 인덱스를 벗어나지 않으면서
                if 0 <= nx < N and 0 <= ny < M:
                    # 방문한적없고 방문 가능한 곳을 방문
                    if table[nx][ny] and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

        # BFS가 끝난곳 기준으로 확인
        dist = visited[x][y]

        # 현재 위치가 이전 최대거리와 같다면
        if dist == max_dist:
            max_dist = dist

            # 합 갱신이 가능하다면 갱신
            max_sum = max(max_sum, table[i][j] + table[x][y])
        
        # 현재 위치가 이전 최대거리보다 크다면
        elif dist > max_dist:
            max_dist = dist
            # 합을 이번 값으로 바꿈
            max_sum = table[i][j] + table[x][y]

print(max_sum if max_dist != -1 else 0)
```