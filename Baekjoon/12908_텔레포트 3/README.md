# [12908] 텔레포트 3

### **난이도**
골드 5
## **📝문제**
수빈이는 크기가 무한대인 격자판 위에 살고 있다. 격자판의 각 점은 두 정수의 쌍 (x, y)로 나타낼 수 있다.

제일 처음에 수빈이의 위치는 (xs, ys)이고, 집이 위치한 (xe, ye)로 이동하려고 한다.

수빈이는 두 가지 방법으로 이동할 수 있다. 첫 번째 방법은 점프를 하는 것이다. 예를 들어 (x, y)에 있는 경우에 (x+1, y), (x-1, y), (x, y+1), (x, y-1)로 이동할 수 있다. 점프는 1초가 걸린다.

두 번째 방법은 텔레포트를 사용하는 것이다. 텔레포트를 할 수 있는 방법은 총 세 가지가 있으며, 미리 정해져 있다. 텔레포트는 네 좌표 (x1, y1), (x2, y2)로 나타낼 수 있으며, (x1, y1)에서 (x2, y2)로 또는 (x2, y2)에서 (x1, y1)로 이동할 수 있다는 것이다. 텔레포트는 10초가 걸린다.

수빈이의 위치와 집의 위치가 주어졌을 때, 집에 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 xs와 ys가, 둘째 줄에 xe, ye가 주어진다. (0 ≤ xs, ys, xe, ye ≤ 1,000,000,000)

셋째 줄부터 세 개의 줄에는 텔레포트의 정보 x1, y1, x2, y2가 주어진다. (0 ≤ x1, y1, x2, y2 ≤ 1,000,000,000)

입력으로 주어지는 모든 좌표 8개는 서로 다르다.
### **출력**
수빈이가 집에 가는 가장 빠른 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
4 5
1000 1001 1000 1002
1000 1003 1000 1004
1000 1005 1000 1006
```

**예제 출력1**

```
3
```

**예제 입력2**

```
0 0
20 20
1 1 18 20
1000 1003 1000 1004
1000 1005 1000 1006
```

**예제 출력2**

```
14
```

**예제 입력3**

```
0 0
20 20
1000 1003 1000 1004
18 20 1 1
1000 1005 1000 1006
```

**예제 출력3**

```
14
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop

def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

teleport_map = {}
nodes = {start, end}

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    a, b = (x1, y1), (x2, y2)
    teleport_map[a] = b
    teleport_map[b] = a
    nodes.add(a)
    nodes.add(b)

dist = {}
pq = [(0, start)]

while pq:
    time, now = heappop(pq)
    if now in dist:
        continue
    dist[now] = time

    for nxt in nodes:
        if nxt not in dist:
            heappush(pq, (time + calc_dist(now, nxt), nxt))

    if now in teleport_map:
        tp = teleport_map[now]
        if tp not in dist:
            heappush(pq, (time + 10, tp))

print(dist[end])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35508|52|Python3|788
#### **📝해설**

**알고리즘**
```
1. 최단 경로
```

### **다른 풀이**

```python
def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

INF = 1e11
d = [[INF] * 8 for _ in range(8)]
p = []

a, b = map(int, input().split())
p.append((a, b))
a, b = map(int, input().split())
p.append((a, b))

for i in range(3):
    i1 = 2 * i + 2
    i2 = 2 * i + 3

    x1, y1, x2, y2 = map(int, input().split())
    p.append((x1, y1))
    p.append((x2, y2))
    d[i1][i2] = 10
    d[i2][i1] = 10

for i in range(8):
    for j in range(8):
        d[i][j] = min(d[i][j], dist(p[i][0], p[i][1], p[j][0], p[j][1]))

for k in range(8):
    for i in range(8):
        for j in range(8):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d[0][1])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
5tarlight|31120|36|Python3|664
#### **📝해설**

```python
from heapq import heappush, heappop

# 좌표가 주어졌을 때 거리를 계산하는 함수
def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 시작, 끝 지점
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

# 텔레포트가 가능한 지점을 딕셔너리로 저장
teleport_map = {}

# 시작점, 끝점, 텔레포트 지점을 set로 저장(주어진 노드끼리만 탐색하면 됨)
nodes = {start, end}

# 텔레포트 입력받기
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    a, b = (x1, y1), (x2, y2)
    teleport_map[a] = b
    teleport_map[b] = a
    nodes.add(a)
    nodes.add(b)

# 현재 노드까지의 거리를 딕셔너리로 저장
dist = {}
pq = [(0, start)]

# 다익스트라
while pq:

    # 거리, 현재 노드
    time, now = heappop(pq)

    # 이미 방문했다면 넘어감
    if now in dist:
        continue
    dist[now] = time

    # 다음 노드로 이동
    for nxt in nodes:
        if nxt not in dist:
            heappush(pq, (time + calc_dist(now, nxt), nxt))

    # 텔레포트로 이동
    if now in teleport_map:
        tp = teleport_map[now]
        if tp not in dist:
            heappush(pq, (time + 10, tp))

print(dist[end])
```