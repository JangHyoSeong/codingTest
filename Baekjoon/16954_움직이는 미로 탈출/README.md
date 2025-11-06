# [16954] 움직이는 미로 탈출

### **난이도**
골드 3
## **📝문제**
욱제는 학교 숙제로 크기가 8×8인 체스판에서 탈출하는 게임을 만들었다. 체스판의 모든 칸은 빈 칸 또는 벽 중 하나이다. 욱제의 캐릭터는 가장 왼쪽 아랫 칸에 있고, 이 캐릭터는 가장 오른쪽 윗 칸으로 이동해야 한다.

이 게임의 특징은 벽이 움직인다는 점이다. 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 아래에 행이 없다면 벽이 사라지게 된다. 욱제의 캐릭터는 1초에 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있다. 이동할 때는 빈 칸으로만 이동할 수 있다.

1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다. 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.

욱제의 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해보자.
### **입력**
8개 줄에 걸쳐서 체스판의 상태가 주어진다. '.'은 빈 칸, '#'는 벽이다. 가장 왼쪽 아랫칸은 항상 벽이 아니다.
### **출력**
욱제의 캐릭터가 가장 오른쪽 윗 칸에 도착할 수 있으면 1, 없으면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
........
........
........
........
........
........
........
........
```

**예제 출력1**

```
1
```

**예제 입력2**

```
........
........
........
........
........
........
##......
........
```

**예제 출력2**

```
0
```

**예제 입력3**

```
........
........
........
........
........
.#......
#.......
.#......
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

board = [list(input()) for _ in range(8)]

walls = set()
for i in range(8):
    for j in range(8):
        if board[i][j] == "#":
            walls.add((i, j))

q = deque()
q.append((7, 0))

while True:

    visited = [[False] * 8 for _ in range(8)]
    new_q = deque()

    while q:
        x, y = q.popleft()
        
        if (x, y) in walls:
            continue

        if x == 0 and y == 7:
            print(1)
            exit()

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:
                    if (nx, ny) not in walls:
                        new_q.append((nx, ny))
                        visited[nx][ny] = True
    q = new_q
    if not new_q:
        break
    
    new_walls = set()

    for wall in walls:
        if wall[0] == 7:
            continue

        new_walls.add((wall[0]+1, wall[1]))
    walls = new_walls

print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34976|56|Python3|1008
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
def bfs():
    while True:
        Okjae = []
        hashs = []
        for i in range(8):
            for j in range(8):
                if graph[i][j] == 'O':
                    Okjae.append((i, j))
                elif graph[i][j] == '#':
                    hashs.append((i, j))

        if len(Okjae) == 0:
            return False

        for x, y in Okjae:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and graph[nx][ny] == '.':
                    graph[nx][ny] = 'O'
                    if nx == 0 and ny == 7:
                        return True
        hashs.sort(reverse=True)
        for x, y in hashs:
            if x < 7:
                graph[x + 1][y] = '#'
                graph[x][y] = '.'
            else:
                graph[x][y] = '.'


graph = [list(input()) for _ in range(8)]
graph[7][0] = 'O'

if bfs():
    print(1)
else:
    print(0)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
juwon0208|31120|32|Python3|1009
#### **📝해설**

```python
from collections import deque

# 미로 입력받기
board = [list(input()) for _ in range(8)]

# 벽의 위치를 set로 저장
walls = set()
for i in range(8):
    for j in range(8):
        if board[i][j] == "#":
            walls.add((i, j))

# BFS를 위한 큐 선언
q = deque()
q.append((7, 0))

# 일단 무한반복
while True:

    # 현재 단계에서 방문했던 위치를 저장
    visited = [[False] * 8 for _ in range(8)]

    # 현재위치에서 갈 수 있는 곳을 새로운 큐로 저장
    new_q = deque()

    # 벽이 이동하기 전에 먼저 BFS
    while q:
        x, y = q.popleft()
        
        # 이미 벽이랑 겹쳐있다면 고려하지 않음
        if (x, y) in walls:
            continue
        
        # 도착했다면 종료
        if x == 0 and y == 7:
            print(1)
            exit()

        # 현재위치에서 인접한 칸, 제자리를 탐색
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy

                # 인덱스를 벗어나지 않았고, 이번 BFS에서 아직 방문하지 않았다면
                if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:

                    # 방문할 위치에 벽이 없다면 방문
                    if (nx, ny) not in walls:
                        new_q.append((nx, ny))
                        visited[nx][ny] = True
    
    # 다음 방문할 위치로 큐를 초기화
    q = new_q

    # 만약 이번에 아무곳도 방문할 수 없었다면, 도착지에 도착할 수 없으니 종료
    if not new_q:
        break
    
    # 벽을 이동한 뒤 위치를 저장할 set
    new_walls = set()

    # 모든 벽의 위치를 확인하면서
    for wall in walls:

        # 벽이 아래에 도착했다면 사라짐
        if wall[0] == 7:
            continue
        
        # 새로운 벽은 한칸씩 내려감
        new_walls.add((wall[0]+1, wall[1]))
    walls = new_walls

# 출력
print(0)
```