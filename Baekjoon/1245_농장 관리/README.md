# [1245] 농장 관리

### **난이도**
골드 5
## **📝문제**
농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.

산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. 여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이가 모두 1 이하인 경우이다. 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.

문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.
### **입력**
첫째 줄에 정수 N(1 < N ≤ 100), M(1 < M ≤ 70)이 주어진다. 둘째 줄부터 N+1번째 줄까지 각 줄마다 격자의 높이를 의미하는 M개의 정수가 입력된다. 격자의 높이는 500보다 작거나 같은 음이 아닌 정수이다.
### **출력**
첫째 줄에 산봉우리의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0
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

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

near = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
visited = [[False] * M for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        visited[i][j] = True
        q = deque([(i, j)])
        flag = True

        now_height = table[i][j]

        while q:
            x, y = q.popleft()

            for d in range(8):
                nx, ny = x + near[d][0], y + near[d][1]

                if 0 <= nx < N and 0 <= ny < M:

                    if table[nx][ny] > now_height:
                        flag = False

                    if table[nx][ny] == table[i][j] and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    
        
        if flag:
            count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34992|88|Python3|984
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(x, y):
    visited[y][x] = True
    is_peak = True
    
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if grid[ny][nx] > grid[y][x]:
                is_peak = False
            
            if not visited[ny][nx] and grid[ny][nx] == grid[y][x]:
                if not dfs(nx, ny):
                    is_peak = False
    
    return is_peak

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if dfs(j, i):
                cnt += 1

print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tenyver|31120|40|Python3|823
#### **📝해설**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 인접한 칸 탐색을 위한 리스트
near = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

# 방문 여부
visited = [[False] * M for _ in range(N)]

# 산봉우리 개수
count = 0

# 모든 칸을 확인하면서
for i in range(N):
    for j in range(M):

        # 이미 확인한 칸이면 넘어감
        if visited[i][j]:
            continue

        # 현재위치부터 BFS
        visited[i][j] = True
        q = deque([(i, j)])

        # 산봉우리인지 여부를 확인하는 변수
        flag = True

        # 현재 높이
        now_height = table[i][j]

        # BFS 시작
        while q:
            x, y = q.popleft()

            # 인접한 칸을 확인하면서
            for d in range(8):
                nx, ny = x + near[d][0], y + near[d][1]

                # 인덱스를 벗어나지 않는다면
                if 0 <= nx < N and 0 <= ny < M:
                    
                    # 인접한 칸이 더 높다면 산봉우리가 아님
                    if table[nx][ny] > now_height:
                        flag = False

                    # 높이가 같은 칸이 있다면 한 그룹으로 계속 BFS 검사
                    if table[nx][ny] == table[i][j] and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    
        # 산봉우리 증가
        if flag:
            count += 1

print(count)
```