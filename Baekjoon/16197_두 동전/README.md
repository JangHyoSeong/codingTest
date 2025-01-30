# [16197] 두 동전

### **난이도**
골드 4
## **📝문제**
N×M 크기의 보드와 4개의 버튼으로 이루어진 게임이 있다. 보드는 1×1크기의 정사각형 칸으로 나누어져 있고, 각각의 칸은 비어있거나, 벽이다. 두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.

버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다. 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동하게 된다.

- 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.  
- 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.  
- 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.  
두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 20)

둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.

- o: 동전
- .: 빈 칸
- #: 벽  
동전의 개수는 항상 2개이다.
### **출력**
첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다. 만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
1 2
oo
```

**예제 출력1**

```
1
```

**예제 입력2**

```
6 2
.#
.#
.#
o#
o#
##
```

**예제 출력2**

```
4
```

**예제 입력3**

```
6 2
..
..
..
o#
o#
##
```

**예제 출력3**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

q = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)])
visited = set([(coins[0][0], coins[0][1], coins[1][0], coins[1][1])])

while q:
    x1, y1, x2, y2, count = q.popleft()
    
    if count >= 10:
        break
    
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        
        out1 = not (0 <= nx1 < N and 0 <= ny1 < M)
        out2 = not (0 <= nx2 < N and 0 <= ny2 < M)
        
        if out1 and out2:
            continue
        if out1 or out2:
            print(count + 1)
            exit()
        
        if not out1 and board[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if not out2 and board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        
        if (nx1, ny1, nx2, ny2) not in visited:
            visited.add((nx1, ny1, nx2, ny2))
            q.append((nx1, ny1, nx2, ny2, count + 1))

print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35016|64|Python3|1184
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

# 상하좌우 이동을 위한 리스트
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# 초기 동전의 위치를 입력
coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

# BFS를 위한 queue, 방문 여부를 저장할 집합을 하나 정의
q = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)]) # x1, y1, x2, y2, 이동횟수
visited = set([(coins[0][0], coins[0][1], coins[1][0], coins[1][1])])

# BFS 시작
while q:
    x1, y1, x2, y2, count = q.popleft()
    
    # 이동횟수가 10번을 넘으면 종료
    if count >= 10:
        break
    
    # 상하좌우를 탐색
    for i in range(4):

        # 새로운 좌표 정의
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        
        # 보드를 벗어나는지 여부를 저장
        out1 = not (0 <= nx1 < N and 0 <= ny1 < M)
        out2 = not (0 <= nx2 < N and 0 <= ny2 < M)

        # 둘다 벗어난다면 X        
        if out1 and out2:
            continue

        # 하나만 벗어난다면 출력 후 종료
        if out1 or out2:
            print(count + 1)
            exit()
        
        # 벽에 막힌다면 하나만 이동
        if not out1 and board[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if not out2 and board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        
        # 아직 방문하지 않은 케이스라면 새롭게 방문
        if (nx1, ny1, nx2, ny2) not in visited:
            visited.add((nx1, ny1, nx2, ny2))
            q.append((nx1, ny1, nx2, ny2, count + 1))

# 10번 이내로 조건을 만족하지 못하면 -1 출력
print(-1)
```