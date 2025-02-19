# [3055] 탈출

### **난이도**
골드 4
## **📝문제**
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.
### **입력**
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.
### **출력**
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
D.*
...
.S.
```

**예제 출력1**

```
3
```

**예제 입력2**

```
3 3
D.*
...
..S
```

**예제 출력2**

```
KAKTUS
```

**예제 입력3**

```
3 6
D...*.
.X.X..
....S.
```

**예제 출력3**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
water = []
visited = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if table[i][j] == "S":
            q.append((i, j, 0))
            visited[i][j] = True
        elif table[i][j] == "*":
            water.append((i, j))

while q:

    new_water = []
    new_queue = deque()

    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and table[nx][ny] == ".":
                table[nx][ny] = "*"
                new_water.append((nx, ny))

    water = new_water
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if table[nx][ny] == "D":
                    print(count+1)
                    exit()
                elif table[nx][ny] == ".":
                    new_queue.append((nx, ny, count+1))
                    visited[nx][ny] = True

    q = new_queue

print("KAKTUS")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|114200|124|PyPy3|1201
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS를 위한 queue
q = deque()

# 물의 위치를 저장해둘 리스트
water = []

# 방문 여부를 저장할 리스트
visited = [[False] * C for _ in range(R)]

# 시작 정보를 저장
for i in range(R):
    for j in range(C):
        if table[i][j] == "S":
            q.append((i, j, 0))
            visited[i][j] = True
        elif table[i][j] == "*":
            water.append((i, j))

# BFS
while q:

    # 물의 다음 위치를 저장할 리스트
    new_water = []

    # 고슴도치의 다음 이동에서 가능한 위치를 저장할 queue
    new_queue = deque()

    # 모든 물을 탐색하면서
    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 퍼질 수 있는 위치로 물을 모두 퍼트림
            if 0 <= nx < R and 0 <= ny < C and table[nx][ny] == ".":
                table[nx][ny] = "*"
                new_water.append((nx, ny))

    # 새로운 물의 위치를 갱신
    water = new_water

    # 고슴도치 BFS
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:

                # 도착했다면 출력후 종료
                if table[nx][ny] == "D":
                    print(count+1)
                    exit()

                # 빈 공간으로 이동
                elif table[nx][ny] == ".":
                    new_queue.append((nx, ny, count+1))
                    visited[nx][ny] = True

    # 새롭게 queue를 갱신
    q = new_queue

# BFS를 통해 도착하지 못했다면 종료
print("KAKTUS")
```