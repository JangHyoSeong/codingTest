# [1584] 게임

### **난이도**
골드 5
## **📝문제**
세준이는 위험한 지역에서 탈출하는 게임을 하고 있다. 이 게임에는 세준이가 들어갈 수 없는 죽음의 구역이 있고, 들어가서 한 번 움직일 때 마다 생명이 1씩 소모되는 위험한 구역이 있다. 그리고, 자유롭게 생명의 위협없이 움직일 수 있는 안전한 구역이 있다. (안전한 구역은 죽음의 구역과 위험한 구역을 제외한 나머지 이다.)

세준이는 (0, 0)에서 출발해서 (500, 500)으로 가야 한다. 세준이는 위, 아래, 오른쪽, 왼쪽으로만 이동할 수 있다. 현재 세준이는 (0, 0)에 있다. 그리고, 게임 판을 벗어날 수는 없다.

세준이가 (0, 0)에서 (500, 500)으로 갈 때 잃는 생명의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 위험한 구역의 수 N이 주어진다. 다음 줄부터 N개의 줄에는 X1 Y1 X2 Y2와 같은 형식으로 위험한 구역의 정보가 주어진다. (X1, Y1)은 위험한 구역의 한 모서리이고, (X2, Y2)는 위험한 구역의 반대 모서리이다. 그 다음 줄에는 죽음의 구역의 수 M이 주어진다. 다음 줄부터 M개의 줄에는 죽음의 구역의 정보가 위험한 구역의 정보와 같이 주어진다. 주어지는 구역은 모두 겹칠 수 있으며, 서로 다른 구역이 겹칠 때는, 더 심한 구역이 해당된다. 예를 들어, 죽음+위험 = 죽음, 위험+안전 = 위험, 위험+위험 = 위험, 죽음+안전 = 죽음이다. 위험한 구역이 아무리 겹쳐도 생명은 1씩 감소된다. 생명의 감소는 구역에 들어갈 때만, 영향을 미친다. 예를 들어, (500, 500)이 위험한 구역일 때는, (500, 500)에 들어갈 때, 생명이 1 감소되지만, (0, 0)이 위험한 구역이더라도 생명은 감소되지 않는다. 마찬가지로, (0, 0)이 죽음의 구역이더라도 세준이는 이미 그 곳에 있으므로 세준이에게 영향을 미치지 않는다. N과 M은 50보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 정답을 출력한다. 만약 (500, 500)으로 갈 수 없을 때는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
1
500 0 0 500
1
0 0 0 0
```

**예제 출력1**

```
1000
```

**예제 입력2**

```
0
0
```

**예제 출력2**

```
0
```

**예제 입력3**

```
2
0 0 250 250
250 250 500 500
2
0 251 249 500
251 0 500 249
```

**예제 출력3**

```
1000
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

table = [[0] * 501 for _ in range(501)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            table[i][j] = -1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            table[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[int(21e8)] * 501 for _ in range(501)]

dist[0][0] = 0
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 500 and 0 <= ny <= 500:
            if table[nx][ny] == 1:
                continue

            cost = 1 if table[nx][ny] == -1 else 0
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost

                if cost == 0:
                    q.appendleft((nx, ny))
                else:
                    q.append((nx, ny))

print(dist[500][500] if dist[500][500] != int(21e8) else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|48708|836|Python3|1182
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
from collections import deque

INF = 1000000000

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
map_grid = [[0] * 501 for _ in range(501)]
visit = [[0] * 501 for _ in range(501)]

def bfs():
    dq = deque()
    dq.append((0, 0, 0))

    while dq:
        x, y, dmg = dq.popleft()

        if x == 500 and y == 500:
            print(dmg)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ndmg = dmg

            if nx < 0 or ny < 0 or nx > 500 or ny > 500:
                continue
            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if map_grid[nx][ny] == 1:
                    dq.append((nx, ny, ndmg + 1))
                else:
                    dq.appendleft((nx, ny, ndmg))

    print(-1)

def main():
    n = int(input())
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                map_grid[i][j] = 1

    m = int(input())
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                visit[i][j] = 1

    bfs()

if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
nicejun|129240|168|PyPy3|1450
#### **📝해설**

```python
from collections import deque

# 죽음, 위험 땅을 구분할 테이블
table = [[0] * 501 for _ in range(501)]

# 위험땅 입력
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            table[i][j] = -1

# 죽음땅 입력
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            table[i][j] = 1

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# i, j까지 도달할때 최소 생명력 소모
dist = [[int(21e8)] * 501 for _ in range(501)]

# 시작지점
dist[0][0] = 0
q = deque()
q.append((0, 0))

# BFS 시작
while q:
    x, y = q.popleft()

    # 상하좌우를 탐색하면서
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 500 and 0 <= ny <= 500:
            # 죽음의 땅은 고려하지 않음
            if table[nx][ny] == 1:
                continue
            
            # 위험한 경우 +1
            cost = 1 if table[nx][ny] == -1 else 0

            # 더 적은 생명력으로 이동가능하다면 이동
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost

                # 위험하지 않은 곳으로 이동하는경우
                if cost == 0:

                    # q의 왼쪽에 삽입해서 우선탐색
                    q.appendleft((nx, ny))

                # 아니라면 평범하게 BFS
                else:
                    q.append((nx, ny))

# 출력
print(dist[500][500] if dist[500][500] != int(21e8) else -1)
```