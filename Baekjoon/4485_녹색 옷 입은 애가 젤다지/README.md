# [4485] 녹색 옷 입은 애가 젤다지?

### **난이도**
골드 4
## **📝문제**
젤다의 전설 게임에서 화폐의 단위는 루피(rupee)다. 그런데 간혹 '도둑루피'라 불리는 검정색 루피도 존재하는데, 이걸 획득하면 오히려 소지한 루피가 감소하게 된다!

젤다의 전설 시리즈의 주인공, 링크는 지금 도둑루피만 가득한 N x N 크기의 동굴의 제일 왼쪽 위에 있다. [0][0]번 칸이기도 하다. 왜 이런 곳에 들어왔냐고 묻는다면 밖에서 사람들이 자꾸 "젤다의 전설에 나오는 녹색 애가 젤다지?"라고 물어봤기 때문이다. 링크가 녹색 옷을 입은 주인공이고 젤다는 그냥 잡혀있는 공주인데, 게임 타이틀에 젤다가 나와있다고 자꾸 사람들이 이렇게 착각하니까 정신병에 걸릴 위기에 놓인 것이다.

하여튼 젤다...아니 링크는 이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다. 동굴의 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 된다. 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며, 한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.

링크가 잃을 수밖에 없는 최소 금액은 얼마일까?
### **입력**
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N이 주어진다. (2 ≤ N ≤ 125) N = 0인 입력이 주어지면 전체 입력이 종료된다.

이어서 N개의 줄에 걸쳐 동굴의 각 칸에 있는 도둑루피의 크기가 공백으로 구분되어 차례대로 주어진다. 도둑루피의 크기가 k면 이 칸을 지나면 k루피를 잃는다는 뜻이다. 여기서 주어지는 모든 정수는 0 이상 9 이하인 한 자리 수다.
### **출력**
각 테스트 케이스마다 한 줄에 걸쳐 정답을 형식에 맞춰서 출력한다. 형식은 예제 출력을 참고하시오.
### **예제입출력**

**예제 입력1**

```
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0
```

**예제 출력1**

```
Problem 1: 20
Problem 2: 19
Problem 3: 36
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush

testcase = 1
while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    
    dist = [[int(21e8)] * N for _ in range(N)]
    dist[0][0] = table[0][0]

    pq = [(table[0][0], 0, 0)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while pq:
        now_dist, x, y = heappop(pq)

        if now_dist > dist[x][y]:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = now_dist + table[nx][ny]

                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
    
    print(f'Problem {testcase}: {dist[N-1][N-1]}')
    testcase += 1
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35508|144|Python3|893
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
def bfs(y, x):
    q = []
    heapq.heappush(q, (cave[y][x], y, x))
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1
    while q:
        w, y, x = heapq.heappop(q)
        if x == n - 1 and y == n - 1: return w
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                visited[ny][nx] = 1
                heapq.heappush(q, (w + cave[ny][nx], ny, nx))

import sys, heapq
input = sys.stdin.readline
tc = 1
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while True:
    n = int(input())
    if n == 0: break
    cave = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {tc}: {bfs(0, 0)}')
    tc += 1
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
po042|35508|72|Python3|726
#### **📝해설**

```python
import sys
from heapq import heappop, heappush

# 정답 출력을 위한 변수
testcase = 1
while True:

    # 입력받기
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    
    # 시작지점부터 각 노드까지의 거리를 저장할 리스트
    dist = [[int(21e8)] * N for _ in range(N)]
    dist[0][0] = table[0][0]

    # 우선순위 큐를 사용해 다익스트라 알고리즘 구현
    pq = [(table[0][0], 0, 0)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 다익스트라 시작
    while pq:
        now_dist, x, y = heappop(pq)

        if now_dist > dist[x][y]:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = now_dist + table[nx][ny]

                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
    
    # 출력
    print(f'Problem {testcase}: {dist[N-1][N-1]}')
    testcase += 1
```