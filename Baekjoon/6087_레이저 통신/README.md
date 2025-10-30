# [6087] 레이저 통신

### **난이도**
골드 3
## **📝문제**
크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.

'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.

레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.

아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.
```
7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . * . .         2 . . . . * | .
1 . C . . * . .         1 . C . . * | .
0 . . . . . . .         0 . \-------/ .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
```
### **입력**
첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)

둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.

- .: 빈 칸
- *: 벽
- C: 레이저로 연결해야 하는 칸

'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.
### **출력**
첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......
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

INF = int(21e8)

W, H = map(int, input().split())
table = [list(input()) for _ in range(H)]

points = []
for i in range(H):
    for j in range(W):
        if table[i][j] == "C":
            points.append((i, j))

start, end = points

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
q = deque()

for d in range(4):
    dist[start[0]][start[1]][d] = 0
    q.append((start[0], start[1], d))

while q:
    x, y, dir = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < H and 0 <= ny < W:
            if table[nx][ny] == "*":
                continue

            add = 0 if dir == d else 1

            if dist[nx][ny][d] > dist[x][y][dir] + add:
                dist[nx][ny][d] = dist[x][y][dir] + add

                if add == 0:
                    q.appendleft((nx, ny, d))
                else:
                    q.append((nx, ny, d))

print(min(dist[end[0]][end[1]]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34992|144|Python3|1022
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
import heapq
input = sys.stdin.readline


def updateCntMaps(cnt, y, x):
    # 직선으로 쭉 나아감
    for i in range(4):      # 4방향으로
        dirY, dirX = dir[i]
        curY, curX = y, x
        while True:     # 쭉 나아감
            nextY, nextX = curY + dirY, curX + dirX
            if 0 <= nextY < h and 0 <= nextX < w:
                match maps[nextY][nextX]:
                    case '.':       # 빈 칸
                        if cntMaps[nextY][nextX] > cnt or \
                        (cntMaps[nextY][nextX] == cnt and chkMaps[i % 2][nextY][nextX] == False):        # 만약 기존의 거울 개수보다 적거나 같게 사용한다면
                            cntMaps[nextY][nextX] = cnt
                            chkMaps[i % 2][nextY][nextX] = True        # 방문 표시
                            heapq.heappush(hq, (cnt, nextY, nextX))
                            curY, curX = nextY, nextX       # 한 쪽으로 쭉 나아가기 위해
                        else:
                            break
                    case '*':
                        break
                    case 'C':
                        print(cnt)
                        exit(0)
            else:
                break


if __name__ == "__main__":
    w, h = map(int, input().split())
    maps = [list(input().strip()) for _ in range(h)]
    cntMaps = [[sys.maxsize] * w for _ in range(h)]      # 거울의 개수 체크
    chkMaps = [[[False]  * w for _ in range(h)] for _ in range(2)]      # 방문 체크, [0]은 수직, [1]은 수평
    hq = []
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'C':
                heapq.heappush(hq, (-1, i, j))
                maps[i][j] = '*'        # 벽으로 만듬

                # 다익스트라 알고리즘
                while hq:
                    cnt, y, x = heapq.heappop(hq)
                    updateCntMaps(cnt + 1, y, x)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
lunearave07|33220|44|Python3|1993
#### **📝해설**

```python
from collections import deque

INF = int(21e8)

W, H = map(int, input().split())
table = [list(input()) for _ in range(H)]

# 시작점과 도착점 찾기
points = []
for i in range(H):
    for j in range(W):
        if table[i][j] == "C":
            points.append((i, j))

start, end = points

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# dist[x][y][dir] : x, y위치에서 dir 방향으로 이동 할 때 방향전환을 한 최소 횟수
dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]

# BFS를 위한 deque
q = deque()

# 시작점부터 4방향으로 모두 움직이는 것을 큐에 삽입
for d in range(4):
    dist[start[0]][start[1]][d] = 0
    q.append((start[0], start[1], d))

# BFS
while q:
    x, y, dir = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 인덱스를 벗어나지 않고
        if 0 <= nx < H and 0 <= ny < W:

            # 벽이라면 고려하지 않음
            if table[nx][ny] == "*":
                continue
            
            # 현재 이동방향과 같다면 방향전환횟수를 0, 다르다면 1 추가
            add = 0 if dir == d else 1
            
            # 만약 더 낮은 방향전환으로 이동할 수 있었다면
            if dist[nx][ny][d] > dist[x][y][dir] + add:

                # 갱신
                dist[nx][ny][d] = dist[x][y][dir] + add

                # 이번에 방향전환이 이루어지지 않았다면
                if add == 0:

                    # deque의 맨 앞에 삽입(최적화)
                    q.appendleft((nx, ny, d))
                else:
                    q.append((nx, ny, d))

# 가장 최소횟수로 도착점에 도착한 경우를 출력
print(min(dist[end[0]][end[1]]))
```