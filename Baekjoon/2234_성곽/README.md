# [2234] 성곽

### **난이도**
골드 3
## **📝문제**
![이미지](https://www.acmicpc.net/JudgeOnline/upload/201008/cas.PNG)
대략 위의 그림과 같이 생긴 성곽이 있다. 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로를 나타낸다. 이러한 형태의 성의 지도를 입력받아서 다음을 계산하는 프로그램을 작성하시오.

1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
위의 예에서는 방은 5개고, 가장 큰 방은 9개의 칸으로 이루어져 있으며, 위의 그림에서 화살표가 가리키는 벽을 제거하면 16인 크기의 방을 얻을 수 있다.

성은 M × N(1 ≤ M, N ≤ 50)개의 정사각형 칸으로 이루어진다. 성에는 최소 두 개의 방이 있어서, 항상 하나의 벽을 제거하여 두 방을 합치는 경우가 있다.
### **입력**
첫째 줄에 두 정수 N, M이 주어진다. 다음 M개의 줄에는 N개의 정수로 벽에 대한 정보가 주어진다. 벽에 대한 정보는 한 정수로 주어지는데, 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다. 참고로 이진수의 각 비트를 생각하면 쉽다. 따라서 이 값은 0부터 15까지의 범위 안에 있다.
### **출력**
첫째 줄에 1의 답을, 둘째 줄에 2의 답을, 셋째 줄에 3의 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
```

**예제 출력1**

```
5
9
16
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]

# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direction_bit = [1, 2, 4, 8]

room_size = []
room_id = 1

for i in range(M):
    for j in range(N):
        if visited[i][j] != 0:
            continue

        q = deque([(i, j)])
        visited[i][j] = room_id
        size = 1
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < M and 0 <= ny < N:
                    if not (table[x][y] & direction_bit[d]) and visited[nx][ny] == 0:
                        visited[nx][ny] = room_id
                        q.append((nx, ny))
                        size += 1
        
        room_size.append(size)
        room_id += 1

max_after_removal = 0

for i in range(M):
    for j in range(N):
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < M and 0 <= nj < N:
                if visited[i][j] != visited[ni][nj]:
                    combined = room_size[visited[i][j] - 1] + room_size[visited[ni][nj] - 1]
                    max_after_removal = max(max_after_removal, combined)

print(len(room_size))
print(max(room_size))
print(max_after_removal)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35016|72|Python3|1366
#### **📝해설**

**알고리즘**
```
1. 비트마스킹
2. BFS
```

### **다른 풀이**

```python
n, m = map(int, input().split())

wall = []
dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

for _ in range(m):
    l = list(map(int, input().split()))
    wall.append(l)

visited = [[0] * n for _ in range(m)]
roomCnt = 0
maxRoomSize = 0

def dfs(x, y):
    roomSize = 0
    stack = []
    stack.append((x, y))

    while stack:
        roomSize += 1
        curX, curY = stack[-1]
        stack.pop()

        wallNum = wall[curX][curY]

        for i in range(4):
            if wallNum % 2 == 0:
                nextX = curX + dir[i][0]
                nextY = curY + dir[i][1]

                if not visited[nextX][nextY]:
                    visited[nextX][nextY] = roomCnt
                    stack.append((nextX, nextY))

            wallNum //= 2

    return roomSize

roomCntArray = [0]

for x in range(m):
    for y in range(n):
        if not visited[x][y]:
            roomCnt += 1
            visited[x][y] = roomCnt
            roomSize = dfs(x, y)
            roomCntArray.append(roomSize)
            maxRoomSize = max(maxRoomSize, roomSize)

dir = [[0, 1], [1, 0]]
maxAddRoomSize = 0

for x in range(m):
    for y in range(n):
        for dx, dy in dir:
            nearX = x + dx
            nearY = y + dy

            if 0 <= nearX < m and 0 <= nearY < n and visited[x][y] != visited[nearX][nearY]:
                roomSize1 = roomCntArray[visited[x][y]]
                roomSize2 = roomCntArray[visited[nearX][nearY]]
                maxAddRoomSize = max(maxAddRoomSize, roomSize1 + roomSize2)

print(roomCnt)
print(maxRoomSize)
print(maxAddRoomSize)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
chldbswl9|31120|36|Python3|1565
#### **📝해설**

```python
from collections import deque

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

# 현재 어느 방인지 저장할 이차원 리스트
visited = [[0] * N for _ in range(M)]

# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direction_bit = [1, 2, 4, 8]

# 방의 크기를 저장할 리스트
room_size = []

# 1번 방부터 시작해서, 어느 방인지 확인하기 위한 변수
room_id = 1

# 모든 위치를 순회하면서
for i in range(M):
    for j in range(N):

        # 이미 방으로 확인된 경우 넘어감
        if visited[i][j] != 0:
            continue
        
        # 현재 위치부터 BFS
        q = deque([(i, j)])

        # 현재 방 번호
        visited[i][j] = room_id

        # 현재 방 크기
        size = 1

        # 위치부터 BFS 시작
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                # 상하좌우 인덱스를 벗어나지 않으면서
                if 0 <= nx < M and 0 <= ny < N:

                    # 벽이 없는 곳으로만 이동하고, 방문한 적 없었던 곳만 방문
                    if not (table[x][y] & direction_bit[d]) and visited[nx][ny] == 0:
                        visited[nx][ny] = room_id
                        q.append((nx, ny))
                        size += 1
        
        # BFS가 끝난 후에 방 크기를 저장
        room_size.append(size)

        # 다음 방 번호를 부여
        room_id += 1

# 벽을 허물었을 때 최대 크기
max_after_removal = 0

# 모든 위치를 확인하면서
for i in range(M):
    for j in range(N):
        for d in range(4):

            # 상하좌우 모든 벽을 확인
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < M and 0 <= nj < N:
                # 옆의 칸이 다른 방인 경우 허물어봄
                if visited[i][j] != visited[ni][nj]:
                    combined = room_size[visited[i][j] - 1] + room_size[visited[ni][nj] - 1]
                    max_after_removal = max(max_after_removal, combined)

# 출력
print(len(room_size))
print(max(room_size))
print(max_after_removal)
```