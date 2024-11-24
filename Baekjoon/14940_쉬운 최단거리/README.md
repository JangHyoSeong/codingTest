# [14940] 쉬운 최단거리

### **난이도**
실버 1
## **📝문제**
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.
### **입력**
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.
### **출력**
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
```

**예제 출력1**

```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

n, m = map(int, input().split())
table = []

flag = False
for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp)

    if not flag:
        for j in range(m):
            if temp[j] == 2:
                start = (i, j)
                flag = True
                break

dist = [[0] * m for _ in range(n)]
q = deque([start])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1 and not dist[nx][ny]:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if dist[i][j] == 0 and table[i][j] == 1:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|120752|232|PyPy3|863
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

# 입력
n, m = map(int, input().split())
table = []

flag = False

for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp)

    # 2를 찾으면 시작지점으로 설정
    if not flag:
        for j in range(m):
            if temp[j] == 2:
                start = (i, j)
                flag = True
                break

# 거리를 저장할 리스트
dist = [[0] * m for _ in range(n)]

# q에 시작지점 삽입
q = deque([start])


# 상하좌우 탐색을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    x, y = q.popleft()


    # 상하좌우를 검사하면서
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 인덱스를 벗어나지않고, 갈 수 있고, 방문한적 없으면 방문
        if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1 and not dist[nx][ny]:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))


# 출력
for i in range(n):
    for j in range(m):

        # 방문할 수 있는 위치인데 방문하지 않았다면 -1 출력
        if dist[i][j] == 0 and table[i][j] == 1:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
```

### **🔖정리**

1. 배운점