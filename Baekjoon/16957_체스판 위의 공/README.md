# [16957] 체스판 위의 공

### **난이도**
골드 3
## **📝문제**
크기가 R×C인 체스판이 있고, 체스판의 각 칸에는 정수가 하나씩 적혀있다. 체스판에 적혀있는 정수는 모두 서로 다르다.

체스판의 각 칸 위에 공을 하나씩 놓는다. 이제 공은 다음과 같은 규칙에 의해서 자동으로 움직인다.

- 인접한 8방향 (가로, 세로, 대각선)에 적힌 모든 정수가 현재 칸에 적힌 수보다 크면 이동을 멈춘다.
- 그 외의 경우에는 가장 작은 정수가 있는 칸으로 공이 이동한다.

공의 크기는 매우 작아서, 체스판의 한 칸 위에 여러 개의 공이 있을 수 있다. 체스판의 상태가 주어진다. 공이 더 이상 움직이지 않을 때, 각 칸에 공이 몇 개 있는지 구해보자.
### **입력**
첫째 줄에 체스판의 크기 R, C가 주어진다. 둘째 줄부터 R개의 줄에 체스판에 적혀있는 정수가 주어진다.
### **출력**
총 R개의 줄에 걸쳐서 체스판에 적힌 정수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1 3 4
5 6 7
8 9 2
```

**예제 출력1**

```
6 0 0
0 0 0
0 0 3
```

**예제 입력2**

```
1 6
10 20 3 4 5 6
```

**예제 출력2**

```
1 0 5 0 0 0
```

**예제 입력3**

```
4 4
20 2 13 1
4 11 10 35
3 12 9 7
30 40 50 5
```

**예제 출력3**

```
0 4 0 4
0 0 0 0
4 0 0 0
0 0 0 4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(1_000_000)

R, C = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]
answer = [[0] * C for _ in range(R)]
destination = [[(-1, -1) for _ in range(C)] for _ in range(R)]

direction = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def dfs(x, y):
    if destination[x][y] != (-1, -1):
        return destination[x][y]
    
    min_val = table[x][y]
    move_x, move_y = -1, -1

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if table[nx][ny] < min_val:
                min_val = table[nx][ny]
                move_x, move_y = nx, ny

    if move_x == -1:
        destination[x][y] = (x, y)
    else:
        destination[x][y] = dfs(move_x, move_y)

    return destination[x][y]

for i in range(R):
    for j in range(C):
        x, y = dfs(i, j)
        answer[x][y] += 1

for row in answer:
    print(" ".join(map(str, row)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|48712|544|Python3|983
#### **📝해설**

**알고리즘**
```
1. DP
2. 메모이제이션
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

class union:
    def __init__(self, size = 10**6):
        self.l = [i for i in range(size)]
        
    def find(self, i):
        if self.l[i] == i:
            return i
        self.l[i] = self.find(self.l[i])
        return self.l[i]
    
    def union(self, i, j):
        self.l[self.find(j)] = self.find(i)
        return

r, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(r)]

u = union(r*c)
dm = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
for y in range(r):
    for x in range(c):
        mv = 1 << 30
        mui = 0
        for k in range(8):
            xv, yv = dm[k]
            if not (0 <= x+xv < c and 0 <= y+yv < r):
                continue
            if l[y+yv][x+xv] < mv:
                mv = l[y+yv][x+xv]
                mui = (y+yv)*c+(x+xv)
        if mv < l[y][x]:
            u.union(mui, y*c+x)

ol = [[0] * c for i in range(r)]
for i in range(r*c):
    x = u.find(i)
    ol[x//c][x%c] += 1
for i in ol:
    print(*i)

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yyyy7089|118264|232|PyPy3|1051
#### **📝해설**

```python
import sys
sys.setrecursionlimit(1_000_000)

# 입력받기
R, C = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]

# 해당위치에 마지막에 공이 몇개있는지 저장할 리스트
answer = [[0] * C for _ in range(R)]

# 해당 칸의 마지막 목적지가 어디인지 저장할 리스트
destination = [[(-1, -1) for _ in range(C)] for _ in range(R)]

# 인접한 칸을 탐색하기 위한 리스트
direction = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

# DFS를 통해 (x, y)에서 출발 후 어디로 도착하는지 검사
def dfs(x, y):

    # 해당 위치의 도착지가 이미 계산되어있다면 그 위치를 리턴
    if destination[x][y] != (-1, -1):
        return destination[x][y]
    
    # 아직 탐색하지 않은 칸이라면 탐색 시작

    # 인접한 칸 중 가장 작은 값을 저장할 변수
    min_val = table[x][y]

    # 다른 칸으로 이동하는 경우 그 방향
    move_x, move_y = -1, -1

    # 인접한 칸을 모두 검사하면서
    for dx, dy in direction:
        nx, ny = x + dx, y + dy

        # 인덱스를 벗어나지 않고
        if 0 <= nx < R and 0 <= ny < C:

            # 현재 칸보다 더 작다면
            if table[nx][ny] < min_val:

                # 그 값을 저장
                min_val = table[nx][ny]
                move_x, move_y = nx, ny

    # 현재 칸이 인접한 칸중 가장 작다면
    if move_x == -1:

        # 현재 위치가 마지막 위치
        destination[x][y] = (x, y)
    
    # 이동할 칸이 있다면
    else:

        # 그 칸으로 이동해서 새로 DFS
        destination[x][y] = dfs(move_x, move_y)

    # 마지막 목적지를 리턴
    return destination[x][y]

# 모든 칸을 확인하면서
for i in range(R):
    for j in range(C):

        # 해당 칸의 목적지에 답을 + 1
        x, y = dfs(i, j)
        answer[x][y] += 1

# 결과 출력
for row in answer:
    print(" ".join(map(str, row)))
```