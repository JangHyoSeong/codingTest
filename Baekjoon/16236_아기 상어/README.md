# [16236] 아기 상어

### **난이도**
골드 3
## **📝문제**
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

- 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.  
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
### **입력**

첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

- 0: 빈 칸
- 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
- 9: 아기 상어의 위치  
아기 상어는 공간에 한 마리 있다.
### **출력**
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
3
0 0 0
0 0 0
0 9 0
```

**예제 출력1**

```
0
```

**예제 입력2**

```
3
0 0 1
0 0 0
0 9 0
```

**예제 출력2**

```
3
```

**예제 입력3**

```
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
```

**예제 출력3**

```
14
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

def find_shark():
    # 상어의 위치를 찾음
    for i in range(N):
        for j in range(N):
            if table[i][j] == 9:
                # 상어가 있던 위치는 0으로 초기화
                table[i][j] = 0
                # 현재 위치, 현재 크기, 먹은 물고기 수
                return [i, j, 2, 0]
shark = find_shark()

# 동서남북 한칸씩 이동하기 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 상어의 초기위치를 deque에 삽입, 물고기를 먹기까지의 이동횟수가 됨
q = deque([(shark[0], shark[1], 0)])

# 총 이동횟수
count = 0
# 방문 여부를 나타내는 리스트   
visited = [[False] * N for _ in range(N)]
visited[shark[0]][shark[1]] = True

# 현재 같은 거리에 있고, 먹을 수 있는 물고기 정보를 저장할 리스트
can_eat = []

# BFS
while q or can_eat:
    # 현재위치, 현재 먹기까지 이동횟수
    if q:
        x, y, temp_count = q.popleft()

    # 만약 먹을 수 있는 물고기가 있다면
    # 그 물고기를 먹기까지의 거리가 현재 이동거리보다 짧다면
    # 혹은 q가 비어서 더이상 이동할 곳이 없는데 먹을 물고기가 있다면
    if can_eat and (can_eat[0][2] < temp_count or q == deque()):
        # 먹는 로직을 수행할것임
        # 일단 먹을 수 있는 물고기중 하나를 빼서 먹을 물고기로 저장
        left_top = can_eat.pop()

        # 먹을 수 있는 물고기를 모두 순회하면서
        while can_eat:
            # 맨 위 왼쪽에 있는 물고기를 left_top에 저장
            temp_eat = can_eat.pop()
            if left_top[0] > temp_eat[0]:
                left_top = temp_eat
            elif left_top[0] == temp_eat[0]:
                if left_top[1] > temp_eat[1]:
                    left_top = temp_eat
        
        
        # 먹을 물고기를 정하고 나면, 그 위치를 0으로 초기화
        table[left_top[0]][left_top[1]] = 0

        # 하나 먹음
        shark[3] += 1
        
        # 먹어서 현재 사이즈와 같아졌다면 사이즈를 증가하고, 먹은 숫자를 0으로 초기화
        if shark[3] == shark[2]:
            shark[2] += 1
            shark[3] = 0

        # q를 현재위치부터 다시 시작
        q = deque([(left_top[0], left_top[1], 0)])
        
        # 현재 물고기를 먹기까지의 이동 횟수를 총 이동횟수에 더해줌
        count += left_top[2]
        # 방문 여부 리스트 다시 초기화
        visited = [[False] * N for _ in range(N)]
        visited[left_top[0]][left_top[1]] = True
        continue

    # 현재 위치가 먹을 수 있는 물고기라면 can_eat에 넣어줌
    if table[x][y] != 0 and table[x][y] < shark[2]:
        can_eat.append([x, y, temp_count])


    # 다음 위치로 탐색을 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 방문 가능한 위치면 q에 삽입
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if table[nx][ny] <= shark[2]:
                q.append((nx, ny, temp_count+1))
                visited[nx][ny] = True

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|114160|168|PyPy3|3290
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
def find_init_pos(N, M):
    for i in range(N):
        for j in range(N):
            if M[i][j] == 9:
                return i, j


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def search_prey(N, M, size, current_pos):
    stack, stack_, prey = [current_pos], [], []
    dist = 0
    visited = set()
    while stack and not prey:
        dist += 1
        for (x, y) in stack:
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for (i, j) in direction:
                x_, y_ = x + i, y + j
                if (0 <= x_ < N) and (0 <= y_ < N):
                    if 0 < M[x_][y_] < size:
                        prey.append((x_, y_))
                    elif M[x_][y_] == 0 or M[x_][y_] == size:
                        stack_.append((x_, y_))
        stack = stack_
        stack_ = []
    if prey:
        prey.sort()
        return prey[0], dist
    else:
        return None, 0


def hunt():
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    pos = find_init_pos(N, M)
    M[pos[0]][pos[1]] = 0
    time, size, eat = 0, 2, 0
    while True:
        pos, dist = search_prey(N, M, size, pos)
        if pos is None:
            break
        M[pos[0]][pos[1]] = 0
        time += dist
        eat += 1
        if size == eat:
            size += 1
            eat = 0
    print(time)


hunt()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jeuk|30616|36|Python3|1387

### **🔖정리**

1. 메모리 초과를 방지하기 위해 방문 처리는 q에 삽입할 때 하는 것이 좋다