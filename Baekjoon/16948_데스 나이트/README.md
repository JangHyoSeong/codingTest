# [16948] 데스 나이트

### **난이도**
실버 1
## **📝문제**
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.
### **입력**
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.
### **출력**
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
7
6 6 0 1
```

**예제 출력1**

```
4
```

**예제 입력2**

```
6
5 1 0 5
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
7
0 3 4 3
```

**예제 출력3**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
start_x, start_y, target_x, target_y = map(int, input().split())

moves = [
    (-2, -1),
    (-2, 1),
    (0, -2),
    (0, 2),
    (2, -1),
    (2, 1)
]

q = deque()
q.append((start_x, start_y, 0))

visited = [[False] * N for _ in range(N)]
visited[start_x][start_y] = True

while q:
    x, y, count = q.popleft()

    if x == target_x and y == target_y:
        print(count)
        break

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34044|96|Python3|675
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

N = int(input())
start_x, start_y, target_x, target_y = map(int, input().split())

# 이동할 수 있는 위치 정의
moves = [
    (-2, -1),
    (-2, 1),
    (0, -2),
    (0, 2),
    (2, -1),
    (2, 1)
]

# BFS를 위한 deque 선언
q = deque()
q.append((start_x, start_y, 0))

# 방문 여부를 표시할 리스트
visited = [[False] * N for _ in range(N)]
visited[start_x][start_y] = True

# BFS 시작
while q:
    x, y, count = q.popleft()

    if x == target_x and y == target_y:
        print(count)
        break

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

else:
    print(-1)
```